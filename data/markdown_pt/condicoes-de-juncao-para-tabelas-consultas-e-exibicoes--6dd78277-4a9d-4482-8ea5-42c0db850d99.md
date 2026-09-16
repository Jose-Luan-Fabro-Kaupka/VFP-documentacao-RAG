# Condições de junção para tabelas, consultas e exibições

O Visual FoxPro suporta sintaxe de junção SQL-92, permitindo criar consultas que vinculam linhas em duas ou mais tabelas comparando os valores em campos especificados. Ao recuperar dados de tabelas para criar consultas e exibições, você pode usar operações de junção e condições de junção para controlar como os registros são comparados e quais são retornados e especificar relacionamentos entre tabelas, geralmente baseados em chaves primárias e estrangeiras. Especificar junções em campos diferentes das chaves primárias e estrangeiras pode ser útil em casos específicos; no entanto, a maioria das consultas não usa junções em campos que não são chaves.

Este tópico contém as seguintes seções:
 - Partes das operações de junção
- Tipos de junção
- Sequência de junção
- Condições de junção
- Considerações sobre junções

Você pode especificar operações de junção e condições de junção para consultas e exibições nos designers Query and View e usando a linguagem Visual FoxPro. Para obter mais informações, consulte Join Tab, Query and View Designers e SELECT - SQL Command.

# Partes das operações de junção

A lista a seguir contém partes das operações de junção que você pode definir entre tabelas em consultas e exibições:
 - Campos de tabela na junção.
- Tipo de junção entre tabelas ou entre campos de tabela em uma consulta ou exibição.
- Sequência de junção.
- Condições de junção entre campos usando operadores como Between, Equal (=), Greater Than (>) e Less Than (<).

# Tipos de junção

Como o SQL é baseado na teoria dos conjuntos matemáticos, cada tabela pode ser representada como um círculo em um diagrama de Venn. A cláusula ON na instrução SQL SELECT que especifica condições de junção determina o ponto de sobreposição desses círculos e representa o conjunto de linhas que correspondem. Por exemplo, em uma junção interna, a sobreposição ocorre dentro da porção interior ou "interna" dos dois círculos. Uma junção externa inclui não apenas as linhas correspondentes encontradas na seção cruzada interna das tabelas, mas também as linhas na parte externa do círculo à esquerda ou à direita da interseção.

Você pode expandir ou restringir os resultados de sua pesquisa especificando o tipo de junção desejado entre tabelas. A tabela a seguir descreve os tipos de junção que você pode especificar.

| Tipo de junção | Descrição |
| --- | --- |
| Inner | Recupera apenas os registros das tabelas em ambos os lados da junção que correspondem à condição de junção entre os campos envolvidos na junção. Junções internas são o tipo de junção mais comum. |
| Left (outer) | Recupera todos os registros da tabela no lado esquerdo da junção e apenas os registros que correspondem à condição de junção da tabela no lado direito da junção. |
| Right (outer) | Recupera apenas os registros da tabela no lado esquerdo da condição de junção que correspondem à condição de junção, mas todos os registros do lado direito da condição de junção. |
| Full | Recupera todos os registros das tabelas em ambos os lados da condição de junção, independentemente de os registros corresponderem à condição de junção. |

### Registros correspondentes exatamente nos resultados

Se você deseja recuperar apenas os registros que correspondem à condição de junção das tabelas em ambos os lados da operação, use uma junção interna.

Por exemplo, suponha que você deseje criar uma consulta contendo apenas as empresas que possuem pedidos e exibir apenas os números de pedido dessas empresas. O exemplo de código a seguir cria uma consulta que recupera apenas os nomes de empresas da tabela Customer que possuem pedidos na tabela Orders e os números de pedido apenas dessas empresas. O exemplo usa uma junção interna para exibir apenas os registros de ambas as tabelas que correspondem à condição de junção baseada no campo Cust_ID.

> **Observação:** A instrução SELECT usa aliases locais de tabela para distinguir o mesmo nome de campo, Cust_ID, em ambas as tabelas e uma cláusula ORDER BY para organizar os resultados por nome da empresa em ordem ascendente.

```foxpro
CLOSE ALL
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\TestData')
SELECT TAlias1.company, TAlias2.order_ID ;
   FROM customer AS TAlias1 ;
   INNER JOIN orders AS TAlias2 ;
      ON TAlias1.cust_id = TAlias2.cust_id ;
   ORDER BY TAlias1.company ASC
```

