# Comando DEFINE MENU

Cria uma barra de menu.

```foxpro
DEFINE MENU MenuBarName [BAR [AT LINE nRow]]
   [IN [WINDOW] WindowName | IN SCREEN]
      [FONT cFontName [, nFontSize [, nFontCharSet]]]
   [STYLE cFontStyle] [KEY KeyLabel] [MARK cMarkCharacter]
   [MESSAGE cMessageText] [NOMARGIN]
   [COLOR SCHEME nSchemeNumber | COLOR ColorPairList]
```

#### Parâmetros
 **MenuBarName**
Especifica o nome da barra de menu a ser criada. O nome da barra de menu permite referenciar a barra de menu em outros comandos e funções.
**BAR [AT LINE nRow ]**
Cria uma barra de menu que se comporta como a barra de menu do sistema do Visual FoxPro. A barra de menu tem estas características: Uma barra de menu horizontal de uma linha de altura é desenhada na largura da janela principal do Visual FoxPro ou da janela definida pelo usuário em que é colocada. O posicionamento dos títulos de menu na barra de menu é tratado automaticamente. Se o tamanho ou o número de títulos de menu que você define exceder o tamanho da tela ou de uma janela em que a barra de menu é colocada, a barra de menu rola. O número da linha é especificado com nRow.
**IN [WINDOW] WindowName**
Coloca uma barra de menu em uma janela definida pelo usuário. Especifique o nome da janela em que deseja colocar a barra de menu com WindowName. Se você omitir IN WINDOW, a barra de menu é colocada na janela principal do Visual FoxPro por padrão, a menos que haja uma janela definida pelo usuário ativa. Se houver uma janela definida pelo usuário ativa, a barra de menu é colocada na janela ativa. Esta cláusula é suportada somente em formulários de nível superior, que podem ser definidos com ShowWindow=2 ou Desktop=.T.
**IN SCREEN**
Coloca explicitamente a barra de menu na janela principal do Visual FoxPro.
**FONT cFontName [, nFontSize [, nFontCharSet ]]**
Especifica uma fonte padrão para todos os títulos de menu na barra de menu. Você pode substituir a fonte padrão para um título de menu individual incluindo a cláusula FONT em DEFINE PAD. cFontName especifica o nome da fonte, e nFontSize especifica o tamanho em pontos. Você pode especificar um script de idioma com nFontCharSet. Consulte a função GETFONT( ) para uma lista de valores de script de idioma disponíveis. Por exemplo, o comando a seguir cria uma barra de menu com títulos de menu em fonte Courier de 12 pontos: DEFINE MENU mnuExample FONT 'Courier', 12 Se a fonte que você especificar não estiver disponível, uma fonte com características de fonte semelhantes é substituída. Se você incluir a cláusula FONT, mas omitir o tamanho em pontos nFontSize, uma fonte de 10 pontos é usada. A cláusula FONT é ignorada para títulos de menu adicionados ao menu do sistema do Visual FoxPro _MSYSMENU. Observe que o Menu Designer usa o menu do sistema do Visual FoxPro.
**STYLE cFontStyle**
Especifica um estilo de fonte padrão para todos os títulos de menu na barra de menu. Você pode substituir o estilo padrão para títulos de menu individuais incluindo a cláusula STYLE em DEFINE PAD. Se você omitir a cláusula STYLE, ou se o estilo de fonte que você especificar não estiver disponível, o estilo de fonte Normal é usado. Os estilos de fonte que você pode especificar com cFontStyle são os seguintes: Caractere Estilo de fonte B Negrito I Itálico N Normal Q Opaco - Tachado T Transparente U Sublinhado Você pode incluir mais de um caractere para especificar uma combinação de estilos de fonte. Por exemplo, o comando a seguir especifica Negrito Itálico: DEFINE MENU mnuExample STYLE 'BI' A cláusula STYLE é ignorada para títulos de menu adicionados ao menu do sistema do Visual FoxPro _MSYSMENU. O Menu Designer usa o menu do sistema do Visual FoxPro.
**KEY KeyLabel**
Especifica a tecla ou combinação de teclas usada para ativar a barra de menu. Para uma lista de teclas e combinações de teclas disponíveis e seus nomes de etiqueta de tecla, consulte Comando ON KEY LABEL. Incluir a cláusula KEY é equivalente a emitir o comando a seguir: ON KEY LABEL KeyLabel ACTIVATE MENU MenuName Observação Se uma macro de teclado já estiver definida com a mesma etiqueta de tecla, a macro de teclado tem precedência e a barra de menu não pode ser ativada com a tecla ou combinação de teclas especificada.
**MARK cMarkCharacter**
Especifica um caractere de marca que aparece à esquerda dos títulos de menu na barra de menu. MARK pode ser incluído para alterar o caractere de marca padrão para um caractere especificado com cMarkCharacter. Se cMarkCharacter incluir mais de um caractere, somente o primeiro caractere é usado como caractere de marca. O caractere de marca padrão é uma marca de verificação. A cláusula MARK é ignorada e o caractere de marca padrão é usado se a barra de menu for o menu do sistema do Visual FoxPro. Além disso, a cláusula MARK é ignorada se FoxFont não for a fonte da janela principal do Visual FoxPro ou da janela definida pelo usuário em que a barra de menu é colocada. Observação Especificar um caractere de marca não marca os nomes de menu em uma barra de menu. Use SET MARK OF para marcar os títulos de menu em uma barra de menu com o caractere que você especificar. Caracteres de marca especificados com DEFINE PAD têm precedência sobre caracteres de marca especificados com a cláusula MARK em DEFINE MENU. SET MARK OF é usado para alternar caracteres de marca ligados ou desligados, e também pode ser usado para especificar um caractere de marca para um item de menu individual ou para todos os itens de menu.
**MESSAGE cMessageText**
Exibe uma mensagem quando o usuário seleciona um título de menu. A mensagem é colocada na barra de status gráfica. Se a barra de status gráfica estiver desligada com SET STATUS BAR OFF, a mensagem é centralizada na última linha da janela principal do Visual FoxPro.
**NOMARGIN**
Remove os espaços que são colocados à esquerda e à direita de cada nome de menu por padrão.
**COLOR SCHEME nSchemeNumber**
Especifica as cores para uma barra de menu individual.
**COLOR ColorPairList**
Especifica as cores para uma barra de menu individual. Por padrão, as cores dos itens de menu são determinadas pelo esquema de cores 2 do conjunto de cores atual.

