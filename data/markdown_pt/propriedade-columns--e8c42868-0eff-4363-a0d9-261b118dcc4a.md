# Propriedade Columns

Uma matriz para acessar objetos Column individuais no controle Grid por número de coluna. Disponível em tempo de design e somente leitura em tempo de execução.

```foxpro
Grid.Columns(nCol).Property [ = Setting]
```

# Valor de retorno
 **nCol**
Especifica a coluna em agGrid cuja propriedade é referenciada. A Column mais à esquerda é o número 1.
**Property**
Especifica a propriedade da coluna a ser acessada.
**Setting**
Especifica a nova configuração de propriedade para todas as células especificadas com nCol.

# Observações

Aplica-se a: Grid Control

Use a propriedade Columns para acessar as propriedades de uma Column específica em um Grid. Por exemplo, SpecialGrid.Columns(1).BackColor = RGB(255,0,0) altera a propriedade BackColor de todas as células na Column 1 para vermelho brilhante.
