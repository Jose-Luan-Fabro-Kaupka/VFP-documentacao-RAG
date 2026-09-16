# Comando DEFINE POPUP

Cria um menu.

```foxpro
DEFINE POPUP MenuName [FROM nRow1, nColumn1] [TO nRow2, nColumn2]
   [IN [WINDOW] WindowName | IN SCREEN]
      [FONT cFontName [, nFontSize] [, nFontCharSet]] [STYLE cFontStyle]
     [FOOTER cFooterText] [KEY KeyLabel] [MARGIN]
   [MARK cMarkCharacter] [MESSAGE cMessageText] [MOVER] [MULTISELECT]
   [PROMPT FIELD FieldName | PROMPT FILES [LIKE FileSkeleton]
      | PROMPT STRUCTURE] [RELATIVE] [SCROLL] [SHORTCUT]
   [TITLE cMenuTitleText] [RTLJUSTIFY]
   [COLOR SCHEME nSchemeNumber | COLOR ColorPairList]
```

#### Parâmetros
 **MenuName**
Especifica o nome do menu a criar.
**FROM nRow1 , nColumn1 TO nRow2 , nColumn2**
Especifica onde o menu é colocado. nRow1 , nColumn1 especifica coordenadas para o canto superior esquerdo do menu. Se você omitir a cláusula FROM, o Visual FoxPro coloca o canto superior esquerdo do menu na primeira linha e primeira coluna da janela principal do Visual FoxPro ou de uma janela definida pelo usuário. Para criar um menu com um tamanho específico, você também pode incluir TO nRow2 , nColumn2 para especificar a localização do canto inferior direito do menu. Se você incluir FROM nRow1 , nColumn1 e omitir TO nRow2 , nColumn2 , o Visual FoxPro dimensiona automaticamente o menu. O menu é tão largo quanto o item de menu mais longo nele (se os itens são criados com DEFINE BAR) e tão longo quanto necessário para exibir todos os itens de menu. O comprimento do menu é limitado pelo tamanho da janela principal do Visual FoxPro ou da janela definida pelo usuário na qual o menu é colocado. Se um menu não é grande o suficiente para conter todos os itens de menu, uma barra de rolagem aparece para que você possa rolar pelos itens de menu.
**IN [WINDOW] WindowName**
Coloca um menu em uma janela definida pelo usuário que você especifica com WindowName . Se você omitir esta cláusula, o menu é colocado na janela principal do Visual FoxPro por padrão, a menos que haja uma janela definida pelo usuário ativa. Se houver uma janela definida pelo usuário ativa, o menu é colocado na janela ativa.
**IN SCREEN**
Coloca explicitamente um menu na janela principal do Visual FoxPro.
**FONT cFontName [, nFontSize [, nFontCharSet ]]**
Especifica uma fonte padrão para o menu. Você pode substituir a fonte padrão para um item de menu individual incluindo a cláusula FONT em DEFINE BAR. cFontName specifies the name of the font, and nFontSize specifies the point size. You can specify a language script with nFontCharSet . Consulte a Função GETFONT( ) para uma lista de valores de script de idioma disponíveis. Por exemplo, o seguinte comando cria um menu em fonte Courier de 12 pontos: DEFINE POPUP popMyPopup FONT 'Courier', 12 Se a fonte que você especifica não estiver disponível, uma fonte com características de fonte semelhantes é substituída. Se você incluir a cláusula FONT mas omitir o tamanho em pontos nFontSize , uma fonte de 10 pontos é usada.
**STYLE cFontStyle**
Especifica um estilo de fonte padrão para o menu. Você pode substituir o estilo padrão para um item de menu individual incluindo a cláusula FONT em DEFINE BAR. Se você omitir a cláusula STYLE, ou se o estilo de fonte que você especifica não estiver disponível, o estilo de fonte Normal é usado. Os estilos de fonte que você pode especificar com cFontStyle estão listados na tabela a seguir: Caractere Estilo de fonte B Bold I Italic N Normal Q Opaque - Strikeout T Transparent U Underline Você pode incluir mais de um caractere para especificar uma combinação de estilos de fonte. Por exemplo, o seguinte comando especifica Bold Italic: DEFINE MENU popMyPopup STYLE 'BI'
**FOOTER cFooterText**
Cria um rodapé com o texto especificado com cFooterText centralizado na borda inferior do menu.
**KEY KeyLabel**
Especifica uma tecla de acesso ou combinação de teclas para um menu. Para uma lista de teclas e combinações de teclas disponíveis e seus nomes de etiqueta de tecla, consulte Comando ON KEY LABEL . Incluir KEY é equivalente a emitir o seguinte comando: ON KEY LABEL KeyLabel ACTIVATE POPUP MenuName Observação Se uma macro de teclado já estiver definida com a mesma etiqueta de tecla, a macro de teclado tem precedência, e o menu não pode ser ativado com a tecla ou combinação de teclas especificada.
**MARGIN**
Coloca um espaço extra à esquerda e à direita de cada item de menu. Caracteres de marca são exibidos no espaço à esquerda de um item, e setas indicando submenus em cascata adicionais disponíveis são exibidas à direita dos itens de menu. Se você omitir MARGIN, os caracteres de marca substituem o primeiro caractere dos nomes dos itens de menu; setas hierárquicas substituem o último caractere dos itens de menu. Observação Você deve incluir esta cláusula se desejar usar as cláusulas DEFINE BAR ... PICTURE ou PICTRES.
**MARK cMarkCharacter**
Especifica um caractere que aparece à esquerda de um item no menu. O caractere de marca padrão é uma marca de seleção. A cláusula MARK é ignorada e o caractere de marca padrão é usado se o menu estiver integrado ao menu do sistema do Visual FoxPro. Além disso, a cláusula MARK é ignorada se FoxFont não for a fonte da janela principal do FoxPro ou da janela definida pelo usuário na qual o menu é colocado. MARK pode ser incluído para alterar o caractere de marca padrão para um caractere especificado com cMarkCharacter . Se cMarkCharacter inclui mais de um caractere, apenas o primeiro caractere é usado como caractere de marca. Observação Especificar um caractere de marca não marca um item de menu. Use SET MARK OF para marcar um item de menu. A cláusula MARK define o caractere de marca para todos os itens no menu. Caracteres de marca especificados com comandos DEFINE BAR têm precedência sobre caracteres de marca especificados com a cláusula MARK em DEFINE POPUP. SET MARK OF é usado para alternar caracteres de marca ligados ou desligados e também pode ser usado para especificar um caractere de marca para um item de menu individual ou para todos os itens de menu.
**MESSAGE cMessageText**
Exibe uma mensagem quando você seleciona um item de menu. A mensagem é colocada na barra de status gráfica. Se a barra de status baseada em caracteres estiver ligada com SET STATUS ON, a mensagem é centralizada na última linha da janela principal do Visual FoxPro.
**MOVER**
Coloca uma seta de duas pontas na caixa Mover à esquerda do item selecionado no menu. Você pode arrastar a seta de duas pontas para mover um item para outra posição no menu. GETBAR( ) pode ser usado para determinar onde cada item está posicionado no menu. Você não pode reorganizar itens em um menu criado com uma cláusula PROMPT.
**MULTISELECT**
Permite que o usuário selecione vários itens de um menu ao mesmo tempo. Quando o usuário escolhe um item de um menu, o caractere de marca é colocado à esquerda do item. Você não pode fazer seleções múltiplas de um menu criado com uma cláusula PROMPT. MRKBAR( ) pode ser usado para determinar quais itens são escolhidos do menu. Se você incluir MULTISELECT em DEFINE POPUP, pode incluir MARGIN para reservar espaço em cada item para o caractere de marca. No exemplo a seguir, um menu chamado popFruits é criado. MULTISELECT é incluído para criar um menu que permite que vários itens sejam escolhidos. Cada um dos quatro itens tem um caractere de marca diferente. Quando um usuário escolhe itens do menu, os itens são marcados e uma rotina chamada yourchoice exibe os itens escolhidos. CLEAR ACTIVATE SCREEN DEFINE POPUP popFruits FROM 5,5 ; MULTISELECT MARGIN && Create multi-choice menu DEFINE BAR 1 OF popFruits ; PROMPT '\<Apples' MARK CHR(3) && First item DEFINE BAR 2 OF popFruits ; PROMPT '\<Bananas' MARK CHR(4) && Second item DEFINE BAR 3 OF popFruits ; PROMPT '\<Grapes' MARK CHR(5) && Third item DEFINE BAR 4 OF popFruits ; PROMPT '\<Lemons' MARK CHR(6) && Fourth item @ 12,5 SAY 'Your choices:' ON SELECTION POPUP popFruits DO yourchoice && Choice routine ACTIVATE POPUP popFruits PROCEDURE yourchoice && Executed when choice is made @ 13,5 CLEAR FOR gnCount = 1 TO CNTBAR('popFruits') && Loop for # of items IF MRKBAR('popFruits', gnCount) = .T. && Option is marked, ? PRMBAR('popFruits', gnCount) AT 5 && display caption ENDIF NEXT
**PROMPT FIELD FieldName**
Especifica o nome do campo de uma tabela aberta cujos registros se tornam os itens no menu. O menu contém um item para cada registro na tabela. Quando o menu é ativado, a área de trabalho da tabela é selecionada. Dica Você pode aproveitar a Rushmore Query Optimization se definir um filtro no campo especificado com PROMPT FIELD usado no menu. Para obter mais informações sobre Rushmore Query Optimization, consulte Comando SET OPTIMIZE e Using Rushmore Query Optimization to Speed Data Access in Optimizing Applications . FieldName também pode conter vários nomes de campo e expressões concatenados com o operador de adição (+). FieldName também pode ser o nome do campo em uma tabela aberta em outra área de trabalho ou uma função definida pelo usuário. Não há limite para o número de entradas que podem aparecer em um menu criado com PROMPT FIELD.
**PROMPT FILES [LIKE FileSkeleton ]**
Cria um menu que exibe os nomes dos arquivos disponíveis no diretório atual. LIKE FileSkeleton permite especificar os arquivos exibidos no menu usando curingas. Por exemplo, para criar um menu que exibe os nomes das tabelas na unidade e diretório padrão, inclua o seguinte comando: PROMPT FILES LIKE *.DBF Você pode criar um menu que exibe os nomes de arquivos em outras unidades e em outros diretórios ou pastas incluindo uma especificação de unidade ou volume, uma especificação de diretório, ou ambos. Por exemplo, para criar um menu que exibe os nomes de arquivos de programa em um diretório chamado PROGRAMS na unidade C, inclua o seguinte comando: PROMPT FILES LIKE C:\PROGRAMS\*.PRG
**PROMPT STRUCTURE**
Exibe os nomes dos campos na tabela atual no menu de acordo com a estrutura de campos da tabela. Quando o menu é ativado, a área de trabalho da tabela é selecionada.
**RELATIVE**
Especifica a ordem na qual os itens são colocados em um menu. Se você criar um menu sem a cláusula RELATIVE, um item é posicionado em um menu em uma ordem ditada pelo número da barra do item. Espaço no menu é reservado para itens indefinidos. Por exemplo, se o primeiro e o terceiro itens estão definidos e o menu é ativado, uma linha em branco reservada para o segundo item é colocada no menu. Se você criar um menu com RELATIVE, os itens aparecem no menu na ordem em que são definidos. Espaço no menu não é reservado para itens indefinidos. Definir um menu com RELATIVE também permite usar as cláusulas BEFORE e AFTER em DEFINE BAR para posicionar itens em um menu em relação a outros itens. Se um menu é criado sem RELATIVE, incluir BEFORE ou AFTER em DEFINE BAR gera um erro. Execute os dois exemplos de programa a seguir e compare o posicionamento dos itens em cada menu. *** RELATIVE Example *** DEFINE POPUP popRelatYes RELATIVE FROM 1,1 DEFINE BAR 4 OF popRelatYes PROMPT '4444' DEFINE BAR 3 OF popRelatYes PROMPT '3333' DEFINE BAR 2 OF popRelatYes PROMPT '2222' DEFINE BAR 1 OF popRelatYes PROMPT '1111' DEFINE BAR 6 OF popRelatYes PROMPT '6666' BEFORE 4 ACTIVATE POPUP popRelatYes *** NON-RELATIVE Example *** DEFINE POPUP popRelatNo FROM 1,1 DEFINE BAR 4 OF popRelatNo PROMPT '4444' DEFINE BAR 3 OF popRelatNo PROMPT '3333' DEFINE BAR 2 OF popRelatNo PROMPT '2222' DEFINE BAR 1 OF popRelatNo PROMPT '1111' DEFINE BAR 6 OF popRelatNo PROMPT '6666' ACTIVATE POPUP popRelatNo
**SCROLL**
Coloca uma barra de rolagem à direita do menu que você cria. A barra de rolagem é exibida apenas quando há mais itens do que podem caber no menu, ou se o menu é muito longo para caber na janela principal do Visual FoxPro ou na janela definida pelo usuário na qual é colocado.
**SHORTCUT**
Cria um menu de atalho. Um menu de atalho geralmente aparece quando uma seleção, toolbar ou botão da barra de tarefas é clicado com o botão direito do mouse. O menu de atalho lista comandos pertinentes à região da tela na qual o mouse foi clicado com o botão direito. Você pode incluir MROW( ) e MCOL( ) na cláusula FROM para ativar o popup no local onde o mouse é clicado.
**TITLE cMenuTitleText**
Exibe um título no centro da borda superior do menu. cTitleText especifica o título do menu.
**RTLJUSTIFY**
Especifica que o texto no popup é justificado em direção da direita para a esquerda. A cláusula RTLJUSTIFY é destinada ao uso com fontes que suportam alinhamentos bidirecionais. Emita SET SYSMENU TO LTRJUSTIFY para retornar o sistema de menu à justificação padrão da esquerda para a direita. Esta opção está disponível apenas quando o Windows está configurado para uma localidade do Oriente Médio.
**COLOR SCHEME nSchemeNumber**
Especifica as cores para todos os elementos de um menu. Por padrão, as cores dos menus criados com DEFINE POPUP são controladas pelo esquema de cores 2.
**COLOR ColorPairList**
Especifica as cores para todos os elementos de um menu.

