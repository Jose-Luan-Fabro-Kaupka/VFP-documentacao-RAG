# Comando ACTIVATE MENU

Exibe e ativa uma barra de menu.

```foxpro
ACTIVATE MENU MenuBarName   [NOWAIT]   [PAD MenuTitleName]
```

#### Parâmetros
 **MenuBarName**
Especifica o nome da barra de menu a ativar.
**NOWAIT**
Especifica que, em tempo de execução, o programa não deve aguardar que o usuário escolha um menu na barra de menu ativa ou pressione ESC. Em vez disso, o programa continua a ser executado. Um menu ativado com a opção NOWAIT não retorna a execução do programa à linha após o comando ACTIVATE MENU quando DEACTIVATE MENU é emitido.
**PAD MenuTitleName**
Especifica o nome do título de menu que é selecionado automaticamente quando a barra de menu é ativada. Se você não especificar um nome de título de menu, o primeiro nome de título de menu na barra de menu ativada é ativado por padrão.

# Observações

Exibe e ativa a barra de menu especificada com MenuBarName. Este comando funciona em conjunto com DEFINE MENU e DEFINE PAD.

> **Observação:** Quando você inclui a barra de menu do sistema do Visual FoxPro (_MSYSMENU) em um aplicativo, não há necessidade de ativar o menu. Em vez disso, emita SET SYSMENU AUTOMATIC.

# Exemplo

O exemplo a seguir usa ACTIVATE MENU para exibir e ativar um sistema de menu definido pelo usuário. A barra de menu do sistema atual é primeiro salva na memória com SET SYSMENU SAVE e depois todos os títulos de menu do sistema são removidos com SET SYSMENU TO.

Dois títulos de menu são criados com DEFINE PAD; DEFINE POPUP é usado para criar um menu suspenso para cada título de menu. DEFINE BAR é usado para criar itens de menu em cada um dos menus. Quando um título de menu é escolhido, ON PAD usa ACTIVATE POPUP para ativar o menu correspondente. ACTIVATE MENU exibe e ativa a barra de menu.

Quando um item de menu é escolhido em um menu, o procedimento CHOICE é executado. CHOICE exibe o nome do item escolhido e o nome do menu que contém o item.

```foxpro
*** Name this program ACTIMENU.PRG ***
CLEAR
SET SYSMENU SAVE
SET SYSMENU TO
ON KEY LABEL ESC KEYBOARD CHR(13)
DEFINE MENU example BAR AT LINE 1
DEFINE PAD convpad OF example PROMPT '\<Conversions' COLOR SCHEME 3 ;
   KEY ALT+C, ''
DEFINE PAD cardpad OF example PROMPT 'Card \<Info' COLOR SCHEME 3 ;
   KEY ALT+I, ''
ON PAD convpad OF example ACTIVATE POPUP conversion
ON PAD cardpad OF example ACTIVATE POPUP cardinfo
DEFINE POPUP conversion MARGIN RELATIVE COLOR SCHEME 4
DEFINE BAR 1 OF conversion PROMPT 'Ar\<ea' ;
   KEY CTRL+E, '^E'
DEFINE BAR 2 OF conversion PROMPT '\<Length' ;
   KEY CTRL+L, '^L'
DEFINE BAR 3 OF conversion PROMPT 'Ma\<ss' ;
   KEY CTRL+S, '^S'
DEFINE BAR 4 OF conversion PROMPT 'Spee\<d' ;
   KEY CTRL+D, '^D'
DEFINE BAR 5 OF conversion PROMPT '\<Temperature' ;
   KEY CTRL+T, '^T'
DEFINE BAR 6 OF conversion PROMPT 'T\<ime' ;
   KEY CTRL+I, '^I'
DEFINE BAR 7 OF conversion PROMPT 'Volu\<me' ;
   KEY CTRL+M, '^M'
ON SELECTION POPUP conversion DO choice IN actimenu;
   WITH PROMPT(), POPUP()
DEFINE POPUP cardinfo MARGIN RELATIVE COLOR SCHEME 4
DEFINE BAR 1 OF cardinfo PROMPT '\<View Charges' ;
   KEY ALT+V, ''
DEFINE BAR 2 OF cardinfo PROMPT 'View \<Payments' ;
   KEY ALT+P, ''
DEFINE BAR 3 OF cardinfo PROMPT 'Vie\<w Users' ;
   KEY ALT+W, ''
DEFINE BAR 4 OF cardinfo PROMPT '\-'
DEFINE BAR 5 OF cardinfo PROMPT '\<Charges ' ;
   KEY ALT+C, ''
ON SELECTION POPUP cardinfo;
   DO choice IN actimenu WITH PROMPT(), POPUP()
ACTIVATE MENU example
DEACTIVATE MENU example
RELEASE MENU example EXTENDED
SET SYSMENU TO DEFAULT
ON KEY LABEL ESC
PROCEDURE choice
PARAMETERS mprompt, mpopup
WAIT WINDOW 'You chose ' + mprompt + ' from popup ' + mpopup NOWAIT
```
