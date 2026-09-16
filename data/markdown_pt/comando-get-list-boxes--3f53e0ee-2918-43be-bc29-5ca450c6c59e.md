# Comando @ ... GET - List Boxes

Incluído para compatibilidade com versões anteriores. Use o ListBox Control em vez disso.

Cria uma lista.

```foxpro
@ row, column
GET memvar | field
FROM array [RANGE expN1
	[, expN2]]
| POPUP pop-up name
	[FUNCTION expC1]
	| [PICTURE expC2]
	[FONT expC3 [, expN3]]
	[STYLE expC4]
	[DEFAULT expr]
	[SIZE expN4, expN5]
	[ENABLE | DISABLE]
	[MESSAGE expC5]
	[VALID expL1 | expN6]
	[WHEN expL2]
	[COLOR SCHEME expN7
	| COLOR color pair list]
```

#### Parâmetros
 row, column

 Row e column são expressões numéricas with values of 0 or greater that determine where the list appears.

 A primeira linha é o número 0 in the main FoxPro window or a user-defined window. Rows are numbered from top to bottom. In FoxPro for Windows, row 0 is the row immediately under the FoxPro system menu bar. In FoxPro for Macintosh, row 0 is the row immediately under the FoxPro title bar. In FoxPro for MS-DOS, row 0 is the row the FoxPro system menu bar occupies. See SET SYSMENU for information about manipulating the system menu bar so you can place output on row 0 in FoxPro for MS-DOS.

 A primeira coluna é o número 0 in the main FoxPro window or a user-defined window. Columns are numbered from left to right.

 Quando a lista é direcionada a uma janela definida pelo usuário, the row and column coordinates are relative to the user-defined window, not the main FoxPro window.

 In FoxPro for Windows and FoxPro for Macintosh, a position in the main FoxPro window or in a user-defined window is determined by the font of the main FoxPro window or the user-defined window. Most fonts can be displayed in a wide variety of sizes, and some are proportionally spaced. A row corresponds to the height of the current font; a column corresponds to the average width of a letter in the current font.

 In FoxPro for Windows and FoxPro for Macintosh, you can position the list in a window with decimal fractions for row and column coordinates. In FoxPro for MS-DOS, decimal fractions used for row and column coordinates are rounded to the nearest integer value.

 memvar | field

 Quando você escolhe um item de uma lista, a value corresponding to your choice is stored to the memory variable or array element memvar, or the field field. memvar or field must be of numeric or character type. If memvar or field is numeric, the chosen item's position in the list is stored. If memvar or field is character, the chosen item's prompt is stored.

Seleção inicial de opção

 Quando uma lista aparece, the value of memvar or field determines which list option (if any) is initially selected. For example, if the value of memvar or field is 4, the fourth option in the list is selected when the list is activated by READ. If memvar or field doesn't correspond to any of the options in the list (the value is less than 1 or greater than the number of options), no option is initially selected.

FROM array

 A cláusula FROM array cria uma lista a partir de uma matriz. If the array is one-dimensional, the contents of the first array element are the first item in the list, the contents of the second array element are the second item and so on.

 If the array is two-dimensional, the elements in the first column of the array are used to create the list items. The first element in the first column is the first item in the list, the second element in the first column is the second item, and so on.