# Observações

Para colocar um conjunto de itens de menu que você define em um menu, use uma série de comandos DEFINE BAR. Para colocar registros, arquivos ou campos em um menu, use as opções PROMPT FIELD, PROMPT FILES ou PROMPT STRUCTURE de DEFINE POPUP.

Quando o menu é exibido e ativado com ACTIVATE POPUP, você pode escolher um dos itens no menu. Dependendo do item escolhido, uma rotina pode ser executada ou outro menu pode ser exibido e ativado. Um menu que exibe outro menu quando um item é escolhido é chamado de submenu em cascata. Para obter mais informações sobre a criação de submenus, consulte Comando ON BAR.

Se você usar os Menu and Shortcut Designers para criar seu menu, talvez não precise usar esses comandos. O Menu Designer cria automaticamente os comandos para seu menu. O Menu Designer usa o menu do sistema do Visual FoxPro, que você pode então modificar adicionando seus próprios itens de menu.

Para obter mais informações sobre a criação de menus, consulte Menu System Creation.

# Exemplo

O exemplo a seguir usa DEFINE POPUP para criar menus que são ativados quando um título de menu na barra de menu é escolhido. A barra de menu do sistema atual é primeiro salva na memória com SET SYSMENU SAVE, e então todos os títulos de menu do sistema são removidos com SET SYSMENU TO.

