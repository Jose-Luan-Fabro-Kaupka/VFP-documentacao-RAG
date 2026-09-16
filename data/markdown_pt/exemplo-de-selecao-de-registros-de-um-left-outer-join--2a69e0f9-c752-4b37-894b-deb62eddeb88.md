# Exemplo de seleção de registros de um left outer join

Arquivo: ...\Samples\Data\Louterj.qpr

A consulta LOUTERJ, no projeto Solution, combina informações das tabelas orders e customer usando um left outer join. Cada registro de resultado possui um campo para `order_id` da tabela orders e para os campos `cust_id`, `company`, `country` da tabela customer, conforme especificado na cláusula SELECT da instrução SELECT-SQL.

```foxpro
SELECT Customer.cust_id, Customer.company, Customer.country,;
 Orders.order_id;
 FROM testdata!orders LEFT OUTER JOIN testdata!customer ;
  ON Orders.cust_id = Customer.cust_id
```

Normalmente, um left outer join pode responder a duas perguntas sobre os registros no seu banco de dados. Algumas das perguntas que esta consulta pode responder incluem:
 - Quais pedidos pertencem a quais clientes?
- Quais pedidos não possuem informações de cliente relacionadas?

Essas informações ajudam o administrador do banco de dados a determinar quais registros de pedidos estão com informações ausentes.

O left outer join retorna todos os registros da tabela à esquerda da condição de junção combinados com os registros da tabela à direita da condição que correspondem à condição. O conjunto de resultados inclui os dois subconjuntos de registros a seguir:
 - Registros que correspondem à condição de junção e combinam informações de um registro em cada tabela.
- Registros da tabela orders que não correspondem à condição de junção.

Como cada registro nos resultados possui os mesmos campos, os registros com um `order_id` que não teve correspondência na tabela customer possuem valores NULL nos campos que, de outra forma, conteriam valores da tabela customer. Por exemplo, se o registro do pedido 11079 não tivesse registros de cliente relacionados na tabela customer, esse registro apareceria nos resultados com o valor NULL nos campos `cust_id`, `company` e `country`.

Você pode alterar os resultados da consulta especificando filtros, uma ordem de classificação, agrupamento ou outras opções diversas para a consulta.
