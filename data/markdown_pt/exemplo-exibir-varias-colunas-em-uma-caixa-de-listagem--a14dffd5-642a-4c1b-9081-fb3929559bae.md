# Exemplo Exibir várias colunas em uma caixa de listagem

Arquivo: ...\Samples\Solution\Controls\Lists\Lmulcol.scx

Este exemplo demonstra a exibição de várias colunas em uma caixa de listagem. O formulário exibido contém uma caixa de listagem e um spinner. O número de colunas na caixa de listagem é definido pela propriedade Value do spinner: 1, 2, 3 ou 4.

Para definir a largura das colunas em uma caixa de listagem de várias colunas, use a propriedade ColumnWidths. Por exemplo, se houver 3 colunas na caixa de listagem, o comando a seguir definirá as larguras das colunas como 10, 15 e 20, respectivamente:

```foxpro
Form.List.ColumnWidths = "10, 15, 20"
```

Para definir os campos a serem exibidos nas colunas, defina a propriedade RowSource. Por exemplo, o comando a seguir define as fontes de três colunas em uma caixa de listagem de 3 colunas para os campos contact, city e country da tabela customer:

```foxpro
Form.List.RowSource = "contact,city,country"
```

A propriedade ColumnLines determina se linhas são exibidas entre as colunas na lista.
