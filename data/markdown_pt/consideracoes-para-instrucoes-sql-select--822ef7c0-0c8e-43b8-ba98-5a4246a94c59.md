# Considerações para instruções SQL SELECT

Ao criar consultas e views com instruções SQL SELECT, esteja ciente das seguintes considerações, convenções e restrições.
 - User-Defined Functions in SQL SELECT Statements
- Aggregate Functions
- Rules Applied to Column Names
- UNION Operations

# Funções definidas pelo usuário em instruções SQL SELECT

Você pode especificar expressões contendo funções definidas pelo usuário para Select_Item em instruções SQL SELECT. No entanto, observe as seguintes recomendações e restrições ao usar funções definidas pelo usuário em instruções SQL SELECT:
 - Use funções de API e funções definidas pelo usuário escritas em C ou linguagem assembly em vez de realizar manipulações de alto volume com funções definidas pelo usuário. A velocidade na qual funções definidas pelo usuário são executadas pode limitar a velocidade das operações realizadas com SQL SELECT.
- Não presuma nada sobre o ambiente de entrada/saída (I/O) ou de tabelas do Visual FoxPro ao usar funções definidas pelo usuário em SQL SELECT. Em geral, você não sabe qual área de trabalho está selecionada, o nome da tabela atual ou mesmo os nomes dos campos sendo processados. O valor dessas variáveis depende da localização precisa no processo de otimização onde a função definida pelo usuário é chamada.
- Não altere o ambiente de I/O ou de tabelas do Visual FoxPro em funções definidas pelo usuário chamadas em SQL SELECT. Em geral, os resultados podem ser imprevisíveis.
- Use a lista de argumentos passada à função quando ela é chamada como a única maneira confiável de passar valores a funções definidas pelo usuário em SQL SELECT.
- Entenda que manipulações "proibidas" podem fornecer resultados em uma versão do Visual FoxPro, mas podem não funcionar em versões posteriores.

Fora dessas restrições, funções definidas pelo usuário são aceitáveis em instruções SQL SELECT. No entanto, lembre-se de que usar SQL SELECT em geral pode reduzir o desempenho.

Para mais informações sobre funções definidas pelo usuário, consulte User-Defined Procedures and Functions.

# Funções de agregação

Você pode usar funções de agregação com um Select_Item que é um campo ou uma expressão envolvendo um campo ou dentro de uma condição de filtro na cláusula HAVING. No entanto, você não pode aninhar funções de agregação.

A tabela a seguir lista funções de agregação que você pode usar em instruções SQL SELECT.

| Aggregate function | Description |
| --- | --- |
| AVG( ) | Averages a column of numeric data. |
| COUNT( ) or CNT( ) | Counts the number of select items in a column. COUNT(*) counts the number of rows in the query output. |
| MIN( ) | Determines the smallest value of Select_Item in a column. |
| MAX( ) | Determines the largest value of Select_Item in a column. |
| SUM( ) | Totals a column of numeric data. |

O exemplo a seguir cria uma consulta que exibe nomes de colunas de saída conforme descrito:

```foxpro
CLEAR ALL
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\TestData')
SELECT AVG(TAlias1.order_amt), MIN(TAlias1.order_amt) ;
   FROM Orders AS TAlias1
```

Para mais informações sobre as funções de agregação que você pode usar com instruções SELECT, consulte MIN( ) Function, MAX( ) Function e o comando CALCULATE, que contém informações sobre as funções AVG( ), COUNT( ) ou CNT( ) e SUM( ).

# Regras aplicadas a nomes de coluna

As seguintes regras se aplicam quando você especifica uma coluna com a cláusula AS para exibir resultados em uma coluna separada:
 - Se Select_Item for um campo com um nome exclusivo, o nome da coluna de saída é o nome do campo.