### Múltiplas operações de junção

Você pode especificar mais de uma operação de junção para incluir dados de outras tabelas.

Por exemplo, suponha que você deseje criar uma consulta contendo apenas as empresas que possuem pedidos, apenas os números de pedido dessas empresas e os funcionários que receberam os pedidos. O exemplo de código a seguir cria uma consulta que recupera apenas os nomes de empresas da tabela Customer que possuem pedidos na tabela Orders, os números de pedido apenas dessas empresas e os nomes dos funcionários que receberam esses pedidos. O exemplo usa duas cláusulas inner join para exibir apenas os registros das três tabelas que correspondem nos campos Cust_ID e Emp_ID.

> **Observação:** A instrução SELECT usa aliases locais de tabela para distinguir os nomes de campo comuns, Cust_ID e Emp_ID, nas tabelas.

```foxpro
CLOSE ALL
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\TestData')
SELECT TAlias1.company, TAlias2.order_ID, ;
   TAlias3.first_name, TAlias3.last_name ;
   FROM customer AS TAlias1 ;
   INNER JOIN orders AS TAlias2 ;
      ON TAlias1.cust_id = TAlias2.cust_id ;
   INNER JOIN employee AS TAlias3 ;
      ON TAlias2.emp_id = TAlias3.emp_id ;
   ORDER BY TAlias1.company ASC
```

### Registros não correspondentes nos resultados

Se você deseja incluir quaisquer linhas que não correspondam às condições de junção em seus resultados, pode usar uma junção externa esquerda, externa direita ou completa entre tabelas. Quando você usa uma junção externa, os campos vazios das linhas não correspondentes retornam valores nulos.

Por exemplo, suponha que você deseje criar uma consulta contendo uma lista de todos os clientes, independentemente de terem feito um pedido, e os números de pedido dos clientes que fizeram pedidos. O exemplo de código a seguir usa uma junção externa esquerda para exibir todos os registros de um campo em uma tabela e apenas os registros em outra tabela que correspondem à condição de junção.

> **Observação:** A sintaxe no exemplo usa uma cláusula LEFT JOIN porque a palavra-chave OUTER é opcional.

Este exemplo cria uma consulta contra o banco de dados de exemplo do Visual FoxPro, TestData.dbc, que recupera todos os nomes de empresas da tabela Customer e apenas os registros na tabela Orders que possuem números de ID de cliente que correspondem em ambas as tabelas. No entanto, nem todos os registros correspondentes possuem números de pedido para todas as empresas na tabela Customer.

> **Observação:** A instrução SELECT usa aliases locais de tabela para distinguir o mesmo nome de campo, Cust_ID, em ambas as tabelas.

```foxpro
CLOSE ALL
CLOSE DATABASES
```

`OPEN DATABASE (HOME(2) + 'Data\TestData')`

`SELECT TAlias1.company, TAlias2.order_id ;`

`FROM customer TAlias1 ;`

`LEFT JOIN orders TAlias2 ;`

`ON TAlias1.cust_id = TAlias2.cust_id`

Todos os nomes de empresas na consulta, exceto um, possuem números de pedido na coluna Order_ID da consulta. Wenna Wines contém um valor nulo na coluna Order_ID.

Para obter mais informações sobre os tipos de junção que você pode definir entre tabelas no Query Designer e View Designer, consulte Join Condition Dialog Box.

# Sequência de junção

Quando você precisa de dados de várias tabelas, os resultados desejados e o tipo de junção selecionado afetam a posição e a sequência de junção em que você coloca as tabelas em sua consulta. Você pode especificar a ordem em que as tabelas são unidas nos designers Query and View ou na cláusula JOIN da instrução SQL SELECT.

Por exemplo, suponha que você deseje todos os registros de um campo em uma tabela e apenas os registros em outra tabela que correspondam à condição de junção. Você poderia usar a operação LEFT JOIN e colocar a primeira tabela no lado esquerdo e a segunda tabela no lado direito da cláusula JOIN. No entanto, se você selecionasse uma operação RIGHT JOIN, precisaria inverter a ordem dessas duas tabelas para obter os mesmos resultados.

