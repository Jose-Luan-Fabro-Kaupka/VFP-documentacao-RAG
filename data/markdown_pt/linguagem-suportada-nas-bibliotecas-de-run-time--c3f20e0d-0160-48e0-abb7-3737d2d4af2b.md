# Linguagem suportada nas bibliotecas de run-time

A biblioteca de run-time principal do Visual FoxPro, VFPVersionNumberR.dll com VersionNumber representando a versão específica desta release, suporta todo o conjunto de linguagem de objetos, comandos e funções, excluindo linguagem específica de tempo de design.

Para projetar a biblioteca de run-time multithread do Visual FoxPro, VFPVersionNumberT.dll, como uma biblioteca de run-time leve para servidores in-process, muitos comandos e funções de entrada do usuário foram removidos. Toda a sintaxe de Object ainda está disponível, embora eventos de classes visuais como formulários estejam desabilitados. As seguintes categorias de linguagem foram removidas da biblioteca de run-time multithread do Visual FoxPro:
 - READ, @...Get/Says
- Menu, Popup, and Bar commands and functions
- MESSAGEBOX() and WAIT WINDOW
- User-defined Window commands and functions

# Comandos desabilitados que geram erros de run-time

A tabela a seguir é uma lista de comandos não suportados, que gerarão um destes erros em run-time na biblioteca de run-time multithread do Visual FoxPro:
 - Commands: Feature is not available
- Functions: Function is not implemented
- System variables: Variable is not found

A tabela a seguir mostra os comandos não suportados.

| @...BOX | @...CLASS | @...CLEAR |
| --- | --- | --- |
| @...EDIT | @...FILL | @...GET |
| @...MENU | @...PROMPT | @...SAY |
| @...SCROLL | @...TO | _ALIGNMENT |
| _ASSIST | _BEAUTIFY | _BOX |
| _CALCMEM | _CALCVALUE | _CONVERTER |
| _COVERAGE | _CUROBJ | _DBLCLICK |
| _DIARYDATE | _FOXDOC | _GALLERY |
| _GENMENU | _GENPD | _GENSCRN |
| _GETEXPR | _INCSEEK | _INDENT |
| _LMARGIN | _PADVANCE | _PBPAGE |
| _PCOLNO | _PCOPIES | _PDRIVER |
| _PDSETUP | _PECODE | _PEJECT |
| _PEPAGE | _PLENGTH | _PLINENO |
| _PLOFFSET | _PPITCH | _PQUALITY |
| _PSCODE | _PSPACING | _PWAIT |
| _RMARGIN | _SCCTEXT | _SPELLCHK |
| _STARTUP | _TABS | _THROTTLE |
| _TRANSPORT | _WRAP | |
| ACCEPT | ACTIVATE MENU | ACTIVATE POPUP |
| ACTIVATE SCREEN | ACTIVATE WINDOW | AGETCLASS() |
| AMOUSEOBJ() | ANSITOOEM() | APROCINFO() |
| ASELOBJ() | ASSERT | ASSIST |
| BAR() | BARCOUNT() | BARPROMPT() |
| BROWSE | CALL | CHANGE |
| CLEAR DEBUG | CLEAR GETS | CLEAR MACROS |
| CLEAR MENUS | CLEAR POPUPS | CLEAR PROMPT |
| CLEAR READ | CLOSE DEBUGGER | CLOSE FORMAT |
| CLOSE MEMO | CNTBAR() | CNTPAD() |
| COL() | CREATE | CREATE CLASS |
| CREATE CLASSLIB | CREATE COLOR SET | CREATE FORM |
| CREATE LABEL | CREATE MENU | CREATE PROJECT |
| CREATE QUERY | CREATE REPORT | CREATE SCREEN |
| DEACTIVATE MENU | DEACTIVATE POPUP | DEACTIVATE WINDOW |
| DEBUG | DEBUGOUT | DEFINE BAR |
| DEFINE BOX | DEFINE MENU | DEFINE PAD |
| DEFINE POPUP | DEFINE WINDOW | EDIT |
| FKLABEL() | FKMAX() | GETBAR() |
| GETCOLOR() | GETCP() | GETDIR() |
| GETEXPR() | GETFILE() | GETFONT() |
| GETPAD() | GETPICT() | GETPRINTER() |
| HELP | HIDE MENU | HIDE POPUP |
| HIDE WINDOW | IMESTATUS() | INPUT |
| KEYBOARD | LOAD | LOCFILE() |
| MCOL() | MDOWN() | MENU |
| MENU TO | MENU() | MESSAGEBOX() |
| MODIFY Commands | MOUSE | MOVE POPUP |
| MOVE WINDOW | MRKBAR() | MRKPAD() |
| MROW() | MWINDOW() | OBJNUM() |
| OBJVAR() | OEMTOANSI() | ON BAR() |
| ON ESCAPE | ON EXIT Commands | ON KEY |
| ON KEY LABEL | ON PAD | ON PAGE |
| ON READERROR | ON SELECTION BAR | ON SELECTION MENU |
| ON SELECTION PAD | ON SELECTION POPUP | PAD() |
| PLAY MACRO | POP KEY | POP MENU |
| POP POPUP | POPUP() | PRMBAR() |
| PRMPAD() | PROMPT() | PUSH KEY |
| PUSH MENU | PUSH POPUP | PUTFILE() |
| RDLEVEL() | READ | READ MENU |
| READKEY() | RELEASE BAR | RELEASE MENUS |
| RELEASE PAD | RELEASE POPUPS | RELEASE WINDOWS |
| RESTORE MACROS | RESTORE SCREEN | RESTORE WINDOW |
| ROW() | SAVE MACROS | SAVE SCREEN |
| SAVE WINDOWS | SCROLL | SHOW GET(S) |
| SHOW MENU | SHOW OBJECT | SHOW POPUP |
| SHOW WINDOW | SIZE POPUP | SIZE WINDOW |
| SKPBAR() | SKPPAD() | SUSPEND |
| VARREAD() | WAIT | WBORDER() |
| WCHILD() | WCOLS() | WEXIST() |
| WFONT() | WLAST() | WLCOL() |
| WLROW() | WMAXIMUM() | WONTOP() |
| WOUTPUT() | WMINIMUM() | WPARENT() |
| WREAD() | WROWS() | WTITLE() |
| WVISIBLE() | ZOOM WINDOW | |

