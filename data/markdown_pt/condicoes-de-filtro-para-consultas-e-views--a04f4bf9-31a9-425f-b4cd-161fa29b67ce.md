# Condições de Filtro para Consultas e Views

Em declarações SQL SELECT, condições de filtro especificam critérios de filtro que os registros recuperados de uma declaração SQL SELECT devem atender para serem incluídos nos resultados da consulta ou view. Ao criar consultas e views com declarações SQL SELECT para recuperar dados, você pode usar condições de filtro nas cláusulas ON e WHERE para extrair apenas os registros que atendem às condições de filtro. Por exemplo, você pode usar condições de filtro para recuperar apenas os registros em que os valores de um campo são menores que um valor de filtro, como uma data.

Você pode especificar condições de filtro de forma semelhante à especificação de condições de junção, mas usando valores de filtro de uma única tabela e personalizar condições de filtro usando operadores de comparação para controlar como esses valores de campo se comparam a esses valores de filtro. Condições de junção comparam um valor de campo em uma tabela a um valor de campo em outra tabela em vez de um valor de filtro na mesma tabela.

Para a sintaxe de condições de filtro em declarações SQL SELECT, consulte Comando SELECT - SQL.

Este tópico contém as seguintes seções:
 - Partes das Condições de Filtro
- Operadores de Comparação de Filtro
- Opções e Valores de Filtro
- Caracteres Curinga em Condições de Filtro

# Partes das Condições de Filtro

A lista a seguir contém partes de condições de filtro que você pode especificar:
 - Campos de tabela a comparar
- Operadores de comparação de filtro, como > ou !=
- Opções de filtro, como ANY ou LIKE , e valores, como valores de campo, expressões, conjuntos de valores e subconsultas

# Operadores de Comparação de Filtro

Além de usar a sintaxe de condições de junção para uma tabela para especificar um filtro, você pode usar operadores de comparação, como =, <=, e >, para comparar um valor de campo a um valor de filtro. Os operadores de comparação que você pode usar são os mesmos disponíveis para operadores de comparação em condições de junção.

A tabela a seguir lista os operadores de comparação disponíveis para condições de filtro.

| Operador | Descrição |
| --- | --- |
| = | Igual |
| == | Exatamente igual |
| LIKE | SQL LIKE |
| <>, !=, # | Diferente |
| > | Maior que |
| >= | Maior ou igual a |
| < | Menor que |
| <= | Menor ou igual a |

O exemplo a seguir ilustra o uso do operador menor que (<) na condição de filtro, TAlias2.order_date < {^1994-02-16}, usando a sintaxe, FieldName Comparison Expression, e exibe apenas os nomes de empresa no campo Company da tabela Customer que possuem pedidos correspondentes na tabela Orders com datas de pedido no campo Order_Date anteriores a 02/16/1994.

```foxpro
CLOSE ALL
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\TestData')
SELECT TAlias1.company, TAlias2.order_date ;
   FROM customer TAlias1, orders TAlias2 ;
   WHERE TAlias1.cust_id = TAlias2.cust_id ;
      AND TAlias2.order_date < {^1994-02-16}
```

# Opções e Valores de Filtro

Você pode usar opções de filtro além de operadores de comparação para personalizar sua condição de filtro para escolher subconjuntos de registros. Ao usar essas opções, a sintaxe da condição de filtro pode ser uma das seguintes:
 - FieldName Comparison Expression | ALL ( Subquery ) | ANY ( Subquery ) | SOME ( Subquery ) -OU-
- FieldName [NOT] LIKE cExpression | IS [NOT] NULL | [NOT] BETWEEN Start_Range AND End_Range | [NOT] IN Value_Set | [NOT] IN ( Subquery ) -OU-
- [NOT] EXISTS ( Subquery )

A tabela a seguir descreve as opções disponíveis para condições de filtro.