# Observações

Use DEFINE MENU para criar a barra de menu do sistema de menu do seu aplicativo. Use DEFINE PAD para criar cada um dos títulos de menu (pads) na barra de menu. Use ON PAD ... ACTIVATE para especificar qual menu é exibido sob cada título de menu. Use DEFINE POPUP para criar os menus sob cada título de menu. Use ACTIVATE MENU para ativar todo o sistema de menu.

Se você usar o Menu and Shortcut Designers para criar seu menu, talvez não precise usar esses comandos. O Menu Designer cria automaticamente os comandos para seu menu. O Menu Designer usa o menu do sistema do Visual FoxPro, que você pode então modificar adicionando seus próprios itens de menu.

Para obter mais informações sobre como criar menus, consulte Criação de sistema de menu.

# Exemplo

O exemplo a seguir usa DEFINE MENU para criar um sistema de menu definido pelo usuário. A barra de menu do sistema atual é primeiro salva na memória com SET SYSMENU SAVE e depois os títulos de menu do sistema são limpos com SET SYSMENU TO.

DEFINE MENU cria a barra de menu, e dois títulos de menu são criados com DEFINE PAD. DEFINE POPUP cria um menu para cada título de menu. DEFINE BAR cria itens em cada um dos menus. Quando um título de menu é escolhido, ON PAD usa ACTIVATE POPUP para ativar o menu correspondente. ACTIVATE MENU exibe e ativa a barra de menu.

Quando um item é escolhido de um menu, o procedimento CHOICE é executado. CHOICE exibe o nome do item escolhido e o nome do menu que contém o item.

```foxpro
*** Name this program DEFIMENU.PRG ***
CLEAR
SET SYSMENU SAVE
SET SYSMENU TO
ON KEY LABEL ESC KEYBOARD CHR(13)
DEFINE MENU example BAR AT LINE 1
DEFINE PAD convpad OF example PROMPT '\<Conversions' COLOR SCHEME 3 ;
   KEY ALT+C, ''
DEFINE PAD cardpad OF example PROMPT 'Card \<Info' COLOR SCHEME 3 ;
   KEY ALT+I, ''
ON PAD convpad OF example ACTIVATE POPUP conversion
ON PAD cardpad OF example ACTIVATE POPUP cardinfo
DEFINE POPUP conversion MARGIN RELATIVE COLOR SCHEME 4
DEFINE BAR 1 OF conversion PROMPT 'Ar\<ea' ;
   KEY CTRL+E, '^E'
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
ON SELECTION POPUP conversion DO choice IN defimenu WITH PROMPT(), POPUP()
DEFINE POPUP cardinfo MARGIN RELATIVE COLOR SCHEME 4
DEFINE BAR 1 OF cardinfo PROMPT '\<View Charges' ;
   KEY ALT+V, ''
DEFINE BAR 2 OF cardinfo PROMPT 'View \<Payments' ;
   KEY ALT+P, ''
DEFINE BAR 3 OF cardinfo PROMPT 'Vie\<w Users' ;
   KEY ALT+W, ''
DEFINE BAR 4 OF cardinfo PROMPT '\-'
DEFINE BAR 5 OF cardinfo PROMPT '\<Charges '
ON SELECTION POPUP cardinfo;
   DO choice IN defimenu WITH PROMPT(), POPUP()
ACTIVATE MENU example
DEACTIVATE MENU example
RELEASE MENU example EXTENDED
SET SYSMENU TO DEFAULT
ON KEY LABEL ESC
PROCEDURE choice
PARAMETERS mprompt, mpopup
WAIT WINDOW 'You chose ' + mprompt + ;
    ' from popup ' + mpopup NOWAIT
```
