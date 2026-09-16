# Comando DEFINE PAD

Cria um título de menu (pad) em uma barra de menu definida pelo usuário ou na barra de menu do sistema do Visual FoxPro.

```foxpro
DEFINE PAD MenuTitle1 OF MenuBarName PROMPT cMenuTitleText
   [AT nRow, nColumn] [BEFORE MenuName2 | AFTER MenuName3]
   [NEGOTIATE cContainerPosition [, cObjectPosition]]
   [FONT cFontName [, nFontSize [, nFontCharSet]]] [STYLE cFontStyle]
   [KEY KeyLabel [, cKeyText]] [MARK cMarkCharacter]
   [SKIP [FOR lExpression]] [MESSAGE cMessageText]
   [COLOR SCHEME nSchemeNumber | COLOR ColorPairList]
```

#### Parâmetros
 **MenuTitle1**
Especifica o título de menu a criar. O título de menu permite referenciar o título de menu em outros comandos e funções.
**OF MenuBarName**
Especifica o nome da barra de menu na qual o título de menu é colocado.
**PROMPT cMenuTitleText**
Especifica o texto que aparece no título de menu. Você pode criar uma tecla de acesso para um título de menu colocando uma barra invertida e um sinal de menor que (\<) antes do caractere que deseja ser a tecla de acesso. No exemplo a seguir, o usuário pode pressionar a tecla I para escolher Invoices no menu Receive e pressionar a tecla Q para escolher Inquiry no mesmo menu: DEFINE MENU mnuReceive DEFINE PAD padInvoice OF mnureceive PROMPT "\<Invoices" DEFINE PAD padInquire OF mnureceive PROMPT "In\<quiry" ACTIVATE MENU mnuReceive
**AT nRow , nColumn**
Especifica onde o título de menu aparece na barra de menu. nRow , nColumn são as coordenadas do lado esquerdo do título de menu na janela principal do Visual FoxPro ou em uma janela definida pelo usuário. Se você omitir a cláusula AT, o lado esquerdo do primeiro título de menu é colocado na linha 0 da janela principal do Visual FoxPro ou da janela definida pelo usuário. O próximo título de menu é colocado à direita do primeiro nome na linha 0, e assim por diante. Observação Você não pode incluir AT para especificar uma localização para títulos de menu em barras de menu criadas com a cláusula BAR em DEFINE MENU.
**BEFORE MenuName2**
Coloca o título de menu na barra de menu à esquerda do título de menu especificado com MenuName2 . A ordem em que os títulos de menu são acessados pelo teclado corresponde à localização dos títulos de menu na barra de menu.
**AFTER MenuName3**
Coloca o título de menu na barra de menu à direita do título de menu especificado com MenuName3 . A ordem em que os títulos de menu são acessados pelo teclado corresponde à localização dos títulos de menu na barra de menu. Você deve primeiro criar o título de menu que especifica em uma cláusula BEFORE ou AFTER. Se você não criar o título de menu primeiro, a colocação do título de menu na barra de menu é determinada pela ordem em que é criado ou por uma localização especificada com a cláusula AT. Para barras de menu criadas sem BAR, BEFORE ou AFTER determina a ordem em que os títulos de menu são acessados pelo teclado. A localização de um título de menu é determinada pela localização especificada com a cláusula AT. Execute os dois exemplos a seguir e observe as diferenças na colocação e ordem de acesso dos títulos de menu quando os títulos de menu são definidos com e sem a cláusula AT: *** Program Example 1 without ATs *** DEFINE MENU mnuBefAft DEFINE PAD padOne OF mnuBefAft PROMPT '1111' DEFINE PAD padTwo OF mnuBefAft PROMPT '2222' DEFINE PAD padThree OF mnuBefAft PROMPT '3333' DEFINE PAD padFour OF mnuBefAft PROMPT '4444' BEFORE padTwo ACTIVATE MENU mnuBefAft *** Program Example 2 with ATs *** DEFINE MENU mnuBefAft DEFINE PAD padOne OF mnuBefAft PROMPT '1111' AT 1,5 DEFINE PAD padTwo OF mnuBefAft PROMPT '2222' AT 1,15 DEFINE PAD padThree OF mnuBefAft PROMPT '3333' AT 1,25 DEFINE PAD padFour OF mnuBefAft PROMPT '4444' BEFORE padTwo AT 1,35 WAIT WINDOW 'Press ESC to erase menu' NOWAIT ACTIVATE MENU mnuBefAft
**NEGOTIATE cContainerPosition [, cObjectPosition ]**
cContainerPosition especifica a localização do título de menu na barra de menu do Visual FoxPro quando a edição visual OLE ocorre para um controle ActiveX contido em um formulário do Visual FoxPro. As configurações para cContainerPosition são: Configuração Descrição NONE O título de menu não é exibido. LEFT O título de menu é colocado à esquerda do File Group. MIDDLE O título de menu é colocado à esquerda do Container Group, após o menu Edit. RIGHT O título de menu é colocado à esquerda do Window Group. As configurações para cObjectPosition são: Configuração Descrição NONE O título de menu não é exibido. LEFT O título de menu é colocado à direita do File Group. MIDDLE O título de menu é colocado à direita do Container Group, após o menu Edit. RIGHT O título de menu é colocado no menu Help. Se você omitir a cláusula NEGOTIATE, o título de menu é removido da barra de menu quando a edição visual OLE ocorre; NONE é o padrão para cContainerPosition e cObjectPosition .
**FONT cFontName [, nFontSize [, nFontCharSet ]]**
Especifica uma fonte para o título de menu. cFontName especifica o nome da fonte, e nFontSize especifica o tamanho em pontos. Você pode especificar um script de idioma com nFontCharSet . Consulte a Função GETFONT( ) para uma lista de valores de script de idioma disponíveis. Por exemplo, o comando a seguir cria um título de menu em fonte Courier de 12 pontos: DEFINE PAD padPageAccts OF mnuReceive FONT 'Courier', 12 Se a fonte que você especifica não está disponível, uma fonte com características semelhantes é substituída. Se você incluir a cláusula FONT mas omitir o tamanho em pontos nFontSize , uma fonte de 10 pontos é usada. A cláusula FONT é ignorada para títulos de menu adicionados ao menu do sistema do Visual FoxPro _MSYSMENU. Observe que o Menu Designer usa o menu do sistema do Visual FoxPro.
**STYLE cFontStyle**
Especifica um estilo de fonte para o título de menu. Se você omitir a cláusula STYLE, ou se o estilo de fonte que você especifica não está disponível, o estilo de fonte Normal é usado. Os estilos de fonte que você pode especificar com cFontStyle são os seguintes: Caractere Estilo de fonte B Bold I Italic N Normal Q Opaque - Strikeout T Transparent U Underline Você pode incluir mais de um caractere para especificar uma combinação de estilos de fonte. Por exemplo, o comando a seguir especifica Bold Italic: DEFINE PAD padPageAccts OF mnuReceive STYLE 'BI' A cláusula STYLE é ignorada para títulos de menu adicionados ao menu do sistema do Visual FoxPro _MSYSMENU. Observe que o Menu Designer usa o menu do sistema do Visual FoxPro.
**KEY KeyLabel [, cKeyText ]**
Especifica uma tecla de acesso ou combinação de teclas para um título de menu. Para uma lista de teclas e combinações de teclas disponíveis e seus nomes de etiqueta de tecla, consulte Comando ON KEY LABEL . Observação Se uma macro de teclado já está definida com a mesma etiqueta de tecla, a macro de teclado tem precedência, e o título de menu não pode ser escolhido com a tecla ou combinação de teclas especificada. A etiqueta de tecla é colocada à direita dos títulos de menu em barras de menu criadas sem a cláusula BAR. A etiqueta de tecla não é exibida em barras de menu criadas com a cláusula BAR ou para títulos de menu na barra de menu do sistema do Visual FoxPro. Inclua cKeyText para substituir a etiqueta de tecla pelo seu próprio texto. Você pode usar qualquer caractere no parâmetro cKeyText; por exemplo, pode usar o texto "^B" para indicar uma etiqueta de tecla CTRL+B. Por exemplo, incluir KEY CTRL+B coloca o texto CTRL+B no menu à direita do nome do item de menu, mas especificar KEY CTRL+B, "^B" coloca o texto ^+B no menu. Você pode suprimir a exibição de uma etiqueta de tecla especificando uma cadeia de caracteres vazia para cKeyText .
**MARK cMarkCharacter**
Especifica um caractere de marca que aparece à esquerda do título de menu. MARK pode ser incluído para alterar o caractere de marca padrão para um caractere especificado com cMarkCharacter . Se cMarkCharacter inclui mais de um caractere, apenas o primeiro caractere é usado como caractere de marca. O caractere de marca padrão é uma marca de verificação. A cláusula MARK é ignorada e o caractere de marca padrão é usado se a barra de menu que contém o título de menu é o menu do sistema do Visual FoxPro. Além disso, a cláusula MARK é ignorada se FoxFont não é a fonte da janela principal do Visual FoxPro ou da janela definida pelo usuário na qual a barra de menu que contém o título de menu é colocada. Caracteres de marca especificados com DEFINE PAD têm precedência sobre caracteres de marca especificados com a cláusula MARK em DEFINE MENU. SET MARK OF é usado para alternar marcas ativadas ou desativadas e também pode ser usado para especificar um caractere de marca para um título de menu individual ou para todos os títulos de menu. Observação Especificar um caractere de marca não marca o título de menu. Use SET MARK OF para marcar um título de menu com o caractere que você especifica.
**SKIP [FOR lExpression ]**
Especifica uma condição pela qual, se lExpression avalia como true (.T.), o título de menu é desabilitado, impedindo o usuário de escolhê-lo. Se lExpression avalia como false (.F.), o título de menu é habilitado. Você também pode desabilitar um item de menu colocando uma barra invertida (\) antes do texto do título de menu. Por exemplo: DEFINE PAD padPageAccts OF mnuReceive PROMPT '\Age Accounts' O título de menu padPageAccts é exibido esmaecido, indicando que não pode ser escolhido. Um título de menu desabilitado pode ser exibido, mas não pode ser selecionado. No entanto, uma mensagem especificada com a cláusula MESSAGE é exibida.
**MESSAGE cMessageText**
Exibe uma mensagem quando o usuário seleciona um título de menu. A mensagem é colocada na barra de status gráfica. Se a barra de status gráfica está desativada com SET STATUS BAR OFF, a mensagem é centralizada na última linha da janela principal do Visual FoxPro.
**COLOR SCHEME nSchemeNumber**
Especifica as cores para um título de menu individual, substituindo as cores padrão ou as cores especificadas com DEFINE MENU.
**COLOR ColorPairList**
Especifica as cores para um título de menu individual, substituindo as cores padrão ou as cores especificadas com DEFINE MENU. Por padrão, as cores dos títulos de menu em barras de menu são determinadas pelo esquema de cores 2 do conjunto de cores atual.

