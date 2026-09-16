# Comando SELECT - SQL - Cláusula FROM

A cláusula FROM especifica uma ou mais tabelas contendo os dados que a query recupera.

Para a sintaxe completa, consulte Comando SELECT - SQL.

A sintaxe detalhada da cláusula FROM é a seguinte:

```foxpro
FROM [FORCE] Table_List_Item [, ...]
      [[JoinType] JOIN DatabaseName!]Table [[AS] Local_Alias]
      [ON JoinCondition [AND | OR [JoinCondition | FilterCondition] ...]
```

#### Parâmetros
 **[FORCE]**
FORCE especifica que as tabelas na lista de tabelas são unidas na ordem em que aparecem na cláusula FROM. Observação Se FORCE for omitido, o Visual FoxPro tenta otimizar a query. No entanto, a query pode ser executada mais rapidamente incluindo a palavra-chave FORCE para desabilitar a otimização de query do Visual FoxPro.
**Table_List_Item [, ...]**
Especifica uma ou mais tabelas que contêm os dados que a query recupera. Table_List_Item can have the following syntaxes: [ DatabaseName !] Table [[AS] Local_Alias ] DatabaseName ! especifica o nome de um banco de dados contendo a tabela se a tabela estiver em um banco de dados não atual. Se a tabela estiver em um banco de dados não atual, você deve incluir o nome do banco de dados. Use um ponto de exclamação (!) como delimitador imediatamente após o nome do banco de dados e antes do nome da tabela. Table especifica o nome da tabela da qual você deseja recuperar dados. Se nenhuma tabela estiver aberta, o Visual FoxPro exibe a caixa de diálogo Abrir para que você possa especificar o local do arquivo. Depois que a tabela é aberta, ela permanece aberta quando a query é concluída. Local_Alias especifica um nome temporário para a tabela especificada em Table . Se você especificar um alias local, deve usar o alias local em vez do nome da tabela em toda a instrução SELECT. Não há limite para o número de tabelas e aliases por instrução SELECT. Você também pode especificar várias tabelas usando uma ou mais cláusulas JOIN. ( Subquery ) AS Subquery_Alias Subquery especifica uma instrução SELECT dentro de outra instrução SELECT. Observação Na cláusula FROM, cada subquery requer um alias. Subqueries na cláusula FROM não têm as restrições que se aplicam a subqueries em condições de filtro e podem usar quaisquer cláusulas SQL SELECT, incluindo cláusulas UNION. Todas as subqueries na cláusula FROM são executadas antes que a instrução SELECT principal seja avaliada.
**[[ JoinType ] JOIN DatabaseName !] Table [[AS] Local_Alias ]**
Especifica uma cláusula JOIN para recuperar dados de mais de uma tabela. O Visual FoxPro suporta joins aninhados. Observação Não há limite para o número de joins por instrução SELECT.

> **Observação:** A tabela a seguir descreve os diferentes tipos de joins que você pode especificar com JoinType.

| JoinType | Descrição |
| --- | --- |
| INNER | O resultado da query contém apenas linhas de uma tabela que correspondem a uma ou mais linhas em outra tabela. (Padrão) |
| LEFT [OUTER] | O resultado da query contém todas as linhas da tabela à esquerda da palavra-chave JOIN e apenas linhas correspondentes da tabela à direita da palavra-chave JOIN. A palavra-chave OUTER é opcional; inclua-a para esclarecer que um outer join é criado. |
| RIGHT [OUTER] | O resultado da query contém todas as linhas da tabela à direita da palavra-chave JOIN e apenas linhas correspondentes da tabela à esquerda da palavra-chave JOIN. The OUTER keyword is optional; it can be included to clarify that an outer join is created. |
| FULL [OUTER] | O resultado da query contém todas as linhas correspondentes e não correspondentes de ambas as tabelas. The OUTER keyword is optional; you can include it to clarify that an outer join is created. |