RANGE expN1 [, expN2]

 Os itens da lista, por padrão, começam com o conteúdo do primeiro elemento da matriz. You can designate a different starting element in the array by including RANGE expN1. For example, if the array is one-dimensional and expN1 is 3, the third element in the array is the first item in the list, the fourth element is the second item, and so on.

 O número de posição de um elemento em uma matriz bidimensional is determined by counting along rows. For example, suppose you create the following 3-by-3 array:

 a b c

 d e f

 g h i

 Elements a, b, and c are in position numbers 1, 2, and 3. Elements d, e, and f are in position numbers 4, 5, and 6, and so on. If a two-dimensional array is used, only elements in the same column as array element expN1 become items in the list. For example, if expN1 is 2, the contents of elements b, e, and h are the list items. If expN1 is 5, only the contents of elements e and h are included.

 Se você incluir um elemento inicial expN1, you can also specify the number of elements in the list by including expN2. If expN2 isn't included, the contents of all array elements from the starting element expN1 through the last element in the column are items in the list.

 Se SHOW GETS for emitido, the RANGE clause is reevaluated. If the value of expN1 or expN2 has changed, the list is updated to reflect the changes.

 O conteúdo de uma lista pode ser alterado dinamicamente. You can insert and remove items by modifying the array. The ACOPY(), ADEL(), ADIR(), AELEMENT(), AFIELDS(), AINS(), ALEN(), ASCAN(), ASORT() and ASUBSCRIPT() functions facilitate the manipulation of arrays.

POPUP pop-up name

 A lista também pode ser construída a partir de um popup created with DEFINE POPUP. Each popup item is used to create an item in the list.

 Para criar uma lista a partir de um popup, first create the popup with DEFINE POPUP. Include in the POPUP popup name clause the name of the popup created with DEFINE POPUP.

 Você pode criar um popup (and thus, a list) containing records from a field in a table (PROMPT FIELDS), files available on disk (PROMPT FILES) or the names of the fields in a table (PROMPT STRUCTURE).

 O exemplo a seguir demonstra como criar uma lista a partir de um popup. DEFINE POPUP is used to create a popup containing the names of table files available on disk. The table names appear as options in the list. MARGIN is included to provide an additional space for the mark character. The SCROLL option places a scroll bar to the right of the list.

 CLEAR

 SET TALK OFF

 STORE 1 TO mchoice

 DEFINE POPUP scrollopts FROM 0, 0 PROMPT FILES LIKE *.DBF ;

 MARGIN SCROLL

 @ 2,2 GET mchoice POPUP scrollopts SIZE 8, 20

 READ && Activate the list.

FUNCTION expC1 | PICTURE expC2

 Para encerrar o READ quando um item é escolhido da lista, include FUNCTION '&T' or PICTURE '@&T'. Include FUNCTION '&N' or PICTURE '@&N' to prevent the READ from terminating when an item is chosen from the list. For example:

 ... FUNCTION '&T' ...

 ... PICTURE '@&T' ...

 Se uma cláusula FUNCTION ou PICTURE não for incluída, the READ isn't terminated when an item is chosen.

 No FoxPro para Macintosh, você pode criar uma lista bidimensional ou tridimensional by including 2 or 3 after the & specification code. Include 2 to create a flat, two-dimensional list identical to lists in Macintosh dialogs. Include 3 to create a three-dimensional list identical to lists in FoxPro for Macintosh dialogs. A two-dimensional list is created by default if you omit the 2 and 3 specification codes.

 No FoxPro para Macintosh, a cláusula a seguir cria uma lista tridimensional and doesn't cause the READ to terminate when an item is chosen from the list.

 ... FUNCTION '&N3' ...

FONT expC3 [, expN3]

 A expressão de caractere expC3 é o nome da fonte, and the numeric expression expN3 is the font size. Por exemplo, a cláusula a seguir pode ser usada para exibir os itens na lista em fonte Courier de 16 pontos:

 FONT 'Courier', 16

 Se você incluir a cláusula FONT, mas omitir o tamanho da fonte expN3, uma fonte de 10 pontos é usada.

 No FoxPro para Windows, se a fonte que você especificar não estiver disponível, a font with similar font characteristics is substituted.

 No FoxPro para Macintosh, se a fonte que você especificar não estiver disponível, the Chicago font is used.

 No FoxPro para MS-DOS, a cláusula FONT é ignorada.

 Se a cláusula FONT for omitida e a lista for colocada na janela principal do FoxPro, the main FoxPro window font is used. If the FONT clause is omitted and the list is placed in a user-defined window, the user-defined window font is used.

