# Propriedades DisabledItemBackColor e DisabledItemForeColor

Especificam a cor de fundo ou de primeiro plano dos itens desativados em um controle ComboBox ou ListBox. Disponíveis em tempo de design e de execução. Há duas versões da sintaxe para cada propriedade.

```foxpro
Control.DisabledItemBackColor[ = nColor]
```

```foxpro
Control.DisabledItemBackColor RGB(nRedValue, nGreenValue,  nBlueValue)
```

```foxpro
Control.DisabledItemForeColor[ = nColor]
```

```foxpro
Control.DisabledItemForeColor RGB(nRedValue, nGreenValue, nBlueValue)
```

# Valor de retorno
**nColor**
Especifica um único número para representar a cor. Observação: na janela Properties, você pode clicar duas vezes em qualquer propriedade de cor para exibir a caixa de diálogo Color. Nessa caixa, é possível escolher ou definir cores. As intensidades de vermelho, verde e azul correspondentes à cor escolhida tornam-se as configurações dessas propriedades depois que a caixa de diálogo Color é fechada. Para obter mais informações, consulte a tabela de cores no tópico Propriedades BackColor e ForeColor.

# Observações

Aplica-se a: controle ComboBox | controle ListBox
