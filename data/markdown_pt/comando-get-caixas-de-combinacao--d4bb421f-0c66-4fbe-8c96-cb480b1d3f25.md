# Comando @ ... GET - Caixas de combinação

Incluído para compatibilidade com versões anteriores. Use o controle ComboBox.

Cria um pop-up.

```foxpro
@ row, column
GET memvar | field
FUNCTION expC1 | PICTURE expC2
	[FONT expC3 [, expN1]]
	[STYLE expC4]
	[DEFAULT expr]
	[FROM array]
	[RANGE expN2 [, expN3]]
	[SIZE expN4, expN5]
	[ENABLE | DISABLE]
	[MESSAGE expC5]
	[VALID expL1 | expN6]
	[WHEN expL2]
	[COLOR SCHEME expN7
		[, expN8]
	| COLOR color pair list]
```

#### Parâmetros
 row, column

 Row e column são expressões numéricas com valores de 0 ou maior que determinam onde a lista aparece.

 A primeira linha é o número 0 na janela principal do FoxPro ou em uma janela definida pelo usuário. As linhas são numeradas de cima para baixo. In FoxPro for Windows, row 0 is the row immediately under the FoxPro system menu bar. In FoxPro for Macintosh, row 0 is the row immediately under the FoxPro title bar. In FoxPro for MS-DOS, row 0 is the row the FoxPro system menu bar occupies. See SET SYSMENU for information about manipulating the system menu bar so you can place output on row 0 in FoxPro for MS-DOS.

 A primeira coluna é o número 0 na janela principal do FoxPro ou em uma janela definida pelo usuário. As colunas são numeradas da esquerda para a direita.

 When the list is directed to a user-defined window, the row and column coordinates are relative to the user-defined window, not the main FoxPro window.

 In FoxPro for Windows and FoxPro for Macintosh, a position in the main FoxPro window or in a user-defined window is determined by the font of the main FoxPro window or the user-defined window. Most fonts can be displayed in a wide variety of sizes, and some are proportionally spaced. A row corresponds to the height of the current font; a column corresponds to the average width of a letter in the current font.

 In FoxPro for Windows and FoxPro for Macintosh, you can position the list in a window with decimal fractions for row and column coordinates. In FoxPro for MS-DOS, decimal fractions used for row and column coordinates are rounded to the nearest integer value.

 memvar | field

 Quando você escolhe uma opção do pop-up, sua escolha é armazenada na variável de memória ou elemento de matriz especificado com memvar ou em um campo especificado com field. If you press Esc to exit the popup, the value of memvar or field isn't changed.

 memvar or field must be of numeric or character type. If memvar or field is character, the prompt of the item you choose is stored to memvar. If memvar or field is numeric, the number representing the position of the item in the popup is stored to memvar or field.

 Seleção inicial de opção

 Quando um pop-up aparece, o valor de memvar ou field determina qual opção do pop-up (se houver) é exibida inicialmente na face do pop-up.

 If memvar or field is numeric, the option in the specified numeric position in the list of options is initially displayed on the face of the popup. For example, if the memory variable, array element or field contains 1, the first popup option you specify is initially displayed. If the value of memvar or field doesn't correspond to any of the popup options (the value is less than 1 or greater than the number of options), the face of the popup is initially blank.

 If memvar or field is of character type, a case-sensitive comparison is made between memvar or field and each popup option. When the comparison is made, all special characters and any leading or trailing spaces are ignored. If a match is found, the matching option is initially displayed on the face of the popup. If a match isn't found, the character value of memvar or field is initially displayed on the face of the popup and is added as a temporary option at the end of the list of options.

 FUNCTION expC1 | PICTURE expC2

 Ao criar pop-ups, você deve incluir a cláusula FUNCTION, a cláusula PICTURE ou ambas. There is no advantage to any of the three methods. The FUNCTION or PICTURE clause contains the popup specification code ^ and the set of popup options.

 As opções também podem ser especificadas na cláusula FROM array. If the options are specified there, you do not need to include them in the FUNCTION or PICTURE clause.

 However, if you include FROM array, ^ must still be included in the FUNCTION or PICTURE clause.

 The FUNCTION character expression expC1 must begin with ^. To create the options that appear in the popup list, include a space after ^ followed by a list of options separated by semicolons. The following example creates the option prompts Cash, Charge, Net 30 and Net 60:

 ... FUNCTION '^ Cash;Charge;Net 30;Net 60' ...

 The PICTURE character expression expC2 uses the same syntax as the FUNCTION character expression except the PICTURE expression must begin with @ followed by ^.

 For example, the following PICTURE clause creates the option prompts Cash, Charge, Net 30 and Net 60:

 ... PICTURE '@^ Cash;Charge;Net 30;Net 60' ...

 You can also include both the FUNCTION and PICTURE clauses to create popups. If both are included, the FUNCTION character expression expC1 must contain ^ to create the popup, and can also include a space and the popup options. The PICTURE character expression expC2 can include prompts to create additional options.

 The following examples illustrate the various forms of syntax you can use to create a popup. In all the examples, a popup is placed in the second row and column. It contains four options with the prompts Cash, Charge, Net 30 and Net 60. It is initialized by the memory variable MCHOICE. When you choose one of the options from the popup, your choice is stored to MCHOICE.

 FUNCTION clause only:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '^ Cash;Charge;Net 30;Net 60'

 READ

 STORE 1 TO mchoice

 STORE '^ Cash;Charge;Net 30;Net 60' TO mfunc

 @ 2,2 GET mchoice FUNCTION mfunc

 READ

 PICTURE clause only:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice PICTURE '@^ Cash;Charge;Net 30;Net 60'

 READ

 STORE 1 TO mchoice

 @ 2,2 GET mchoice PICTURE '@^' + ' Cash;Charge;Net 30;Net 60'

 READ

 FUNCTION and PICTURE clauses:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '^' ;

 PICTURE ' Cash;Charge;Net 30;Net 60'

 READ

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '^ Cash;Charge' ;

 PICTURE ';Net 30;Net 60'

 READ

 Opções PICTURE e FUNCTION N, T, 2 e 3

 Additional options can be placed after the caret ()^ ) specification code in the FUNCTION or PICTURE clause to modify the behavior (N and T) and appearance (2 and 3) of the popup.

 The 2 (two-dimensional) and 3 (three-dimensional) specification codes are only available in FoxPro for Macintosh.

 Option Description

 ------ -----------

 N Does not terminate the READ when an option is chosen. This is the default behavior.

 T Terminates the READ when an option is chosen.

 2 Creates a flat (two-dimensional) popup identical to popups in Macintosh dialogs. This is the default popup in FoxPro for Macintosh.

 3 Creates a three-dimensional popup identical to popups in FoxPro for Macintosh dialogs.

 Popup Options with Special Features

 When defining a prompt, you can assign special characteristics to a popup option. For example, you can assign a hot key to the option or disable the option by including special characters.

 Teclas de atalho

 No FoxPro for MS-DOS, uma tecla de atalho é uma letra destacada em um prompt que você pode digitar para escolher imediatamente uma opção em um pop-up aberto. To assign a hot key, place a backslash and a less-than sign (\<) before the desired character of the popup option.

 In FoxPro for Windows, a hot key is an underlined letter on a prompt that you can type to immediately choose an option on the popup. The popup doesn't have to be open to choose an option with a hot key if KEYCOMP is set to WINDOWS.

 In FoxPro for Macintosh, if KEYCOMP is set to MAC (the default), hot keys aren't highlighted or underlined. If KEYCOMP is set to DOS or WINDOWS, hot keys are underlined.

 The following example assigns the hot keys C and R to the Cash and Charge options, respectively:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '^ \<Cash;Cha\<rge;Net 30;Net 60'

 READ

 Opções desabilitadas

 Você pode desabilitar uma opção para que não possa ser escolhida. Opções desabilitadas são exibidas nas cores desabilitadas. To disable a popup option, place a backslash (\) before the option. To disable the entire popup, include the DISABLE keyword.

 The Charge option is disabled in this example:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '^ Cash;\Charge;Net 30;Net 60'

 READ

 FONT expC3 [, expN1]

 The character expression expC3 is the name of the font, and the numeric expression expN1 is the font size. For example, the following clause can be used to display the options in the popup in 16-point Courier font:

 FONT 'Courier', 16

 If you include the FONT clause but omit the font size expN1, a 10-point font is used.

 In FoxPro for Windows, if the font you specify is not available, a font with similar font characteristics is substituted.

 In FoxPro for Macintosh, if the font you specify is not available, the Chicago font is used.

 In FoxPro for MS-DOS, the FONT clause is ignored.

 If the FONT clause is omitted and the popup is placed in the main FoxPro window, the main FoxPro window font is used. If the FONT clause is omitted and the popup is placed in a user-defined window, the user-defined window font is used.

 STYLE expC4

 In FoxPro for Windows and FoxPro for Macintosh, include the STYLE clause to specify a font style for the options in the popup.

 The font style is specified with expC4. If the STYLE clause is omitted, the normal font style is used.

 In FoxPro for Windows, if the font style you specify is not available, a font style with similar characteristics is substituted.

 In FoxPro for Macintosh, if the font you specify is not available, the normal font style is used.

 The STYLE clause is ignored in FoxPro for MS-DOS.

 Character Font Style

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

 * The Condense and Extend styles are only available in FoxPro for Macintosh. The Strikeout style is only available in FoxPro for Windows.

 You can include more than one character to specify a combination of font styles. For example, the following specifies Bold Italic:

 STYLE 'BI'

 DEFAULT expr

 When you choose an option from a popup, your choice is saved in the memory variable, array element or field you specify. If you specify a memory variable that doesn't exist, it is automatically created and initialized if you include the DEFAULT clause. However, an array element isn't created if you specify an array element in a DEFAULT clause. The DEFAULT clause is ignored if the memory variable already exists or you specify a field.

 -------------------------------

 Note - If the DEFAULT clause isn't included and the memory variable memvar doesn't exist, the error message "Variable not found" appears.

 -------------------------------

 The DEFAULT expression expr determines the type of memory variable created and its initial value. expr must be a numeric or character expression. Here are examples of DEFAULT clauses for popups:

 @ 2,2 GET mchoice FUNCTION '^ Cash;Charge;Net 30;Net 60' ;

 DEFAULT 'Cash'

 READ

 @ 2,2 GET mchoice FUNCTION '^ Cash;Charge;Net 30;Net 60';

 DEFAULT 3

 READ

 FROM array

 The FROM array clause can be included to create the popup options from a predefined array. If you create popup options with FROM array, you must still specify @^ in the PICTURE clause or ^ in the FUNCTION clause. For example:

 ... FROM marray PICTURE '@^' ...

 ... FROM marray FUNCTION '^' ...

 If FROM array is included, any option prompts specified in the PICTURE or FUNCTION clause are ignored.

 The options that appear in the popup are taken from the elements of the array you specify with array. If the array is one-dimensional, the first element in the array creates the first option in the popup, the second array element creates the second option, and so on.

 If the array is two-dimensional, only the elements in the first column of the array create the options in the popup. The first element in the array creates the first option in the popup, the second element in the first column creates the second option, and so on.

 RANGE expN2 [, expN3]

 By default, popup options start with the first array element. You can designate a different starting element in the array by including the RANGE value expN2. For example, if the array is one-dimensional and expN2 is 3, the third element in the array creates the first option in the popup, the fourth element creates the second option, and so on.

 An element's position number in a two-dimensional array is determined by counting along rows. For example, suppose you create the following 3-by-3 array:

 a b c

 d e f

 g h i

 Elements a, b, and c are in position numbers 1, 2, and 3. Elements d, e, and f are in position numbers 4, 5, and 6, and so on. With two-dimensional arrays, only elements in the same column as array element expN2 create the options on the popup. For example, if expN2 is 2, the contents of elements b, e, and h are used to create the popup options. If expN2 is 5, only the contents of elements e and h are used.

 If you include a starting element expN2, you can also specify the number of elements used to create options by including the numeric expression expN3. The number of options appearing in the popup is determined by expN3. If expN3 isn't included, the contents of all array elements in the specified column from the starting element expN2 through the last element in the column are the popup options.

 If the array is two-dimensional, expN3 designates the number of elements used from the array column containing the starting element expN2. For example, if expN2 is 2 and expN3 is 3, the second array element and the next two elements in the same array column create options on the popup.

 The contents of a popup can be dynamically changed. You can insert and delete options by modifying the array. When SHOW GETS is issued, the RANGE clause is reevaluated. If the value of the element numbered expN2 or expN3 has changed, the popup is updated to reflect the change.

 The ACOPY(), ADEL(), ADIR(), AELEMENT(), AFIELDS(), AINS(), ALEN(), ASCAN(), ASORT() and ASUBSCRIPT() functions facilitate the manipulation of arrays.

 The following program example demonstrates how a popup can be dynamically changed. Two radio buttons, Vegetable and Fruits, can be chosen. Another set of radio buttons specifies the color (red, yellow or green) of the vegetables or fruits. The popup is modified and refreshed as different buttons are chosen.

 CLEAR

 SET TALK OFF

 STORE 1 TO color, fruitorveg, popchoice, start

 DIMENSION poparray(4,3)

 STORE 'Apples' TO poparray(1,1)

 STORE 'Bananas' TO poparray(1,2)

 STORE 'Limes' TO poparray(1,3)

 STORE 'Strawberries' TO poparray(2,1)

 STORE 'Lemons' TO poparray(2,2)

 STORE 'Grapes' TO poparray(2,3)

 STORE 'Radishes' TO poparray(3,1)

 STORE 'Corn' TO poparray(3,2)

 STORE 'Lettuce' TO poparray(3,3)

 STORE 'Beets' TO poparray(4,1)

 STORE 'Squash' TO poparray(4,2)

 STORE 'Celery' TO poparray(4,3)

 @ 9,2 SAY 'Color:'

 @ 11,2 SAY 'Type:'

 @ 9,10 GET color FUNCTION '*RH \<Red;\<Yellow;\<Green' ;

 SIZE 1, 9, 1 VALID PROC1()

 @ 11,10 GET fruitorveg FUNCTION '*RH \<Fruit;\<Vegetable' ;

 SIZE 1, 12, 1 VALID PROC2()

 @ 4,14 GET popchoice FUNCTION '^' FROM poparray RANGE start,2

 @ 14,17 GET ok FUNCTION '*T OK' DEFAULT 1 SIZE 1, 8

 @ 10,0,10,41 BOX

 @ 8,0,12,41 BOX

 READ CYCLE

 PROCEDURE PROC1

 DO CASE

 CASE COLOR = 1

 IF fruitorveg = 1

 start = 1

 ELSE

 start = 7

 ENDIF

 CASE COLOR = 2

 IF fruitorveg = 1

 start = 2

 ELSE

 start = 8

 ENDIF

 CASE COLOR = 3

 IF fruitorveg = 1

 start = 3

 ELSE

 start = 9

 ENDIF

 ENDCASE

 STORE 1 TO popchoice

 SHOW GETS

 RETURN .T.

 PROCEDURE PROC2

 IF fruitorveg = 1

 DO CASE

 CASE color = 1

 STORE 1 TO start

 CASE color = 2

 STORE 2 TO start

 CASE color = 3

 STORE 3 TO start

 ENDCASE

 ELSE

 DO CASE

 CASE color = 1

 STORE 7 TO start

 CASE color = 2

 STORE 8 TO start

 CASE color = 3

 STORE 9 TO start

 ENDCASE

 ENDIF

 STORE 1 TO popchoice

 SHOW GETS

 RETURN .T.

 SIZE expN4 [, expN5]

 By default, the width of the popup is determined by the length of the longest option text in columns. You can optionally specify the width of the popup in columns by specifying expN5. For popups, the first SIZE argument expN4 is ignored, because the height of a popup is determined by the number of options. You can include any numeric value for expN4.

 In FoxPro for Windows and FoxPro for Macintosh, the popup font determines the size of the popup. The popup font is specified with the FONT clause. If the FONT clause is omitted, the popup uses the font of its parent window (the main FoxPro window or a user-defined window).

 ENABLE | DISABLE

 Pop-ups são habilitados por padrão quando READ ou READ CYCLE é emitido. You can prevent a popup from being activated when READ or READ CYCLE is issued by including DISABLE. A disabled popup cannot be selected and appears in disabled colors. To disable individual popup options instead of the entire popup, see "Disabled Options" earlier in this section. Use SHOW GET ENABLE to enable a disabled popup.

 MESSAGE expC5

 The MESSAGE clause character expression expC5 appears when the pop-up is selected. In FoxPro for MS-DOS, the message is centered by default on the last line of the main FoxPro window. The message location can be changed with SET MESSAGE.

 In FoxPro for Windows and FoxPro for Macintosh, the message is placed in the graphics-based status bar. If the graphics-based status bar has been turned off with SET STATUS BAR OFF, the message is placed on the last line of the main FoxPro window.

 VALID expL1 | expN6

 You can include an optional VALID expression expL1 or expN6 that is evaluated when a popup option is chosen. That is, VALID isn't evaluated when you select the popup, but when you choose an option in the popup.

 Tipicamente, expL1 ou expN6 é uma função definida pelo usuário (UDF). With a user-defined function (UDF) you can select, enable or disable other objects; open a Browse window, open another data-entry screen or move to a new record. CLEAR READ may be included in the user-defined function to terminate the READ.

 expL1

 When a logical value is returned to the VALID clause, the logical value is ignored and the pop-up remains the current control. However, you can specify a UDF that returns a logical value to the VALID clause and activates another object.

 expN6

 A VALID clause that includes a numeric expression is used to specify which object is activated after an option in the popup is chosen. Objects are @ ... GET input fields, check boxes, lists, popups, spinners, text-editing regions and each individual button in a set of push, radio and invisible buttons.

 The expression expN6 has one of these effects:

  When expN6 = 0, the popup remains the active control.

  When expN6 is positive, expN6 specifies the number of objects to advance. For example, when the popup is the current object and VALID returns 1, the next object is activated. If expN6 is greater than the number of objects remaining, the READ is terminated (unless READ CYCLE is issued to activate the objects).

  When expN6 is negative, expN6 specifies the number of objects to move back. For example, if the popup is the current object and VALID returns -1, the previous object is activated. If expN6 moves back past the first object, the READ is terminated (unless READ CYCLE is issued to activate the objects).

 WHEN expL2

 The WHEN clause allows or prohibits selection of a popup based on the logical value of expL2, which must evaluate to a logical true (.T.) before a popup can be selected. If expL2 evaluates to a logical false (.F.), the popup cannot be selected and is skipped over if placed between other objects.

 COLOR SCHEME expN7 [, expN8] | COLOR color pair list

 If you do not include a COLOR clause, popup colors are determined by the color scheme for the main FoxPro window; if a popup is placed in a user-defined window, the window's color scheme determines the popup's colors.

 The colors of a popup can be specified by including the number of an existing color scheme in the COLOR SCHEME clause or a set of color pairs in the COLOR clause.

 Um esquema de cores é um conjunto de 10 pares de cores predefinidos. The color pairs in a color scheme can be changed with SET COLOR OF SCHEME. In FoxPro for MS-DOS, the color pairs in a color scheme can also be changed in the Color Picker.

 A color pair is a set of two letters separated by a forward slash. The first letter specifies the foreground color and the second letter specifies the background color.

 For example, this color pair specifies a red foreground on a white background:

 R/W

 For a list of colors and their corresponding color letters, see SET COLOR Overview or Color Table by Color Pair.

 A color pair can also be specified with a set of six RGB (Red Green Blue) color values separated by commas. The first three color values specify the foreground color and the second three color values specify the background color. The color values can range from 0 through 255.

 The R/W color pair in the example above can also be specified with this RGB color pair:

 RGB(255,0,0,255,255,255)

 By default, the colors of a popup and its options are derived from the color scheme of the main FoxPro window or the active user-defined window and color scheme 2.

 The first color scheme expN7 determines the colors of the face of the popup when the popup is selected, enabled or disabled. It also determines the color of the message. The second color scheme expN8 determines the color of the popup options and the border of the box containing the options.

 The following table lists the color pairs in each color scheme and what each color pair controls in a popup.

 Color Pair expN7 or

 Number Output window

 ---------- -------------

 5 Message

 6 Selected popup

 9 Enabled popups

 10 Disabled popups

 Color Pair expN8 or

 Number Color Scheme 2

 ---------- --------------

 1 Disabled options

 2 Enabled options

 3 Border

 6 Selected option

 7 Hot keys

 A color pair list only controls colors of the face of the popup when the popup is selected, enabled or disabled and the color of the message (popup color attributes controlled by color scheme expN7). For complete color control of a popup, specify two color schemes.

 This example shows how to override the current color scheme with other predefined color schemes:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '^ Cash;Charge;Net 30;Net 60' ;

 COLOR SCHEME 4, 5

 READ

