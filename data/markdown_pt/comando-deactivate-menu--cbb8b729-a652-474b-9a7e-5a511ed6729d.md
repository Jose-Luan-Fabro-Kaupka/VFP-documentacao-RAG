# Comando DEACTIVATE MENU

Desativa uma barra de menu definida pelo usuário e a remove da tela; mas não remove a definição da barra de menu da memória.

```foxpro
DEACTIVATE MENU MenuName1 [, MenuName2 ...] | ALL
```

#### Parâmetros
 **MenuName1 [, MenuName2 ...]**
Especifica os nomes das barras de menu a desativar. Você pode desativar um conjunto de barras de menu incluindo uma lista de nomes de barras de menu separados por vírgulas.
**ALL**
Desativa todos os menus ativos.

# Observações

DEACTIVATE MENU remove uma barra de menu ativa ou um conjunto de barras de menu da janela principal do Visual FoxPro ou de uma janela definida pelo usuário sem remover a definição da barra de menu da memória. Uma barra de menu pode ser reativada com ACTIVATE MENU e o nome da barra de menu.

> **Dica:** Quando você inclui a barra de menu do sistema (_MSYSMENU) em uma aplicação, você não precisa definir, ativar ou desativar a barra de menu. Em vez disso, emita SET SYSMENU AUTOMATIC.

Para liberar uma barra de menu específica ou um conjunto de barras de menu da memória, use RELEASE MENUS. Você pode liberar todas as barras de menu da memória com CLEAR MENUS ou CLEAR ALL.

O controle do programa retorna à linha do programa imediatamente após a linha que ativou a barra de menu, a menos que DEFINE MENU BAR seja usado para criar a barra de menu ou ACTIVATE MENU NOWAIT seja usado para ativar a barra de menu.

# Exemplo

O exemplo a seguir usa DEACTIVATE MENU para desativar um menu e removê-lo da tela. A barra de menu do sistema atual é salva na memória com SET SYSMENU SAVE, e todos os títulos de menu do sistema são removidos com SET SYSMENU TO.

Dois títulos de menu são criados com DEFINE PAD, e DEFINE POPUP cria um menu para cada título de menu. DEFINE BAR cria itens de menu em cada um dos menus. Quando um título de menu é escolhido, ON PAD usa ACTIVATE POPUP para ativar o menu correspondente. ACTIVATE MENU exibe e ativa a barra de menu.

Quando um item é escolhido de um menu, a procedure CHOICE é executada. CHOICE exibe o nome do item escolhido e o nome do menu que contém o item. O controle do programa continua na linha após ACTIVATE MENU.

Finalmente, o menu é desativado e removido da tela e então é liberado da memória com RELEASE MENUS EXTENDED.

```foxpro
*** Name this program DEACMENU.PRG ***
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
ON SELECTION POPUP conversion DO choice IN deacmenu WITH PROMPT(), POPUP()
DEFINE POPUP cardinfo MARGIN RELATIVE COLOR SCHEME 4
DEFINE BAR 1 OF cardinfo PROMPT '\<View Charges' ;
   KEY ALT+V, ''
DEFINE BAR 2 OF cardinfo PROMPT 'View \<Payments' ;
   KEY ALT+P, ''
DEFINE BAR 3 OF cardinfo PROMPT 'Vie\<w Users' ;
   KEY ALT+W, ''
DEFINE BAR 4 OF cardinfo PROMPT '\-'
DEFINE BAR 5 OF cardinfo PROMPT '\<Charges '
ON SELECTION POPUP cardinfo;
   DO choice IN deacmenu WITH PROMPT(), POPUP()
ACTIVATE MENU example
DEACTIVATE MENU example
RELEASE MENU example EXTENDED
SET SYSMENU NOSAVE
SET SYSMENU TO DEFAULT
ON KEY LABEL ESC
PROCEDURE choice
PARAMETERS mprompt, mpopup
WAIT WINDOW 'You chose ' + mprompt + ;
   ' from popup ' + mpopup NOWAIT
```
