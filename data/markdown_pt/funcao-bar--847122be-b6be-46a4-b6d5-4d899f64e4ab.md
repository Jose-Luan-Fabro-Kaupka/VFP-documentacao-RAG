# Função BAR( )

Retorna o número do item escolhido mais recentemente de um menu definido com DEFINE POPUP ou um item de menu escolhido de um menu do Visual FoxPro.

```foxpro
BAR()
```

# Valor de retorno

Numeric

# Observações

Cada item em um menu recebe um número com DEFINE BAR. Quando um item de menu é escolhido do menu, BAR( ) retorna o número atribuído a esse item. Um programa pode ramificar para outras rotinas baseado no valor que BAR( ) retorna.

BAR( ) retorna 0 se não houver menu ativo ou se o usuário pressionar ESC para sair do menu.

# Exemplo

O exemplo a seguir usa BAR( ) para passar o número de um item de menu para um procedimento. O menu bar do sistema atual é salvo na memória com SET SYSMENU SAVE, e então todos os títulos de menu do sistema são removidos com SET SYSMENU TO.

Dois títulos de menu são criados com DEFINE PAD; DEFINE POPUP é usado para criar um menu para cada título de menu. DEFINE BAR é usado para criar itens em cada menu. Quando você escolhe um título de menu, ON PAD usa ACTIVATE POPUP para ativar o menu correspondente.

Quando você escolhe um item de um menu, ON SELECTION POPUP usa BAR( ) e POPUP( ) para passar o número do item e o título do menu para o procedimento `choice`. O procedimento `choice` exibe o número do item escolhido e o nome do menu contendo o item, e o menu do sistema Visual FoxPro original é restaurado com SET SYSMENU TO DEFAULT.

```foxpro
*** Name this program BAR_EXAM.PRG ***
CLEAR
SET SYSMENU SAVE
SET SYSMENU TO
DEFINE PAD padConv OF _MSYSMENU ;
   PROMPT '\<Conversions' COLOR SCHEME 3 ;
   KEY ALT+C, ''
DEFINE PAD padCard OF _MSYSMENU ;
   PROMPT 'Card \<Info' COLOR SCHEME 3 ;
   KEY ALT+I, ''
ON PAD padConv OF _MSYSMENU ACTIVATE POPUP popConv
ON PAD padCard OF _MSYSMENU ACTIVATE POPUP popCard
DEFINE POPUP popConv MARGIN RELATIVE COLOR SCHEME 4
DEFINE BAR 1 OF popConv PROMPT 'Ar\<ea' KEY CTRL+E, '^E'
DEFINE BAR 2 OF popConv PROMPT '\<Length' ;
   KEY CTRL+L, '^L'
DEFINE BAR 3 OF popConv PROMPT 'Ma\<ss' ;
   KEY CTRL+S, '^S'
DEFINE BAR 4 OF popConv PROMPT 'Spee\<d' ;
   KEY CTRL+D, '^D'
DEFINE BAR 5 OF popConv PROMPT '\<Temperature' ;
   KEY CTRL+T, '^T'
DEFINE BAR 6 OF popConv PROMPT 'T\<ime' ;
   KEY CTRL+I, '^I'
DEFINE BAR 7 OF popConv PROMPT 'Volu\<me' ;
   KEY CTRL+M, '^M'
*** Here is where the POPCONV menu uses the BAR() function
*** to pass a bar number to the procedure called choice below.
ON SELECTION POPUP popConv;
   DO choice IN bar_exam WITH BAR(), POPUP()
DEFINE POPUP popCard MARGIN RELATIVE COLOR SCHEME 4
DEFINE BAR 1 OF popCard PROMPT '\<View Charges' ;
   KEY ALT+V, ''
DEFINE BAR 2 OF popCard PROMPT 'View \<Payments' ;
   KEY ALT+P, ''
DEFINE BAR 3 OF popCard PROMPT 'Vie\<w Users' ;
   KEY ALT+W, ''
DEFINE BAR 4 OF popCard PROMPT '\-'
DEFINE BAR 5 OF popCard PROMPT '\<Charges ';
   KEY ALT+C
DEFINE BAR 6 OF popCard PROMPT '\-'
DEFINE BAR 7 OF popCard PROMPT 'E\<xit ';
   KEY ALT+X
*** Here is where the POPCARD menu uses the BAR() function
*** to pass a bar number to the procedure called choice below.
ON SELECTION POPUP popCard;
   DO choice IN bar_exam WITH BAR(), POPUP()
*** The procedure choice uses the gnBar parameter
*** to contain the value passed by the BAR() function.
PROCEDURE choice
PARAMETERS gnBar, gcPopup
WAIT WINDOW 'You chose bar #' + LTRIM(STR(gnBar)) + ;
   ' from popup ' + gcPopup NOWAIT
SET SYSMENU TO DEFAULT
```