Dois novos títulos de menu do sistema são criados com DEFINE PAD, e DEFINE POPUP cria um menu suspenso para cada título de menu. DEFINE BAR cria itens em cada um dos menus. Quando um título de menu é escolhido, ON PAD usa ACTIVATE POPUP para ativar o menu correspondente.

Quando um item é escolhido de um menu, ON SELECTION POPUP usa PROMPT( ) e POPUP( ) para passar o número do item e o nome do menu ao procedimento CHOICE. CHOICE exibe o texto do item escolhido e o nome do menu que contém o item. Se o item Exit for escolhido do menu Card Info, o menu do sistema original do Visual FoxPro é restaurado.

```foxpro
*** Name this program DEFINPOP.PRG ***
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
   DO choice IN definpop WITH PROMPT(), POPUP()
DEFINE POPUP cardinfo MARGIN RELATIVE COLOR SCHEME 4
DEFINE BAR 1 OF cardinfo PROMPT '\<View Charges' ;
   KEY ALT+V, ''
DEFINE BAR 2 OF cardinfo PROMPT 'View \<Payments' ;
   KEY ALT+P, ''
DEFINE BAR 3 OF cardinfo PROMPT 'Vie\<w Users' ;
   KEY ALT+W, ''
DEFINE BAR 4 OF cardinfo PROMPT '\-'
DEFINE BAR 5 OF cardinfo PROMPT '\<Charges '
DEFINE BAR 6 OF cardinfo PROMPT '\-'
DEFINE BAR 7 OF cardinfo PROMPT 'E\<xit '
ON SELECTION POPUP cardinfo;
   DO choice IN definpop WITH PROMPT(), POPUP()
PROCEDURE choice
PARAMETERS mprompt, mpopup
WAIT WINDOW 'You chose ' + mprompt + ;
   ' from popup ' + mpopup NOWAIT
IF mprompt = 'Exit'
   SET SYSMENU TO DEFAULT
ENDIF
```