# Observações

Você deve criar cada título de menu colocado na barra de menu com seu próprio comando DEFINE PAD. Uma barra de menu deve ser definida com DEFINE MENU antes que você possa colocar títulos de menu nela, e você deve incluir o nome da barra de menu em DEFINE PAD.

Se você usar o Menu and Shortcut Designers para criar seu menu, pode não precisar usar esses comandos. O Menu Designer cria automaticamente os comandos para seu menu. O Menu Designer usa o menu do sistema do Visual FoxPro, que você pode então modificar adicionando seus próprios itens de menu. Para obter mais informações sobre criação de menus, consulte Criação do sistema de menu.

# Exemplo

O exemplo a seguir usa DEFINE PAD para colocar títulos de menu na barra de menu do sistema do Visual FoxPro. A barra de menu do sistema atual é primeiro salva na memória com SET SYSMENU SAVE, e depois todos os títulos de menu do sistema são removidos com SET SYSMENU TO.

Vários títulos de menu do sistema são criados com DEFINE PAD. Quando um título de menu é escolhido, o procedimento CHOICE é executado. CHOICE exibe o nome do título de menu escolhido e o nome da barra de menu, e alterna o caractere de marca dos títulos de menu ativado e desativado. Se o título de menu Exit é escolhido, o menu do sistema original do Visual FoxPro é restaurado.

