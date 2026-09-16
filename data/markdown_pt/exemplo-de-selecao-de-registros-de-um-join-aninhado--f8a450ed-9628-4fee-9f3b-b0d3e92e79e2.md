# Exemplo de seleção de registros de um join aninhado

Arquivo: ...\Samples\Data\Nested.qpr

A consulta NESTED, no projeto Solution, combina informações das tabelas customer, orders e orditems usando duas condições de inner join. Uma condição de join é entre customer e orders; a outra, entre orders e orditems. Cada registro do resultado contém campos para `cust_id` e `company` da tabela customers, `order_id` da tabela orders e `line_no` da tabela orditems, conforme especificado na cláusula SELECT da instrução SELECT-SQL.

```foxpro
SELECT Customer.cust_id, Customer.company, Orders.order_id, Orditems.line_no;
 FROM testdata!customer INNER JOIN testdata!orders;
 INNER JOIN testdata!orditems ;
 ON Orders.order_id = Orditems.order_id ;
 ON Customer.cust_id = Orders.cust_id
```

A ordem em que as tabelas são unidas determina a ordem em que as condições de join são avaliadas. Nesta consulta, o join entre orders e orditems é avaliado primeiro e produz um subconjunto de registros que atende à condição de join. Esse subconjunto de registros é comparado aos registros da tabela customer e produz o conjunto de resultados final.

Você pode alterar os resultados da consulta especificando filtros, uma ordem de classificação, agrupamento ou outras opções diversas para a consulta.
