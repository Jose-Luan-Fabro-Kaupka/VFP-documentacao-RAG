# Como: controlar a seleção de registros com joins

Quando você tem múltiplas tabelas em uma query ou view, pode controlar quais registros a query ou view recupera adicionando ou alterando condições de join entre as tabelas. Trabalhar com joins é semelhante para queries e views; portanto, os procedimentos usam queries como exemplos. Embora você possa executar uma query ou view sem joins, os resultados geralmente têm pouco valor prático e podem exigir grandes quantidades de tempo para processar.

Para obter mais informações sobre condições de join, consulte Join Conditions for Tables, Queries, and Views.

# Adicionando condições de join

Joins geralmente aparecem automaticamente quando você adiciona tabelas à query ou view. No entanto, se os nomes dos campos dos campos relacionados não coincidirem, pode ser necessário especificar o join desejado para a tabela que você adiciona usando a caixa de diálogo Join Condition nos designers Query e View.

O processo para adicionar um join é semelhante entre os designers Query e View. O procedimento a seguir descreve a adição de um join no Query Designer.

### Para criar um join entre tabelas usando o Query Designer
- Crie ou abra uma query.
- Adicione uma tabela à query para ter duas ou mais tabelas.
- Na barra de ferramentas do Query Designer, clique em Add Join .
- Na caixa de diálogo Join Condition, selecione os nomes dos campos relacionados nas duas tabelas. Observação Defina joins para colunas somente se elas tiverem o mesmo tamanho e tipo de dados.
- Selecione um tipo de join e clique em OK .

Você também pode adicionar joins para tabelas que já aparecem na superfície do designer Query ou View clicando e arrastando o mouse entre os campos nas tabelas ou escolhendo o botão Add Join na barra de ferramentas do designer Query ou View para exibir a caixa de diálogo Join Condition. Você também pode criar um tipo de join usando a cláusula FROM na instrução SQL SELECT.

Para obter mais informações sobre a caixa de diálogo Join Condition, consulte Join Condition Dialog Box. Para obter mais informações sobre instruções SQL SELECT geradas pelos designers Query e View, consulte How to: Create Queries (Visual FoxPro), How to: View and Edit SQL Statements for Views e SELECT - SQL Command.

Por exemplo, suponha que você deseja recuperar informações de pedidos, incluindo informações sobre o cliente que fez o pedido. O exemplo a seguir cria uma view usando duas tabelas, `Customers` e `Orders`. As tabelas `Customer` e `Orders` têm um campo de ID de cliente. As tabelas são relacionadas com base em um inner join, que especifica que os resultados incluem somente as linhas da tabela `Customer` que correspondem a um ou mais registros da tabela `Orders`.

O código a seguir abre o banco de dados de exemplo chamado TestData.dbc, cria uma view usando o comando CREATE SQL VIEW conforme descrito no exemplo e usa a cláusula FROM para especificar a condição de join conforme descrito:

```foxpro
OPEN DATABASE testdata
CREATE SQL VIEW cust_orders_view AS ;
   SELECT * FROM testdata!customer ;
      INNER JOIN testdata!orders ;
      ON customer.cust_id = orders.cust_id
```

# Modificando condições de join

Você pode modificar joins existentes das seguintes maneiras:
 - Escolha um tipo de join diferente para modificar o escopo dos registros retornados.
- Selecione campos diferentes na tabela para o join.
- Altere o operador de comparação.
- Altere a ordem dos joins

O processo para modificar um join é semelhante para os designers Query e View. O procedimento a seguir descreve a modificação de um join no Query Designer.

### Para modificar um join
- Abra uma query contendo as tabelas com joins que deseja modificar.
- Na guia Join do Query Designer, selecione o join e altere as condições de join conforme necessário.

Você também pode modificar tipos de join usando a cláusula FROM no comando SQL SELECT. Para obter mais informações sobre instruções SQL SELECT geradas pelos designers Query e View, consulte How to: Create Queries (Visual FoxPro), How to: View and Edit SQL Statements for Views e SELECT - SQL Command.

# Removendo condições de join

Você pode remover joins entre tabelas. O processo para remover um join é semelhante para os designers Query e View. O procedimento a seguir descreve a remoção de um join no Query Designer.

### Para excluir um join
- Abra a query que contém as tabelas com o join que deseja remover.
- Na guia Join do Query Designer, selecione a condição de join e clique em Remove .

Você também pode selecionar a linha de join que deseja remover entre duas tabelas na superfície do designer Query ou View. No menu Query, clique em Remove Join Condition.
