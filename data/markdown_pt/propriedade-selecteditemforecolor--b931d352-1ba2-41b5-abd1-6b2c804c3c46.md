# Propriedade SelectedItemForeColor

Especifica a cor de primeiro plano do texto de um item selecionado em um ComboBox ou ListBox ou célula (somente TextBox) em um controle Grid. SelectedItemForeColor está relacionada às propriedades HighlightForeColor e HighlightBackColor porque você precisa controlar a cor da célula selecionada em uma linha de grade. Leitura/gravação em tempo de design e em tempo de execução. Há duas versões da sintaxe.

```foxpro
Control.SelectedItemForeColor [= nColor ]
```

```foxpro
Control.SelectedItemForeColor = RGB( nRedValue, nGreenValue, nBlueValue )
```

#### Parâmetros
 **nColor**
Tipo de dados numérico. SelectedItemForeColor especifica um inteiro representando um valor de cor. O Visual FoxPro deriva a configuração de cor padrão da configuração de cor de fonte do sistema operacional Windows para Selected Items. Para obter informações sobre valores de cor válidos, consulte BackColor, ForeColor Properties .

# Observações

Aplica-se a: ComboBox Control | ListBox Control | Grid Control

Para obter mais informações sobre as propriedades Grid SelectedItemForeColor e GridSelectedItemBackColor, consulte SelectedItemBackColor Property.
