# Sequência de eventos no Visual FoxPro

Embora alguns eventos ocorram isoladamente, uma ação do usuário frequentemente dispara vários eventos. Alguns são independentes; porém, certas sequências são fixas, como a que ocorre quando um formulário é criado ou destruído.

Quando uma sequência de eventos é disparada para um controle, toda ela é associada ao controle. Por exemplo, suponha que você clique com o botão esquerdo em um botão de comando e arraste o ponteiro para fora dele. O evento MouseMove do botão continua ocorrendo mesmo quando o ponteiro passa sobre o formulário. Se o botão do mouse for solto sobre o formulário, e não sobre o botão, o evento MouseUp será associado ao botão de comando, não ao formulário.

A tabela a seguir mostra a sequência geral de eventos do Visual FoxPro, supondo que a propriedade AutoOpenTables do ambiente de dados esteja definida como True (.T.). Outros eventos podem ocorrer conforme a interação do usuário e a resposta do sistema.
 Sequência de eventos do Visual FoxPro
| Objeto | Evento que ocorre |
| --- | --- |
| Ambiente de dados | BeforeOpenTables |
| Conjunto de formulários | Load |
| Formulário | Load |
| Cursor(es) do ambiente de dados | Init |
| Ambiente de dados | Init |
| Objetos 1 | Init |
| Formulário | Init |
| Conjunto de formulários | Init |
| Conjunto de formulários | Activate |
| Formulário | Activate |
| Object1 2 | When |
| Formulário | GotFocus |
| Object1 | GotFocus |
| Object1 | Message |
| Object1 | Valid 3 |
| Object1 | LostFocus |
| Object2 3 | When |
| Object2 | GotFocus |
| Object2 | Message |
| Object2 | Valid 4 |
| Object2 | LostFocus |
| Formulário | QueryUnload |
| Formulário | Destroy |
| Objeto 5 | Destroy |
| Formulário | Unload |
| Conjunto de formulários | Unload |
| Ambiente de dados | AfterCloseTables |
| Ambiente de dados | Destroy |
| Cursor(es) do ambiente de dados | Destroy |

1. Para cada objeto, do objeto mais interno ao contêiner mais externo
2. Primeiro objeto na ordem de tabulação
3. Próximo objeto a receber foco
4. Quando o objeto perde o foco
5. Para cada objeto, do contêiner mais externo ao objeto mais interno

# Exemplo de sequência de eventos

O exemplo a seguir usa um formulário para ilustrar a ordem dos eventos em resposta à interação do usuário.
 Um formulário de exemplo

Neste exemplo, o usuário executa as seguintes ações:
 - Executa o formulário.
- Digita texto na caixa de texto Text1.
- Seleciona o texto e o copia para a área de transferência.
- Vai para Text2 pressionando TAB.
- Cola o texto em Text2.
- Fecha o formulário clicando no botão Command2.

Essas ações disparam eventos do sistema para cada objeto. As tabelas a seguir listam os eventos que ocorrem em resposta a cada ação.

> **Observação:** Neste exemplo, o evento Paint foi removido das tabelas porque ocorre com frequência e dificulta visualizar as sequências dos demais eventos.

Ação 1

O usuário executa o formulário digitando o seguinte comando na janela Command:

```foxpro
DO FORM form1 NAME frmObject
```

O Visual FoxPro carrega o formulário, inicializa cada objeto e então inicializa o formulário. O formulário é ativado e a primeira caixa de texto recebe o foco de entrada.

| Objeto | Evento |
| --- | --- |
| DataEnvironment | BeforeOpenTables |
| Form1 | Load |
| DataEnvironment | Init |
| Text1 | Init |
| Text2 | Init |
| Command1 | Init |
| Command2 | Init |
| Form1 | Init |
| Form1 | Activate |
| Form1 | GotFocus |
| Text1 | When |
| Text1 | GotFocus |

Ação 2

O usuário digita "Test" em Text1. Cada pressionamento de tecla gera dois eventos.

> **Observação:** O evento KeyPress recebe dois parâmetros: um número que representa a tecla pressionada e o estado das teclas SHIFT, ALT e CTRL.

| Objeto | Evento | Parâmetros |
| --- | --- | --- |
| Text1 | KeyPress | (84 para "T", 1) |
| Text1 | InteractiveChange | |
| Text1 | KeyPress | (101 para "e", 0) |
| Text1 | InteractiveChange | |
| Text1 | KeyPress | (115 para "s", 0) |
| Text1 | InteractiveChange | |
| Text1 | KeyPress | (116 para "t",0) |
| Text1 | InteractiveChange | |

Ação 3

O usuário seleciona o texto de Text1 clicando duas vezes nele e o copia para a área de transferência com CTRL+C. Eventos do mouse e Click acompanham DblClick.

> **Observação:** Os eventos MouseMove, MouseDown e MouseUp recebem quatro parâmetros: um número que indica o botão pressionado, o estado de SHIFT e as coordenadas (X, Y). As coordenadas são relativas ao formulário e refletem seu modo de escala, por exemplo, pixels. Embora apenas um MouseMove seja listado para cada controle, na prática ele pode ocorrer seis vezes ou mais.

| Objeto | Evento | Parâmetros |
| --- | --- | --- |
| Form1 | MouseMove | (0, 0, 100, 35) |
| Text1 | MouseMove | (0, 0, 44, 22) |
| Text1 | MouseDown | (1, 0, 44, 22) |
| Text1 | MouseUp | (1, 0, 44, 22) |
| Text1 | Click | |
| Text1 | MouseDown | (1, 0, 44, 22) |
| Text1 | MouseUp | (1, 0, 44, 22) |
| Text1 | DblClick | |

Ação 4

O usuário vai para Text2 pressionando TAB.

| Objeto | Evento | Parâmetros |
| --- | --- | --- |
| Text1 | KeyPress | (9, 0) |
| Text1 | Valid | |
| Text1 | LostFocus | |
| Text2 | When | |
| Text2 | GotFocus | |

Ação 5

O usuário cola o texto em Text2 pressionando CTRL+V.

| Objeto | Evento |
| --- | --- |
| Text2 | InteractiveChange |

Ação 6

O usuário clica em Command2 para fechar o formulário.

| Objeto | Evento | |
| --- | --- | --- |
| Form1 | MouseMove | |
| Command2 | MouseMove | |
| Text2 | Valid | |
| Command2 | When | |
| Text2 | LostFocus | |
| Command2 | GotFocus | |
| Command2 | MouseDown | (1, 0, 143, 128) |
| Command2 | MouseUp | (1, 0, 143, 128) |
| Command2 | Click | |
| Command2 | Valid | |
| Command2 | When | |

Quando o formulário é fechado e os objetos são liberados, eventos adicionais ocorrem na ordem inversa à da Ação 1.

| Objeto | Evento |
| --- | --- |
| Form1 | Destroy |
| Command2 | Destroy |
| Command1 | Destroy |
| Text2 | Destroy |
| Text1 | Destroy |
| Form1 | Unload |
| DataEnvironment | AfterCloseTables |
| DataEnvironment | Destroy |