```foxpro
*** Name this program DEFINPAD.PRG ***
CLEAR
SET TALK OFF
SET SYSMENU SAVE
SET SYSMENU TO
PUBLIC markpad
markpad = .T.
DEFINE PAD syspad  OF _MSYSMENU PROMPT '\<System'  COLOR SCHEME 3 ;
   KEY ALT+S, ''
DEFINE PAD editpad OF _MSYSMENU PROMPT '\<Edit'  COLOR SCHEME 3 ;
   KEY ALT+E, ''
DEFINE PAD recordpad OF _MSYSMENU PROMPT '\<Record'  COLOR SCHEME 3 KEY ALT+R, ''
DEFINE PAD windowpad OF _MSYSMENU PROMPT '\<Window'  COLOR SCHEME 3 ;
   KEY ALT+W, ''
DEFINE PAD reportpad OF _MSYSMENU PROMPT 'Re\<ports' COLOR SCHEME 3 ;
   KEY ALT+P, ''
DEFINE PAD exitpad OF _MSYSMENU PROMPT 'E\<xit'  COLOR SCHEME 3 ;
   KEY ALT+X, ''
ON SELECTION MENU _MSYSMENU ;
   DO choice IN definpad WITH PAD(), MENU()
PROCEDURE choice
PARAMETER mpad, mmenu
WAIT WINDOW 'You chose ' + mpad + ;
   ' from menu ' + mmenu NOWAIT
SET MARK OF PAD (mpad) OF _MSYSMENU TO ;
   ! MRKPAD('_MSYSMENU', mpad)
markpad = ! markpad
IF mpad = 'EXITPAD'
   SET SYSMENU TO DEFAULT
ENDIF
```
