# Propriedade SplitBar

Especifica se a split bar é exibida em um controle Grid. Disponível em tempo de design; somente leitura em tempo de execução.

```foxpro
Grid.SplitBar[ = lExpr]
```

# Valor de retorno
 **lExpr**
Um dos seguintes: lExpr Description True (.T.) (Padrão) A split bar é exibida em um controle Grid, permitindo dividir o Grid em dois painéis separados. Para sincronizar as duas metades do grid, adicione "This.Refresh" ao evento AfterRowColChange do Grid. False (.F.) A split bar não é exibida em um controle Grid, impedindo que você divida o Grid em painéis separados.

# Observações

Aplica-se a: Grid Control

Observe que a propriedade SplitBar tem precedência sobre a propriedade Partition.