- Se mais de um Select_Item tiver o mesmo nome, um sublinhado (_) e uma letra são acrescentados ao final do nome da coluna de saída. Por exemplo, se uma instrução SQL SELECT especificar exibir os campos Cust_ID de duas tabelas, Customer e Orders, os nomes de coluna exibidos são FieldName_a e FieldName_b, ou neste exemplo, Cust_ID_a e Cust_Id_b. O exemplo a seguir cria uma consulta que exibe nomes de coluna conforme descrito: CLEAR ALL CLOSE DATABASES OPEN DATABASE (HOME(2) + 'Data\TestData') SELECT TAlias1.cust_id, TAlias2.cust_id ; FROM Customer AS TAlias1, Orders AS TAlias2 ; WHERE TAlias1.cust_id = TAlias2.cust_id Em uma tabela livre, se mais de um item SQL SELECT tiver o mesmo nome e o nome tiver 10 ou mais caracteres, o nome é truncado para adicionar um número. Por exemplo, um nome de coluna de saída como Department apareceria como Department e Departmen2.
- Se Select_Item for uma expressão, o nome da coluna de saída aparece como Exp_1. Nomes de coluna de saída adicionais aparecem como Exp_2, Exp_3 e assim por diante. O exemplo a seguir cria uma consulta que exibe nomes de coluna de saída conforme descrito: CLEAR ALL CLOSE DATABASES OPEN DATABASE (HOME(2) + 'Data\TestData') SELECT TAlias1.postalcode+"-1234", TAlias2.postalcode+"-5678" ; FROM Customer AS TAlias1, Orders AS TAlias2 ; WHERE TAlias1.cust_id = TAlias2.cust_id
- Se uma função de agregação, como COUNT( ), for usada com Select_Item, a coluna de saída é nomeada Cnt_FieldName. Se mais de um Select_Item for usado com funções de agregação, as colunas de saída são nomeadas AggregateFunction_FieldName com os nomes das funções de agregação abreviados conforme necessário. O exemplo a seguir cria uma consulta que exibe nomes de coluna de saída conforme descrito: CLEAR ALL CLOSE DATABASES OPEN DATABASE (HOME(2) + 'Data\TestData') SELECT COUNT(order_id), SUM(order_net)FROM Orders Para mais informações sobre funções de agregação, consulte Aggregate Functions.

# Operações UNION

Ao realizar operações UNION entre instruções SQL SELECT usando a cláusula UNION, esteja ciente das seguintes considerações e restrições:
 - Todas as listas de seleção nas instruções que estão sendo combinadas com UNION devem ter o mesmo número de expressões (nomes de coluna, expressões aritméticas, funções de agregação e assim por diante).
- Colunas correspondentes nos conjuntos de resultados que estão sendo combinados com UNION, ou qualquer subconjunto de colunas usadas em consultas individuais, devem ser do mesmo tipo de dados, ter uma conversão de dados implícita possível entre os dois tipos de dados ou ter uma conversão explícita fornecida. Por exemplo, um UNION entre uma coluna do tipo de dados datetime e uma do tipo de dados binary não funcionará, a menos que uma conversão explícita seja fornecida. No entanto, um UNION funcionará entre uma coluna do tipo de dados money e uma do tipo de dados int, porque podem ser convertidas implicitamente. Colunas do tipo de dados xml devem ser equivalentes. Todas as colunas devem ser tipadas para um esquema XML ou não tipadas. Se tipadas, devem ser tipadas para a mesma coleção de esquema XML.
- Os nomes de coluna na tabela resultante de UNION são tomados da primeira consulta individual na instrução UNION. Para referir-se a uma coluna no conjunto de resultados por um novo nome (por exemplo, em uma cláusula ORDER BY), a coluna deve ser referida dessa forma na primeira SELECT.
- Colunas de conjunto de resultados correspondentes nas instruções individuais que estão sendo combinadas com UNION devem ocorrer na mesma ordem, porque UNION compara as colunas uma a uma na ordem dada nas consultas individuais. Quando tipos de dados diferentes são combinados em uma operação UNION, eles são convertidos usando as regras de precedência de tipo de dados. No exemplo anterior, os valores int são convertidos para float, porque float tem precedência maior que int.