O exemplo de código a seguir cria uma consulta que exibe três conjuntos de resultados, mas todos recuperam todos os valores do campo na primeira tabela e apenas os valores do campo na segunda tabela que atendem à condição de junção. A condição de junção é especificada pela cláusula ON.

> **Observação:** A instrução SELECT usa aliases locais de tabela para distinguir o mesmo nome de campo, Cust_ID, em ambas as tabelas.

```foxpro
CLOSE ALL
CLOSE DATABASES
```

`OPEN DATABASE (HOME(2) + 'Data\TestData')`

Para a primeira instrução SQL SELECT, a consulta recupera todos os nomes do campo Company na tabela Customer e apenas os números de pedido do campo Order_ID na tabela Orders que correspondem no campo Cust_ID.

`SELECT TAlias1.company, TAlias2.order_id ;`

`FROM customer TAlias1 ;`

`LEFT JOIN orders TAlias2 ;`

`ON TAlias1.cust_id = TAlias2.cust_id`

Para a segunda instrução SQL SELECT, a operação LEFT JOIN é substituída por uma operação RIGHT JOIN, mas a sequência das tabelas não foi alterada. No entanto, o conjunto de resultados é diferente. A consulta recupera todos os números de pedido do campo Order_ID na tabela Orders para os registros que correspondem no campo Cust_ID em ambas as tabelas. Neste exemplo, nenhum número de pedido deve existir sem um registro de cliente correspondente, portanto nenhum valor nulo aparece na coluna Company. No entanto, apenas os nomes do campo Company na tabela Customer aparecem onde o campo Cust_ID na tabela Customer corresponde ao campo Cust_ID na tabela Orders.

`SELECT TAlias1.company, TAlias2.order_id ;`

`FROM customer TAlias1 ;`

`RIGHT JOIN orders TAlias2 ;`

`ON TAlias1.cust_id = TAlias2.cust_id`

Para a terceira instrução SQL SELECT, a operação RIGHT JOIN permanece, mas a sequência das tabelas é invertida. No entanto, os resultados são os mesmos da primeira instrução SQL SELECT.

`SELECT TAlias1.company, TAlias2.order_id ;`

`FROM orders TAlias2 ;`

`RIGHT JOIN customer TAlias1 ;`

`ON TAlias1.cust_id = TAlias2.cust_id`

Para obter mais informações, consulte Join Tab, Query and View Designers e SELECT - SQL Command.

# Condições de junção

Condições de junção especificam condições nas quais as tabelas em uma instrução SQL SELECT são unidas. Por exemplo, você pode usar condições de junção para comparar valores em duas tabelas que possuem campos comuns e retornar apenas os registros em que esses campos possuem os mesmos valores.

> **Observação:** Se você incluir mais de uma tabela em uma consulta, deve especificar uma condição de junção para cada tabela após a primeira.

Você pode personalizar a condição de junção para consultas e exibições usando operadores de comparação para controlar como os registros são comparados e quais são retornados, de forma semelhante ao uso de uma condição de filtro. No entanto, condições de junção comparam o valor do campo em uma tabela com o valor do campo em outra tabela, enquanto condições de filtro comparam um valor de campo com um valor de filtro. Para informações sobre condições de filtro, consulte Filter Conditions for Queries and Views.

Por exemplo, você pode usar o operador igual (=) ao consultar duas tabelas unidas em seus respectivos campos de ID de cliente, como Customer.cust_id = Orders.cust_id. Esta consulta recupera apenas os registros em que esses dois campos correspondem e atendem a qualquer outro filtro definido na consulta. Como outro exemplo, se você estiver usando um campo de data em uma junção, pode usar um operador de condição de comparação para incluir apenas registros antes ou depois de uma determinada data.

A tabela a seguir lista os operadores de comparação disponíveis para condições de junção.

| Operador | Descrição |
| --- | --- |
| = | Igual |
| == | Exatamente igual |
| LIKE | Operação SQL LIKE |
| <>, !=, # | Diferente |
| > | Maior que |
| >= | Maior ou igual a |
| < | Menor que |
| <= | Menor ou igual a |

Você pode especificar condições de junção com a cláusula ON ou a cláusula WHERE de uma instrução SQL SELECT, mas não ambas.

Por exemplo, suponha que você deseje todos os registros de um campo em uma tabela e apenas os valores de dois campos em outra tabela que atendam a uma condição de junção e uma condição de filtro. O exemplo de código a seguir usa a cláusula ON para especificar uma condição de junção, que inclui uma condição de filtro especificada pela cláusula AND.

