# Comando @ ... GET - Botões de comando

Incluído para compatibilidade com versões anteriores. Use o Controle CommandButton em vez disso.

Cria um conjunto de botões de pressão ou botões de pressão com imagem.

```foxpro
@ row, column
GET memvar | field
FUNCTION expC1 | PICTURE expC2
	[FONT expC3 [, expN1]]
	[STYLE expC4]
	[DEFAULT expr]
	[SIZE expN2, expN3
		[, expN4]]
	[ENABLE | DISABLE]
	[MESSAGE expC5]
	[VALID expL1 | expN5]
	[WHEN expL2]
	[COLOR SCHEME expN6
	| COLOR color pair list]
```

#### Parâmetros
 row, column

 Row e column são expressões numéricas with values of 0 or greater that determine where the first button in a set of push buttons appears.

 A primeira linha é o número 0 in the main FoxPro window or a user-defined window. Rows are numbered from top to bottom. In FoxPro for Windows, row 0 is the row immediately under the FoxPro system menu bar. In FoxPro for Macintosh, row 0 is the row immediately under the FoxPro title bar. In FoxPro for MS-DOS, row 0 is the row the FoxPro system menu bar occupies. See SET SYSMENU for information about manipulating the system menu bar so you can place output on row 0 in FoxPro for MS-DOS.

 A primeira coluna é o número 0 in the main FoxPro window or a user-defined window. Columns are numbered from left to right.

 Quando o primeiro botão em um conjunto de botões de pressão é direcionado a uma janela definida pelo usuário, the row and column coordinates are relative to the user-defined window, not the main FoxPro window.

 No FoxPro para Windows e no FoxPro para Macintosh, uma posição na janela principal do FoxPro or in a user-defined window is determined by the font of the main FoxPro window or the user-defined window. Most fonts can be displayed in a wide variety of sizes, and some are proportionally spaced. A row corresponds to the height of the current font; a column corresponds to the average width of a letter in the current font.

 No FoxPro para Windows e no FoxPro para Macintosh, você pode posicionar o primeiro botão in a set of push buttons in a window with decimal fractions for row and column coordinates. No FoxPro para MS-DOS, frações decimais usadas para coordenadas de linha e coluna são arredondadas to the nearest integer value.

 memvar | field

 Quando você escolhe um botão de pressão, your choice is stored to the memory variable or array element memvar or to the field field. memvar or field must be of numeric or character type.

 If memvar or field is of numeric type, a number corresponding to the push button choice is stored to the memory variable, array element or field specified with memvar or field. For example, if you create four push buttons and choose the third button, 3 is stored. If memvar or field is of character type, the prompt of the push button you choose is stored to the memory variable, array element or field specified with memvar or field.

 FUNCTION expC1 | PICTURE expC2

 Ao criar botões de pressão, you must include the FUNCTION clause, the PICTURE clause or both. There is no advantage to any of the three methods. The FUNCTION or PICTURE clause contains the push button specification code, an asterisk (*), and the text for the individual push button prompts.

 A expressão de caractere FUNCTION expC1 must begin with *. To create the push button prompts, include a space after the asterisk followed by a list of the prompts separated by semicolons. One button is created for each prompt. For example, the following FUNCTION clause creates push buttons with the prompts OK and Cancel:

 ... FUNCTION '* OK;Cancel' SIZE 1, 8 ...

 A expressão de caractere PICTURE expC2 uses the same syntax as the FUNCTION character expression except the PICTURE character expression must begin with @ followed by an asterisk (*). For example, the following PICTURE clause creates push buttons with the prompts OK and Cancel:

 .. PICTURE '@* OK;Cancel' SIZE 1, 8 ...

 You can also include both the FUNCTION and PICTURE clauses to create push buttons. If both are included, the FUNCTION character expression expC1 must contain * to create the push buttons followed by a space and the push button prompts. A expressão de caractere PICTURE expC2 can include prompts to create additional push buttons.

 Os exemplos a seguir ilustram the various forms of syntax you can use to create push buttons. Two push buttons are created: OK and Cancel. The first button (OK) is placed in the second row and second column. A number corresponding to the button chosen is stored to the memory variable MCHOICE.

 Somente cláusula FUNCTION:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '* OK;Cancel' SIZE 1, 8

 READ

 STORE 1 TO mchoice

 STORE '* OK;Cancel' TO mprompts

 @ 2,2 GET mchoice FUNCTION mprompts SIZE 1, 8

 READ

 Somente cláusula PICTURE:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice PICTURE '@* OK;Cancel' SIZE 1, 8

 READ

 STORE 1 TO mchoice

 @ 2,2 GET mchoice PICTURE '@*' + ' OK;Cancel' SIZE 1, 8

 READ

 Cláusulas FUNCTION e PICTURE:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '*' ;

 PICTURE ' OK;Cancel' SIZE 1, 8

 READ

 Botões de pressão com prompts de imagem

 In FoxPro for Windows and FoxPro for Macintosh, the prompt for a push button can also be the name of a picture file. In FoxPro for Windows, the picture file can be a bitmap file with a .BMP extension. In FoxPro for Macintosh, you can use a picture file of PICT type or a .BMP bitmap file.

 Quando um botão de pressão usa um arquivo de imagem como prompt, the push button mimics the behavior of a push button with a text prompt. For example, the picture file appears on a button but the push button isn't displayed. Like choosing a push button, choosing the picture prompt stores the push button's value to memvar or field.

 Para usar um arquivo de imagem em um botão de pressão, add B to the push button specification code. The FUNCTION and PICTURE clause specification codes that create a push button are * and @*, respectively. To create a push button with picture prompts, use the codes *B and @*B, followed by a space and the picture filename. If the picture file is not located in the default directory or folder, include the path to the picture file with the picture filename.

 -------------------------------

 Observação - As imagens não são recortadas, reduced or enlarged to fit the push button. Use the SIZE clause to adjust the size of the push buttons to accommodate the pictures.

 -------------------------------

 Se você omitir a extensão do arquivo de imagem, FoxPro for Macintosh first looks for a picture file with the name you specified and a .BMP extension. If a picture file with a .BMP extension and the name you specified isn't found, FoxPro for Macintosh then looks for a file with the name you specified and a .PCT extension. If a picture file with a .PCT extension and the name you specified isn't found, FoxPro for Macintosh then looks for a picture file with the name you specified without an extension.

 Máscaras de imagem e botões de pressão

 In FoxPro for Windows and FoxPro for Macintosh, a picture push button has three states: up, down and disabled. FoxPro automatically controls the appearance of a picture push button when it is in each of these three states, but you can override the default appearance by using a picture mask.

 Uma máscara é usada para controlar as áreas transparentes of a picture push button. Por padrão, as áreas brancas são transparentes. If a mask is present, the white areas of the mask, not the picture file, are transparent.

 A mask is a monochrome picture file. In FoxPro for Windows, a mask is a .BMP with an .MSK extension. In FoxPro for Macintosh, a mask can be a .BMP with an .MSK extension or a PICT type file with a .PCM extension. The mask must have the same base name as the picture file and the appropriate extension. FoxPro automatically looks for a mask for a picture file in the same directory or folder where the picture file is located.

 Na maioria dos casos, uma máscara não é necessária. If you don't need anything in your picture to appear white or your picture file has a white background, the picture push button will appear as desired in the up, down and disabled states.

 When a picture push button has a mask and is in the up or down state, any white areas in the picture file appear transparent, allowing the color of the button face to show through. However, you can maintain the white color of certain areas.

 Suponha que você tenha um arquivo de imagem with a dog on a white background; the dog has white eyes and the button face is red. You want the background of the button to appear red but you want the dog's eyes to be white, not red. Make a mask that is the same size as the picture file but includes only two colors, black and white. Leave the background of the mask white but make the dog - including his eyes - completely black. When the button appears, the background is red to match the button face but the dog's eyes are white.

 Quando um botão de pressão com imagem está desabilitado, any white areas in the picture file appear transparent so the color of the button face shows through. Any non-white areas appear dark gray. If the button has a mask, all white areas in the mask are transparent so the color of the button face shows through, and all black areas appear dark gray.

 Opções PICTURE e FUNCTION N, T, H, V, 2 e 3

 Opções adicionais podem ser combinadas with the * specification code to modify the behavior (N and T) and appearance (H, V, 2 and 3) of push buttons.

 Os códigos de especificação 2 (bidimensional) e 3 (tridimensional) estão disponíveis somente in FoxPro for Macintosh.

 Opção Descrição

 ------ -----------

 N Não encerra o READ quando um botão de pressão é escolhido.

 T Encerra o READ quando um botão de pressão é escolhido. Este é o comportamento padrão.

 H Posiciona os botões de pressão em uma linha horizontal.

 V Posiciona os botões de pressão em uma coluna vertical. Esta é a orientação padrão.

 2 Cria botões de pressão planos (bidimensionais) em preto e branco idênticos aos botões de pressão em caixas de diálogo do Macintosh.

 3 Cria botões de pressão tridimensionais idênticos aos botões de pressão em caixas de diálogo do FoxPro para Macintosh. Este é o tipo padrão de botão de pressão no FoxPro para Macintosh.

 Você pode combinar a opção T ou N with the H, V and 2 or 3 options. For example, the following clause creates a horizontal row of buttons and doesn't cause the READ to terminate when one of the buttons is chosen:

 ... FUNCTION '*NH ... '

 In FoxPro for Macintosh, the following clause creates a horizontal row of two-dimensional buttons and doesn't cause the READ to terminate when one of the buttons is chosen:

 ... FUNCTION '*NH2 ... '

 Botões de pressão com recursos especiais

 Você pode atribuir uma tecla de atalho a um botão, disable a button, or create a default or escape button. To assign these special features to a push button, you must include special characters when defining the prompt. The special characters are removed when the prompt is stored to memvar or field.

 Teclas de atalho

 No FoxPro para MS-DOS, uma tecla de atalho é uma letra destacada in the push button prompt that you can type to immediately choose a push button. Pressing the hot key selects the button and chooses it. To assign a hot key, place a backslash and a less-than sign (\<) before the desired character of the push button prompt.

 Uma tecla de atalho não escolhe o botão de pressão se the current object is a GET field, a text-editing region, a pop-up or a list.

 If the current object is an @ ... GET input field or a text-editing region, pressing the hot key enters the character in the field or the text-editing region. If the current object is a popup or a list, pressing the hot key selects the first option on the popup or list whose prompt begins with the hot key character.

 No FoxPro para Windows, uma tecla de atalho é uma letra sublinhada in the push button prompt that you can type to immediately choose the button. If the current object is an @ ... GET input field, a text-editing region, a popup or a list and KEYCOMP is set to WINDOWS, you can press the Alt key and the hot key to choose the push button.

 No FoxPro para Macintosh, se KEYCOMP estiver definido como MAC (the default), hot keys aren't highlighted or underlined. If KEYCOMP is set to DOS or WINDOWS, hot keys are underlined.

 O exemplo a seguir cria os botões OK e Cancel with hot keys O and C, respectively:

 STORE 1 TO mchoice

 @ 2,8 GET mchoice FUNCTION '* \<OK;\<Cancel'

 READ

 Botões de pressão desabilitados

 Você pode desabilitar um botão de pressão para que ele não possa ser selecionado ou escolhido. Disabled push buttons are shown in disabled colors. To disable a single push button, place two backslashes (\\) before the button's prompt. To disable a set of push buttons, include the DISABLE keyword.

 O botão de pressão OK está desabilitado no exemplo a seguir:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '* \\OK;Cancel'

 READ

 Botões de pressão padrão

 Um botão de pressão padrão é normalmente usado para sair a data-entry screen, dialog or routine and accept any changes made in the screen, dialog or routine. Para criar um botão de pressão padrão, place a backslash and an exclamation point (\!) before the push button's prompt.

 O exemplo a seguir especifica o botão OK como o botão de pressão padrão:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '* \!OK;Cancel'

 READ

 No FoxPro para MS-DOS, o botão de pressão padrão é cercado por colchetes angulares duplos to distinguish it from other push buttons. The default push button is automatically chosen when you press Ctrl+Enter or Ctrl+W. You can specify only one default push button for each READ.

 No FoxPro para Windows, o botão de pressão padrão é cercado por uma borda grossa. Press Enter, Ctrl+Enter or Ctrl+W to choose the default push button. A configuração KEYCOMP determina o comportamento dos botões de pressão padrão in FoxPro for Windows in the following ways:

  If you SET KEYCOMP TO DOS, the behavior of the default push button is the same as the behavior of a default push button in FoxPro for MS-DOS.

  If you SET KEYCOMP TO WINDOWS, the default push button changes as you move between buttons. The push button specified with \! is the default button when objects besides push buttons are active. When a push button is active, it becomes the default push button.

 No FoxPro para Macintosh, o botão de pressão padrão é cercado por uma borda grossa. A configuração KEYCOMP determina o comportamento dos botões de pressão padrão in FoxPro for Macintosh in the following ways:

  If you SET KEYCOMP TO DOS, the default push button is always the same and is chosen by pressing Ctrl+Enter.

  If you SET KEYCOMP TO WINDOWS, the default button in a dialog is surrounded by a bold border and is always the same. It is chosen by pressing Enter or Ctrl+Enter. However, pressing Enter when a text editing region is the current control moves the cursor to the next line in the text editing region. In text editing regions, press Ctrl+Enter to chose the default button.

  If you SET KEYCOMP TO MAC, the default button in a dialog is surrounded by a bolder border and is always the same. It is chosen by pressing Enter. However, pressing Enter when a text editing region is the current control moves the cursor to the next line in the text editing region. In text editing regions, press Ctrl+Enter to chose the default button.

 Botões de pressão de escape

 Um botão de pressão de escape é escolhido automaticamente quando você pressiona a tecla Esc. Um botão de escape é normalmente usado para sair a data-entry screen, dialog or routine and discard any changes made in the screen, dialog or routine. You can specify only one escape push button for each READ.

 Na ausência de um botão de pressão de escape, pressing Esc when editing an @ ... GET input field ends the editing and restores the original value to the field. If the field has a VALID procedure, the procedure isn't executed. When an escape push button is present, pressing Esc saves the contents of the current @ ... GET input field contents and executes the VALID procedure.

 Para criar um botão de pressão de escape, place a backslash and a question mark (\?) before the push button's prompt.

 O exemplo a seguir especifica o botão de pressão Cancel como o botão de pressão de escape:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '* OK;\?Cancel'

 READ

 Botões de pressão com características combinadas

 Você pode criar um botão de pressão com mais de um recurso especial. In the following example, the OK button is the default button and is assigned O as its hot key character. The Cancel button is the escape button and is assigned C as its hot key character. The hot key designators immediately precede the desired hot key character.

 STORE 1 TO mchoice

 @ 2, 2 GET mchoice FUNCTION '* \!\<OK;\?\<Cancel'

 READ

 FONT expC3 [, expN1]

 A expressão de caractere expC3 é o nome da fonte, and the numeric expression expN1 is the font size. Por exemplo, a cláusula a seguir pode ser usada para exibir the push button prompts in 16-point Courier font:

 FONT 'Courier', 16

 Se você incluir a cláusula FONT, mas omitir o tamanho da fonte expN1, a 10-point font is used.

 No FoxPro para Windows, se a fonte especificada não estiver disponível, a font with similar font characteristics is substituted.

 No FoxPro para Macintosh, se a fonte especificada não estiver disponível, the Chicago font is used.

 No FoxPro para MS-DOS, a cláusula FONT é ignorada.

 Se a cláusula FONT for omitida e os botões de pressão forem colocados na janela principal do FoxPro, the main FoxPro window font is used. If the FONT clause is omitted and the push buttons are placed in a user-defined window, the user-defined window font is used.

 STYLE expC4

 No FoxPro para Windows e no FoxPro para Macintosh, inclua a cláusula STYLE to specify a font style for the push button prompts. If the font style you specify is not available, a font style with similar characteristics is substituted.

 O estilo da fonte é especificado com expC4. Se a cláusula STYLE for omitida, o estilo de fonte normal é usado.

 Caractere Estilo de fonte

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

 * Os estilos Condense e Extend estão disponíveis somente no FoxPro para Macintosh. The Strikeout style is only available in FoxPro for Windows.

 Você pode incluir mais de um caractere para especificar uma combinação de estilos de fonte. Por exemplo, a cláusula a seguir especifica Negrito Itálico:

 STYLE 'BI'

 A cláusula STYLE é ignorada no FoxPro para MS-DOS.

 DEFAULT expr

 Quando você escolhe um botão de pressão, sua escolha é salva na variável de memória, array element or field you specify. Se você especificar uma variável de memória que não existe, it is automatically created and initialized if you include DEFAULT. No entanto, um elemento de matriz não é criado se você especificar um elemento de matriz in a DEFAULT clause. A cláusula DEFAULT é ignorada se a variável de memória já existir or you specify a field.

 -------------------------------

 Observação - Se a cláusula DEFAULT não for incluída and the memory variable you specify doesn't exist, a mensagem de erro "Variable not found" aparece.

 --------------------------------

 A expressão DEFAULT expr determina o tipo de variável de memória criada and its initial value. expr must be of numeric or character type. Os exemplos a seguir são de cláusulas DEFAULT para botões de pressão:

 @ 2,2 GET mchoice FUNCTION '* OK;Cancel' DEFAULT 'OK'

 READ

 @ 2,2 GET mchoice FUNCTION '* OK;Cancel' DEFAULT 2

 READ

 STORE 'OK' TO button

 @ 2,2 GET mchoice FUNCTION '* OK;CANCEL' DEFAULT button

 READ

 SIZE expN2, expN3 [, expN4]

 A expressão numérica expN2 especifica a altura em linhas of the push buttons. No FoxPro para MS-DOS, um botão de pressão tem sempre uma linha de altura, so the numeric expression expN2 is ignored.

 Por padrão, a largura de cada botão individual é determinada by the length of the push button prompt text. The numeric expression expN3 specifies the width (in columns) of each push button. Um botão de pressão nunca será dimensionado menor que seu prompt.

 Por padrão, nenhuma linha é colocada entre botões verticais and a single column is placed between horizontal buttons. O espaçamento entre botões de pressão é especificado com expN4. Se você criar botões de pressão verticais, expN4 especifica o número de linhas between the buttons. Se você criar botões horizontais, expN4 especifica o número de colunas between the buttons.

 No FoxPro para Windows e no FoxPro para Macintosh, a fonte do botão de pressão determina o tamanho of the push buttons. The push button font is specified with the FONT clause. If the FONT clause is omitted, the push buttons use the font of the parent window (the main FoxPro window or a user-defined window).

 O exemplo a seguir demonstra como a cláusula SIZE controla the button spacing:

 CLEAR

 @ 2,2 GET mchoice FUNCTION '* OK;Cancel' ;

 DEFAULT 1 SIZE 2, 10, 1

 @ 2,16 GET mchoice FUNCTION '* OK;Cancel' ;

 DEFAULT 1 SIZE 2, 10, 2

 READ

 ENABLE | DISABLE

 Botões de pressão, por padrão, estão habilitados quando READ ou READ CYCLE é emitido. Você pode impedir que um conjunto de botões seja selecionado when READ or READ CYCLE is issued by including DISABLE.

 Botões de pressão desabilitados não podem ser selecionados e são exibidos nas cores desabilitadas. Para desabilitar botões de pressão individuais em vez do conjunto inteiro, consulte "Disabled Push Buttons" anteriormente nesta seção. Use SHOW GET ENABLE para habilitar um conjunto de botões de pressão desabilitados.

 MESSAGE expC5

 A expressão de caractere expC5 da cláusula MESSAGE aparece quando um botão de pressão é selecionado. No FoxPro para MS-DOS, a mensagem é centralizada por padrão na última linha of the main FoxPro window. O local da mensagem pode ser alterado com SET MESSAGE.

 No FoxPro para Windows e no FoxPro para Macintosh, a mensagem é colocada na barra de status gráfica. Se a barra de status gráfica foi desativada com SET STATUS BAR OFF, the message is placed on the last line of the main FoxPro window.

 VALID expL1 | expN5

 Você pode incluir uma expressão VALID opcional expL1 or expN5 that is evaluated when a push button is chosen. Ou seja, VALID não é avaliado quando você seleciona (move para) um botão, but when you actually choose a button by pressing Enter or Spacebar or clicking the button.

 Normalmente, expL1 ou expN5 é uma função definida pelo usuário (UDF). Com uma função definida pelo usuário, você pode selecionar, habilitar ou desabilitar outros objetos, open a Browse window, open another data-entry screen, or move to a new record. CLEAR READ pode ser incluído na função definida pelo usuário para encerrar o READ.

 expL1

 Quando um valor lógico é retornado à cláusula VALID, the logical value is ignored and the push buttons remain the active control. However, you can specify a UDF that returns a logical value to the VALID clause and activates another object.

 expN5

 Uma cláusula VALID que inclui uma expressão numérica é usada para especificar qual objeto é ativado after a push button is chosen. Os objetos são campos de entrada @ ... GET, check boxes, lists, popups, spinners, text-editing regions and each individual button in a set of push, radio and invisible buttons.

 A expressão expN5 tem um de três efeitos:

  Quando expN5 = 0, o botão de pressão escolhido permanece o botão ativo.

  Quando expN5 é positivo, expN5 indica o número de objetos a avançar. For example, when the last button in a set of push buttons is selected and VALID returns 1, the next object is activated. If expN5 is greater than the number of objects remaining, the READ is terminated (unless READ CYCLE is issued to activate the objects).

  Quando expN5 é negativo, expN5 indica o número de objetos a retroceder. For example, when the first button in a set of push buttons is selected and VALID returns -1, the previous object is activated. If expN5 moves back past the first object, the READ is terminated (unless READ CYCLE is issued to activate the objects).

 O exemplo a seguir mostra o que você pode fazer com uma função definida pelo usuário. Cinco botões são exibidos verticalmente. As escolhas dos botões são usadas para posicionar o ponteiro de registro. A opção N é incluída para que o READ não seja encerrado quando você escolhe um botão. Quando você escolhe um botão, a função definida pelo usuário GOREC é executada.

 CLOSE DATABASES

 USE customer

 SET TALK OFF

 DEFINE WINDOW one FROM 3,5 TO 18,20 FLOAT DOUBLE COLOR SCHEME 5

 ACTIVATE WINDOW one

 @ 1,2 GET mchoice FUNCTION '*NV Next;Prior;Top;Bottom;Quit';

 SIZE 2, 10, 1 VALID GOREC() DEFAULT 1

 READ CYCLE

 CLEAR WINDOW

 PROCEDURE gorec

 DO CASE

 CASE mchoice = 1

 SKIP

 IF EOF()

 SKIP -1

 ENDIF

 CASE mchoice = 2

 SKIP -1

 IF BOF()

 SKIP

 ENDIF

 CASE mchoice = 3

 GO TOP

 CASE mchoice = 4

 GO BOTTOM

 CASE mchoice = 5

 CLEAR READ

 ENDCASE

 @ 12,6 SAY ALLTRIM(STR(RECNO()))

 RETURN

 WHEN expL2

 A cláusula WHEN permite ou proíbe a seleção de um conjunto de botões de pressão based on the logical value of expL2, which must evaluate to a logical true (.T.) before the push buttons can be selected. If expL2 evaluates to a logical false (.F.), the push buttons cannot be selected and are skipped over if placed between other objects.

 COLOR SCHEME expN6 | COLOR color pair list

 Se você não incluir uma cláusula COLOR, as cores dos botões de pressão são determinadas by the color scheme for the main FoxPro window; if push buttons are placed in a user-defined window, the window's color scheme determines the push button colors.

 As cores dos botões de pressão podem ser especificadas incluindo o número de um esquema de cores existente in the COLOR SCHEME clause or a set of color pairs in the COLOR clause.

 Um esquema de cores é um conjunto de 10 pares de cores predefinidos. Os pares de cores em um esquema de cores podem ser alterados com SET COLOR OF SCHEME. No FoxPro para MS-DOS, os pares de cores em um esquema de cores também podem ser alterados no Seletor de cores.

 Um par de cores é um conjunto de duas letras separadas por uma barra. A primeira letra especifica a cor de primeiro plano e a segunda letra especifica a cor de fundo.

 Por exemplo, este par de cores especifica primeiro plano vermelho em fundo branco:

 R/W

 Para uma lista de cores e suas letras correspondentes, consulte Visão geral do SET COLOR ou Tabela de cores por par de cores.

 Um par de cores também pode ser especificado com um conjunto de seis valores RGB (Red Green Blue) color values separated by commas. The first three color values specify the foreground color and the second three color values specify the background color. Os valores de cor podem variar de 0 a 255.

 The R/W color pair in the example above can also be specified with this RGB color pair:

 RGB(255,0,0,255,255,255)

 No FoxPro para Windows e no FoxPro para Macintosh, a cláusula COLOR não afeta a cor dos botões de pressão. Somente a cor da mensagem (se a mensagem não for exibida na barra de status) é afetada pela cláusula COLOR.

 A tabela a seguir lista os pares de cores e o que cada par de cores na lista controla.

 Par de cores Botão de pressão

 Número Atributo

 ---------- -----------

 5 Message

 6 Selected button prompt - FoxPro for MS-DOS only

 7 Hot keys - FoxPro for MS-DOS only

 9 Enabled button prompt - FoxPro for MS-DOS only

 10 Disabled button prompt - FoxPro for MS-DOS only

 O exemplo a seguir cria botões de pressão OK e Cancel com as teclas de atalho O e C, respectivamente. Além disso, os botões possuem as seguintes características de cor:

  O botão selecionado é exibido com prompt branco brilhante em fundo azul (W+/B).

  Os caracteres de tecla de atalho são exibidos em vermelho em fundo azul (R/B).

  Botões habilitados são exibidos com prompt amarelo em fundo azul (GR+/B).

  Botões desabilitados são exibidos com prompt branco em fundo azul (W/B).

 Quando você pula um par de cores, deve incluir uma vírgula onde o par de cores é omitido.

 Aqui estão os comandos:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '* \<OK;\<CANCEL;\\DISABLED';

 COLOR ,,,,,W+/B,R/B,,GR+/B,W/B

 READ

# Observações

Esta variação de @ ... GET cria botões de pressão ou botões de pressão com imagem. Um único botão ou um grupo de botões pode ser criado. No FoxPro para MS-DOS, um botão de pressão é exibido como uma cadeia de texto entre colchetes angulares direito e esquerdo.

Se você usar o Construtor de telas para criar suas telas de entrada de dados, talvez não precise usar este comando. O Construtor de telas gera automaticamente os comandos que criam botões de pressão e botões de pressão com imagem.

A cadeia de texto, frequentemente chamada de prompt, é especificada na cláusula FUNCTION ou PICTURE. Normalmente, um botão de pressão é usado para acionar uma ação. A ação acionada é especificada em uma cláusula VALID. Um botão de pressão é ativado emitindo READ ou READ CYCLE.

Você pode criar botões de pressão com imagem no FoxPro para Windows e no FoxPro para Macintosh. Imagens nos botões substituem os prompts dos botões de pressão.
