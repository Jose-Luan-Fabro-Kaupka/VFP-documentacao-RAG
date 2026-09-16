# Propriedades ItemBackColor, ItemForeColor

Especificam a cor de plano de fundo ou de primeiro plano usada para exibir o texto dos itens em um controle ComboBox ou ListBox. Disponíveis em tempo de design e em tempo de execução.

```foxpro
Control.ItemBackColor [= nColor ]
-or-
Control.ItemBackColor = RGB( nRedValue, nGreenValue, nBlueValue )
```

```foxpro
Control.ItemForeColor [ = nColor ]
-or-
Control.ItemForColor = RGB( nRedValue, nGreenValue, nBlueValue )
```

# Valor de retorno
 **nColor**
Especifica um inteiro que representa a cor do texto. Para obter mais informações, consulte a tabela de cores no tópico Propriedades BackColor, ForeColor.

# Observações

Aplica-se a: Controle ComboBox | Controle ListBox

Para escolher ou definir cores, clique duas vezes em qualquer uma das propriedades de cor na janela Properties para exibir a caixa de diálogo Color. Os valores de cor vermelho, verde e azul correspondentes à cor escolhida tornam-se as configurações dessas propriedades depois que você fecha a caixa de diálogo Color.
