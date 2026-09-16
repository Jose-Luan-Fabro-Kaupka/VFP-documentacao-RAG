# Exemplo de seleção de registros de um right outer join

Arquivo: ...\Samples\Data\Routerj.qpr

A consulta ROUTERJ, no projeto Solution, usa o banco de dados testdata e combina informações das tabelas orders e employee usando um right outer join. Cada registro do resultado tem um campo para `order_id` da tabela orders e para o campo `lastname` da tabela employee.

```foxpro
SELECT Orders.order_id, Employee.last_name;
 FROM testdata!employee RIGHT OUTER JOIN testdata!orders ;
 ON Employee.emp_id = Orders.emp_id
```

Normalmente, um right outer join pode responder a duas perguntas sobre os registros do seu banco de dados. Algumas das perguntas que esta consulta pode responder incluem:
 - Quais pedidos foram inseridos por quais funcionários?
- Quais pedidos não têm um funcionário especificado?

Essas informações podem ajudar a rastrear pedidos específicos e identificar pedidos que não têm um funcionário especificado como responsável pelo pedido.

O right outer join recupera todos os registros da tabela à direita da condição de junção combinados com os registros da tabela à esquerda que correspondem à condição de junção. O conjunto de resultados inclui os dois subconjuntos de registros a seguir:
 - Registros que correspondem à condição de junção e combinam informações de um registro em cada tabela.
- Registros da tabela orders que não correspondem à condição de junção.

Como cada registro no resultado tem os mesmos campos, os registros com `lastname` que não tiveram correspondência na tabela orders têm valores NULL no campo que, de outra forma, conteria valores da tabela orders. Por exemplo, se um registro do pedido número 11078 não tivesse registros de funcionário relacionados na tabela employee, esse registro apareceria nos resultados com o valor NULL no campo `lastname`.

Você pode alterar os resultados da consulta especificando filtros, ordem de classificação, agrupamento ou outras opções diversas para a consulta.