# Comandos desabilitados que não geram erros de run-time

A tabela a seguir é uma lista de comandos não suportados, que não geram um erro quando executados em run-time na biblioteca de run-time multithread do Visual FoxPro. Essas funções estão desabilitadas para uso em run-time; no entanto, devido à frequência de uso em código comum e bibliotecas de classes entre diferentes tipos de aplicativos, elas não causam um erro. Quando um desses comandos ou funções é encontrado no código, o Visual FoxPro ignora essa linha de código e continua a execução. Isso inclui certos comandos SET e funções SYS.

| CD | CHDIR | DOEVENTS |
| --- | --- | --- |
| SET ASSERTS | SET BELL | SET BORDER |
| SET BROWSEME | SET BRSTATUS | SET CONSOLE |
| SET COLOR | SET CLEAR | SET CLOCK |
| SET CONFIRM | SET CURSOR | SET CPDIALOG |
| SET DEBUGOUT | SET DEBUG | SET DEFAULT |
| SET DEVELOPMENT | SET DELIMITERS | SET DISPLAY |
| SET DOHISTORY | SET ESCAPE | SET ECHO |
| SET EVENTLIST | SET EVENTTRACKING | SET FORMAT |
| SET FUNCTION | SET HELP | SET INTENSITY |
| SET MARK OF | SET MACDESKTOP | SET MACKEY |
| SET MARGIN | SET MESSAGE | SET NOTIFY |
| SET ODOMETER | SET PALETTE | SET PDSETUP |
| SET READBORDER | SET REFRESH | SET RESOURCE |
| SET SAFETY | SET SKIP OF | SET STICKY |
| SET STATUS | SET SYSMENU | SET TALK |
| SET TRBETWEEN | SET TYPEAHEAD | SET VIEW |
| SET WINDOW | SYS(1037) | SYS(18) |
| SYS(103) | SYS(2002) | SYS(1270) |
| SYS(2017) | SYS(4204) | SYS(2016) |

A tabela a seguir lista as propriedades e funções que facilitam o gerenciamento de clientes e servidores Automation.

| Comando ou propriedade | Descrição |
| --- | --- |
| COMARRAY( ) Function | Especifica como arrays são passados para objetos COM. |
| COMCLASSINFO( ) Function | Retorna informações de registro sobre um objeto COM, como um servidor Automation Visual FoxPro. |
| COMRETURNERROR( ) Function | Preenche a estrutura de exceção COM com informações que clientes Automation podem usar para determinar a origem de erros do servidor Automation. |
| CREATEOBJECTEX( ) Function | Cria uma instância de um objeto COM registrado (como um servidor Automation Visual FoxPro) em um computador remoto. Para um Visual FoxPro in-process .dll, você pode usar Microsoft Transaction Server para criar uma instância do .dll em um computador remoto. |
| EVENTHANDLER( ) Function | Vincula um evento de servidor COM a métodos de interface implementados em um objeto Visual FoxPro instanciado. |
| ProcessID Property | Retorna o ID do Process que criou o objeto. |
| ServerName Property | Contém o caminho completo e o nome do arquivo de um servidor Automation. A propriedade ServerName é uma propriedade do objeto Application. |
| StartMode Property | Contém um valor numérico que indica como a instância do Visual FoxPro foi iniciada. |
| SYS(2334) – Automation Server Invocation Mode | Retorna um valor que indica como um método de servidor Automation Visual FoxPro foi invocado. |
| SYS(2335) – Unattended Server Mode | Habilita ou desabilita suporte para estados modais em servidores Automation Visual FoxPro .exe distribuíveis. |
| SYS(2336) - Critical Section Support Function | Controla o acesso de seção crítica em servidores Multithreaded. |
| SYS(2339) - Internal Global Variable Function | Retorna o valor atual da variável global interna chamada g_fCallCoFreeOnRelease . |
| ThreadID Property | Retorna o ID da thread na qual o objeto foi criado. |
