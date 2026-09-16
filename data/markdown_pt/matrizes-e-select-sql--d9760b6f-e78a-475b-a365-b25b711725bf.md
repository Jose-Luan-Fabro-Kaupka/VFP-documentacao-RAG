# Matrizes e SELECT - SQL

Use a Cláusula INTO ou TO do Comando SELECT - SQL para consultar tabelas e direcionar os resultados da consulta para uma matriz.

Se uma matriz não existir e a instrução SQL SELECT retornar um ou mais registros, o comando cria uma matriz. Uma matriz existente é recriada para acomodar os resultados da consulta.

Observação Se a instrução SQL SELECT não retornar nenhum registro, uma matriz existente permanece inalterada e pode conter resultados anteriores. Se uma matriz não existir, o comando não cria uma. Considere usar a variável de sistema _TALLY para determinar se uma instrução SQL SELECT retorna algum registro.

# Exemplo

No exemplo a seguir, SELECT - SQL direciona os resultados de sua consulta para uma matriz chamada RESULTS:

```foxpro
SELECT DISTINCT a.cust_id, a.company, b.amount ;
FROM customer a, payments b ;
WHERE a.cust_id = b.cust_id INTO ARRAY results
DISPLAY MEMORY LIKE results
RESULTS   Priv A            TEST
  ( 1, 1)   C  "000004"
  ( 1, 2)   C  "Stylistic Inc."
  ( 1, 3)   N    13.91  (    13.91000000)
  ( 2, 1)   C  "000008"
  ( 2, 2)   C  "Ashe Aircraft"
  ( 2, 3)   N    4021.98  (  4021.98000000)
  ( 3, 1)   C  "000010"
  ( 3, 2)   C  "Miakonda Industries"
  ( 3, 3)   N     9.84  (   9.84000000)
```
