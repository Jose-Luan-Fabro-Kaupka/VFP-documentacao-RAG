# Função MRKPAD( )

Determina se um título de menu em uma barra de menu definida pelo usuário ou na barra de menu do sistema do Visual FoxPro está marcado.

```foxpro
MRKPAD(cMenuBarName, cMenuTitleName)
```

#### Parâmetros
 **cMenuBarName**
Especifica o nome da barra de menu que contém o título do menu.
**cMenuTitleName**
Especifica o nome do título do menu.

# Valor de retorno

Logical

# Observações

Use SET MARK OF para marcar ou desmarcar um título de menu.

Se o título de menu especificado estiver marcado, MRKPAD( ) retorna verdadeiro (.T.); caso contrário, MRKPAD( ) retorna falso (.F.).

# Exemplo

O seguinte programa de exemplo, chamado MARKPAD.PRG, usa MRKPAD( ) para alternar o caractere de marca de um título de menu quando você o escolhe.

A barra de menu do sistema atual é salva na memória com SET SYSMENU SAVE, e todos os itens de menu do sistema são removidos com SET SYSMENU TO.

Vários itens de menu do sistema são criados com DEFINE PAD. Quando você escolhe um item de menu, o procedimento `choice` é executado. `choice` exibe o nome do item de menu que você escolheu e o nome da barra de menu. SET MARK OF é usado com MRKPAD( ) para exibir ou remover o caractere de marca do item de menu. Se você escolher o menu Exit, o menu do sistema original do Visual FoxPro é restaurado.

```foxpro
*** Name this program MARKPAD.PRG ***
CLEAR
SET SYSMENU SAVE
SET SYSMENU TO
SET MARK OF MENU _MSYSMENU TO CHR(4)
PUBLIC glMarkPad
glMarkPad = .T.
DEFINE PAD padSys OF _MSYSMENU PROMPT '\<System'  COLOR SCHEME 3 ;
   KEY ALT+S, ''
DEFINE PAD padEdit OF _MSYSMENU PROMPT '\<Edit'  COLOR SCHEME 3 ;
   KEY ALT+E, ''
DEFINE PAD padRecord OF _MSYSMENU PROMPT '\<Record'  COLOR SCHEME 3 ;
   KEY ALT+R, ''
DEFINE PAD padWindow OF _MSYSMENU PROMPT '\<Window'  COLOR SCHEME 3 KEY ALT+W, ''
DEFINE PAD padReport OF _MSYSMENU PROMPT 'Re\<ports' COLOR SCHEME 3 ;
   KEY ALT+P, ''
DEFINE PAD padExit OF _MSYSMENU PROMPT 'E\<xit'  COLOR SCHEME 3 ;
   KEY ALT+X, ''
ON SELECTION MENU _MSYSMENU ;
   DO choice IN markpad WITH PAD(), MENU()
PROCEDURE choice
PARAMETER gcPad, gcMenu
WAIT WINDOW 'You chose ' + gcPad + ;
   ' from menu ' + gcMenu NOWAIT
SET MARK OF PAD (gcPad) OF _MSYSMENU TO ;
   ! MRKPAD('_MSYSMENU', gcPad)
glMarkPad= ! glMarkPad
IF gcPad = 'PADEXIT'
   SET SYSMENU TO DEFAULT
ENDIF
```
