# Comando DEFINE WINDOW

Cria uma janela e especifica seus atributos.

```foxpro
DEFINE WINDOW WindowName1 FROM nRow1, nColumn1 TO nRow2, nColumn2
   | AT nRow3, nColumn3 SIZE nRow4, nColumn4
   [IN [WINDOW] WindowName2 | IN SCREEN | IN DESKTOP [NAME ObjectName]
      [FONT cFontName [, nFontSize [, nFontCharSet]]] [STYLE cFontStyle]
      [FOOTER cFooterText] [TITLE cTitleText] [HALFHEIGHT]
      [DOUBLE | PANEL | NONE | SYSTEM | cBorderString]
      [CLOSE | NOCLOSE] [FLOAT | NOFLOAT] [GROW | NOGROW] [MDI | NOMDI]
      [MINIMIZE | NOMINIMIZE] [ZOOM | NOZOOM] [ICON FILE FileName1]
      [FILL cFillCharacter | FILL FILE FileName2]
      [COLOR SCHEME nSchemeNumber   | COLOR ColorPairList]]
```

#### Parâmetros
 **WindowName1**
Especifica o nome da janela a ser criada. Os nomes de janela podem ter até 254 caracteres in Visual FoxPro. Devem começar com uma letra ou sublinhado, and cannot begin with a number. Podem conter qualquer combinação de letras, números e sublinhados.
**FROM nRow1 , nColumn1 TO nRow2 , nColumn2**
Especifica a posição e o tamanho da janela definida pelo usuário on the main Visual FoxPro window. FROM nRow1 , nColumn1 specifies the position of the upper-left corner of the user-defined window on the main Visual FoxPro window. TO nRow2 , nColumn2 specifies the position of the lower-right corner of the user-defined window on the main Visual FoxPro window. Uma janela pode ser definida com coordenadas que ficam fora the Visual FoxPro window border and can be larger than the main Visual FoxPro window. A localização e o tamanho da janela são determinados pela fonte of the window's parent. The window's parent can be another user-defined window or the main Visual FoxPro window.
**AT nRow3 , nColumn3S IZE nRow4 , nColumn4**
Specifies the position and size of a user-defined window. AT nRow3 , nColumn3 specifies the position of the upper-left corner of the user defined window on the main Visual FoxPro window. This position is determined by the current font of the window's parent. Como a cláusula AT é idêntica à cláusula FROM in all respects, as duas cláusulas podem ser usadas de forma intercambiável. SIZE nRow4 , nColumn4 especifica em linhas e colunas o tamanho da janela definida pelo usuário e garante que o texto exibido em uma fonte específica se ajustará à janela que você criar. You can specify a font and font style for a user-defined window by including the FONT and STYLE clauses. If you specify a font for the window and include the SIZE clause, its size is determined by the window's font height and width. If you don't specify a font for a window, the window's font is the default system font, 10-point FoxFont.
**IN [WINDOW] WindowName2**
Coloca uma janela definida pelo usuário em uma janela pai. A janela definida pelo usuário torna-se uma janela filha and cannot be moved outside the parent window. If the parent window is moved, the child window moves with it. When a child window is placed in a parent window, the child window coordinates specified with the FROM and TO clauses or the AT and SIZE clauses are relative to the parent window, not the main Visual FoxPro window. In the following example, a parent window, wParent , is created. A child window, wChild , is placed in the parent window. CLEAR DEFINE WINDOW wParent ; FROM 1, 1 TO 20, 30 ; TITLE "Parent" && Parent window. ACTIVATE WINDOW wParent DEFINE WINDOW wChild ; FROM 1, 1 TO 20, 20 ; TITLE "Child" ; IN WINDOW wParent && Child window. ACTIVATE WINDOW wChild ACTIVATE SCREEN WAIT WINDOW 'Press a key to clear the windows' RELEASE WINDOW wParent, wChild CLEAR
**IN SCREEN**
Coloca explicitamente uma janela definida pelo usuário na janela principal do Visual FoxPro. Se você omitir IN SCREEN, a janela definida pelo usuário é colocada na janela principal do Visual FoxPro por padrão. You can include the IN WINDOW clause in ACTIVATE WINDOW to place the window in another user-defined window and override this IN SCREEN clause.
**IN DESKTOP**
Coloca uma janela definida pelo usuário na área de trabalho do Microsoft Windows, outside the main Visual FoxPro window. The position of the window is relative to the Windows desktop, and the current font of the main Visual FoxPro window.
**NAME ObjectName**
Cria uma referência de objeto para a janela, allowing you to manipulate the window with object-oriented properties available for the form object. Para obter informações adicionais sobre programação orientada a objetos in Visual FoxPro, see Object-Oriented Programming . Para obter informações adicionais sobre as propriedades do objeto form you can specify for a window created with the NAME clause, see the Form Object topic.
**FONT cFontName [, nFontSize [, nFontCharSet ]]**
Especifica uma fonte para o texto colocado na janela. cFontName especifica o nome da fonte and nFontSize especifica o tamanho em pontos. Se você omitir nFontSize , uma fonte de 9 pontos é usada. Você pode especificar um script de idioma com nFontCharSet . Consulte GETFONT( ) Function para uma lista de valores de script de idioma disponíveis. Por exemplo, este comando cria uma janela que exibe a saída directed to the window in a 16-point Courier font: DEFINE WINDOW wDisplayFont FROM 2,2 TO 12,22 FONT 'Courier', 16 Se você omitir a cláusula FONT, uma FoxFont de 10 pontos é usada. Se a fonte que você especificar não estiver disponível, uma fonte com características semelhantes é substituída.
**STYLE cFontStyle**
Especifica um estilo de fonte para o texto colocado na janela. cFontStyle specifies the font. Se você omitir a cláusula STYLE, ou se o estilo de fonte que você especificar não estiver disponível, o estilo de fonte Normal é usado. A tabela a seguir lista estilos de fonte e seus caracteres correspondentes. Caractere Estilo de fonte B Bold I Italic N Normal Q Opaque - Strikeout T Transparent U Underline Você pode incluir mais de um caractere para especificar uma combinação de estilos de fonte. No Visual FoxPro, os comandos a seguir especificam o estilo Bold Italic: DEFINE WINDOW wDisplayStyle FROM 2, 2 TO 12, 22 STYLE 'BI'
**FOOTER cFooterText**
Incluído para compatibilidade com versões anteriores. Ignorado nas versões Windows do Visual FoxPro.
**TITLE cTitleText**
Atribui um título com a cláusula TITLE. cTitleText especifica o texto do título e é centralizado na borda superior da janela. Se o título for mais largo que a janela, o título é truncado.
**HALFHEIGHT**
Cria uma janela com barra de título de meia altura. Isso fornece compatibilidade para janelas criadas em versões anteriores of FoxPro that are imported into Visual FoxPro. Quando você usa DEFINE WINDOW para criar uma janela, uma barra de título de meia altura é usada, unless you include the SYSTEM keyword or you include a FONT clause. Se você incluir a palavra-chave HALFHEIGHT, uma barra de título de meia altura é usada independentemente of whether the SYSTEM or FONT clause is included.
**DOUBLE | PANEL | NONE | SYSTEM | cBorderString**
Especifica um estilo de borda para uma janela definida pelo usuário. A borda padrão é uma linha única. Argumento Descrição DOUBLE Especifica uma borda de linha dupla ao redor da janela. PANEL Especifica uma borda larga ao redor da janela. NONE Suprime a borda inteiramente. SYSTEM Especifica que a janela definida pelo usuário pareça uma janela do sistema. When you include certain other clauses (GROW, ZOOM, and so on), the appropriate window controls are placed in the window's border. cBorderString Especifica uma borda personalizada. Para obter mais informações sobre como definir uma borda personalizada, see SET BORDER Command . Including DOUBLE or a custom border string creates a window with the PANEL border. Including the CLOSE, FLOAT, GROW, ZOOM, or MINIMIZE clauses places the appropriate controls on the window even if the SYSTEM window definition clause is not included.
**CLOSE**
Permite que o usuário feche uma janela definida pelo usuário using the keyboard or mouse. Fechar uma janela a remove da janela principal do Visual FoxPro or a parent user-defined window and removes its definition from memory. Se você omitir CLOSE, não poderá fechar a janela usando a interface; the window must be closed using a command in a program or in the Command window.
**NOCLOSE**
Impede que a janela seja fechada, exceto por um comando in a program or in the Command window.
**FLOAT**
Permite que a janela seja movida usando o teclado ou o mouse. Se você omitir FLOAT, não poderá mover a janela, exceto usando o comando MOVE WINDOW in a program or in the Command window.
**NOFLOAT**
Impede que a janela seja movida, exceto usando o comando MOVE WINDOW in a program or in the Command window.
**GROW**
Permite redimensionar uma janela definida pelo usuário using the keyboard or mouse. Se você omitir GROW, não poderá dimensionar a janela, exceto usando o comando SIZE WINDOW in a program or in the Command window.
**NOGROW**
Impede que a janela seja redimensionada, exceto pelo comando SIZE WINDOW in a program or in the Command window.
**MDI**
Cria uma janela definida pelo usuário compatível com MDI. MDI (multiple document interface) é uma especificação that allows multiple document windows and determines their structure and behavior. Se você omitir MDI, a janela que você criar não será compatível com MDI. Quando uma janela compatível com MDI é maximizada: A janela assume o tamanho da janela principal do Visual FoxPro. Os controles da janela desaparecem e seu ícone de menu pop-up aparece in the Visual FoxPro system menu bar. O botão Restore da janela também é colocado na barra de menu do sistema do Visual FoxPro. O título da janela é colocado na barra de título do Visual FoxPro and is separated from the Visual FoxPro title by a hyphen. Se você ativar outra janela compatível com MDI, ela é automaticamente maximizada.
**NOMDI**
Cria uma janela que não é compatível com MDI.
**MINIMIZE**
Permite minimizar uma janela definida pelo usuário using the keyboard or mouse.
**NOMINIMIZE**
Impede que a janela seja minimizada.
**ZOOM**
Permite que a janela seja maximizada usando o teclado ou o mouse. Você também pode restaurar a janela ao seu tamanho original.
**NOZOOM**
Impede que a janela seja maximizada.
**ICON FILE FileName**
Especifica o ícone exibido quando a janela é minimizada. Você deve incluir a palavra-chave MINIMIZE em DEFINE WINDOW. Você pode especificar apenas um arquivo de ícone (.ico); não pode especificar um arquivo bitmap (.bmp).
**FILL FILE FileName2**
Especifica papel de parede (o fundo) para a janela. A janela é preenchida com o FileName2 especificado. Você especifica um arquivo bitmap .bmp.
**COLOR SCHEME nSchemeNumber**
Especifica as cores para a janela definida pelo usuário. Por padrão, as cores das janelas criadas com DEFINE WINDOW são controladas pelo esquema de cores 1.
**COLOR ColorPairList**
Especifica as cores para a janela definida pelo usuário.

