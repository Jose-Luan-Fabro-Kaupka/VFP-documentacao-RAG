# Como: definir a origem dos dados exibidos no Grid

Você pode definir a origem de dados do grid e de cada coluna individualmente.

### Para definir a origem de dados de um grid
- Selecione o grid e clique na propriedade RecordSourceType na Properties Window (Visual FoxPro).
- Defina a propriedade RecordSourceType como 0 - Table, se desejar que o Visual FoxPro abra a tabela para você, ou 1 - Alias se desejar que o grid seja preenchido com os campos de uma tabela que já está aberta.
- Clique na propriedade RecordSource na janela Properties.
- Digite o nome do alias ou da tabela que servirá como origem de dados do grid.

Se desejar especificar campos particulares para serem exibidos em colunas particulares, também pode definir a origem de dados de uma coluna.

### Para definir a origem de dados de uma coluna
- Selecione a coluna e clique na propriedade ControlSource na Properties Window (Visual FoxPro).
- Digite o nome do alias ou da tabela e o campo que servirão como origem dos valores exibidos na coluna. Por exemplo, você pode digitar: Orders.order_id
