# Formatação de grades

Você pode personalizar a formatação de grades de várias maneiras.

# Uso de formatação condicional em grades

Uma formatação especial em uma grade pode facilitar a localização de determinadas informações nos registros. Para fornecer formatação condicional, use as propriedades dinâmicas de fonte e cor de uma coluna.

Por exemplo, adicione uma grade a um formulário e defina a propriedade ColumnCount como 2. Defina ControlSource da primeira coluna como `orders.to_name` e ControlSource da segunda como `orders.order_net`. Para exibir totais de pedidos inferiores a 500,00 em preto e totais maiores ou iguais a 500,00 em vermelho, inclua a linha a seguir no código do evento Init da grade:

```foxpro
THIS.Column2.DynamicForeColor = ;
   "IIF(orders.order_net >= 500, RGB(255,0,0), RGB(0,0,0))"
```

# Propriedades comuns de grades

As propriedades de grade a seguir são normalmente definidas em tempo de design.

| Propriedade | Descrição |
| --- | --- |
| ChildOrder | A chave estrangeira da tabela filha associada à chave primária da tabela pai. |
| ColumnCount | Número de colunas. Se ColumnCount for -1, a grade terá tantas colunas quantos forem os campos de RecordSource. |
| LinkMaster | A tabela pai dos registros filhos exibidos na grade. |
| RecordSource | Os dados a exibir na grade. |
| RecordSourceType | A origem dos dados exibidos: uma tabela, um alias, uma consulta ou uma tabela selecionada pelo usuário em resposta a uma solicitação. |

# Propriedades comuns de colunas

As propriedades de coluna a seguir são normalmente definidas em tempo de design.

| Propriedade | Descrição |
| --- | --- |
| ControlSource | Os dados a exibir na coluna, geralmente um campo de uma tabela. |
| Sparse | Se Sparse for true (.T.), os controles de uma grade serão exibidos como controles somente quando a célula da coluna estiver selecionada. As demais células exibem o valor subjacente em uma caixa de texto. Definir Sparse como true (.T.) permite redesenho mais rápido ao percorrer uma grade com muitas linhas. |
| CurrentControl | O controle ativo na grade. O padrão é Text1, mas, se você adicionar um controle à coluna, poderá especificá-lo como CurrentControl. |

> **Observação:** A propriedade ReadOnly de um controle dentro da coluna é substituída pela propriedade ReadOnly de Column. Se você definir ReadOnly do controle no código associado ao evento AfterRowColChange, a nova configuração será válida enquanto estiver nessa célula.
