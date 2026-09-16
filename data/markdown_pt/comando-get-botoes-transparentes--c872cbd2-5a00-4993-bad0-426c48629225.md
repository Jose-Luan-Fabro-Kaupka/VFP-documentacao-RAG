# Comando @ ... GET - Botões transparentes

Incluído para compatibilidade com versões anteriores. Use o controle CommandButton em vez disso.

Cria botões invisíveis.

```foxpro
@ row, column
GET memvar | field
FUNCTION expC1 | PICTURE expC2
	[DEFAULT expN1]
	[SIZE expN2, expN3
		[, expN4]]
	[ENABLE | DISABLE]
	[MESSAGE expC5]
	[VALID expL1 | expN5]
	[WHEN expL2]
	[COLOR SCHEME expN6
	| COLOR color pair list]
```

#### Parameters
 row, column

 Row and column are numeric expressions with values 0 or greater that determine where the first button in a set of invisible buttons appears.

 The first row is number 0 in the main FoxPro window or a user-defined window. Rows are numbered from top to bottom. In FoxPro for Windows, row 0 is the row immediately under the FoxPro system menu bar. In FoxPro for Macintosh, row 0 is the row immediately under the FoxPro title bar. In FoxPro for MS-DOS, row 0 is the row the FoxPro system menu bar occupies. See SET SYSMENU for information about manipulating the system menu bar so you can place output on row 0 in FoxPro for MS-DOS.

 The first column is number 0 in the main FoxPro window or a user-defined window. Columns are numbered from left to right.

 When the first button in a set of invisible buttons is directed to a user-defined window, the row and column coordinates are relative to the user-defined window, not the main FoxPro window.

 In FoxPro for Windows and FoxPro for Macintosh, a position in the main FoxPro window or in a user-defined window is determined by the font of the main FoxPro window or the user-defined window. Most fonts can be displayed in a wide variety of sizes, and some are proportionally spaced. A row corresponds to the height of the current font; a column corresponds to the average width of a letter in the current font.

 In FoxPro for Windows and FoxPro for Macintosh, you can position the first button in a set of invisible buttons in a window with decimal fractions for row and column coordinates. In FoxPro for MS-DOS, decimal fractions used for row and column coordinates are rounded to the nearest integer value.

 memvar | field

 When you choose an invisible button, a number corresponding to your choice is stored to a memory variable, an array element or a field. For example, if you create four invisible buttons and choose the third button, 3 is stored to the memory variable, array element or field named by memvar or field. The initial value of memvar or field determines which button is initially selected.

FUNCTION expC1 | PICTURE expC2

 When creating invisible buttons, you must include the FUNCTION clause, the PICTURE clause or both. There is no advantage to any of the three methods. The FUNCTION or PICTURE clause contains the invisible button specification code *I.

 The FUNCTION clause character expression expC1 must begin with *I. To create more than one invisible button, include a semicolon for each additional button. For example, this clause creates three invisible buttons:

 ... FUNCTION '*I ;;' ...

 Note that the clause contains only two semicolons.

 The PICTURE clause character expression expC2 uses the same syntax as the FUNCTION character expression, except the PICTURE clause expression must begin with @ followed by *I and a space. For example, this clause creates three invisible buttons:

 ... PICTURE '@*I ;;' ...

 You can also include both the FUNCTION and PICTURE clauses to create invisible buttons. If both are included, FUNCTION expC1 must contain *I to create the invisible buttons and can also include a space followed by semicolons to create additional invisible buttons. PICTURE expC2 can include semicolons to create additional invisible buttons.

 The following examples illustrate the various forms of syntax you can use to create invisible buttons. Five invisible buttons are created and a number corresponding to each button chosen is stored to MCHOICE. The first button is placed in the second row and column. Each button is two rows high and four columns wide, and the buttons are separated by a single row.

 FUNCTION clause only:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '*I ;;;;' SIZE 2, 4, 1

 READ

 STORE 1 TO mchoice

 STORE '*I ;;;;' TO mfunc

 @ 2,2 GET mchoice FUNCTION mfunc SIZE 2, 4, 1

 READ

 PICTURE clause only:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice PICTURE '@*I ;;;;' SIZE 2, 4, 1

 READ

 STORE 1 TO mchoice

 @ 2,2 GET mchoice PICTURE '@*I' + ' ;;;;' SIZE 2, 4, 1

 READ

 FUNCTION and PICTURE clauses:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '*I' PICTURE ' ;;;;' SIZE 2, 4, 1

 READ

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '*I ;;' PICTURE ';;' SIZE 2, 4, 1

 READ

PICTURE and FUNCTION Options N, T, H and V

 Additional options can be combined with the *I specification code to modify the behavior (N and T options) and appearance (H and V options) of invisible buttons. These options are described below:

 Option Description

 ------ -----------

 N Does not terminate the READ when an invisible button is chosen. This is the default behavior.

 T Terminates the READ when an invisible button is chosen.

 H Positions the invisible buttons in a horizontal row.

 V Positions the invisible buttons in a vertical row. This is the default position.

 You can combine the H and V options with the T and N options in the following ways: NH, NV, TH and TV. For example, the following clause creates a vertical set of buttons and doesn't cause the READ to terminate when one of the buttons is selected:

 ... FUNCTION '*INV ... '

