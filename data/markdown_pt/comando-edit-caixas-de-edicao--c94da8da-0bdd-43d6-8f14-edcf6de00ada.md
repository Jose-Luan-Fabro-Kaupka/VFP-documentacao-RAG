# Comando @ ... EDIT - Caixas de edição

Incluído para compatibilidade com versões anteriores. Use o controle EditBox em vez disso.

Cria uma região de edição de texto.

```foxpro
@ row, column
EDIT memvar | field
SIZE expN1, expN2 [, expN3]
	[FUNCTION expC1]
	[FONT expC2 [, expN4]]
	[STYLE expC3]
	[DEFAULT expr]
	[ENABLE | DISABLE]
	[MESSAGE expC4]
	[VALID expL1 | expN5
		[ERROR expC5]]
	[WHEN expL2]
	[NOMODIFY]
	[SCROLL]
	[TAB]
	[COLOR SCHEME expN6
	| COLOR color pair list]
```

#### Parameters
 row, column

 Row and column are numeric expressions with values of 0 or greater that determine where the text-editing region appears.

 The first row is number 0 in the main FoxPro window or a user-defined window. Rows are numbered from top to bottom. In FoxPro for Windows, row 0 is the row immediately under the FoxPro system menu bar. In FoxPro for Macintosh, row 0 is the row immediately under the FoxPro title bar. In FoxPro for MS-DOS, row 0 is the row the FoxPro system menu bar occupies. See SET SYSMENU for information about manipulating the system menu bar so you can place output on row 0 in FoxPro for MS-DOS.

 The first column is number 0 in the main FoxPro window or a user-defined window. Columns are numbered from left to right.

 When the text-editing region is directed to a user-defined window, the row and column coordinates are relative to the user-defined window, not the main FoxPro window.

 In FoxPro for Windows and FoxPro for Macintosh, a position in the main FoxPro window or in a user-defined window is determined by the font of the main FoxPro window or the user-defined window. Most fonts can be displayed in a wide variety of sizes, and some are proportionally spaced. A row corresponds to the height of the current font; a column corresponds to the average width of a letter in the current font.

 In FoxPro for Windows and FoxPro for Macintosh, you can position the text-editing region in a window with decimal fractions for row and column coordinates. In FoxPro for MS-DOS, decimal fractions used for row and column coordinates are rounded to the nearest integer value.

 SIZE expN1, expN2 [, expN3]

 The SIZE clause must be included to specify the height and width of the text-editing region. The height of the text-editing region in rows is specified by expN1, and the width in columns is specified by expN2.

 If expN1 is 1, a special one-line text-editing region is created. You can scroll horizontally in the one-line region. Pressing Enter moves you to the next object.

 The optional numeric expression expN3 specifies the number of characters in the memory variable, array element or field that can be edited, starting with the first character. If expN3 is omitted, all of the memory variable, array element or field can be edited.

 In FoxPro for Windows and FoxPro for Macintosh, the text-editing region font determines the size of the editing region. The text-editing region font is specified with the FONT clause. If the FONT clause is omitted, the text-editing region uses the font of its parent window (the main FoxPro window or a user-defined window).

 FUNCTION expC1

 You can include the I or J options in the FUNCTION clause to specify how text is justified in the text-editing region, and the 2 or 3 options to specify the appearance of the text-editing region. The 2 (two-dimensional) and 3 (three-dimensional) options are only available in FoxPro for Macintosh. Any additional characters included in the FUNCTION clause are ignored.

 Option Purpose

 ------ -------

 I Centers text in the text-editing region.

 J Right-justifies text. Text in the text-editing region is left-justified by default.

 2 Creates a flat (two-dimensional) text-editing region. This is the default text-editing region in FoxPro for Macintosh.

 3 Creates a three-dimensional text-editing region identical to text-editing regions in FoxPro for Macintosh.

 This example creates a text-editing region in which text is right-justified:

 STORE 'This will be edited' TO text

 @ 2,2 EDIT text FUNCTION 'J' SIZE 5, 50

 READ

 This example creates a three-dimensional text-editing region in FoxPro for Macintosh:

 STORE 'This will be edited' TO text

 @ 2,2 EDIT text FUNCTION '3' SIZE 5, 50

 READ

 FONT expC2[, expN4]

 The character expression expC2 is the name of the font, and the numeric expression expN4 is the font size. For example, the following clause can be used to display the text in the text-editing region in 16-point Courier font:

 FONT 'Courier', 16

 If you include the FONT clause but omit the font size expN4, a 10-point font is used.

 If the FONT clause is omitted and the text-editing region is placed in the main FoxPro window, the main FoxPro window font is used. If the FONT clause is omitted and the text-editing region is placed in a user-defined window, the user-defined window font is used.

 If the font you specify is not available, a font with similar font characteristics is substituted.

 The FONT clause is ignored in FoxPro for MS-DOS.

 STYLE expC3

 In FoxPro for Windows and FoxPro for Macintosh, include the STYLE clause to specify a font style for the text-editing region. If the font style you specify is not available, a font style with similar characteristics is substituted.

 The font style is specified with expC3. If the STYLE clause is omitted, the standard font style is used.

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

 You can include more than one character to specify a combination of font styles. For example, the following clause specifies Bold Italic:

 STYLE 'BI'

 The STYLE clause is ignored in FoxPro for MS-DOS.

 DEFAULT expr

 When you edit the text in a text-editing region, the text is read from and saved to the memory variable, array element or field specified with memvar or field. If you specify a memory variable that doesn't exist, it is automatically created and initialized if you include the DEFAULT clause. However, an array element isn't created if you specify an array element in a DEFAULT clause. The DEFAULT clause is ignored if the memory variable already exists or you specify a table or memo field.

 -------------------------------

 Note - If the DEFAULT clause isn't included and memvar doesn't exist, the error message "Variable not found" appears.

 -------------------------------

 The DEFAULT expression expr determines the type of memory variable created and its initial value. It must be of character or memo type. Here are examples of DEFAULT clauses for text-editing regions:

 @ 2,2 EDIT text DEFAULT 'This will be edited' SIZE 5, 50

 READ

 @ 2,2 EDIT text DEFAULT SPACE(20) SIZE 5, 50

 READ

 ENABLE | DISABLE

 Text-editing regions are by default enabled when READ or READ CYCLE is issued. Include DISABLE to prevent a text-editing region from being selected when READ or READ CYCLE is issued. A disabled text-editing region cannot be selected and appears in disabled colors. Use SHOW GET ENABLE to enable a disabled text-editing region.

 MESSAGE expC4

 The MESSAGE clause character expression expC4 appears when a text-editing region is selected. In FoxPro for MS-DOS, the message is centered on the last line of the main FoxPro window by default. The message location can be changed with SET MESSAGE.

 In FoxPro for Windows and FoxPro for Macintosh, the message is placed in the graphics-based status bar. If the graphics-based status bar has been turned off with SET STATUS BAR OFF, the message is placed on the last line of the main FoxPro window.

 VALID expL1 | expN5

 You can include an optional VALID expression expL1 or expN5 that is evaluated when you exit the text-editing region.

 Typically, expL1 or expN5 is a user-defined function. With a user-defined function you can select, enable or disable other objects, open a Browse window, open another data-entry screen or move to a new record. CLEAR READ can be included in the user-defined function to terminate the READ.

 expL1

 If expL1 evaluates to true (.T.), your changes are saved if you press Tab, Ctrl+Tab or Shift+Tab to exit the text-editing region. If you press Esc, your changes are discarded.

 If you press Tab, Ctrl+Tab or Shift+Tab to save changes to a memo field and expL1 evaluates to false (.F.), a message appears prompting you for proper input. If you then press Esc to exit the text-editing region, your changes are saved.

 If expL1 evaluates to false and you are editing a memory variable, array element or field, pressing Esc exits the text-editing region and discards your changes.

 expN5

 A VALID clause that includes a numeric expression is used to specify which object is activated after the text-editing region is exited.

 The expression expN5 has one of these effects:

  When expN5 = 0, the text-editing region remains the active control and the MESSAGE expC4 and ERROR expC5 messages are suppressed. A special error message routine can be written as part of a user-defined function called by the VALID clause.

  When expN5 is positive, expN5 specifies the number of objects to advance. For example, when the text-editing region is selected and VALID returns 1, the next object is activated. If expN5 is greater than the number of remaining objects, the READ is terminated (unless READ CYCLE is issued to activate the objects).

  When expN5 is negative, expN5 specifies the number of objects to move back. For example, when the text-editing region is selected and VALID returns -1, the previous object is activated. If expN5 moves back past the first object, the READ is terminated (unless READ CYCLE is issued to activate the objects).

 ERROR expC5

 When the VALID clause expression expL1 evaluates to false (.F.), the default message "Invalid Input" appears. Including the ERROR clause lets you replace this default message with the character expression expC5.

 WHEN expL2

 The WHEN clause allows or prohibits selection of the editing region based on the logical value of expL2, which must evaluate to a logical true value (.T.) before the text-editing region can be selected. If expL2 evaluates to false (.F.), the region cannot be selected and is skipped if placed between other objects.

 NOMODIFY

 Including NOMODIFY displays the text-editing region but doesn't allow editing. You can scroll through the region and copy text, but you can't modify the text.

 SCROLL

 If SCROLL is included, a scroll bar is placed to the right of the text-editing region. The scroll bar lets you move quickly through the text with the mouse and provides a visual indication of your position in the text-editing region. The scroll bar appears only when the text is too long to fit into the text-editing region.

 TAB

 By default, pressing the Tab key doesn't insert a tab into the text in a text-editing region. Pressing Tab or Ctrl+Tab saves your changes, exits the text-editing region and advances you to the next object.

 If you include TAB, pressing Tab inserts a tab into the text at the current cursor location. Press Ctrl+Tab to save your changes, exit the text-editing region and advance to the next object.

 COLOR SCHEME expN6 | COLOR color pair list

 By default, the colors of text-editing regions are derived from color scheme 2, User Menus. If you do not include a COLOR clause, text-editing region colors are determined by the color scheme for the main FoxPro window; if text-editing regions are placed in a user-defined window, the window's color scheme determines the text-editing region colors.

 The colors of text-editing regions can be specified by including the number of an existing color scheme in the COLOR SCHEME clause or a set of color pairs in the COLOR clause.

 A color scheme is a set of 10 predefined color pairs. The color pairs in a color scheme can be changed with SET COLOR OF SCHEME. In FoxPro for MS-DOS, the color pairs in a color scheme can also be changed in the Color Picker.

 A color pair is a set of two letters separated by a forward slash. The first letter specifies the foreground color and the second letter specifies the background color.

 For example, this color pair specifies a red foreground on a white background:

 R/W

 For a list of colors and their corresponding color letters, see SET COLOR Commands Overview or Color Table by Color Pair.

 A color pair can also be specified with a set of six RGB (Red Green Blue) color values separated by commas. The first three color values specify the foreground color and the second three color values specify the background color. The color values can range from 0 through 255.

 The R/W color pair in the example above can also be specified with this RGB color pair:

 RGB(255,0,0,255,255,255)

