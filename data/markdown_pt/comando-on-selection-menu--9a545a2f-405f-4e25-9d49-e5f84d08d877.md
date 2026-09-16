# Comando ON SELECTION MENU

Especifica um comando que é executado quando você escolhe qualquer título de menu em uma barra de menus.

```foxpro
ON SELECTION MENU MenuBarName | ALL [Command]
```

#### Parâmetros
 **MenuBarName**
Especifica o nome da barra de menus à qual você atribui um comando. O comando é executado quando você escolhe qualquer título de menu da barra de menus. Você pode especificar o nome de uma barra de menus definida pelo usuário criada com DEFINE MENU ou a barra de menus do sistema Microsoft Visual FoxPro _MSYSMENU.
**ALL**
Executa um comando quando você escolhe qualquer título de menu de qualquer barra de menus.
**Command**
Especifica o comando a executar quando você escolhe um título de menu. Use ONSELECTION MENU sem um comando para liberar um comando atribuído a uma barra de menus.

# Observações

Quando você cria e ativa uma barra de menus, coloque ON SELECTION MENU entre DEFINE MENU e ACTIVATE MENU.

Use ON SELECTION PAD para executar um comando quando você escolhe um item de menu específico. ON SELECTION PAD tem precedência sobre ON SELECTION MENU. Use ON PAD para ativar um menu ou barra de menus quando você escolhe um título de menu específico.

Use ON SELECTION MENU sem um comando para liberar um comando atribuído a uma barra de menus.

# Exemplo

No exemplo a seguir, ON SELECTION MENU é usado para executar um procedimento quando um título de menu é escolhido na barra de menus do sistema Visual FoxPro.

A barra de menus do sistema atual é salva na memória com SET SYSMENU SAVE e todos os títulos de menu do sistema são removidos com SET SYSMENU TO.

DEFINE PAD cria vários títulos de menu do sistema. Quando você escolhe um título de menu, o procedimento `choice` atribuído à barra de menus com ON SELECTION MENU é executado. O procedimento `choice` exibe o nome do título de menu que você escolhe e o nome da barra de menus. Se você escolher o título de menu Exit, o menu do sistema Visual FoxPro original é restaurado.

```foxpro
*** Name this program ONMENU.PRG ***
CLEAR
SET SYSMENU SAVE
SET SYSMENU TO
DEFINE PAD padSys OF _MSYSMENU PROMPT '\<System' COLOR SCHEME 3 ;
   KEY ALT+S, ''
DEFINE PAD padEdit OF _MSYSMENU PROMPT '\<Edit' COLOR SCHEME 3 ;
   KEY ALT+E, ''
DEFINE PAD padRecord OF _MSYSMENU PROMPT '\<Record' COLOR SCHEME 3 ;
   KEY ALT+R, ''
DEFINE PAD padWindow OF _MSYSMENU PROMPT '\<Window' COLOR SCHEME 3 ;
   KEY ALT+W, ''
DEFINE PAD padReport OF _MSYSMENU PROMPT 'Re\<ports' COLOR SCHEME 3 KEY ALT+P, ''
DEFINE PAD padExit OF _MSYSMENU PROMPT 'E\<xit' COLOR SCHEME 3 ;
   KEY ALT+X, ''
ON SELECTION MENU _MSYSMENU ;
   DO choice IN onmenu WITH PAD(), MENU()
PROCEDURE choice
PARAMETER gcPad, gcMenu
WAIT WINDOW 'You chose ' + gcPad + ;
   ' from menu ' + gcMenu NOWAIT
IF gcPad = 'PADEXIT'
   SET SYSMENU TO DEFAULT
ENDIF
```