# Observações

Depois que janelas definidas pelo usuário são criadas com DEFINE WINDOW, elas podem ser exibidas na janela principal do Visual FoxPro com ACTIVATE WINDOW ou SHOW WINDOW. O número de janelas definidas pelo usuário que você pode criar é limitado apenas pela quantidade de memória disponível e recursos do sistema.

Janelas ativadas permanecem na janela principal do Visual FoxPro até que DEACTIVATE WINDOW ou HIDE WINDOW seja emitido. DEACTIVATE WINDOW e HIDE WINDOW removem janelas da janela principal do Visual FoxPro, mas não removem as definições de janela da memória. Janelas podem ser colocadas novamente na janela principal do Visual FoxPro com ACTIVATE WINDOW ou SHOW WINDOW.

Use CLEAR WINDOWS ou RELEASE WINDOWS para remover janelas da janela principal do Visual FoxPro e definições de janela da memória. Janelas cujas definições foram removidas da memória devem ser recriadas com DEFINE WINDOW para serem exibidas novamente.

# Exemplo

No exemplo a seguir, uma janela chamada `output` é criada e ativada. O programa aguarda que você pressione uma tecla e depois oculta a janela. O programa aguarda que você pressione uma tecla novamente e depois exibe a janela novamente.

```foxpro
CLEAR
DEFINE WINDOW output FROM 2,1 TO 13,75 TITLE 'Output' ;
   CLOSE FLOAT GROW ZOOM
ACTIVATE WINDOW output
WAIT WINDOW 'press any key to hide window output'
HIDE WINDOW output
WAIT WINDOW 'press any key to show window output'
SHOW WINDOW output
WAIT WINDOW 'press any key to release window output'
RELEASE WINDOW  output
```
