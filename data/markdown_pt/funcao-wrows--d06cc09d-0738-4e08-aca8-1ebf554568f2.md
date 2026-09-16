# Função WROWS( )

Retorna o número de linhas dentro da janela ativa ou especificada.

```foxpro
WROWS([WindowName])
```

#### Parâmetros
 **WindowName**
Especifica a janela para a qual WROWS( ) retorna o número de linhas. No Visual FoxPro, você também pode especificar o nome de uma barra de ferramentas. No Visual FoxPro, o valor retornado por WROWS( ) depende da fonte especificada para a janela. A maioria das fontes pode ser exibida em uma grande variedade de tamanhos, e algumas são proporcionais. Uma linha corresponde à altura da fonte atual. Para obter mais informações, consulte o tópico Fonts Overview. Você pode especificar o nome de uma janela do sistema (a janela Command, a janela Data Session, uma janela Browse, e assim por diante) em WROWS( ) se a janela do sistema tiver sido aberta e estiver visível ou oculta. Se você especificar o nome de uma janela do sistema que está fechada, o FoxPro gera uma mensagem de erro. A janela Debug é uma exceção. Depois que a janela Debug foi aberta, seu nome pode ser incluído em WROWS( ) se estiver visível, oculta ou fechada. Você também pode incluir a cadeia de caracteres vazia em WindowName para retornar o número de linhas na janela principal do Visual FoxPro. A cadeia de caracteres vazia pode ser usada para especificar a janela principal do Visual FoxPro em funções como WLCOL( ), WLROW( ) e WCOLS( ), que retornam localizações ou tamanhos de janela.

# Valor de retorno

Numeric

# Observações

Se você não especificar um nome de janela, o número de linhas na janela de saída ativa é retornado. Se nenhuma janela estiver ativa, o número de linhas na janela principal do Visual FoxPro é retornado.
