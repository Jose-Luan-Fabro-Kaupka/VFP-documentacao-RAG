# Comando DEFINE BAR

Cria um item de menu em um menu criado com DEFINE POPUP.

```foxpro
DEFINE BAR nMenuItemNumber1 | SystemItemName OF MenuName
   PROMPT cMenuItemText [PICTURE cFileName] [PICTRES cMenubarName]
   [BEFORE nMenuItemNumber2 | AFTER nMenuItemNumber3]
   [FONT cFontName [, nFontSize [, nFontCharSet]]] [STYLE cFontStyle]
   [KEY KeyLabel [, cKeyText]] [MARK cMarkCharacter]
   [MESSAGE cMessageText] [SKIP [FOR lExpression]]
   [COLOR SCHEME nSchemeNumber | COLOR ColorPairList]
   [MRU] [INVERT]
```

#### Parâmetros
 **nMenuItemNumber1**
Especifica o número do item de menu. O número do item de menu permite referenciar o item de menu em outros comandos e funções.
**SystemItemName**
Especifica um item de menu no menu do sistema do Visual FoxPro. Por exemplo, para fornecer acesso ao item de menu Print, emita o seguinte: DEFINE BAR _MFI_PRINT OF popMyPopup PROMPT "Print..." Nem todos os itens de menu do sistema do Visual FoxPro estão disponíveis. Use SYS(2013) para retornar uma lista dos nomes de menu do sistema do Visual FoxPro disponíveis.
**OF MenuName**
Especifica o nome do menu no qual os itens de menu são colocados.
**PROMPT cMenuItemText**
Especifica o caption que aparece no item de menu. You can create a barra separadora by specifying a backslash and a dash (\-) for cMenuItemText . A barra separadora is used to separate item groups on a menu. For example, including the following command in a menu definition creates a barra separadora between the third and fifth menu items: DEFINE BAR 4 OF popMyPopup PROMPT '\-' You can create menus de múltiplas colunas by specifying a backslash and a vertical bar (\|) at the beginning of cMenuItemText . The menu item starts a new column, and subsequent menu items are placed in the same column until another menu item beginning with \| is encountered. For example, including the following command in a menu definition creates a new column in the menu: DEFINE BAR 4 OF popMyPopup PROMPT '\|Start a new column' You can create an tecla de acesso for a menu item by placing a backslash and a less-than sign (\<) before the character to be the tecla de acesso. For example: DEFINE POPUP popReceive DEFINE BAR 1 OF popReceive PROMPT '\<Invoices' DEFINE BAR 2 OF popReceive PROMPT 'In\<quiry' ACTIVATE POPUP popReceive The user can press the I key to choose Invoices from the Receive menu and press the Q key to choose Inquiry from the same menu.
**PICTURE cPictureName**
Permite usar uma imagem existente com a barra de menu. You can specify cPictureName in a relative path.
**PICTRES cMenubarName**
Especifica um nome de barra de menu do sistema como recurso para um menu. If cPictureName = "", then contents of Resname field of the .mnx table structure is treated as filename for use in DEFINE BAR...PICTURE. This functionality was introduced in Visual FoxPro 7.0. Observação Você deve incluir uma cláusula MARGIN in the appropriate DEFINE POPUP command in order for the PICTURE or PICTRES clauses to function properly.
**BEFORE nMenuItemNumber2**
Coloca um item de menu antes do item de menu especificado com nMenuItemNumber2.
**AFTER nMenuItemNumber3**
Coloca um item de menu depois do item de menu especificado com nMenuItemNumber3. Observação Para que BEFORE ou AFTER to have an effect, you must include the RELATIVE clause when you create the menu with DEFINE POPUP. You can also include _MFIRST and _MLAST in the BEFORE and AFTER clauses. If you include_MFIRST in the BEFORE clause, the menu item is the first item on the menu. If you include_MFIRST in the AFTER clause, the menu item is the second item on the menu. If you include_MLAST in the AFTER clause, the menu item is the last item on the menu. If you include_MLAST in the BEFORE clause, the menu item is the next-to-last item on the menu. Menus created with DEFINE POPUP RELATIVE do not reserve space for undefined menu items. For example, if you define items 1, 2, 4, and 5 on a menu, a space for item 3 is not reserved. You can later insert item 3. The menu expands to accommodate it. The following program displays the differences in the order and placement of the items on each type of menu: * DEFINE POPUP... relative example DEFINE POPUP popRelatYes RELATIVE FROM 1,1 DEFINE BAR 4 OF popRelatYes PROMPT '4444' DEFINE BAR 3 OF popRelatYes PROMPT '3333' DEFINE BAR 2 OF popRelatYes PROMPT '2222' DEFINE BAR 1 OF popRelatYes PROMPT '1111' DEFINE BAR 6 OF popRelatYes PROMPT '6666' BEFORE 4 * DEFINE POPUP... non-relative example DEFINE POPUP popRelatNo FROM 1,10 DEFINE BAR 4 OF popRelatNo PROMPT '4444' DEFINE BAR 3 OF popRelatNo PROMPT '3333' DEFINE BAR 2 OF popRelatNo PROMPT '2222' DEFINE BAR 1 OF popRelatNo PROMPT '1111' DEFINE BAR 6 OF popRelatNo PROMPT '6666' ACTIVATE POPUP popRelatYes NOWAIT && Display "relative" poup ACTIVATE POPUP popRelatNo && Display "non-relative" popup
**FONT cFontName [, nFontSize [, nFontCharSet ]]**
Especifica uma fonte para o item de menu. cFontName specifies the name of the font, and nFontSize specifies the point size. You can specify a language script with nFontCharSet . See the GETFONT( ) Function for a list of available language script values. For example, the following command creates a menu item in 12-point Courier font: DEFINE BAR 1 OF popReceive PROMPT '\<Invoices' FONT 'Courier', 12 If the font you specify is not available, a font with similar font characteristics is substituted. If you include the FONT clause but omit the point size nFontSize , a 10-point font is used.
**STYLE cFontStyle**
Especifica um estilo de fonte para o item de menu. If you omit the STYLE clause, the normal font style is used. If the font style you specify is not available, the normal font style is used. The font styles you can specify with cFontStyle are as follows: Character Font style B Bold I Italic N Normal Q Opaque – Strikeout T Transparent U Underline You can include more than one character to specify a combination of font styles. For example, the following command specifies Bold Italic: DEFINE BAR 1 OF popReceive PROMPT '\<Invoices' STYLE 'BI'
**KEY KeyLabel [, cKeyText ]**
Especifica uma tecla de acesso ou combinação de teclas para um item de menu. The menu does not have to be activated in order for the menu item to be chosen, unlike when you assign an tecla de acesso using a backslash and a less-than sign (\<). For a list of available keys and key combinations and their key label names, see ON KEY LABEL Command . Observação Se uma macro de teclado is already defined with the same key label, the keyboard macro takes precedence, and the menu item cannot be chosen with the specified key or key combination. Include cKeyText to replace the key label with your own text. You can use any character in the cKeyText parameter; for example, you can use the text "^B" to indicate a key label of CTRL+B. For example, including KEY CTRL+B places the text CTRL+B on the menu to the right of the menu item name, but specifying KEY CTRL+B, "^B" places the text ^+B on the menu. You can suppress the display of a key label by specifying an empty string for cKeyText .
**MARK cMarkCharacter**
Especifica um caractere de marca que aparece à esquerda do item de menu. MARK can be included to change the default caractere de marca to a character specified with cMarkCharacter . If cMarkCharacter includes more than one character, only the first character is used as the caractere de marca. The default caractere de marca is a check. The MARK clause is ignored and the default caractere de marca is used if the menu containing the menu item is integrated into the Visual FoxPro system menu. Also, the MARK clause is ignored if FoxFont is not the font for the main Visual FoxPro window or the user-defined window in which the menu containing the menu item is placed. Observação Especificar um caractere de marca does not mark a menu item. Use SET MARK OF to mark a menu item. Mark characters specified in DEFINE BAR take precedence over caractere de marcas specified with MARK in DEFINE POPUP. SET MARK OF is used to toggle caractere de marcas on or off, and can also be used to specify a caractere de marca for an individual menu item or for all menu items.
**MESSAGE cMessageText**
Exibe uma mensagem quando o usuário seleciona um item de menu. The message is placed in the graphical status bar. If the graphical status bar is turned off with SET STATUS BAR OFF, the message is centered on the last line of the main Visual FoxPro window.
**SKIP [FOR lExpression ]**
Especifica uma condição em que, se lExpression for avaliada como true (.T.), o item de menu é desabilitado, impedindo que o usuário o escolha; se false (.F.), o item de menu é habilitado. A item de menu desabilitado appears in the disabled colors. You can also disable a menu item by placing a backslash (\) before the text of the prompt. For example: DEFINE BAR 1 OF popReceive PROMPT '\Invoices' A menu item disabled with SKIP or \ cannot be selected.
**COLOR SCHEME nSchemeNumber**
Especifica as cores para um item de menu individual, substituindo as cores padrão ou as cores especificadas com DEFINE POPUP.
**COLOR ColorPairList**
Especifica as cores para um item de menu individual, substituindo as cores padrão ou as cores especificadas com DEFINE POPUP. You can specify the colors of all menu items, caractere de marcas, and messages. By default, the colors of menu items are determined by color scheme 2 of the current color set.
**MRU**
Especifica que o menu exibe chevrons verticais indicando um menu do tipo Most Recently Used. You must provide script that dynamically handles the menus and adds any new menu bars. For menus invoked with the MRU keyword, Visual FoxPro imposes a 1-2 second delay before triggering the ON SELECTION BAR command. A user can click on the menu bar to immediately trigger the ON SELECTION BAR command. If you use the MRU keyword, Visual FoxPro ignores PROMPT and other keywords associated with the bar. DEFINE BAR 4 OF popMyPopup MRU
**INVERT**
Especifica que o menu é exibido com efeito rebaixado. DEFINE BAR 4 OF popMyPopup PROMPT '\|Start a new column' ; PICTRES _med_copy INVERT