STYLE expC4

 No FoxPro para Windows e FoxPro para Macintosh, inclua a cláusula STYLE to specify a font style for the items in the list.

 O estilo da fonte é especificado com expC4. Se a cláusula STYLE for omitida, o estilo de fonte normal é usado.

 No FoxPro para Windows, se o estilo de fonte que você especificar não estiver disponível, a font style with similar characteristics is substituted.

 No FoxPro para Macintosh, se a fonte que você especificar não estiver disponível, the normal font style is used.

 A cláusula STYLE é ignorada no FoxPro para MS-DOS.

 Estilo de fonte do caractere

 --------- ----------

 B Bold

 C Condense*

 E Extend*

 I Italic

 N Normal

 O Outline

 Q Opaque

 S Shadow

 - Strikeout*

 T Transparent

 U Underline

 * Os estilos Condense e Extend estão disponíveis apenas no FoxPro para Macintosh. The Strikeout style is only available in FoxPro for Windows.

 Você pode incluir mais de um caractere para especificar uma combinação de estilos de fonte. For example, the following clause specifies Bold Italic:

 STYLE 'BI'

DEFAULT expr

 Quando você escolhe um item da lista, sua escolha é salva in a memory variable, array element or field you specified. If you specify a memory variable that doesn't exist, it is automatically created and initialized if you include the DEFAULT clause. However, an array element isn't created if you specify an array element in a DEFAULT clause. The DEFAULT clause is ignored if the memory variable already exists or you specify a field.

 -------------------------------

 Observação - Se a cláusula DEFAULT for omitida and the memory variable memvar doesn't exist, the error message "Variable not found" appears.

 -------------------------------

 A expressão DEFAULT expr determina o tipo de variável de memória created and its initial value. expr must be of numeric or character type.

SIZE expN4, expN5

 A largura da lista é, por padrão, determinada pela largura do texto do item mais longo in the list. The number of items in the pop-up or array by default determines the number of items displayed in the list. You can optionally specify the length and width of the list by including SIZE. The length of the list in rows is specified by expN4, and the width of the list in columns is specified by expN5.

 Se houver mais itens do que podem ser exibidos na lista de uma vez, a scroll bar is automatically placed to the right of the list items.

 No FoxPro para Windows e FoxPro para Macintosh, a fonte da lista determina o tamanho of the editing region. The list's font is specified with the FONT clause. If the FONT clause is omitted, the list uses the font of its parent window (the main FoxPro window or a user-defined window).

ENABLE | DISABLE

 As listas são habilitadas por padrão quando READ é emitido. You can prevent a list from being activated when READ is issued by including DISABLE. A disabled list cannot be selected and appears in disabled colors. Use SHOW GET ENABLE to enable a disabled list.

MESSAGE expC5

 A expressão de caractere expC5 da cláusula MESSAGE aparece quando uma lista é selecionada. In FoxPro for MS-DOS, the message is centered on the last line of the main FoxPro window and the message location can be changed with SET MESSAGE.

 In FoxPro for Windows and FoxPro for Macintosh, the message is placed in the graphics-based status bar. If the graphics-based status bar has been turned off with SET STATUS BAR OFF, the message is placed on the last line of the main FoxPro window.

