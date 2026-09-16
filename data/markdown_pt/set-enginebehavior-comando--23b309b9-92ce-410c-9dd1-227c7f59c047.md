# SET ENGINEBEHAVIOR Comando

Enables SQL data engine compatibility with Visual FoxPro 7.0, 8.0, and 9.0.

```foxpro
SET ENGINEBEHAVIOR 70 | 80 | 90
```

Parâmetros
 **70**
Especifica que Visual FoxPro tratam SQL comandos com comportamento como nas versões anteriores Visual FoxPro 8.0.
**80**
Specifies that Visual FoxPro treat SQL commands with behavior as in Visual FoxPro 8.0. The following table describes behavior for the SQL SELECT statement. SQL SELECT clause Behavior DISTINCT You cannot use the DISTINCT clause with Memo or General fields. Instead, wrap a Memo field inside a function such as PADR( ) or ALLTRIM( ) . For more information, see PADL( ) | PADR( ) | PADC( ) Functions and ALLTRIM( ) Function . UNION The UNION clause does not support Memo fields unless the ALL clause is included in the SQL SELECT statement. GROUP BY The GROUP BY clause must list every field in the SELECT list except for fields contained in an aggregate function, such as the COUNT( ) function. In addition, the GROUP BY clause must also list every field in a HAVING clause except for fields contained in an aggregate function. For example, the following code raises an error because the field company is not listed in the GROUP BY clause. SELECT company, country FROM Customer GROUP BY country You can include an aggregate function in the SELECT list without having it in the GROUP BY clause. For example, the following code uses the COUNT( ) function on the field company without having the field company in the GROUP BY clause. SELECT COUNT(company), country FROM Customer GROUP BY country HAVING A SQL SELECT statement can contain the HAVING clause without the GROUP BY clause as long as the SQL SELECT statement does not contain any aggregate functions. For example, the following code filters query results by specifying the country field must equal "Sweden". SELECT customerid FROM customers HAVING country="Sweden" LIKE SQL SELECT statements do not automatically remove trailing spaces from values compared with the LIKE operation. In versions before Visual FoxPro 8.0, both values in the LIKE operation were trimmed from the right before evaluation. For example, the following code assumes that you have a table named table1 , and the table has three rows that contain values of "1.", "12 ", and "123", respectively. SELECT * FROM table1 WHERE column1 LIKE "1__" Visual FoxPro 7.0 and earlier returns one row with the value of "123". Visual FoxPro 8.0 returns three rows with the values, "1 ", "12 ", and "123". If the beginning of the filter condition matches the pattern of the expression in the LIKE operation, and the rest of the filter condition contains trailing spaces, the LIKE operation ignores the trailing spaces and returns True (.T.). Trailing spaces in the pattern are not ignored.
**90**
Specifies that Visual FoxPro treat SQL commands with standard Visual FoxPro 9.0 behavior. This is the default setting. The following table describes behavior for the SQL SELECT statement. SQL SELECT clause Behavior TOP nExpr When you enable this setting, including the TOP nExpr [PERCENT] clause in the SQL SELECT command returns no more than nExpr [PERCENT] records. In addition, the SQL engine uses available memory more efficiently and it speeds evaluation for the TOP clause without the PERCENT keyword when you work with large result sets, low memory conditions, or both. GROUP BY When you use aggregate functions, such as MAX( ) , in the SQL SELECT command without a GROUP BY clause, and the system does not find any matching records, Visual FoxPro returns a result set with a single record and it sets _TALLY to 1. In versions before Visual FoxPro 9.0, the system does not return any records and it sets _TALLY to 0. ORDER BY A SELECT … DISTINCT … ORDER BY command will generate an error if the specified ORDER BY field is not in the SELECT field list. CREATE CURSOR foo (f1 int, f2 int) SELECT DISTINCT f1 FROM foo ORDER BY f2 INTO CURSOR res HAVING A SELECT … DISTINCT … HAVING command will generate an error if the specified HAVING field is not in the SELECT field list. CREATE CURSOR foo (f1 int, f2 int) SELECT DISTINCT f1 from foo HAVING f2>1 INTO CURSOR res

Observações

O escopo de SET ENGINEBEHAVIOR é global.

Usar SET ENGINEBEHAVIOR definido como 70 pode levar a resultados ambíguos de comandos SQL SELECT. Isto ocorre quando utiliza o seguinte:
 - DISTINCT and UNION clauses with memos and the GROUP BY clause
- HAVING clause without a GROUP BY clause
- LIKE cláusula

When you set SET ENGINEBEHAVIOR to 70 or 80, results from the TOP clause in the SQL SELECT command might include more than nExpr records when there are rows with identical values for columns specified by the ORDER BY clause. For example, suppose you specified 10 rows for nExpr. If there are more than 10 rows with identical values in the columns specified in the ORDER BY clause, the query result might contain more than 10 rows.

When you set SET ENGINEBEHAVIOR to 70 or 80 and the code page of the table (CPDBF( )) differs from the current Visual FoxPro code page setting (CPCURRENT( )), SQL or other Rushmore optimizable commands could return or act upon incorrect records. When you set SET ENGINEBEHAVIOR to 90, Visual FoxPro builds temporary indexes to ensure correct results.

Para mais informações, consulte Compreendendo Páginas de Código em Visual FoxPro, Usando a Otimização de Consulta Rushmore para Acelerar o Acesso de Dados e Alterações na Funcionalidade para a Lançamento atual.

Veja também
- SET Command Overview
- SELECT - SQL Command
- SYS(3099) - SQL Data Engine Compatibility Mode
