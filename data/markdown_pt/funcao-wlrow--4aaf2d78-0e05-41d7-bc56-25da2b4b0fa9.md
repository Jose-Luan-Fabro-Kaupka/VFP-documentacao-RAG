# Função WLROW( )

Retorna a coordenada de linha do canto superior esquerdo da janela ativa ou especificada.

```foxpro
WLROW([WindowName])
```

#### Parâmetros
 **WindowName**
Especifica a janela para a qual WLROW( ) retorna a coordenada de linha. No Visual FoxPro, você também pode especificar o nome de uma barra de ferramentas. Se você omitir WindowName , WLROW( ) retorna a coordenada de linha da janela de saída ativa. Você também pode usar a cadeia de caracteres vazia para WindowName para especificar a janela principal do Visual FoxPro. No Visual FoxPro, se nenhuma janela estiver ativa, WLROW( ) retorna a coordenada de linha da janela principal do Visual FoxPro em relação à área de trabalho do Windows. Se uma janela do sistema (a janela Command, a janela Data Session, uma janela Browse, e assim por diante) foi aberta e está visível ou oculta (seu nome aparece no menu Window), você pode incluir seu nome em WLROW( ). Se você especificar o nome de uma janela do sistema que está fechada, o Visual FoxPro gera uma mensagem de erro. A janela Debug é uma exceção. Depois que a janela Debug foi aberta, seu nome pode ser incluído em WLROW( ) se estiver visível, oculta ou fechada.

# Valor de retorno

Numérico

# Observações

O valor retornado por WLROW( ) depende do modo de exibição de vídeo atual, e a coordenada de linha é relativa à janela principal do Visual FoxPro. O modo de exibição pode ser alterado com SET DISPLAY.

As janelas podem ser posicionadas fora da janela principal do Visual FoxPro. Se o topo da janela estiver acima da janela principal do Visual FoxPro, WLROW( ) retorna um valor negativo. Se o topo da janela estiver abaixo da parte inferior da janela principal do Visual FoxPro, WLROW( ) retorna um valor positivo maior que a altura da janela principal do Visual FoxPro.