# Observações

DEFINE BAR é usado com DEFINE POPUP para criar menus. Um menu é criado e recebe um nome com DEFINE POPUP. Os itens de menu são colocados no menu com uma série de comandos DEFINE BAR.

Se você usar o Menu and Shortcut Designers para criar seu menu, talvez não precise usar esses comandos. O Menu Designer cria automaticamente os comandos para seu menu. O Menu Designer usa o menu do sistema do Visual FoxPro, que você pode modificar adicionando seus próprios itens de menu. Para obter mais informações sobre criação de menus, consulte Designing Menus and Toolbars.

Você também pode criar um menu que contém registros ou campos de uma tabela ou uma lista de arquivos disponíveis no disco. Para obter mais informações, consulte as cláusulas PROMPT FIELD, PROMPT STRUCTURE e PROMPT FILES no comando DEFINE POPUP.

Use ON BAR para criar um submenu em cascata para um item de menu.

# Exemplo

O exemplo a seguir usa DEFINE BAR para criar itens em menus. A barra de menu do sistema atual é primeiro salva na memória com SET SYSMENU SAVE, e depois todos os títulos de menu do sistema são removidos com SET SYSMENU TO.

Dois novos títulos de menu do sistema são criados com DEFINE PAD, e DEFINE POPUP é usado para criar um menu suspenso para cada título de menu. DEFINE BAR é usado para criar itens em cada um dos menus. Quando um título de menu é escolhido, ON PAD usa ACTIVATE POPUP para ativar o menu correspondente.

