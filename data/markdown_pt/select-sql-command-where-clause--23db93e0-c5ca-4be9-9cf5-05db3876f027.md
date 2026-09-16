# SELECT - SQL Command - WHERE Clause

A cláusula WHERE especifica as condições de junção e filtro que determinam as linhas que a consulta retorna. Juntar operações na cláusula WHERE funciona da mesma forma que JOIN operações na cláusula FROM.

> **Note:** Including the EVALUATE( ) function in the WHERE clause of a SQL query can return incorrect data.

For the more information, see SELECT - SQL Command.

A sintaxe detalhada para a cláusula WHERE é a seguinte:

```foxpro
[WHERE JoinCondition | FilterCondition [AND | OR JoinCondition | FilterCondition] ...]
```

Parâmetros
** JoinCondition**
Specifies conditions on which the tables in a SQL SELECT statement are joined. For multiple join conditions, you must use the AND or OR operator to connect those conditions. For more information about JoinCondition , see the ON clause in the FROM clause.
**FilterCondition**
Specifies criteria that records must meet to be included in the query results. For more information about FilterCondition , see the ON clause in the FROM clause.

Observações

JoinCondition or FilterCondition can be an IN clause. The IN clause is of the form IN (Value_Set) where Value_Set is Expr1[, Expr2[, ...[ ,ExprN]]]. In Visual FoxPro 9.0 the IN clause is evaluated in a different manner than previous versions; see Changes in Functionality for the Current Release for more information.

O seguinte demonstra o formato da cláusula IN.

```foxpro
CLOSE DATABASES ALL
CREATE CURSOR MyCursor(Field1 I, Field2 I)
INSERT INTO MyCursor values(1,6)
INSERT INTO MyCursor values(2,5)
INSERT INTO MyCursor values(3,4)
SELECT * FROM MyCursor WHERE MyCursor. Field1 ;
IN (1,2,3,4,5)
```

O seguinte código apresenta um resumo das principais cláusulas do SELECT - SQL Comando:

```foxpro
SELECT Select_List
   FROM Table_List
...[WITH (BUFFERING = lExpr)]
   [WHERE Conditions]
   [GROUP BY Column_List]
   [UNION Clause]
   [HAVING Conditions]
   [ORDER BY Column_List]
   [INTO Clause | TO Clause ]
   [Additional_Display_Options]
```

Para mais informações sobre uma cláusula específica do comando SQL SELECT, consulte os seguintes tópicos:
 - SELECT Clause
- FROM Clause
- SELECT - SQL Command - WITH Clause
- GROUP BY Clause
- HAVING Clause
- UNION Clause
- ORDER BY Cláusula
INTO ou TO Cláusula
- Opções de exibição adicionais

Você pode criar condições de filtro que procuram dados contendo caracteres wildcard SQL SELECT, tais como porcentagem (%) e sublinha ( ), usando a cláusula ESCAPE na cláusula WHERE. Na cláusula ESCAPE, você pode especificar um caractere que, quando colocado imediatamente antes do caractere wildcard, indica que o caractere wildcard é tratado como um caractere literal. Para mais informações e exemplos, consulte Condições de Filtro para Consultas e Visualizações.

Exemplo

O exemplo a seguir mostra três campos de duas tabelas, mas apenas os registros que atendem as condições de junção e filtro na cláusula WHERE. O exemplo junta-se à tabela Customer and Orders no campo Cust ID e exibe os campos Company, Order Date e Shipped On para apenas os registros que têm uma data de pedido anterior a 16/02/1994. A instrução SELECT especifica apelidos locais para as tabelas distinguirem o mesmo nome de campo, Cust ID, em ambas as tabelas.

```foxpro
CLOSE ALL
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\TestData')
SELECT TAlias1.company, TAlias2.order_date, TAlias2.shipped_on ;
   FROM customer TAlias1, orders TAlias2 ;
   WHERE TAlias1.cust_id = TAlias2.cust_id ;
   AND TAlias2.order_date < {^1994-02-16}
```

Veja também
- CREATE QUERY Command
- CREATE TABLE - SQL Command
- MODIFY QUERY Command
- Trabalhando com Consultas
- Trabalhar com Visualizações (Visual FoxPro)
