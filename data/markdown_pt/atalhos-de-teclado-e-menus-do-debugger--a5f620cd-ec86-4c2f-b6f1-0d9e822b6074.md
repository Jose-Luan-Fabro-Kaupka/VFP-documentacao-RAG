# Atalhos de teclado e menus do Debugger

Os seguintes atalhos de teclado se aplicam às ferramentas de depuração na janela Debugger ou no frame FoxPro.

| Ação | Teclado |
| --- | --- |
| Resume | F5 |
| Cancel | ESC |
| Step Into | F8 |
| Step Over | F6 |
| Step Out | SHIFT+F7 |
| Run To Cursor | F7 |
| Trace Window | ALT+8 |
| Watch Window | ALT+3 |
| Locals Window | ALT+4 |
| Call Stack Window | ALT+7 |
| Debug Output Window | ALT+2 |
| Toggle Breakpoint | F9 |
| Clear Breakpoints | CTRL+SHIFT+F9 |
| Breakpoints | CTRL+B |
| Open File | CTRL+O |
| Save Configuration | ALT+S |
| Exit Debugger | ALT+F4 |

# Menu File, janela Debugger

Contém opções que permitem abrir programas e configurações de depuração. Você também pode salvar a saída de depuração em um arquivo.

### Comandos do menu
 **Open**
Exibe a caixa de diálogo Open para que você possa especificar um programa a ser exibido na janela Trace. Abrir um programa não executa o programa.
**Load Configuration**
Carrega pontos de interrupção, watches e eventos a serem rastreados de um arquivo de configuração (arquivo .dbg). Selecione o botão de diálogo para exibir a caixa de diálogo Open, que permite especificar um arquivo.
**Save Configuration**
Salva os pontos de interrupção, watches e eventos atuais a serem rastreados em um arquivo de configuração (arquivo .dbg) para que possam ser restaurados posteriormente. Selecione o botão de diálogo para exibir a caixa de diálogo Open, que permite especificar um arquivo.
**Save Output As**
Grava o texto exibido na janela Debug Output em um arquivo especificado na caixa de diálogo Save As.
**Exit**
Fecha a janela Debugger e retorna à janela principal do Visual FoxPro.

# Menu Debug, janela Debugger

Contém opções para percorrer o código passo a passo. Você também pode definir a velocidade na qual os comandos são executados enquanto observa.

### Comandos do menu
 **Do**
Inicia a execução do programa aberto na janela Trace. Se nenhum programa estiver aberto na janela Trace, exibe a caixa de diálogo Do para que você possa especificar um programa ou formulário a ser rastreado. O programa ou formulário especificado é executado com a execução do programa suspensa na primeira linha de código executável.
**Resume**
Está disponível se a execução do programa estiver suspensa. Continua a execução do programa na janela Trace na linha de código atual.
**Cancel**
Fecha e interrompe a execução do programa ou formulário na janela Trace.
**Fix**
Está disponível se a execução do programa estiver suspensa. Se você estiver rastreando um programa, Fix solicita que você cancele o programa e depois o abre em uma janela de edição, na mesma posição em que o cursor está na janela Trace. Se você estiver rastreando código em um formulário, Fix solicita que você cancele a execução e limpe o objeto de formulário da memória. Em seguida, uma janela de edição no Form Designer abre na mesma posição em que o cursor está na janela Trace.
**Step Out**
Continua executando o código em um procedimento sem percorrer o código linha por linha. A execução do programa é suspensa novamente na linha de código seguinte à chamada do procedimento no programa chamador.
**Step Over**
Executa a próxima linha de código. Se a próxima linha de código chamar uma função, método ou procedimento, a função, método ou procedimento é executado em segundo plano.
**Step Into**
Executa a próxima linha de código.
**Run To Cursor**
Executa o código do indicador de linha atual até a linha de código com o cursor. Clique na linha de código na qual deseja suspender a execução para posicionar o cursor nessa linha.
**Throttle**
Abre a caixa de diálogo Execution Throttle para que você possa especificar o atraso em segundos entre a execução de cada linha de código.
**Set Next Statement**
Posiciona o marcador de linha atual na linha de código com o cursor. Esta linha de código será executada quando você percorrer ou retomar a execução.

# Menu Tools, janela Debugger

Fornece acesso às caixas de diálogo do Debugger.

### Comandos do menu
 **Breakpoints**
Abre a caixa de diálogo Breakpoints para que você possa adicionar, excluir, habilitar ou desabilitar pontos de interrupção.
**Event Tracking**
Abre a caixa de diálogo Event Tracking para que você possa especificar quais eventos são gravados na janela Debug Output ou em um arquivo quando ocorrem.
**Coverage Logging**
Abre a caixa de diálogo Coverage para que você possa ativar ou desativar o registro de cobertura e especificar um arquivo para o log de cobertura.
