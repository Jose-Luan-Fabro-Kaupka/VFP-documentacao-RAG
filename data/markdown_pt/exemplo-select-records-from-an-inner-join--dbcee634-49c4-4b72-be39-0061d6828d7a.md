# Exemplo Select Records from an Inner Join

Arquivo: ...\Samples\Data\Innerj.qpr

A consulta INNERJ, no projeto Solution, usa o banco de dados TESTDATA e combina informações das tabelas ORDERS e CUSTOMER usando uma condição de inner join. Cada registro de resultado tem campos para CUST_ID, COMPANY e COUNTRY da tabela CUSTOMERS, e ORDER_ID da tabela ORDERS, conforme especificado na cláusula SELECT da instrução SELECT-SQL.

```foxpro
SELECT Customer.cust_id, Customer.company, Customer.country,;
 Orders.order_id;
 FROM testdata!orders INNER JOIN testdata!customer ;
 ON Orders.cust_id = Customer.cust_id
```

Esta consulta recupera e combina os registros entre as duas tabelas que correspondem à condição de join. A condição especifica que os registros devem ter o mesmo valor no campo `cust_id`.

Um inner join normalmente responde a uma pergunta básica. Nesta consulta, a pergunta é: quais pedidos cada cliente fez? Se um cliente tiver um registro no banco de dados, mas não tiver feito um pedido, o registro não aparece nos resultados porque não faz parte do subconjunto que corresponde à condição de join.

Você pode alterar os resultados da consulta especificando filtros, uma ordem de classificação, agrupamento ou outras opções diversas para a consulta.