Quando um item é escolhido de um menu, ON SELECTION POPUP usa PROMPT( ) e POPUP( ) para passar o número do item e o nome do menu ao procedimento CHOICE. CHOICE exibe o prompt do item escolhido e o nome do menu que contém o item. Se Exit for escolhido no menu Card Info, o menu do sistema original do Visual FoxPro é restaurado.

```foxpro
   *** Name this program DEFINBAR.PRG ***
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
      DO choice IN definbar WITH PROMPT(), POPUP()
   DEFINE POPUP cardinfo MARGIN RELATIVE COLOR SCHEME 4
   DEFINE BAR 1 OF cardinfo PROMPT '\<View Charges' ;
      KEY ALT+V, ''
   DEFINE BAR 2 OF cardinfo PROMPT 'View \<Payments' ;
      KEY ALT+P, ''
   DEFINE BAR 3 OF cardinfo PROMPT 'Vie\<w Users' KEY ALT+W, ''
   DEFINE BAR 4 OF cardinfo PROMPT '\-'
   DEFINE BAR 5 OF cardinfo PROMPT '\<Charges '
   DEFINE BAR 6 OF cardinfo PROMPT '\-'
   DEFINE BAR 7 OF cardinfo PROMPT 'E\<xit '
   ON SELECTION POPUP cardinfo;
      DO choice IN definbar WITH PROMPT(), POPUP()
   PROCEDURE choice
   PARAMETERS mprompt, mpopup
   WAIT WINDOW 'You chose ' + mprompt + ;
      ' from popup ' + mpopup NOWAIT
   IF mprompt = 'Exit'
      SET SYSMENU TO DEFAULT
   ENDIF
```
