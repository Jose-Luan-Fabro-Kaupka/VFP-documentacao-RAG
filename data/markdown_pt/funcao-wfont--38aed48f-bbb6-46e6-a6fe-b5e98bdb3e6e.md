# Função WFONT( )

Retorna o nome, o tamanho ou o estilo da fonte atual de uma janela no Visual FoxPro para Windows.

```foxpro
WFONT(nFontAttribute [, WindowName])
```

#### Parâmetros
 **nFontAttribute**
Especifica o atributo de fonte que você deseja retornar. Se nFontAttribute for 1, WFONT( ) retorna o nome da fonte atual da janela ativa ou especificada. Se nFontAttribute for 2, WFONT( ) retorna o tamanho da fonte. Se nFontAttribute for 3, WFONT( ) retorna um código que identifica o estilo da fonte. O código de estilo da fonte é um caractere ou conjunto de caracteres que correspondem ao estilo da fonte atual. Por exemplo, o estilo da fonte atual é Bold Italic se WFONT(3) retornar BI. A tabela a seguir lista os códigos de cada estilo de fonte: Character Font Style B Bold I Italic N Normal O Outline Q Opaque S Shadow – StrikeThru T Transparent U Underline
**WindowName**
Especifica o nome da janela para a qual você deseja determinar a fonte, o tamanho da fonte ou o estilo da fonte atual. No Visual FoxPro, você também pode incluir o nome de uma barra de ferramentas. Inclua a cadeia de caracteres vazia para retornar a fonte, o tamanho da fonte ou o estilo da fonte atual da janela principal do Visual FoxPro. WindowName pode ser o nome de uma janela definida pelo usuário criada com DEFINE WINDOW ou uma janela de edição de texto ou memo. Você também pode incluir o nome de uma janela do sistema (View, Trace, Debug e assim por diante). WFONT( ) pode retornar atributos de fonte apenas para uma janela do sistema que foi aberta e está visível ou oculta no momento. Se a janela do sistema especificada estiver fechada, o Visual FoxPro gera uma mensagem de erro. WFONT( ) retorna a fonte, o tamanho da fonte ou o estilo da fonte atual da janela de saída ativa se você omitir WindowName.

# Valor de retorno

Character e Numeric

# Exemplo

O exemplo a seguir cria uma janela definida pelo usuário chamada `wFontChar`. A janela é ativada e suas características de fonte são exibidas na janela. As características de fonte são então exibidas para a janela principal do Visual FoxPro.

```foxpro
CLEAR
DEFINE WINDOW wFontChar ;
   FROM 1,1 TO 3,35 ;
   FONT 'MS SANS SERIF',8 ;
   STYLE 'BI'  && Define window with font and style
ACTIVATE WINDOW wFontChar
? WFONT(1), WFONT(2), WFONT(3)  && wFontChar window
ACTIVATE SCREEN
?
?
?
? 'Font characteristics for the window wFontChar'
?
?
? WFONT(1,''), WFONT(2,''), WFONT(3,'')  && Main Visual FoxPro window
?
? 'Font characteristics for the main Visual FoxPro window'
WAIT WINDOW
RELEASE WINDOW wFontChar
CLEAR
```
