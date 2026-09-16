# SELECT - Comando SQL - Cláusula ORDER BY

A cláusula ORDER BY especifica um ou mais itens usados para ordenar o conjunto de resultados final da consulta e a ordem de classificação dos resultados.

> **Observação:** Se você não especificar uma ordem na cláusula ORDER BY, os resultados da consulta aparecem sem ordem definida.

Para a sintaxe completa, consulte SELECT - Comando SQL.

A sintaxe detalhada da cláusula ORDER BY aparece da seguinte forma:

```foxpro
[ORDER BY Order_Item [ASC | DESC] [, ...]]
```

#### Parâmetros
 **[ORDER BY Order_Item**
Especifica o item usado para ordenar o conjunto de resultados final da consulta. Um campo em uma tabela FROM ou uma subconsulta. Você não pode especificar um campo do tipo Blob ou General. Observação Se a cláusula ORDER BY for aplicada a uma operação UNION, o campo também deve ser um Select_Item na última cláusula SELECT, e não uma subconsulta. Um alias de campo da lista SELECT. Observação Se a cláusula ORDER BY for aplicada a uma operação UNION, o alias deve ser um Select_Item na última cláusula SELECT. Uma expressão numérica que indica a posição da coluna na tabela de resultados. A coluna mais à esquerda é o número 1.
**[ASC]**
Especifica ordem ascendente para os resultados da consulta. ASC é a ordem padrão para ORDER BY.
**[DESC]**
Especifica ordem descendente para os resultados da consulta.

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
 - SELECT Clause
- FROM Clause
- SELECT - SQL Command - WITH Clause
- SELECT - SQL Command - WHERE Clause
- GROUP BY Clause
- HAVING Clause
- UNION Clause
- INTO or TO Clause
- Additional Display Options

# Exemplo

O exemplo a seguir organiza os resultados de uma consulta usando a cláusula ORDER BY Order_Item. O exemplo exibe os campos Country, PostalCode e Company para os registros da tabela Customer em ordem ascendente, por padrão.

```foxpro
CLOSE ALL
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\TestData')
SELECT country, postalcode, company ;
   FROM customer ;
   ORDER BY country, postalcode, company
```
