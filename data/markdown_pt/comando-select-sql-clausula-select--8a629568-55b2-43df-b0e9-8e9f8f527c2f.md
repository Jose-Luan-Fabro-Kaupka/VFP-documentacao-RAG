# Comando SELECT - SQL - Cláusula SELECT

A cláusula SELECT do SQL especifica os campos, constantes e expressões a exibir nos resultados da consulta.

Para a sintaxe completa, consulte Comando SELECT - SQL.

A sintaxe detalhada para a cláusula SELECT é a seguinte:

```foxpro
SELECT [ALL | DISTINCT] [TOP nExpr [PERCENT]] Select_List_Item [AS Column_Name] [, ...]
```

#### Parâmetros
 **[ALL | DISTINCT]**
Exibe todas as linhas nos resultados da consulta, por padrão, ou exclui duplicatas de quaisquer linhas dos resultados da consulta. Você pode usar DISTINCT apenas uma vez por cláusula SELECT. Observação O Visual FoxPro não suporta o uso da cláusula DISTINCT em instruções SQL SELECT que contêm campos Memo , General ou Blob. Em vez disso, para campos Memo, você pode envolver uma expressão de campo Memo dentro de uma função como PADR( ) ou ALLTRIM( ) . Para obter mais informações, consulte Funções PADL( ) | PADR( ) | PADC( ) e Função ALLTRIM( ) .
**[TOP nExpr [PERCENT]]**
Especifica que o resultado da consulta contenha um número específico de linhas ou uma porcentagem de linhas do resultado da consulta. Para nExpr , você pode especificar de 1 a 32.767 linhas, ou, se incluir a opção PERCENT, pode especificar de 0,01 a 99,99 por cento. O Visual FoxPro classifica os registros primeiro e depois extrai os registros TOP nExpr [ PERCENT ]. Observação Ao incluir a cláusula TOP, você deve incluir uma cláusula ORDER BY. A cláusula ORDER BY especifica as colunas para as quais a cláusula TOP determina o número de linhas a incluir no resultado da consulta. Observação A configuração do comando SET ENGINEBEHAVIOR afeta os resultados e o desempenho da cláusula TOP. Para obter mais informações, consulte Comando SET ENGINEBEHAVIOR . PERCENT arredonda para cima o número de linhas retornadas no resultado para o próximo inteiro superior. Observação Linhas com valores idênticos para as colunas especificadas na cláusula ORDER BY são incluídas no resultado da consulta. Portanto, um resultado de consulta pode conter mais linhas do que especificado com nExpr . Por exemplo, se você especificar 10 para nExpr , o resultado da consulta pode conter mais de 10 linhas quando mais de 10 linhas têm valores idênticos conforme especificado com ORDER BY .
**Select_List_Item**
Especifica um ou mais itens a corresponder e incluir nos resultados da consulta. Cada item na lista gera uma coluna nos resultados da consulta. Select_List_Item pode especificar os seguintes itens: Um valor constante que aparece em cada linha dos resultados da consulta. Uma expressão que pode conter funções definidas pelo usuário ou subconsultas. [ Alias .] Select_Item Alias especifica um alias de tabela quando você está recuperando dois ou mais campos Select_Item com o mesmo nome de várias tabelas. Usar um alias de tabela evita que colunas sejam duplicadas. Um espaço entre [ Alias .] e Select_Item é permitido. Select_Item também pode ser um campo de uma tabela na cláusula FROM. ( Subquery ) Subquery especifica uma instrução SQL SELECT dentro de outra instrução SQL SELECT e deve estar entre parênteses (()). Não há limite no número de subconsultas por instrução SQL SELECT. Não há limite na profundidade de aninhamento para subconsultas em uma instrução SQL SELECT. Você pode usar subconsultas correlacionadas até o pai imediato. Uma subconsulta correlacionada usa campos na consulta pai, e a subconsulta é executada para cada linha candidata na consulta pai. Subconsultas podem conter cláusulas TOP nExpr para subconsultas não correlacionadas, várias condições de junção e cláusulas GROUP BY. Se uma subconsulta não retornar nenhum registro, retorna NULL . Observação Se você incluir a cláusula TOP nExpr em uma subconsulta, deve incluir uma cláusula ORDER BY para essa subconsulta. Você pode usar funções de agregação com um Select_List_Item que é um campo ou uma expressão envolvendo um campo. Ao especificar funções de agregação associadas a Select_Item , use a seguinte sintaxe: AggregateFunction([Alias.]Select_Item) Para obter mais informações sobre o uso de funções definidas pelo usuário, funções de agregação e regras aplicáveis a nomes de colunas, consulte Considerações para instruções SQL SELECT .
**[AS Column_Name ]**
Especifica um nome para uma coluna na saída da consulta. Column_Name pode ser uma expressão, mas não pode conter caracteres que não são permitidos, por exemplo, espaços, em nomes de campos de tabela. Dica Quando Select_List_Item é uma expressão ou contém uma função de campo, especificar Column_Name é útil quando você deseja dar à coluna um nome significativo.

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
 - Cláusula FROM
- Comando SELECT - SQL - Cláusula WITH
- Comando SELECT - SQL - Cláusula WHERE
- Cláusula GROUP BY
- Cláusula HAVING
- Cláusula UNION
- Cláusula ORDER BY
- Cláusula INTO ou TO
- Opções de exibição adicionais

# Exemplos

### Exemplo 1

O exemplo a seguir exibe dados únicos de uma consulta usando a opção DISTINCT com uma condição de junção na cláusula WHERE. O exemplo exibe os campos Company, Order_Date e Shipped_On apenas para aqueles registros com dados únicos nas tabelas Customer e Orders. A instrução SELECT especifica aliases locais para as tabelas para distinguir o mesmo nome de campo, Cust_ID, em ambas as tabelas.

```foxpro
CLOSE ALL
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\TestData')
SELECT DISTINCT TAlias1.company, TAlias2.order_date, ;
   TAlias2.shipped_on ;
   FROM customer TAlias1, orders TAlias2 ;
   WHERE TAlias1.cust_id = TAlias2.cust_id
```

### Exemplo 2

O exemplo a seguir exibe todos os registros de uma consulta em uma coluna especificada usando a cláusula AS Column_Name. O exemplo exibe todos os nomes no campo City da tabela Customer em maiúsculas usando a função UPPER( ) e em uma coluna chamada CityList.

```foxpro
CLOSE ALL
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\TestData')
SELECT UPPER(city) AS CityList FROM customer
```