Este exemplo cria uma consulta que recupera todos os nomes no campo Company da tabela Customer e apenas os registros que correspondem no campo Cust_ID na tabela Orders. No entanto, nem todos os registros correspondentes na tabela Orders contêm datas nos campos Order_Date e Shipped_On que passam nos critérios de filtro, com data de pedido anterior a 02/16/1994. Se uma empresa não possui datas de pedido que atendam à condição de filtro, as colunas Order_Date e Shipped_On mostram valores nulos.

> **Observação:** A instrução SELECT usa aliases locais de tabela para distinguir o mesmo nome de campo, Cust_ID, em ambas as tabelas.

```foxpro
CLOSE ALL
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\TestData')
SELECT TAlias1.company, TAlias2.order_date, TAlias2.shipped_on ;
   FROM customer TAlias1 ;
   LEFT JOIN orders TAlias2 ;
      ON TAlias1.cust_id = TAlias2.cust_id ;
         AND TAlias2.order_date < {^1994-02-16}
```

Para obter mais informações sobre as condições de junção que você pode definir para consultas e exibições, consulte SELECT - SQL Command e Join Tab, Query and View Designers.

### Condições de junção na cláusula WHERE

Ao escrever instruções SQL SELECT, você pode especificar condições de junção na cláusula WHERE junto com condições de filtro. Ao especificar filtros para consultas e exibições nos designers Query and View, a guia Filter insere uma cláusula WHERE na instrução SQL SELECT gerada para a consulta ou exibição. Você pode especificar uma condição de junção na guia Filter ou editar a cláusula WHERE na instrução SQL SELECT visualizando e editando na janela SQL. Para exibições remotas, uma condição de junção sempre aparece na cláusula WHERE.

Por exemplo, suponha que você deseje informações de pedidos de clientes, incluindo todas as informações sobre o cliente e o funcionário que recebeu o pedido. O exemplo de código a seguir usa a cláusula WHERE para especificar uma condição de junção correspondendo registros no campo Cust_ID nas tabelas Customer e Orders e, adicionalmente, uma condição de junção correspondendo o número do funcionário no campo Emp_ID para as tabelas Orders e Employee.

Este exemplo recupera apenas os registros de clientes na tabela Customer que correspondem a pedidos na tabela Orders com registros de funcionários na tabela Employee.

```foxpro
CLOSE ALL
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\TestData')
SELECT * FROM customer TAlias1, orders TAlias2, employee TAlias3 ;
   WHERE TAlias1.cust_id = TAlias2.cust_id ;
   AND TAlias2.emp_id = TAlias3.emp_id
```

Para obter mais informações sobre a cláusula WHERE, consulte Filter Tab, Query and View Designers e SELECT - SQL Command.

# Considerações sobre junções

Ao criar operações de junção, esteja ciente das seguintes considerações:
 - Se você incluir duas tabelas em uma consulta e não especificar uma condição de junção, cada registro na primeira tabela é unido a cada registro na segunda tabela, desde que as condições de filtro sejam atendidas. Tal consulta pode produzir resultados extensos.
- Use cautela ao usar funções como DELETED( ) , EOF( ) , FOUND( ) , RECCOUNT( ) e RECNO( ) , que suportam um alias ou área de trabalho opcional. Incluir um alias ou área de trabalho nessas funções pode produzir resultados inesperados. SQL SELECT não usa suas áreas de trabalho; executa o equivalente de USE ... AGAIN . Consultas de tabela única que usam essas funções sem um alias ou área de trabalho opcional retornam resultados corretos. No entanto, consultas de várias tabelas que usam essas funções, mesmo sem um alias ou área de trabalho opcional, podem retornar resultados inesperados.
- Use cautela ao unir tabelas que contêm campos vazios porque o Visual FoxPro corresponde campos vazios. Por exemplo, suponha que você execute uma junção nos campos Customer.zip e Invoice.zip nas tabelas Customer e Invoice no banco de dados de exemplo, TestData.dbc. Se a tabela Customer contém 100 códigos postais vazios e a tabela Invoice contém 400 códigos postais vazios, a saída da consulta contém 40.000 registros extras resultantes dos campos vazios. Para eliminar registros vazios da saída da consulta, use a função EMPTY( ).
