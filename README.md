# RAG da ajuda Visual FoxPro 9

Índice em português da documentação do VFP 9 e um servidor HTTP de busca. O agente no Cursor consulta esse servidor **antes** de inventar assinatura, parâmetro ou comportamento.

Há dois papéis:

- **Servidor** — uma máquina da equipe, **Linux ou Windows**, que roda o `serve`.
- **Desenvolvedor** — Windows, com Cursor no projeto FoxPro. Não precisa desta pasta no PC: só da regra do Cursor e da URL do servidor.

---

## 1. Instalar no servidor (Linux ou Windows)

**Python 3.11+** e **4–8 GB de RAM** livres para o processo (o encoder e5 fica em memória). GPU não é obrigatória: NVIDIA com CUDA acelera o `embed`; no dia a dia o `serve` roda bem em CPU.

A árvore precisa ter `scripts/` e `data/` na mesma raiz. O índice (`data/rag/index.jsonl`) e os embeddings (`data/rag/embeddings.npy`) já vêm nesta cópia: **não rode `build` nem `embed`** só para subir o serviço.

Na primeira instalação o `pip` baixa o modelo `intfloat/multilingual-e5-small` (~120 MB).

### 1.1 Linux

```bash
cd /opt/vfp-rag
python3 -m venv .venv
.venv/bin/pip install -U pip
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/rag.py serve --host 0.0.0.0 --port 8765
```

Para sobreviver a logout e reboot, use `systemd`:

```ini
# /etc/systemd/system/vfp-rag.service
[Unit]
Description=RAG Visual FoxPro 9
After=network.target

[Service]
Type=simple
WorkingDirectory=/opt/vfp-rag
ExecStart=/opt/vfp-rag/.venv/bin/python scripts/rag.py serve --host 0.0.0.0 --port 8765
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now vfp-rag
```

Abra a porta **8765** no firewall só para a rede da equipe (ou VPN), por exemplo com `ufw`/`firewalld`.

### 1.2 Windows