VALID expL1 | expN6

 Você pode incluir uma expressão VALID opcional expL1 or expN6 that is evaluated when an option is chosen from the list. That is, VALID isn't evaluated when you select an item, but when you actually choose an item by selecting it and pressing Enter or double-clicking on the item.

 Normalmente, expL1 ou expN6 é uma função definida pelo usuário (UDF). With a user-defined function you can select, enable or disable other @ ... GET input fields or objects, open a Browse window, open another data-entry screen or move to a new record. CLEAR READ can be included in the user-defined function to terminate the READ.

 expL1

 Quando um valor lógico é retornado à cláusula VALID, the logical value is ignored and the list remains the current control. However, you can specify a UDF that returns a logical value to the VALID clause and then activates another object.

 expN6

 Uma cláusula VALID que inclui uma expressão numérica é usada para especificar qual objeto é ativado after an item in the list is chosen. Objects are @ ... GET input fields, check boxes, lists, popups, spinners, text-editing regions and each individual button in a set of push, radio and invisible buttons.

 A expressão numérica expN6 tem um destes efeitos:

  Quando expN6 = 0, a lista permanece o controle ativo.

  Quando expN6 é positivo, expN6 indicates the number of objects to advance. For example, when the list is selected and VALID returns 1, the next object is activated. If expN6 is greater than the number of objects remaining, the READ is terminated (unless READ CYCLE is issued to activate the objects).

  Quando expN6 é negativo, expN6 specifies the number of objects to move back. For example, when you're positioned on a list and VALID returns -1, the previous object is activated. If expN6 moves back past the first object, the READ is terminated (unless READ CYCLE is issued to activate the objects).

WHEN expL2

 A cláusula WHEN permite ou proíbe a seleção de uma lista based on the logical value of expL2, which must evaluate to a logical true (.T.) before any of the list can be selected. If expL2 evaluates to a logical false (.F.), the list cannot be selected and is skipped over if placed between other objects.

COLOR SCHEME expN7 | COLOR color pair list

 Se você não incluir uma cláusula COLOR, the list's colors are determined by the color scheme for the main FoxPro window; if a list is placed in a user-defined window, the window's color scheme determines the list's colors.

 As cores de uma lista podem ser especificadas by including the number of an existing color scheme in the COLOR SCHEME clause or a set of color pairs in the COLOR clause.

 Um esquema de cores é um conjunto de 10 pares de cores predefinidos. The color pairs in a color scheme can be changed with SET COLOR OF SCHEME. In FoxPro for MS-DOS the color pairs in a color scheme can also be changed in the Color Picker.

 Um par de cores é um conjunto de duas letras separadas por uma barra. The first letter specifies the foreground color and the second letter specifies the background color.

 Por exemplo, este par de cores especifica um primeiro plano vermelho em um fundo branco:

 R/W

 Para uma lista de cores e suas letras de cor correspondentes, see SET COLOR Overview or Color Table by Color Pair.

 Um par de cores também pode ser especificado com um conjunto de seis valores RGB (Red Green Blue) color values separated by commas. The first three color values specify the foreground color and the second three color values specify the background color. The color values can range from 0 through 255.

 The R/W color pair in the example above can also be specified with this RGB color pair:

 RGB(255,0,0,255,255,255)

 Lista de pares de cores

 Número Atributo

 ---------- ---------

 1 Opção desabilitada

 2 Opção habilitada

 3 Borda e barra de rolagem*

 5 Message

 6 Item de lista selecionado

 9 Lista habilitada

 10 Lista desabilitada

 * Controles desenhados na cor de fundo.

 Barra desenhada em tom reduzido da cor de primeiro plano.

 Este exemplo usa a matriz criada no exemplo anterior to override the color scheme of the main FoxPro window with another predefined color scheme:

 ACTIVATE SCREEN

 CLEAR

 SET TALK OFF

 STORE 1 TO mchoice

 DEFINE POPUP scrollopts FROM 0,0 PROMPT FILES LIKE *.DBF ;

 MARGIN SCROLL COLOR SCHEME 4

 @ 2,2 GET mchoice POPUP scrollopts SIZE 8, 20

 READ && Activate the list

 O exemplo a seguir, que usa a matriz criada em um exemplo acima, define uma lista com as seguintes características de cor:

  Um item de lista selecionado é mostrado em branco brilhante em fundo azul (W+/B).

  Uma lista habilitada é mostrada com opções amarelas em fundo azul (GR+/B).

  Uma lista desabilitada é mostrada com opções brancas em fundo azul (W/B).

 Quando você pula um par de cores, deve incluir uma vírgula onde o par de cores estaria.

 Aqui estão os comandos:

 CLEAR

 SET TALK OFF

 STORE 1 TO mchoice

 DEFINE POPUP scrollopts FROM 0,0 PROMPT FILES LIKE *.DBF ;

 MARGIN SCROLL COLOR ,GR+/B,,,,W+/B,,,,W/B

 @ 2,2 GET mchoice POPUP scrollopts SIZE 8, 20

 READ && Activate the list

