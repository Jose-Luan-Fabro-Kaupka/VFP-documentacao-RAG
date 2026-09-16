# Comando ACTIVATE POPUP

Exibe e ativa um menu.

```foxpro
ACTIVATE POPUP MenuName   [AT nRow, nColumn]
[BAR nMenuItemNumber]   [NOWAIT]   [REST]
```

#### Parâmetros
 **MenuName**
Especifica o nome do menu a ser ativado.
**AT nRow , nColumn**
Especifica a posição do menu na tela ou em uma janela definida pelo usuário. As coordenadas de linha e coluna se aplicam ao canto superior esquerdo do menu. A posição especificada com esse argumento tem precedência sobre uma posição especificada com o argumento FROM em DEFINE POPUP.
**BAR nMenuItemNumber**
Especifica o item do menu selecionado quando o menu é ativado. Por exemplo, se nMenuItemNumber for 2, o segundo item será selecionado. O primeiro item será selecionado se você omitir BAR nMenuItemNumber ou se nMenuItemNumber for maior que o número de itens do menu.
**NOWAIT**
Especifica que, em tempo de execução, um programa não aguarda que o usuário escolha um item do menu antes de continuar sua execução. Em vez disso, o programa continua sendo executado.
**REST**
Um menu criado com a cláusula PROMPT FIELD de DEFINE POPUP insere no menu registros de um campo. Quando o menu é ativado, o primeiro item é selecionado inicialmente, mesmo que o ponteiro de registro da tabela que contém o campo esteja posicionado em um registro diferente do primeiro. Inclua REST para especificar que o item selecionado quando o menu é ativado corresponde à posição atual do ponteiro de registro na tabela.

# Observações

ACTIVATE POPUP funciona em conjunto com DEFINE POPUP, usado para criar o menu, e DEFINE BAR, usado para criar os itens do menu.

# Exemplo

Este exemplo usa ACTIVATE POPUP com ON PAD para ativar um menu quando um título de menu é escolhido. A barra de menus atual do sistema é primeiro salva na memória com SET SYSMENU SAVE e, em seguida, todos os títulos de menu do sistema são removidos com SET SYSMENU TO.

Dois novos títulos de menu do sistema são criados com DEFINE PAD; DEFINE POPUP é usado para criar um menu para cada título. DEFINE BAR é usado para criar itens em cada menu. Quando um título de menu é escolhido, ON PAD usa ACTIVATE POPUP para ativar o menu correspondente.

Quando um item é escolhido em um menu, o procedimento CHOICE é executado. CHOICE exibe o nome do item escolhido e o nome do menu que contém o item. Se o item Exit for escolhido no menu Card Info, o menu original do sistema do Visual FoxPro será restaurado.

```foxpro
*** Name this program ACTIPOP.PRG ***
CLEAR
SET SYSMENU SAVE
SET SYSMENU TO
DEFINE PAD convpad OF _MSYSMENU PROMPT '\<Conversions' COLOR SCHEME 3 ;
   KEY ALT+C, ''
DEFINE PAD cardpad OF _MSYSMENU PROMPT 'Card \<Info' COLOR SCHEME 3 ;
   KEY ALT+I, ''
ON PAD convpad OF _MSYSMENU ACTIVATE POPUP conversion
ON PAD cardpad OF _MSYSMENU ACTIVATE POPUP cardinfo
DEFINE POPUP conversion MARGIN RELATIVE COLOR SCHEME 4
DEFINE BAR 1 OF conversion PROMPT 'Ar\<ea' KEY CTRL+E, '^E'
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
ON SELECTION POPUP conversion;
   DO choice IN actipop WITH PROMPT(), POPUP()
DEFINE POPUP cardinfo MARGIN RELATIVE COLOR SCHEME 4
DEFINE BAR 1 OF cardinfo PROMPT '\<View Charges' ;
   KEY ALT+V, ''
DEFINE BAR 2 OF cardinfo PROMPT 'View \<Payments' ;
   KEY ALT+P, ''
DEFINE BAR 3 OF cardinfo PROMPT 'Vie\<w Users' ;
   KEY ALT+W, ''
DEFINE BAR 4 OF cardinfo PROMPT '\-'
DEFINE BAR 5 OF cardinfo PROMPT '\<Charges' ;
   KEY ALT+C, ''
DEFINE BAR 6 OF cardinfo PROMPT '\-'
DEFINE BAR 7 OF cardinfo PROMPT 'E\<xit';
   KEY ALT+X, ''
ON SELECTION POPUP cardinfo;
DO choice IN actipop WITH PROMPT(),POPUP()
PROCEDURE choice
PARAMETERS mprompt, mpopup
WAIT WINDOW 'You chose ' + mprompt + ;
   ' from popup ' + mpopup NOWAIT
IF mprompt = 'Exit'
   SET SYSMENU TO DEFAULT
ENDIF
```