Para obter mais informações sobre a cláusula [DatabaseName!]Table [[AS] Local_Alias], consulte a cláusula FROM. Para obter mais informações sobre operações de join, consulte Condições de join para tabelas, queries e views.
 **[ON JoinCondition | FilterCondition [AND | OR [ JoinCondition | FilterCondition ] ...]**
Especifica condições nas quais tabelas em uma instrução SQL SELECT são unidas ou os resultados são filtrados. Condições de join também podem incluir condições de filtro. Para várias condições de join ou filtro, você deve usar o operador AND ou OR para conectar essas condições. Você pode incluir subqueries e subqueries aninhadas na cláusula ON. Observação Se você incluir mais de uma tabela em uma query, deve especificar uma condição de join para cada tabela após a primeira. JoinCondition especifica condições que podem conter o seguinte: Uma condição de comparação entre campos de tabelas diferentes, por exemplo: FieldName1 Comparison FieldName2 FieldName1 especifica um nome de campo de uma tabela, e FieldName2 especifica um nome de campo de outra tabela. Uma condição de comparação contendo expressões envolvendo campos de tabelas diferentes, por exemplo: Table1 . Field1 + Table2 . Field1 Comparison Table3 . Field1 Uma função definida pelo usuário, por exemplo: MyUDF ( Table1 . Field1 , Table2 . Field1 ) A tabela a seguir lista os operadores disponíveis para Comparison . Comparison Description = Igual Observação Quando você usa o operador igual (=) com cadeias de caracteres, ele funciona de forma diferente dependendo da configuração de SET ANSI . Quando SET ANSI está definido como OFF , o Visual FoxPro compara cadeias de caracteres apenas até o final da cadeia mais curta. Quando SET ANSI está definido como ON , o Visual FoxPro segue os padrões ANSI para comparações de cadeias de caracteres. Para obter mais informações, consulte SET ANSI e SET EXACT . == Exatamente igual LIKE Operação SQL LIKE <>, !=, # Diferente > Maior que >= Maior que or equal to < Menor que <= Menor que or equal to Para obter mais informações sobre condições de join, consulte Condições de join para tabelas, queries e views . FilterCondition especifica uma expressão lógica que descreve critérios de filtro que os registros devem atender para serem incluídos nos resultados da query. Você pode incluir várias condições de filtro em uma query conectando-as com o operador AND ou OR. Para inverter o valor de uma expressão lógica, use o operador NOT. Para verificar um campo vazio, use a função EMPTY( ) . FilterCondition pode usar as sintaxes descritas para JoinCondition, exceto que os campos especificados estão na mesma tabela. Além disso, FilterCondition pode especificar as seguintes sintaxes: FieldName Comparison Expression -OR- FieldName [NOT] LIKE cExpression | IS [NOT] NULL | [NOT] BETWEEN Start_Range AND End_Range | [NOT] IN Value_Set Para obter mais informações sobre operadores válidos para Comparison , consulte a descrição de JoinCondition . A tabela a seguir descreve outras opções disponíveis ao especificar FilterCondition . Option Description Expression Os valores de FieldName devem atender à comparação com uma expressão para inclusão nos resultados da query. LIKE " cExpression " Os valores de FieldName devem corresponder à expressão de caractere cExpression , que pode conter caracteres curinga SQL, como percentual (%) e sublinhado (_), para inclusão nos resultados da query. O caractere % representa qualquer sequência de caracteres desconhecidos na cadeia de caracteres. O caractere _ representa um único caractere desconhecido na cadeia de caracteres. Você pode usar a cláusula ESCAPE para especificar caracteres curinga como literais. A condição de filtro LIKE " sometext %" é totalmente otimizada. IS NULL O valor de FieldName deve ser null para inclusão nos resultados da query. BETWEEN Start_Range AND End_Range Os valores de FieldName devem estar dentro de um intervalo especificado de valores para inclusão nos resultados da query. IN ( Value_Set ) FieldName deve conter um dos valores ou expressões especificados em Value_Set para inclusão nos resultados da query. Ao listar itens no conjunto de valores, separe cada item com vírgulas. Observação O número de valores ou expressões que você pode especificar para Value_Set é afetado pela configuração de SYS(3055) – Complexidade da cláusula FOR e WHERE . Dica O Visual FoxPro pode parar de avaliar valores e expressões na lista Value_Set quando a primeira correspondência é encontrada. Portanto, se a cláusula IN não é otimizada por Rushmore, você pode melhorar o desempenho colocando valores com maior probabilidade de correspondência no início da lista Value_Set.

Para obter mais informações e exemplos sobre condições de filtro, consulte Condições de filtro para queries e views.

# Observações

O código a seguir mostra um resumo das principais cláusulas do Comando SELECT - SQL:

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

Para obter mais informações sobre uma cláusula específica do comando SQL SELECT, consulte os tópicos a seguir:
 - SELECT Clause
- SELECT - SQL Command - WITH Clause
- SELECT - SQL Command - WHERE Clause
- GROUP BY Clause
- HAVING Clause
- UNION Clause
- ORDER BY Clause
- INTO or TO Clause
- Additional Display Options

# Exemplo

O exemplo a seguir exibe dados de um campo em uma tabela usando a cláusula FROM. O exemplo exibe todos os nomes de empresa no campo Company da tabela Customer:

```foxpro
CLOSE ALL
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\TestData')
SELECT customer.company ;
   FROM customer
```