| Opção | Descrição |
| --- | --- |
| ALL ( Subquery ) | Os valores de FieldName devem atender à comparação para todos os valores gerados pela subconsulta para inclusão nos resultados da consulta. |
| ANY ( Subquery ) | SOME ( Subquery ) | Os valores de FieldName devem atender à comparação para pelo menos um dos valores gerados pela subconsulta para inclusão nos resultados da consulta. |
| LIKE " cExpression " | Os valores de FieldName devem corresponder à expressão de caracteres cExpression , que pode conter caracteres curinga SQL, como percentual (%) e sublinhado (_), para inclusão nos resultados da consulta. O caractere % representa qualquer sequência de caracteres desconhecidos na cadeia de caracteres. O caractere _ representa um único caractere desconhecido na cadeia de caracteres. Se você deseja especificar um caractere curinga como literal, use a cláusula ESCAPE. Para obter mais informações, consulte Caracteres Curinga em Condições de Filtro abaixo. A condição de filtro LIKE " cExpression %" é totalmente otimizada. |
| IS NULL | O valor de FieldName deve ser nulo para inclusão nos resultados da consulta. |
| BETWEEN Start_Range AND End_Range | Os valores de FieldName devem estar dentro de um intervalo especificado de valores para inclusão nos resultados da consulta. |
| IN ( Value_Set ) | FieldName deve conter um dos valores ou expressões especificados em Value_Set para inclusão nos resultados da consulta. Ao listar itens no conjunto de valores, separe cada item com vírgulas. Observação O número de valores ou expressões que você pode especificar para Value_Set é afetado pela configuração de SYS(3055) - Complexidade de Cláusulas FOR e WHERE . Dica O Visual FoxPro para de avaliar valores e expressões na lista Value_Set quando a primeira correspondência é encontrada. Portanto, se a cláusula IN não é otimizada pelo Rushmore, você pode melhorar o desempenho colocando valores com maior probabilidade de correspondência no início da lista Value_Set. |
| IN ( Subquery ) | FieldName deve conter um dos valores retornados por Subquery para inclusão nos resultados da consulta. |
| EXISTS ( Subquery ) | A consulta contém resultados apenas quando pelo menos uma linha é retornada da subconsulta. A cláusula EXISTS avalia para True (.T.) ou False (.F.). Observação A cláusula EXISTS ( Subquery ) avalia para True (.T.) a menos que a subconsulta avalie para o conjunto vazio. |

Os pequenos exemplos de código a seguir ilustram várias formas de especificar opções e valores de filtro.
 - A condição de filtro a seguir usa a sintaxe FieldName Comparison ALL ( Subquery ) e inclui apenas os valores que são menores que todos os valores gerados pela subconsulta. Especificamente, esta condição especifica que a consulta inclua apenas os nomes de empresa que vêm alfabeticamente antes daqueles cujo campo country contém "UK" na tabela Customer. company < ALL (SELECT company FROM customer WHERE country = "UK")
- A condição de filtro a seguir usa a sintaxe FieldName LIKE cExpression e inclui apenas os valores que correspondem a cExpression . Especificamente, esta condição especifica que a consulta inclua apenas os registros em que o campo Country na tabela Customer contém valores correspondentes a "UK". customer.country LIKE "UK"
- A condição de filtro a seguir usa a sintaxe FieldName BETWEEN Start_Range AND End_Range e inclui apenas os valores dentro do intervalo especificado de valores. Especificamente, esta condição especifica que a consulta inclua apenas os códigos postais na tabela Customer que estão entre "90000" e "99999." customer.postalcode BETWEEN "90000" AND "99999"
- A condição de filtro a seguir usa a sintaxe FieldName IN ( Value_Set ) e inclui apenas os valores que são um dos especificados em Value_Set . Especificamente, esta condição especifica que a consulta inclua apenas os códigos postais na tabela Customer que são "98052", "98072" e "98034." customer.postalcode IN ("98052","98072","98034")
- A condição de filtro a seguir usa a sintaxe FieldName IN ( Subquery ) e inclui apenas os valores que estão entre os retornados pela subconsulta. Especificamente, esta condição especifica que a consulta inclua apenas os números de ID de cliente na tabela Customer que estão no conjunto de números de ID de cliente na tabela Orders que correspondem a pedidos cujo campo City contém "Seattle". customer.cust_id IN ; (SELECT orders.cust_id FROM orders WHERE orders.city="Seattle")
- A condição de filtro a seguir usa a sintaxe, EXISTS ( Subquery ), e inclui resultados apenas quando pelo menos uma linha é retornada da subconsulta. Especificamente, esta condição especifica que a consulta contenha resultados apenas quando pelo menos um registro é retornado da subconsulta. A subconsulta especifica selecionar todos os registros da tabela Orders em que o código postal na tabela Customer corresponde ao código postal na tabela Orders. EXISTS (SELECT * FROM orders ; WHERE customer.postalcode = orders.postalcode)

