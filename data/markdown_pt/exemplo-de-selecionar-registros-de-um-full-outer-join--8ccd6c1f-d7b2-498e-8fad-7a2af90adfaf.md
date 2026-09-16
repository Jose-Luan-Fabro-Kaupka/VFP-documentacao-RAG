# Exemplo de selecionar registros de um full outer join

Arquivo: ...\Samples\Data\Fouterj.qpr

A consulta FOUTERJ, no projeto Solution, combina informações das tabelas country e customer usando um full outer join. Cada registro de resultado tem um campo para cada um dos campos da tabela country e os campos `country` e `cust_id` do campo da tabela customer conforme especificado na cláusula SELECT da instrução SELECT-SQL.

```foxpro
SELECT Country.*, Customer.country, Customer.cust_id;
 FROM testdata!customer FULL JOIN country ;
  ON Customer.country = Country.country
```

Normalmente, um full outer join responde a três perguntas sobre os registros em seu banco de dados. Algumas das perguntas que esta consulta poderia responder incluem:
 - Quais clientes estão em quais países ou regiões?
- Quais países ou regiões não têm nenhum de nossos clientes?
- Quais registros de cliente estão sem informações de país/região?

Essas informações podem ajudar alguém a decidir se deve expandir os negócios para outros países, alterar a estratégia de marketing em alguns países ou regiões, ou simplesmente que alguns registros no banco de dados precisam que as informações de país/região sejam atualizadas.

O full outer join retorna todos os registros de ambas as tabelas e combina registros que correspondem à condição de junção. O conjunto de resultados inclui os seguintes três subconjuntos de registros:
 - Registros que correspondem à condição de junção que combinam informações de um registro em cada tabela.
- Registros da tabela country que não correspondem à condição de junção.
- Registros da tabela customers que não correspondem à condição de junção.

Como cada registro nos resultados tem os mesmos campos, os registros que não tinham correspondência na outra tabela têm valores NULL nos campos que de outra forma conteriam valores da outra tabela. Por exemplo, se um registro para o país Russia não tivesse registros de cliente relacionados na tabela customer, esse registro aparece nos resultados com NULL como valor do campo `cust_id` e `country_b`.

Você pode alterar os resultados da consulta especificando filtros, uma ordem de classificação, agrupamento ou outras opções diversas para a consulta.
