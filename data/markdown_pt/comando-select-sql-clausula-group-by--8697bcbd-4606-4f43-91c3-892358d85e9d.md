# Comando SELECT - SQL - Cláusula GROUP BY

A cláusula GROUP BY especifica uma ou mais colunas usadas para agrupar linhas retornadas pela consulta. Colunas referenciadas na lista da instrução SQL SELECT, exceto expressões de agregação, devem ser incluídas na cláusula GROUP BY. Você não pode agrupar por campos Memo, General ou Blob.

Para a sintaxe completa, consulte Comando SELECT - SQL.

A sintaxe detalhada da cláusula GROUP BY é a seguinte:

```foxpro
[GROUP BY Column_List_Item [, ...] ]
```

#### Parâmetros
 **Column_List_Item**
Especifica uma ou mais colunas usadas para agrupar linhas retornadas pela consulta.

Column_List_Item pode ser um dos seguintes:
 - Um campo em uma tabela na cláusula FROM ou uma subconsulta.
- Um alias de tabela da lista SQL SELECT.
- Uma expressão numérica indicando a localização da coluna na tabela de resultados. A coluna mais à esquerda é o número 1.

# Observações

O código a seguir mostra um resumo das principais cláusulas do Comando SELECT - SQL:

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
- Cláusula HAVING
- Cláusula UNION
- Cláusula ORDER BY
- Cláusula INTO ou TO
- Opções de Exibição Adicionais
