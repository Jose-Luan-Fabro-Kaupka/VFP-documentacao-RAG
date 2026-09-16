# Comando ON BAR

Especifica um menu ou barra de menu que é ativado quando você escolhe um item de menu específico em um menu.

```foxpro
ON BAR nMenuItemNumber OF MenuName1   [ACTIVATE POPUP MenuName2
   | ACTIVATE MENU MenuBarName]
```

#### Parâmetros
 **nMenuItemNumber OF MenuName1**
Especifica o número do item de menu e o menu do item de menu que ativa outro menu ou barra de menu. Cada item em um menu pode ter outro menu ou barra de menu atribuído a ele. Um item de menu com um menu ou barra de menu atribuído tem uma seta colocada à direita do item de menu. A seta indica que escolher esse item de menu ativa um menu ou barra de menu adicional. Um espaço adicional para a seta do submenu em cascata é colocado à direita de cada item se você definir o menu com DEFINE POPUP ... MARGIN . Se você criar o menu sem a cláusula MARGIN, a seta do submenu em cascata pode sobrepor o último caractere do item de menu.
**ACTIVATE POPUP MenuName2**
Especifica o nome do menu a ser ativado quando o item de menu é escolhido. Use ON BAR sem ACTIVATE POPUP para liberar um menu de um item de menu.
**ACTIVATE MENU MenuBarName**
Especifica o nome da barra de menu a ser ativada quando o item de menu é escolhido. Use ON BAR sem ACTIVATE MENU para liberar uma barra de menu de um item de menu.

# Observações

Um menu que exibe e ativa outro menu é chamado submenu em cascata. Use ON SELECTION BAR ou ON SELECTION POPUP para executar um comando quando um item é escolhido em um menu.

Os menus e a barra de menu podem ser definidos pelo usuário (criados com DEFINE POPUP e DEFINE MENU) ou parte do sistema de menus do Visual FoxPro.

# Exemplo

O exemplo a seguir demonstra um sistema de submenus em cascata. Uma barra de menu chamada `mnuDinner` é criada com dois títulos de barra de menu. Cada título usa ON PAD para ativar o menu chamado `popMainCourse` ou `popDessert`. Os menus chamados `popMainCourse` e `popDessert` têm menus adicionais chamados `popBurger`, `popPizza` e `popPie` atribuídos às suas listas de itens com três comandos ON BAR. Os itens `popOlives` e `popPie` têm menus adicionais atribuídos com dois comandos ON BAR.

Quando você faz uma seleção, ON SELECTION POPUP ALL executa um procedimento chamado `yourchoice` que ativa uma janela e exibe sua escolha. A escolha é determinada com POPUP( ) e PROMPT( ), que retornam o nome do menu e o conteúdo (texto) do item de menu.

```foxpro
DEFINE WINDOW wOrder FROM 10,0 TO 13,39
DEFINE MENU mnuDinner
DEFINE PAD padOne OF mnuDinner PROMPT '\<Main Course' KEY ALT+M, ''
DEFINE PAD padTwo OF mnuDinner PROMPT '\<Dessert'   KEY ALT+D, ''
ON PAD padOne OF mnuDinner ACTIVATE POPUP popMainCourse
ON PAD padTwo OF mnuDinner ACTIVATE POPUP dessert
DEFINE POPUP popMainCourse MARGIN MESSAGE ;
   'We have burgers and pizza today'
DEFINE BAR 1 OF popMainCourse PROMPT '\<Hamburgers'
DEFINE BAR 2 OF popMainCourse PROMPT '\<Pizza'
ON BAR 1 OF popMainCourse ACTIVATE POPUP burger
ON BAR 2 OF popMainCourse ACTIVATE POPUP pizza
DEFINE POPUP burger MARGIN MESSAGE ;
   'What would you like on your burger?'
DEFINE BAR 1 OF burger PROMPT '\<Ketchup'
DEFINE BAR 2 OF burger PROMPT '\<Mustard'
DEFINE BAR 3 OF burger PROMPT '\<Onions'
DEFINE BAR 4 OF burger PROMPT '\<Pickles'
DEFINE POPUP pizza MARGIN MESSAGE ;
   'Here are the available toppings'
DEFINE BAR 1 OF pizza PROMPT '\<Anchovies'
DEFINE BAR 2 OF pizza PROMPT '\<Green Peppers'
DEFINE BAR 3 OF pizza PROMPT '\<Olives'
DEFINE BAR 4 OF pizza PROMPT '\<Pepperoni'
ON BAR 3 OF pizza ACTIVATE POPUP olives
DEFINE POPUP olives MARGIN
DEFINE BAR 1 OF olives PROMPT '\<Black' MESSAGE 'Black olives?'
DEFINE BAR 2 OF olives PROMPT '\<Green' MESSAGE 'Green olives?'
DEFINE POPUP dessert MARGIN MESSAGE 'Our dessert offerings'
DEFINE BAR 1 OF dessert PROMPT '\<Brownies'
DEFINE BAR 2 OF dessert PROMPT '\<Cookies'
DEFINE BAR 3 OF dessert PROMPT '\<Ice Cream'
DEFINE BAR 4 OF dessert PROMPT '\<Pie'
ON BAR 4 OF dessert ACTIVATE POPUP pie
DEFINE POPUP pie MARGIN MESSAGE 'What kind of pie?'
DEFINE BAR 1 OF pie PROMPT '\<Blueberry'
DEFINE BAR 2 OF pie PROMPT '\<Cherry'
DEFINE BAR 3 OF pie PROMPT '\<Peach'
DEFINE BAR 4 OF pie PROMPT '\<Rhubarb'
ON SELECTION POPUP ALL DO yourchoice
ACTIVATE MENU mnuDinner
PROCEDURE yourchoice
ACTIVATE WINDOW wOrder
CLEAR
DO CASE
   CASE POPUP() = 'BURGER'
      @ 0,0 SAY 'A ' + POPUP() + ' order:'
      @ 1,0 SAY 'You ordered a burger with ' + LOWER(PROMPT())
   CASE POPUP() = 'PIZZA'
      @ 0,0 SAY 'A ' + POPUP() + ' order:'
      @ 1,0 SAY 'You ordered a pizza with ' + LOWER(PROMPT())
   CASE POPUP() = 'OLIVES'
      @ 0,0 SAY 'A ' + POPUP() + ' order:'
      @ 1,0 SAY 'You ordered a pizza with ' ;
         + LOWER(PROMPT()) + ' olives'
   CASE POPUP() = 'DESSERT'
      @ 0,0 SAY 'A ' + POPUP() + ' order:'
      @ 1,0 SAY 'You ordered ' + LOWER(PROMPT()) + ' for dessert'
   CASE POPUP() = 'PIE'
      @ 0,0 SAY 'A ' + POPUP() + ' order:'
      @ 1,0 SAY 'You ordered ' + LOWER(PROMPT()) + ' pie'
ENDCASE
WAIT WINDOW
DEACTIVATE WINDOW wOrder
RETURN
```