# Observações

Esta variação de @ ... GET cria um pop-up. Quando selecionado, o pop-up abre, exibindo um conjunto de opções das quais você pode escolher uma. The set of options is specified in the FUNCTION and/or PICTURE clause containing the specification code for a popup - a caret (^).

Se você usar o Screen Builder para criar suas telas de entrada de dados, talvez não precise usar este comando. O Screen Builder gera automaticamente os comandos que criam pop-ups.

To open a popup in FoxPro for MS-DOS, press Enter or the Spacebar or click on the popup. You can open a popup in the same manner in FoxPro for Windows and FoxPro for Macintosh if KEYCOMP is set to DOS.

To open a popup in FoxPro for Windows when KEYCOMP is set to WINDOWS (the default setting), press the Spacebar, Alt+Up Arrow, or Alt+Down, Arrow or click on the popup.

To open a popup in FoxPro for Macintosh when KEYCOMP is set to MAC (the default setting), click the popup. When KEYCOMP is set to DOS or WINDOWS, you can open the popup by pressing the Spacebar or clicking the popup.

# Exemplo

O exemplo a seguir usa um pop-up para obter um campo para a ordem de navegação da tabela CUSTOMER:

```foxpro
SET TALK OFF
DEFINE WINDOW popupex FROM 5,10 TO 15,55 ;
	FLOAT DOUBLE COLOR SCHEME 5
CLOSE DATABASES
USE customer
DIMENSION dbftags(256)
dbftags(1) = 'Record #'
FOR i = 2 to 256
	IF empty(tag(i-1))
		i = i - 1
		DIMENSION dbftags(i)
		EXIT
	ELSE
		dbftags(i) = tag(i-1)
	ENDIF
ENDFOR
dbforder = 'Record #'
ACTIVATE WINDOW popupex
@ 3.5,7  GET dbforder PICTURE '@^' FROM dbftags SIZE 3, 14
@ 0.5,2  TO 7.5,43
@ 0,5  SAY ' Customer Browse Order: '
@ 2.5,27 GET okcancel PICTURE '@*VT \!OK;\?Cancel' SIZE 1,10,2 DEFAULT 0
READ CYCLE
RELEASE WINDOW popupex
IF okcancel = 1
	IF dbforder = "Record #"
		SET ORDER TO
	ELSE
		SET ORDER TO (dbforder)
	ENDIF
	WAIT WINDOW 'Order set to '+dbforder NOWAIT
	BROWSE WIDTH 10 NOWAIT
ELSE
	WAIT WINDOW 'Order not set' NOWAIT
ENDIF
```