Disabled Invisible Buttons

 You can disable an invisible button so that it cannot be selected. When a button is disabled, it appears in disabled colors. To disable an invisible button, place two backslashes (\\) before the semicolon corresponding to the button in the FUNCTION or PICTURE clause.

 In the following example, five invisible buttons are created. The second and fourth buttons are disabled by placing two backslashes before the second and fourth semicolons respectively. If you are using FoxPro for Windows, set the font for the main FoxPro window to 9-point FoxFont to draw the box characters correctly.

 CLEAR

 STORE 1 TO mchoice

 *** Draw boxes for the invisible-button regions. ***

 @ 4,2 SAY CHR(218) + CHR(196) + CHR(196) + CHR(191)

 @ 5,2 SAY CHR(192) + CHR(196) + CHR(196) + CHR(217)

 @ 7,2 SAY CHR(218) + CHR(196) + CHR(196) + CHR(191)

 @ 8,2 SAY CHR(192) + CHR(196) + CHR(196) + CHR(217)

 @ 10,2 SAY CHR(218) + CHR(196) + CHR(196) + CHR(191)

 @ 11,2 SAY CHR(192) + CHR(196) + CHR(196) + CHR(217)

 @ 13,2 SAY CHR(218) + CHR(196) + CHR(196) + CHR(191)

 @ 14,2 SAY CHR(192) + CHR(196) + CHR(196) + CHR(217)

 @ 16,2 SAY CHR(218) + CHR(196) + CHR(196) + CHR(191)

 @ 17,2 SAY CHR(192) + CHR(196) + CHR(196) + CHR(217)

 @ 4,2 GET mchoice FUNCTION '*I ;\\;;\\;' SIZE 2, 4, 1

 READ

DEFAULT expN1

 When you choose an invisible push button, your choice is saved in the memory variable, array element or field you specify. If you specify a memory variable that doesn't exist, it is automatically created and initialized if you include the DEFAULT. However, an array element isn't created if you specify an array element in a DEFAULT clause. The DEFAULT clause is ignored if the memory variable already exists or you specify a field.

 -------------------------------

 Note - If the DEFAULT clause isn't included and the memory variable specified with memvar doesn't exist, the error message "Variable not found" appears.

 -------------------------------

 The DEFAULT expression expN1 determines the initial value of memvar. Here are examples of DEFAULT clauses for invisible buttons:

 @ 2,2 GET mchoice FUNCTION '*I ;;;;' DEFAULT 1

 READ

 STORE 3 TO mbutton

 @ 2,2 GET mchoice FUNCTION '*I ;;;;' DEFAULT mbutton

 READ

SIZE expN2, expN3 [, expN4]

 The SIZE clause determines the size and spacing of invisible buttons. The numeric expressions expN2 and expN3 control the height and width of each button respectively. The default for the height and width is 0.

 By default, no space is placed between vertical buttons, and a single column is placed between horizontal buttons. The spacing between invisible buttons is determined by expN4. If you create vertical buttons, expN4 designates the number of rows between buttons. If you create horizontal buttons, expN4 designates the number of columns between buttons.

ENABLE | DISABLE

 Invisible buttons are enabled by default when READ is issued. You can prevent a set of buttons from being activated when READ is issued by including DISABLE. Disabled invisible push buttons cannot be chosen and are displayed in disabled colors. To disable individual invisible buttons instead of the entire set of buttons, see "Disabled Invisible Buttons" earlier in this section. Use SHOW GET ENABLE to enable a set of disabled invisible buttons.

MESSAGE expC5

 The MESSAGE clause character expression expC5 appears when an invisible button is selected. In FoxPro for MS-DOS, the message is centered on the last line of the main FoxPro window by default. The message location can be changed with SET MESSAGE.

 In FoxPro for Windows and FoxPro for Macintosh, the message is placed in the graphics-based status bar. If the graphics-based status bar has been turned off with SET STATUS BAR OFF, the message is placed on the last line of the main FoxPro window.

VALID expL1 | expN5

 You can include an optional VALID expression expL1 or expN5 that is evaluated when an invisible button is chosen. That is, VALID isn't evaluated when you select (move to) an invisible button, but when you actually choose a button.

 Typically, expL1 or expN5 is a user-defined function. With a user-defined function you can select, enable or disable other objects, open a Browse window, open another data-entry screen or move to a new record. CLEAR READ can be included in the user-defined function (UDF) to terminate the READ.

 expL1

 When a logical value is returned to the VALID clause, the logical value is ignored and the invisible buttons remain the current control. However, you can specify a UDF that returns a logical value to the VALID clause and activates another object.

 expN5

 A VALID clause that includes a numeric expression is used to specify which object is activated after an invisible button is chosen. Objects are @ ... GET input fields, check boxes, lists, popups, spinners, text-editing regions and each individual button in a set of push, radio and invisible buttons.

 The numeric expression expN5 has one of three effects:

  When expN5 = 0, the chosen invisible button remains the active button.

  When expN5 is positive, expN5 indicates the number of objects to advance. For example, when you're positioned on the last button in a set of invisible buttons and VALID returns 1, the next object is activated. If expN5 is greater than the number of objects remaining, the READ is terminated (unless READ CYCLE is issued to activate the objects).

  When expN5 is negative, expN5 indicates the number of objects to move back. For example, when you're positioned on the first button in a set of invisible buttons and VALID returns -1, the previous @ ... GET input field or control is activated. If expN5 moves back past the first object, the READ is terminated (unless READ CYCLE is issued to activate the objects).

