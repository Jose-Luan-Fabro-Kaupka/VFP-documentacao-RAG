# Função WLCOL( )

Retorna a coordenada de coluna do canto superior esquerdo da janela ativa ou especificada.

```foxpro
WLCOL([WindowName])
```

#### Parâmetros
 **WindowName**
Especifica a janela para a qual WLCOL( ) retorna a coordenada de coluna. No Visual FoxPro, você também pode especificar o nome de uma barra de ferramentas. Se você omitir WindowName , WLCOLS( ) retorna a coordenada de coluna da janela de saída ativa. Você também pode usar a cadeia de caracteres vazia para WindowName para especificar a janela principal do Visual FoxPro. No Visual FoxPro, se nenhuma janela estiver ativa, WLCOLS( ) retorna a coordenada de coluna da janela principal do Visual FoxPro em relação à área de trabalho do Windows. Se uma janela do sistema (a janela Command, a janela Data Session, uma janela Browse e assim por diante) foi aberta e está visível ou oculta (seu nome aparece no menu Window), você pode incluir seu nome em WLCOL( ). Se você especificar o nome de uma janela do sistema que está fechada, o Visual FoxPro gera uma mensagem de erro. A janela Debug é uma exceção. Depois que a janela Debug foi aberta, seu nome pode ser incluído em WLCOL( ) se estiver visível, oculta ou fechada.

# Valor de retorno

Numérico

# Observações

O valor retornado por WLCOL( ) depende do modo de exibição de vídeo atual e é relativo à janela principal do Visual FoxPro. O modo de exibição pode ser alterado com SET DISPLAY.

As janelas podem ser posicionadas fora da janela principal do Visual FoxPro. Se a janela especificada estiver à esquerda da janela principal do Visual FoxPro, WCOL( ) retorna um valor negativo. Se a borda esquerda da janela estiver à direita da janela principal do Visual FoxPro, WCOL( ) retorna um valor positivo maior que a largura da janela principal do Visual FoxPro.
