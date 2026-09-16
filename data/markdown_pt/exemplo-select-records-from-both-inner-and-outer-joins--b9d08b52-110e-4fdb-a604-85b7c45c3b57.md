# Exemplo Select Records from Both Inner and Outer Joins

Arquivo: ...\Samples\Data\Comboj.qpr

A consulta COMBOJ usa o banco de dados testdata e combina informações das tabelas customer, orders e orditems. Cada registro de resultado possui campos para `company` da tabela customer, `order_date` da tabela orders e `line_no` da tabela orditems, conforme especificado na cláusula SELECT da instrução SELECT-SQL.

```foxpro
SELECT Customer.company, Orders.order_id, Orditems.line_no;
 FROM testdata!customer LEFT OUTER JOIN testdata!orders;
    INNER JOIN testdata!orditems ;
   ON Orders.order_id = Orditems.order_id ;
   ON Customer.cust_id = Orders.cust_id
```

A ordem em que as tabelas são unidas determina a ordem em que as condições de junção são avaliadas. Nesta consulta, a junção entre orders e orditems é avaliada primeiro e produz um subconjunto de registros que atende à condição de junção. Devido à junção interna, o subconjunto de registros contém apenas registros de ambas as tabelas que correspondem à condição. Este subconjunto de registros é correspondido aos registros na tabela customer. Devido à junção externa entre customer e orders, quaisquer clientes sem pedidos também aparecem nos resultados e possuem o valor NULL.

Você pode alterar os resultados da consulta especificando filtros, uma ordem de classificação, agrupamento ou outras opções diversas para a consulta.
