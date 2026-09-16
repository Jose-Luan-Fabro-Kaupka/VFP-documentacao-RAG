# RAG da ajuda Visual FoxPro 9

Índice em português da documentação do VFP 9 e um servidor HTTP de busca. O agente no Cursor consulta esse servidor **antes** de inventar assinatura, parâmetro ou comportamento.

Há dois papéis: quem **instala o servidor** (uma máquina da equipe) e quem **usa no Cursor** (cada desenvolvedor, no projeto FoxPro). O desenvolvedor **não** precisa desta pasta inteira no notebook — só da regra do Cursor e da URL do servidor.

---

## 1. Instalar no servidor

Máquina Linux ou macOS com **Python 3.11+** e **4–8 GB de RAM** livres para o processo (o encoder e5 fica em memória). GPU não é obrigatória: em Apple Silicon usa MPS; em NVIDIA, CUDA; senão, CPU.

### 1.1 Copiar o projeto

Coloque esta pasta no servidor, por exemplo `/opt/vfp-rag` (ou `~/RAG`). A árvore precisa ter `scripts/` e `data/` na mesma raiz.

```bash
cd /opt/vfp-rag
python3 -m venv .venv
.venv/bin/pip install -U pip
.venv/bin/pip install -r requirements.txt
```

Na primeira vez o `sentence-transformers` baixa o modelo `intfloat/multilingual-e5-small` (~120 MB). O índice (`data/rag/index.jsonl`) e os embeddings (`data/rag/embeddings.npy`) já vêm nesta cópia: **não rode `build` nem `embed`** só para subir o serviço.

### 1.2 Subir a API

```bash
.venv/bin/python scripts/rag.py serve --host 0.0.0.0 --port 8765
```

Quando estiver pronto, o processo imprime algo como:

```text
RAG em http://0.0.0.0:8765/search (6988 passagens). GET /search?q=...&k=4
```

Confira na própria máquina:

```bash
curl -sG "http://127.0.0.1:8765/search" \
  --data-urlencode "q=ALINES" \
  --data-urlencode "k=4"
```

A resposta é JSON com `hits` (`title`, `section`, `kind`, `text`). Deixe a porta **8765** aberta só na rede da equipe (firewall / VPN). Um único processo atende vários Cursors ao mesmo tempo.

Para sobreviver a logout e reboot, use `systemd` (Linux):

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

Em macOS, `tmux` ou um LaunchAgent cumpre o mesmo papel. Não rode um `serve` por desenvolvedor: o encoder é pesado; compartilhem **um** processo.

### 1.3 Quando reconstruir o índice

Só se `data/markdown_pt/`, `data/topics.jsonl` ou as fichas em `data/training/` mudarem:

```bash
.venv/bin/python scripts/rag.py build
.venv/bin/python scripts/rag.py embed
# depois reinicie o serve
```

---

## 2. Usar no Cursor (máquina do desenvolvedor)

O modelo que escreve código é o do Cursor. O servidor **só devolve trechos** da ajuda. Cada pergunta de sintaxe VFP deve consultar o RAG **uma vez**.

### 2.1 Copiar a regra para o projeto FoxPro

No repositório em que você programa (não precisa ser esta pasta RAG):

```bash
mkdir -p .cursor/rules
cp /caminho/para/RAG/.cursor/rules/vfp-rag.mdc .cursor/rules/vfp-rag.mdc
```

A regra já está com `alwaysApply: true`: o agente consulta o RAG em fatos de VFP (comandos, funções, propriedades, erros).

### 2.2 Apontar para o servidor da equipe

Defina a URL do servidor. No Cursor, em **Settings → Cursor Settings**, ou no ambiente do terminal integrado:

```bash
export VFP_RAG_URL="http://IP-OU-HOSTNAME-DO-SERVIDOR:8765"
```

Troque pelo endereço real (exemplo: `http://192.168.1.20:8765` ou `http://rag.empresa.local:8765`). Sem a variável, a regra usa `http://127.0.0.1:8765` — só funciona se o `serve` estiver na **sua** máquina.

Teste do notebook:

```bash
curl -sG "${VFP_RAG_URL}/search" \
  --data-urlencode "q=SEEK vs LOCATE" \
  --data-urlencode "k=4"
```

Se o `curl` devolver JSON com tópicos, o Cursor consegue o mesmo.

### 2.3 Como o agente deve consultar

A regra manda o agente fazer **um** GET por pergunta:

```bash
curl -sG "${VFP_RAG_URL:-http://127.0.0.1:8765}/search" \
  --data-urlencode "q=sua pergunta aqui" \
  --data-urlencode "k=4"
```

Não repetir a busca com outras formulações, não abrir `data/markdown_pt/` e não inventar assinatura se o trecho veio vazio: nesse caso a resposta correta é “não encontrei na documentação”.

Use o RAG para: assinatura, parâmetros, diferença entre comandos, significado de erro, `SET`, propriedades. Não use para: Git, Cursor, arquitetura do seu ERP.

### 2.4 Fallback sem servidor (opcional)

Se o servidor estiver fora do ar **e** você tiver esta pasta localmente, com `.venv` e dependências:

```bash
cd /caminho/para/RAG
.venv/bin/python scripts/rag.py search "sua pergunta aqui" -k 4
```

Isso carrega o e5 a cada chamada (~2 s). No dia a dia, prefira o `serve` da equipe.

---

## Pastas desta cópia

| Pasta | Conteúdo |
| --- | --- |
| `data/rag/` | Índice e embeddings (o que o `serve` lê) |
| `data/markdown_pt/` | Páginas de ajuda em português |
| `data/topics.jsonl` | Catálogo de tópicos |
| `data/training/` | Fichas de assinatura |
| `scripts/rag.py` | Busca, índice e API HTTP |
| `.cursor/rules/` | Regra para colar no projeto FoxPro |
| `ollama/` | Modelfiles (resposta local, opcional) |
| `exemplos/` | Programas FoxPro de exemplo |
| `notebooks/` | Colab / export GGUF |

Não há markdown em inglês nesta cópia. O Help File original (HTML/CHM) permanece no repositório da ajuda, se você ainda o tiver.