Instale o [Python 3.11+](https://www.python.org/downloads/) marcando **Add python.exe to PATH**. No Prompt de comando ou PowerShell, como administrador se a pasta for em `C:\`:

```bat
cd /d C:\vfp-rag
python -m venv .venv
.venv\Scripts\python.exe -m pip install -U pip
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe scripts\rag.py serve --host 0.0.0.0 --port 8765
```

Quando estiver pronto, o processo imprime algo como:

```text
RAG em http://0.0.0.0:8765/search (6988 passagens). GET /search?q=...&k=4
```

No **Firewall do Windows Defender**, crie uma regra de entrada TCP na porta **8765**, restrita à rede local (ou à VPN). Sem isso, o Cursor nos PCs dos desenvolvedores não alcança o servidor.

Para o serviço voltar após reboot, o caminho mais simples é o **Agendador de Tarefas**:

1. Criar tarefa básica → ao iniciar o computador (ou ao fazer logon da conta de serviço).
2. Ação: iniciar um programa.
3. Programa: `C:\vfp-rag\.venv\Scripts\python.exe`
4. Argumentos: `scripts\rag.py serve --host 0.0.0.0 --port 8765`
5. Iniciar em: `C:\vfp-rag`
6. Marcar “Executar estando o usuário conectado ou não”, se for uma conta de serviço.

Não rode um `serve` em cada PC de desenvolvedor: o encoder é pesado; compartilhem **um** processo.

### 1.3 Conferir na própria máquina do servidor

No Linux:

```bash
curl -sG "http://127.0.0.1:8765/search" --data-urlencode "q=ALINES" --data-urlencode "k=4"
```

No Windows (use `curl.exe`, não o `curl` do PowerShell):

```bat
curl.exe -sG "http://127.0.0.1:8765/search" --data-urlencode "q=ALINES" --data-urlencode "k=4"
```

A resposta é JSON com `hits` (`title`, `section`, `kind`, `text`).

### 1.4 Quando reconstruir o índice

Só se `data/markdown_pt/`, `data/topics.jsonl` ou as fichas em `data/training/` mudarem.

Linux:

```bash
.venv/bin/python scripts/rag.py build
.venv/bin/python scripts/rag.py embed
```

Windows:

```bat
.venv\Scripts\python.exe scripts\rag.py build
.venv\Scripts\python.exe scripts\rag.py embed
```

Depois reinicie o `serve`.

---

## 2. Usar no Cursor (Windows do desenvolvedor)

O modelo que escreve código é o do Cursor neste PC. O servidor **só devolve trechos** da ajuda. Cada pergunta de sintaxe VFP deve consultar o RAG **uma vez**.

### 2.1 Copiar a regra para o projeto FoxPro

No repositório em que você programa (Prompt de comando):

```bat
mkdir .cursor\rules
copy C:\vfp-rag\.cursor\rules\vfp-rag.mdc .cursor\rules\vfp-rag.mdc
```

Se a pasta RAG estiver só no servidor, copie `vfp-rag.mdc` daí (compartilhamento, git, e-mail) para `.cursor\rules\` do projeto FoxPro. A regra já está com `alwaysApply: true`.

### 2.2 Apontar para o servidor da equipe

Defina a variável de **usuário** no Windows (assim o Cursor herda ao abrir):

```powershell
[System.Environment]::SetEnvironmentVariable(
  "VFP_RAG_URL",
  "http://IP-OU-HOSTNAME-DO-SERVIDOR:8765",
  "User"
)
```

Exemplos: `http://192.168.1.20:8765` ou `http://rag.empresa.local:8765`. **Feche e reabra o Cursor** depois de gravar a variável.

Sem `VFP_RAG_URL`, a regra usa `http://127.0.0.1:8765` — só funciona se o `serve` estiver neste mesmo PC.

Teste no Prompt de comando:

```bat
curl.exe -sG "%VFP_RAG_URL%/search" --data-urlencode "q=SEEK vs LOCATE" --data-urlencode "k=4"
```

No PowerShell:

```powershell
curl.exe -sG "$env:VFP_RAG_URL/search" --data-urlencode "q=SEEK vs LOCATE" --data-urlencode "k=4"
```

Se voltar JSON com tópicos, o Cursor consegue o mesmo. No Windows, **sempre `curl.exe`**: o comando `curl` no PowerShell é o `Invoke-WebRequest` e não serve para esta chamada.

### 2.3 Como o agente deve consultar

A regra manda o agente fazer **um** GET por pergunta, com `curl.exe`:

```bat
curl.exe -sG "%VFP_RAG_URL%/search" --data-urlencode "q=sua pergunta aqui" --data-urlencode "k=4"
```

Não repetir a busca com outras formulações, não abrir `data/markdown_pt/` e não inventar assinatura se o trecho veio vazio: nesse caso a resposta correta é “não encontrei na documentação”.

Use o RAG para: assinatura, parâmetros, diferença entre comandos, significado de erro, `SET`, propriedades. Não use para: Git, Cursor, arquitetura do seu ERP.

### 2.4 Fallback sem servidor (opcional)

Só se o servidor estiver fora do ar **e** esta pasta existir no PC Windows, com `.venv` já instalado:

```bat
cd /d C:\vfp-rag
.venv\Scripts\python.exe scripts\rag.py search "sua pergunta aqui" -k 4
```

Isso carrega o e5 a cada chamada (~2 s). No dia a dia, prefira o `serve` da equipe.

---

## Pastas desta cópia

| Pasta | Conteúdo |
| --- | --- |
| `data/rag/` | Índice e embeddings (o que o `serve` lê) |
| `data/markdown_pt/` | Páginas de ajuda em português |
| `data/topics.jsonl` | Catálogo de tópicos |
| `data/training/` | Fichas de assinatura usadas no `build` |
| `scripts/rag.py` | Busca, índice e API HTTP |
| `.cursor/rules/` | Regra para colar no projeto FoxPro |

Não há markdown em inglês, notebooks, treino de LLM nem scripts de extração/tradução nesta cópia.