Color Pair Editing Region

 Number Attribute

 ---------- --------------

 2 Enabled text editing region

 3 Scroll bar*

 5 Message

 6 Selected text editing region

 10 Disabled text editing region

 * Controls drawn in background color.

 Bar drawn in dim of foreground color.

 The following example defines a text-editing region with the following color characteristics:

  When text is selected, the text is shown with bright white text on a blue background (W+/B).

  When enabled, the region is shown with yellow text on a blue background (GR+/B).

  When disabled, the region is shown with white text on a blue background (W/B).

 When you skip a color pair, you must include a comma where the color pair is omitted.

 Here are the commands:

 STORE 'To be edited' TO text

 @ 2,2 EDIT text SIZE 5, 50 COLOR ,GR+/B,,,,W+/B,,,,W/B

 READ

 The following example shows how to override the color scheme of the main FoxPro window with another predefined color scheme:

 ACTIVATE SCREEN

 STORE 'To be edited' TO text

 @ 2,2 EDIT text COLOR SCHEME 4 SIZE 5, 50

 READ

# Observações

Este comando cria uma região retangular de edição de texto para editar uma variável de memória ou elemento de array memvar, ou um campo ou campo memo field. A variável de memória, elemento de array ou campo deve ser do tipo caractere.

Se você usar o Screen Builder para criar suas telas de entrada de dados, pode não precisar usar este comando. O Screen Builder gera automaticamente os comandos que criam regiões de edição de texto.

Observação Este controle usa EDIT em sua sintaxe em vez de GET como em outros controles do FoxPro, como caixas de seleção, botões de opção e botões de comando.

Quando uma região de edição de texto é ativada com READ ou READ CYCLE, o conteúdo de memvar ou field é exibido na região para edição. Quando você sai da região de edição de texto, suas alterações podem ser salvas na variável de memória, elemento de array ou campo especificado com memvar ou field.

Pressione Tab ou Ctrl+Tab para salvar suas alterações e mover para o próximo objeto. Para salvar suas alterações e mover para o objeto anterior, pressione Shift+Tab. Pressione Esc para descartar suas alterações e mover para o próximo objeto. Se você estiver editando um campo memo e uma cláusula VALID estiver incluída, suas alterações podem não ser salvas — o valor retornado pela cláusula VALID determina se suas alterações são salvas. Para obter mais informações, consulte a seção sobre a cláusula VALID mais adiante neste tópico.

Todos os recursos padrão de edição do FoxPro, como cortar, copiar e colar, estão disponíveis na região de edição de texto. O texto na região de edição de texto rola verticalmente e as palavras são quebradas horizontalmente.
