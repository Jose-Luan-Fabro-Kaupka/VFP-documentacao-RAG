# Como: exibir registros filhos em uma lista

Você pode exibir registros de uma relação um-para-muitos em uma lista, de modo que ela mostre os registros filhos enquanto o ponteiro percorre a tabela pai.

### Para exibir registros filhos em uma lista
- Adicione uma lista ao formulário.
- Defina a propriedade ColumnCount da lista como o número de colunas a exibir. Por exemplo, para mostrar os campos Order_id, Order_net e Shipped_on, defina ColumnCount como 3.
- Defina ColumnWidths com as larguras apropriadas para os campos selecionados.
- Defina a propriedade RowSourceType da lista como 3 SQL Statement.
- Defina a propriedade RowSource como a instrução SELECT. Por exemplo, a instrução a seguir seleciona três campos da tabela orders para o registro atual da tabela customer: SELECT order_id, order_net, shipped_on from orders ; WHERE order.cust_id = customer.cust_id ; INTO CURSOR temp
- No evento Init do formulário e no código que move o ponteiro pela tabela, consulte novamente a lista: THISFORM.lstChild.Requery