WHEN expL2

 The WHEN clause allows or prohibits selection of the invisible buttons based on the logical value of expL2, which must evaluate to a logical true (.T.) before any of the invisible buttons can be selected. If expL2 evaluates to false (.F.), none of the invisible buttons can be selected and are skipped if placed between other objects.

COLOR SCHEME expN6 | COLOR color pair list

 If you do not include a COLOR clause, invisible button colors are determined by the color scheme for the main FoxPro window; if invisible buttons are placed in a user-defined window, the window's color scheme determines the invisible button colors.

 The colors of invisible buttons can be specified by including the number of an existing color scheme in the COLOR SCHEME clause or a set of color pairs in the COLOR clause.

 A color scheme is a set of 10 predefined color pairs. The color pairs in a color scheme can be changed with SET COLOR OF SCHEME. In FoxPro for MS-DOS, the color pairs in a color scheme can also be changed in the Color Picker.

 A color pair is a set of two letters separated by a forward slash. The first letter specifies the foreground color and the second letter specifies the background color.

 For example, this color pair specifies a red foreground on a white background:

 R/W

 For a list of colors and their corresponding color letters, see SET COLOR Overview or Color Table by Color Pair.

 A color pair can also be specified with a set of six RGB (Red Green Blue) color values separated by commas. The first three color values specify the foreground color and the second three color values specify the background color. The color values can range from 0 through 255.

 The R/W color pair in the example above can also be specified with this RGB color pair:

 RGB(255,0,0,255,255,255)

 Color pair 6 determines the color of the selected invisible button.

# Observações

Esta variação de @ ... GET cria botões invisíveis, which are rectangular regions of the main FoxPro window or a user-defined window that you can select. You can use @ ... SAY to place characters on the rectangular button regions. When you select an invisible button, the characters in the button are highlighted. Issue READ or READ CYCLE to activate the buttons.

Se você usar o Screen Builder para criar suas telas de entrada de dados, pode não precisar usar este comando. O Screen Builder gera automaticamente os comandos que criam botões invisíveis.

# Exemplo

O exemplo a seguir demonstra botões invisíveis. @ ... SAY places four sets of characters (hearts, diamonds, clubs and spades) in the main FoxPro window. Four invisible buttons are created that line up with the characters. When an invisible button is chosen, the SHOWCARD routine is executed that indicates which button has been chosen. If you are using FoxPro for Windows, set the font for the main FoxPro window to 9-point FoxFont to draw the box characters correctly.

```foxpro
STORE 0 TO mchoice
ACTIVATE SCREEN
CLEAR
@ 2,2  SAY REPLICATE(CHR(3),2)  && Hearts
@ 3,2  SAY REPLICATE(CHR(3),2)
@ 2,10 SAY REPLICATE(CHR(4),2)  && Diamonds
@ 3,10 SAY REPLICATE(CHR(4),2)
@ 2,18 SAY REPLICATE(CHR(5),2)  && Clubs
@ 3,18 SAY REPLICATE(CHR(5),2)
@ 2,26 SAY REPLICATE(CHR(6),2)  && Spades
@ 3,26 SAY REPLICATE(CHR(6),2)
@ 1,1,4,4    BOX
@ 1,9,4,12   BOX
@ 1,17,4,20  BOX
@ 1,25,4,28  BOX
*** The next line creates four invisible buttons and ***
*** executes the procedure SHOWCARD when a button is chosen. ***
@ 1,1 GET mchoice PICTURE '@*IH ;;;' SIZE 4, 4, 4 VALID SHOWCARD();
	MESSAGE 'Pick a card, any card!' COLOR ,,,,,R/W
READ CYCLE
PROCEDURE SHOWCARD   && procedure executed when a button is chosen
@ 6,1 CLEAR
DO CASE
	CASE _CUROBJ = 1		&& First button chosen
		@ 6,1 SAY 'Hearts'
	CASE _CUROBJ = 2		&& Second button chosen
		@ 6,9 SAY 'Diamonds'
	CASE _CUROBJ = 3		&& Third  button chosen
		@ 6,17 SAY 'Clubs'
	CASE _CUROBJ = 4		&& Fourth button chosen
		@ 6,25 SAY 'Spades'
ENDCASE
RETURN .T.
```
