# Função WTITLE( )

Retorna o título atribuído à janela ativa ou especificada.

```foxpro
WTITLE([WindowName])
```

#### Parâmetros
 **WindowName**
Especifica uma janela cujo título WTITLE( ) retorna. O título atribuído à janela com a cláusula TITLE é retornado se você incluir o nome de uma janela definida pelo usuário criada com DEFINE WINDOW. Quando você emite BROWSE WINDOW para abrir uma janela Browse em uma janela definida pelo usuário, WTITLE( ) retorna o título da janela definida pelo usuário se a janela Browse não tiver título. WTITLE( ) retorna o título da janela Browse se a janela Browse tiver título. Você também pode usar a cadeia de caracteres vazia para WindowName para especificar a janela principal do Visual FoxPro.

# Valor de retorno

Caractere

# Observações

WTITLE( ) pode ser usado para retornar o título de uma janela, que aparece na borda superior da janela. O título é retornado para a janela ativa se você omitir WindowName. WTITLE( ) retorna a cadeia de caracteres vazia se a janela Debug, Trace ou Command estiver ativa ou se a saída estiver sendo direcionada para a janela principal do Visual FoxPro.

Nomes e títulos de janelas Nomes são atribuídos a janelas definidas pelo usuário, janelas do sistema, barras de ferramentas (no Visual FoxPro) e janelas Browse da seguinte maneira:

Janelas definidas pelo usuário recebem nomes quando são criadas com DEFINE WINDOW. Há uma distinção entre nomes de janelas definidas pelo usuário e títulos. Por padrão, janelas definidas pelo usuário não têm títulos. Se a cláusula TITLE for incluída quando a janela é criada, o título especificado aparece na borda superior da janela, mas não é o nome da janela.

Por padrão, cada janela do sistema, que faz parte da interface do Visual FoxPro, deriva seu nome do título da janela. Exemplos de janelas do sistema incluem a janela Command, a janela Data Session e a janela Trace. No Visual FoxPro, cada barra de ferramentas deriva seu nome do título da barra de ferramentas.

Janelas de programa e edição e as janelas Label e Report Designer derivam seus nomes do nome do arquivo sendo criado ou modificado.

Uma janela Browse deriva seu nome do título da janela. O nome e o título da janela Browse são atribuídos de uma de três maneiras: pela atribuição de título padrão do alias da tabela, pelo título da janela (se existir) ou pelo título do Browse (se existir).

Por padrão, o nome da janela Browse é o alias da tabela.

Para especificar nomes de janelas do sistema e barras de ferramentas em comandos e funções, coloque o nome completo da janela do sistema ou barra de ferramentas entre aspas. Por exemplo, para ocultar a barra de ferramentas Report Controls no Visual FoxPro, emita o seguinte comando:

```foxpro
HIDE WINDOW "Report Controls"
```

Observações adicionais sobre nomes de janelas Se você não tem certeza do nome atribuído a uma janela, verifique o menu Window. Todos os nomes de janelas são listados na parte inferior do menu Window.

Duas janelas existem se você emitir BROWSE WINDOW WindowName. A janela Browse é uma janela separada e assume os atributos da janela definida pelo usuário especificada. Se uma janela estiver ativa quando você emitir BROWSE e você não incluir a cláusula WINDOW, a janela Browse assume os atributos da janela ativa. Você pode substituir esse comportamento incluindo NORMAL em BROWSE.

Você pode incluir nomes de janelas que contêm espaços em comandos e funções que aceitam nomes de janelas, como MOVE WINDOW, DEACTIVATE WINDOW e WONTOP( ), especificando a parte do nome da janela que começa com o primeiro caractere que não é espaço e continuando até que o último caractere que não é espaço seja encontrado.

Por exemplo, uma janela Browse com o nome Invoice Entry pode ser movida com este comando:

```foxpro
MOVE WINDOW invoice BY 1,1
```

Os nomes de janelas definidas pelo usuário não podem conter espaços, mas os nomes de janelas Browse e do sistema podem.