### Conversão de tipo de dados e precedência em operações UNION

Antes do Visual FoxPro 8.0, você precisava realizar conversão explícita de tipo de dados ao realizar operações UNION em instruções SQL SELECT entre dois campos de tipos diferentes. No entanto, o Visual FoxPro suporta conversão implícita de tipo de dados para os tipos de dados que a suportam.

A conversão explícita de tipo de dados exige que você use funções de conversão do Visual FoxPro, como CTOD( ), enquanto conversões implícitas não exigem o uso de tais funções de conversão.

Quando o Visual FoxPro combina duas colunas de tipos de dados diferentes em uma operação UNION, o tipo de dados com precedência menor é convertido para o tipo de dados com precedência maior. Para propriedades de campo, NULL tem precedência maior sobre NOT NULL.

A tabela a seguir mostra todas as conversões explícitas e implícitas de tipo de dados permitidas para tipos de dados de tabela do Visual FoxPro.

| Data type | Implicit conversion | Explicit conversion |
| --- | --- | --- |
| Character | Character (Binary) | CTOD( ), CTOT( ), VAL( ), CTOBIN( ) |
| Character (Binary) | | |
| Currency | MTON( ) | |
| Date | DateTime | DTOC( ), DTOS( ), DTOT( ) |
| DateTime | TTOC( ), TTOD( ) | |
| Double | STR( ), VAL( ) | |
| Float | Numeric | NTOM( ), STR( ), INT( ) |
| Integer | Numeric, Float, Double, Currency | BINTOC( ) |
| Logical | | |
| Numeric | Float | NTOM( ), STR( ), INT( ) |

A tabela a seguir ilustra resultados de conversão implícita de uma operação UNION entre dois campos.

| Data type 1 | Data type 2 | Data type expected |
| --- | --- | --- |
| Character (N) | Character (X) | Character (MAX(N,X)) |
| Character (N) | Character Binary (X) | Character Binary (MAX(N,X)) |
| Character (N) | Memo | Memo |
| Character Binary (N) | Character Binary (X) | Character Binary (MAX(N,X)) |
| Character Binary (N) | Memo | Memo |
| Currency | Currency | Currency |
| Date | Date | Date |
| Date | DateTime | DateTime |
| DateTime | DateTime | DateTime |
| Double (N) | Float (X,Y) | Float (MAX(MAX(8,Y),2)) |
| Double (N) | Integer | Double (N) |
| Double (N) | Numeric (X,Y) | Double (MAX(MAX(8,Y),2)) |
| Double (X) | Double (Y) | Double (MAX(X,Y)) |
| Float (N,M) | Double (X) | Float (20, MAX(M,X)) |
| Float (N,M) | Float (X,Y) | Float (MAX(N,M), MAX(X,Y)) |
| Float (N,M) | Numeric (X,Y) | Float (MAX (N,X), MAX(M,Y)) |
| Integer | Currency | Currency |
| Integer | Double (X) | Double (X) |
| Integer | Float (X,Y) | Float (MAX(11,X), Y) |
| Integer | Integer | Integer |
| Integer | Numeric (X,Y) | Numeric (MAX(11,X), Y) |
| Logical | Logical | Logical |
| Numeric (N,M) | Double (X) | Numeric (20, MAX(M,X)) |
| Numeric (N,M) | Float (X,Y) | Float (MAX(N,X), MAX(M,Y)) |
| Numeric (N,M) | Numeric (X,Y) | Numeric (MAX(N,X), MAX(M,Y)) |
| Varchar (X) | Character (Y) | Varchar (MAX(X,Y)) |
| Varchar Binary (X) | Character Binary (Y) | Varchar Binary (MAX(X,Y)) |

Para mais informações sobre tipos de dados e funções de conversão, consulte Data and Field Types e Data Conversion Functions.
