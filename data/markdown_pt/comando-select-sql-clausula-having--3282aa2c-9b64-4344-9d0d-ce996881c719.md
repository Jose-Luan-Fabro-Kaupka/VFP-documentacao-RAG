# Comando SELECT - SQL - Cláusula HAVING

A cláusula HAVING especifica condições que determinam os grupos incluídos na consulta. Se a instrução SQL SELECT não contiver funções de agregação, você pode usar uma instrução SQL SELECT que contenha uma cláusula HAVING sem uma cláusula GROUP BY.

> **Dica:** A cláusula HAVING sem uma cláusula GROUP BY age como a cláusula WHERE. Se a cláusula HAVING não contiver funções de agregação, use a cláusula WHERE para melhor desempenho.

> **Observação:** A cláusula HAVING deve aparecer antes de uma cláusula INTO; caso contrário, ocorre um erro de sintaxe.

Para a sintaxe completa, consulte Comando SELECT - SQL.

A sintaxe detalhada da cláusula HAVING é a seguinte:

```foxpro
HAVING FilterCondition [AND | OR ...]
```

#### Parâmetros
 **FilterCondition**
Especifica critérios que os grupos devem atender para inclusão nos resultados da consulta. A cláusula HAVING pode incluir várias condições de filtro conectadas por operadores AND ou OR. Para inverter o valor de uma expressão lógica, use NOT. Observação As condições de filtro na cláusula HAVING não podem conter subconsultas. Você pode usar aliases locais e funções de agregação na cláusula HAVING. Para obter mais informações sobre funções de agregação na cláusula HAVING, consulte Considerações para instruções SQL SELECT.

> **Observação:** Para obter mais informações sobre FilterCondition, consulte a cláusula ON na cláusula FROM.

# Observações

O código a seguir mostra um resumo das principais cláusulas do comando SELECT - SQL:

```foxpro
SELECT Select_List
   FROM Table_List
...[WITH (BUFFERING = lExpr)]
   [WHERE Conditions]
   [GROUP BY Column_List]
   [HAVING Conditions]
   [UNION Clause]
   [ORDER BY Column_List]
   [INTO Clause | TO Clause ]
   [Additional_Display_Options]
```

Para obter mais informações sobre uma cláusula específica do comando SQL SELECT, consulte os seguintes tópicos:
 - Cláusula SELECT
- Cláusula FROM
- Comando SELECT - SQL - Cláusula WITH
- Comando SELECT - SQL - Cláusula WHERE
- Cláusula GROUP BY
- Cláusula UNION
- Cláusula ORDER BY
- Cláusula INTO ou TO
- Opções adicionais de exibição