O exemplo completo a seguir usa a cláusula EXISTS (Subquery) para criar uma consulta que contém resultados apenas quando pelo menos um registro é retornado da subconsulta. A subconsulta especifica recuperar nomes de empresa da tabela Customer apenas se pelo menos um registro em que o código postal na tabela Customer corresponde ao código postal na tabela Orders.

```foxpro
CLOSE ALL
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\TestData')
SELECT company FROM customer TAlias1 ;
   WHERE EXISTS (SELECT * FROM orders TAlias2 ;
     WHERE TAlias1.postalcode = TAlias2.postalcode)
```

# Caracteres Curinga em Condições de Filtro

Você pode realizar pesquisas usando caracteres curinga em expressões de condição de filtro na cláusula WHERE de uma declaração SQL SELECT usando os caracteres percentual (%) e sublinhado (_). O caractere % representa qualquer sequência de caracteres desconhecidos na cadeia de caracteres. O caractere _ representa um único caractere desconhecido na cadeia de caracteres.

No entanto, se você deseja especificar uma expressão de condição de filtro que recupera dados contendo caracteres curinga, use a cláusula ESCAPE para tratar os caracteres curinga como caracteres literais. Na cláusula ESCAPE, você pode especificar um caractere que, quando colocado imediatamente antes do caractere curinga, indica que o caractere curinga deve ser tratado como um caractere literal.

Os exemplos a seguir ilustram como realizar pesquisas usando caracteres curinga.
 - O exemplo a seguir usa a opção LIKE cExpression para exibir todos os registros que atendem a uma condição de filtro usando a cláusula WHERE FilterCondition. O exemplo cria uma consulta que exibe todos os registros da tabela Customer com um nome de empresa que começa com a letra maiúscula C e tem comprimento desconhecido especificando o caractere curinga percentual (%). CLOSE ALL CLOSE DATABASES OPEN DATABASE (HOME(2) + 'Data\TestData') SELECT * FROM customer WHERE company LIKE "C%"
- O exemplo a seguir usa a opção LIKE cExpression para exibir todos os registros que atendem a uma condição de filtro usando a cláusula WHERE FilterCondition. O exemplo cria uma consulta que exibe todos os registros da tabela Customer com um nome de país que começa com a letra maiúscula U e é seguido por um caractere desconhecido especificando o caractere curinga sublinhado (_). CLOSE ALL CLOSE DATABASES OPEN DATABASE (HOME(2) + 'Data\TestData') SELECT * FROM customer WHERE country LIKE "U_"

Os exemplos a seguir mostram como criar consultas em dados contendo caracteres curinga, como percentual (%) e sublinhado (_).
 - O exemplo a seguir usa a cláusula ESCAPE para especificar que a barra invertida (\) é o caractere de escape. A barra invertida é inserida imediatamente antes do caractere percentual para indicar que deve ser tratado como literal. Observação As tabelas de exemplo incluídas com o Visual FoxPro não contêm o caractere percentual; portanto, este exemplo não retorna resultados. CLOSE ALL CLOSE DATABASES OPEN DATABASE (HOME(2) + 'Data\TestData') SELECT * FROM customer WHERE company LIKE "10\%" ESCAPE "\"
- O exemplo a seguir usa a cláusula ESCAPE para especificar que o caractere traço (-) é o caractere de escape. No entanto, no exemplo, o caractere traço é especificado como caractere de escape e caractere literal. O exemplo retorna todos os registros em que o nome da empresa começa com um caractere traço. Observação As tabelas de exemplo incluídas com o Visual FoxPro não contêm o caractere traço no nome da empresa; portanto, este exemplo não retorna resultados. CLOSE ALL CLOSE DATABASES OPEN DATABASE (HOME(2) + 'Data\TestData') SELECT * FROM customer WHERE company LIKE "--" ESCAPE "-"