# Observações

Esta variação de @ ... GET cria uma lista. Uma lista é um conjunto de itens dos quais você pode escolher um item. Para escolher um item de uma lista, selecione o item e pressione Enter ou clique duas vezes no item.

Se você usar o Screen Builder para criar suas telas de entrada de dados, you might not have to use this command at all. The Screen Builder automatically generates the commands that create lists.

A lista aparece dentro de uma caixa, often with a scroll bar to the right. The scroll bar lets you move quickly through the items with the mouse and provides a visual indication of your position in the list. Outra maneira rápida de se mover na lista é pressionar a tecla Home to go to the first item, or the End key to go to the last item. This method works even if the list does not have a scroll bar.

Os itens na lista são obtidos de uma matriz ou de um popup. Inclua FROM array para construir a partir de uma matriz. Inclua POPUP pop-up name para construir a lista a partir de um popup criado com DEFINE POPUP.

Emita READ ou READ CYCLE para ativar a lista.

# Exemplo

```foxpro
SET TALK OFF
DEFINE WINDOW example FROM 4,3 TO 21,76 TITLE ' List Example ' ;
	FLOAT SHADOW SYSTEM COLOR SCHEME 8
*** Fill the array cityarray with city data ***
SELECT DISTINCT city FROM customer INTO ARRAY cityarray
SELECT customer
*** Define a pop-up that contains the structure of customer ***
DEFINE POPUP popstru PROMPT STRUCTURE SCROLL MARGIN MARK CHR(16)
*** Define a pop-up containing data from the company field ***
DEFINE POPUP popfield PROMPT FIELD company SCROLL MARGIN MARK CHR(16)
ACTIVATE WINDOW example
@ 1,3 SAY 'Structure Popup:'
*** Get information using predefined popstru pop-up ***
@ 2,2 GET liststructure POPUP popstru SIZE 11, 20;
	DEFAULT FIELD(1,'customer') WHEN refresh();
	VALID dispitem(liststructure) COLOR SCHEME 9
@ 13,3 SAY liststructure SIZE 1, 18
@ 1,26 SAY 'Field Popup:'
*** Get information using predefined popfield pop-up ***
@ 2,25 GET listfield POPUP popfield SIZE 11, 20 ;
	DEFAULT company WHEN refresh() VALID dispitem(listfield);
	COLOR SCHEME 9
@ 13,26 SAY listfield SIZE 1, 18
@ 1,50 SAY 'Array of City Names:'
*** Get information using predefined array ***
@ 2,49 GET arrayitem FROM cityarray SIZE 11, 20 ;
	DEFAULT cityarray(1) WHEN refresh() VALID dispitem(arrayitem);
	COLOR SCHEME 9
@ 13,50 SAY arrayitem SIZE 1,18
@ 14.5,63 GET ok FUNCTION '*t \!OK' DEFAULT 1 SIZE 1, 6
READ CYCLE SHOW popshow()  && Activate gets
RELEASE WINDOW example
RELEASE POPUPS popstru, popfield
FUNCTION refresh
*** Refresh window information without calling subroutine ***
SHOW GETS OFF
FUNCTION dispitem
*** Display which item has been chosen ***
PARAMETER item
WAIT WINDOW 'You have chosen: ' + ALLTRIM(item) NOWAIT
	FUNCTION popshow
*** Display current items for each list ***
@ 13,3 SAY liststructure	SIZE 1, 18
@ 13,26 SAY listfield		SIZE 1, 18
@ 13,50 SAY arrayitem		SIZE 1, 18
```
