# SELECT - SQL Command - Cláusula WITH

A cláusula WITH permite aplicar um único comando a instruções SELECT existentes sem modificar essas instruções.

Para a sintaxe completa, consulte SELECT - SQL Command.

```foxpro
[WITH (BUFFERING = lExpr) ]
```

#### Parâmetros
 **lExpr**
Tipo de dados lógico. A tabela a seguir lista os valores para lExpr . Configuração lExpr True (.T.) Os dados na instrução SQL-SELECT são baseados em dados em buffer, se disponíveis. False (.F.) (Padrão) Os dados na instrução SQL-SELECT são baseados apenas em dados gravados no disco.

# Observações

O código a seguir mostra um resumo das principais cláusulas do SELECT - SQL Command:

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

Para obter mais informações sobre uma cláusula específica do comando SQL SELECT, consulte os seguintes tópicos:
 - SELECT Clause
- FROM Clause
- WHERE Clause
- GROUP BY Clause
- HAVING Clause
- UNION Clause
- ORDER BY Clause
- INTO or TO Clause
- Additional Display Options

Se você definir BUFFERING como True (.T.), pode consultar dados de um cursor local em buffer, que pode incluir registros que foram atualizados mas não confirmados. Caso contrário, seus resultados incluem apenas registros confirmados no disco.

Se o cursor usa buffer de linha, o registro atual é confirmado antes da execução da instrução.

Se o cursor usa buffer de tabela, o registro atual modificado é salvo no buffer.

A cláusula WITH para especificar BUFFERING é suportada apenas em dados locais do Visual FoxPro e não em dados de bancos de dados back-end.

Se você definir BUFFERING como False (.F.), sua instrução SELECT obtém dados do cursor no disco (que pode ser diferente do que está no buffer). Se você não incluir a instrução BUFFERING, seus resultados são baseados na configuração do SET SQLBUFFERING Command. Por padrão, suas consultas obtêm dados do disco. Uma instrução SELECT com WITH BUFFERING definido como True (.T.) substitui a configuração SET SQLBUFFERING.

A opção WITH BUFFERING é efetiva nos seguintes casos:
 - A área de trabalho não tem um alias especificado para suportar o cursor referenciado na instrução.
- O cursor não está em buffer.
- O cursor atua como destino para operações de atualização ou exclusão.

# Exemplo 1

O exemplo a seguir mostra uma instrução simples referenciando uma única tabela. Você precisa ter uma área de trabalho que tenha o alias "Customers" para que a cláusula WITH seja efetiva.

```foxpro
SELECT * FROM customers WITH (BUFFERING=.T.)
```

# Exemplo 2

O exemplo a seguir mostra que cada tabela referenciada na cláusula FROM precisa de uma cláusula WITH BUFFERING.

```foxpro
SET MULTILOCKS ON
CREATE TABLE Table1 (Field1 N(10), Field2 N(10))
CREATE TABLE Table2 (Field3 N(10), Field4 N(10))
CURSORSETPROP("Buffering", 5, "Table1")
CURSORSETPROP("Buffering", 5, "Table2")
INSERT INTO Table1 VALUES (1, 1)
INSERT INTO Table2 VALUES (0, 100)
SELECT Table1.*, Table2.* ;
   FROM FORCE Table1 ;
      JOIN Table2 ;
      ON Field1>=Field3 AND Field2>0 AND Field4<100
REPLACE Field4 WITH 99 IN Table2
SELECT Table1.*, Table2.* ;
   FROM FORCE Table1 ;
      JOIN Table2 ;
      ON Field1>=Field3 AND Field2>0 AND Field4<100
SELECT Table1.*, Table2.* ;
   FROM FORCE Table1 WITH (BUFFERING=.T.) ;
      JOIN Table2 WITH (BUFFERING=.T.) ;
      ON Field1>=Field3 AND Field2>0 AND Field4<100
```
