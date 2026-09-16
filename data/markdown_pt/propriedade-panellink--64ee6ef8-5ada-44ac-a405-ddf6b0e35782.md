# Propriedade PanelLink

Especifica se os painéis esquerdo e direito de um controle Grid estão vinculados quando a grade é dividida. Disponível em tempo de design; leitura/gravação em tempo de execução. Disponível somente se a propriedade Partition estiver definida com um valor maior que 0.

```foxpro
Grid.PanelLink[ = lExpr]
```

# Valor de retorno
 **lExpr**
As configurações da propriedade PanelLink são: Configuração Descrição True (.T.) (Padrão) Os painéis esquerdo e direito da grade estão vinculados quando a grade é dividida. False (.F.) Os painéis esquerdo e direito da grade não estão vinculados quando a grade é dividida.

Se PanelLink estiver definida como true (.T.), ambos os painéis da grade são afetados quando as seguintes propriedades são definidas: HeaderHeight, DeleteMark, GridLineColor, GridLines, GridLineWidth, Highlight, RecordMark, RowHeight e ScrollBars.

Se PanelLink estiver definida como false (.F.), a configuração da propriedade Panel determina em qual painel as seguintes propriedades são definidas: HeaderHeight, DeleteMark, GridLineColor, GridLines, GridLineWidth, HighLight, RecordMark, RowHeight e ScrollBars.

# Observações

Aplica-se a: Grid Control
