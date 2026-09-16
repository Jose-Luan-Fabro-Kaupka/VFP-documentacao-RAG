# Controle de conversão de tipos de dados

Quando você move dados entre um servidor remoto e o Visual FoxPro, pode encontrar diferenças nos tipos de dados disponíveis em seu servidor ou no Visual FoxPro. Raramente há uma correlação um para um entre os tipos de dados disponíveis em uma fonte de dados remota e os disponíveis no Visual FoxPro. Para tratar essas diferenças, o Visual FoxPro usa tipos de dados ODBC ou ADO para mapear tipos de dados remotos para tipos de dados locais do Visual FoxPro. Ao entender como os tipos de dados são mapeados entre ODBC ou ADO e o Visual FoxPro, você pode prever como os dados remotos do servidor são tratados em seu aplicativo Visual FoxPro.

Você também pode ajustar os tipos de dados usados no servidor ou em seu aplicativo. Você pode substituir o tipo de dados de campo padrão do Visual FoxPro criando uma view para o conjunto de dados remoto e depois definindo a propriedade DataType do campo da view no banco de dados. A propriedade DataType é uma propriedade de caractere que indica o tipo de dados desejado para cada campo de uma view remota. Para obter mais informações sobre a propriedade DataType, consulte Função DBSETPROP( ).

# Conversão de tipos de dados entre views remotas e cursores do Visual FoxPro

Quando você recupera dados de uma fonte de dados ODBC ou ADO remota, o Visual FoxPro converte o tipo de dados de cada campo ODBC ou ADO em um tipo de dados equivalente do Visual FoxPro no cursor resultante.

### Tipos de dados remotos para tipos de dados do Visual FoxPro

A tabela a seguir lista o mapeamento padrão de tipos de dados entre tipos de dados de campo remotos e tipos de dados do Visual FoxPro para cursores.

| Tipo de dados ODBC/ADO | Tipos de dados de cursor padrão do Visual FoxPro |
| --- | --- |
| SQL_BINARY / adBinary SQL_VARBINARY / adVarbinary | Memo/Blob1 ou Varbinary Observação O tipo padrão é afetado pela propriedade MapBinary. Para obter mais informações, consulte Função CURSORSETPROP( ). |
| SQL_LONGVARBINARY | General/Blob Observação O tipo padrão é afetado pela propriedade MapBinary. Para obter mais informações, consulte Função CURSORSETPROP( ). |
| adLongVarbinary | Memo ou Character |
| SQL_CHAR / adChar SQL_WCHAR / adWChar | Memo 1 ou Character |
| SQL_LONGVARCHAR / adLongVarChar SQL_WLONGVARCHAR / adLongVarWChar | Memo |
| SQL_VARCHAR / adVarChar SQL_WVARCHAR / adVarWChar | Memo 1 ou Character/Varchar Observação O tipo padrão é afetado pela propriedade MapVarchar. Para obter mais informações, consulte Função CURSORSETPROP( ). |
| SQL_DECIMAL / adNumeric SQL_NUMERIC / adNumeric | Currency 2 |
| SQL_BIT / adBoolean | Logical |
| SQL_TINYINT / adVarbinary SQL_SMALLINT / adSmallInt SQL_INTEGER / adInteger | Integer |
| SQL_BIGINT / adBigInt | Character |
| SQL_REAL / adSingle SQL_FLOAT / adDouble SQL_DOUBLE / adSingle | Double Observação Para Double, o número de casas decimais é o valor de SET DECIMAL no Visual FoxPro. |
| SQL_DATE / adDBTimeStamp | Date |
| SQL_TIME / adDBTTimeStamp | DateTime 4 |
| SQL_TIMESTAMP / adBinary | DateTime 3 |

1 Se a largura do campo ODBC/ADO for menor que o valor da propriedade de cursor UseMemoSize, ele se torna um campo Character/Varchar/Varbinary no cursor do Visual FoxPro; caso contrário, torna-se um campo Memo/Blob.

2 Se o campo do servidor for um tipo de dados money, ele se torna um tipo de dados Currency no Visual FoxPro.

3 Se o valor no campo SQL_TIMESTAMP contiver frações de segundos, as frações são truncadas quando o valor é convertido para um tipo de dados DateTime do Visual FoxPro.

4 O dia assume o padrão 1/1/1900.

A tabela a seguir lista os tipos de dados disponíveis ao usar views remotas ou objetos CursorAdapter com fontes de dados ODBC ou ADO e os tipos de dados equivalentes do Visual FoxPro. Para obter mais informações sobre como especificar o esquema do cursor, consulte o método CursorFill do CursorAdapter.

| Tipo de dados ODBC/ADO | Tipos de dados de cursor aceitáveis do Visual FoxPro |
| --- | --- |
| SQL_BINARY / adBinary SQL_VARBINARY / adVarbinary SQL_LONGVARBINARY / adLongVarbinary SQL_CHAR / adChar SQL_VARCHAR / adVarChar SQL_LONGVARCHAR / adLongVarChar | Blob, Varbinary, Character, Varchar, General, Memo 5 |
| SQL_WCHAR / adWChar SQL_WVARCHAR / adVarWChar SQL_WLONGVARCHAR / adLongVarWChar | Character, Varchar, Memo |
| SQL_BIT / adBoolean | Character, Varchar, Logical |
| SQL_REAL / adSingle SQL_FLOAT / adDouble SQL_DOUBLE / adSingle SQL_DECIMAL / adNumeric SQL_NUMERIC / adNumeric SQL_TINYINT / adVarbinary SQL_SMALLINT / adSmallInt SQL_INTEGER / adInteger SQL_BIGINT / adBigInt | Character, Varchar, Integer, Numeric, Float, Double ou Currency 6 Observação Para Double, o número de casas decimais é o valor de SET DECIMAL no Visual FoxPro. |
| SQL_DATE / adDBTimeStamp SQL_TIMESTAMP / adBinary | Character, Varchar, Date, DateTime 7 |
| SQL_TIME / adDBTTimeStamp | Character, Varchar, DateTime 8 |

5 Se a largura do campo ODBC for menor que o valor da propriedade de cursor UseMemoSize, ele se torna um campo Character no cursor do Visual FoxPro; caso contrário, torna-se um campo Memo.

6 Se o campo do servidor for um tipo de dados money, ele se torna um tipo de dados Currency no Visual FoxPro.

7 Se o valor no campo SQL_TIMESTAMP contiver frações de segundos, as frações são truncadas quando o valor é convertido para um tipo de dados DateTime do Visual FoxPro.

8 O dia assume o padrão 1/1/1900.

> **Observação:** Valores nulos em campos de fonte de dados ODBC tornam-se valores nulos no cursor do Visual FoxPro, independentemente da configuração SET NULL no Visual FoxPro no momento em que seu aplicativo recupera dados remotos.

No Visual FoxPro 9.0, certos tipos de dados ODBC e ADO podem ser mapeados para um tipo de dados lógico em views remotas e no objeto CursorAdapter.

Se o valor do backend for zero, o tipo de dados é mapeado para um valor lógico False (.F.); todos os outros valores são mapeados para True (.T.). Quando atualizações são executadas, o mapeamento de um tipo de dados lógico para um inteiro é específico do backend. Para ODBC, False (.F.) geralmente é mapeado para 0 e True (.T.) geralmente é mapeado para 1. Para ADO, False (.F.) geralmente é mapeado para zero e .T. geralmente é mapeado para 1 ou -1, dependendo do comando sendo executado. A propriedade ConversionFunc do CursorAdapter pode ser usada para impor o mapeamento.

Para views remotas e o objeto CursorAdapter, os tipos de dados ODBC SQL_DECIMAL e SQL_NUMERIC só podem ser mapeados para um valor lógico se Scale estiver definido como zero.

Para o objeto CursorAdapter, os tipos de dados ADO adDecimal e adNumeric só podem ser mapeados para um valor lógico se Scale estiver definido como zero.

A tabela a seguir lista os tipos de dados ODBC e ADO que podem ser mapeados para um tipo de dados lógico.

| Tipo de dados ODBC | Tipo de dados ADO |
| --- | --- |
| SQL_TINYINT SQL_SMALLINT SQL_INTEGER SQL_BIGINT SQL_DECIMAL SQL_NUMERIC | adSingle adTinyInt adSmallInt adInteger adBigInt adUnsignedTinyInt adUnsignedSmallInt adDecimal adNumeric |

A tabela a seguir lista os tipos de dados do Visual FoxPro disponíveis ao usar views remotas com objetos CursorAdapter e dados nativos do Visual FoxPro e seus tipos de dados equivalentes do Visual FoxPro.

| Tipo de dados nativo do Visual FoxPro | Tipo de dados de cursor aceitável do Visual FoxPro |
| --- | --- |
| Character, Memo, General | Character, Varchar, Memo, General |
| Numeric, Float, Currency, Integer, Double | Numeric, Float, Currency, Integer, Double, Character, Varchar |
| Logical | Logical, Character, Varchar |
| Date, DateTime | Character, Varchar, Date, DateTime |

### Valores de parâmetro do Visual FoxPro para tipos de dados de view remota

Se dados do Visual FoxPro existem em um cursor que se originou de dados remotos, os dados revertem para seu tipo de dados ODBC ou ADO original ao enviar dados para o servidor remoto. Se você enviar dados que se originaram no Visual FoxPro para o servidor remoto usando SQL pass-through, a tabela descreve as conversões que se aplicam.

| Tipo de dados do Visual FoxPro | Tipo de dados ODBC |
| --- | --- |
| Character, Varchar, Memo | SQL_CHAR ou SQL_LONGVARCHAR 9 |
| Blob, Varbinary | SQL_BINARY ou SQL_LONGVARBINARY |
| Currency | SQL_DECIMAL |
| Date | SQL_DATE ou SQL_TIMESTAMP 10 |
| DateTime | SQL_TIMESTAMP |
| Double | SQL_DOUBLE |
| Integer | SQL_INTEGER |
| General | SQL_LONGVARBINARY |
| Logical | SQL_BIT |
| Numeric | SQL_DOUBLE |

9 Se a variável do Visual FoxPro que mapeia para um parâmetro cria uma expressão cuja largura é menor que 255, ela se torna um tipo SQL_CHAR na fonte de dados ODBC; caso contrário, torna-se um tipo SQL_LONGVARCHAR.

10 Dados Date do Visual FoxPro são convertidos para SQL_DATE para todas as fontes de dados ODBC, exceto SQL Server, onde se tornam SQL_TIMESTAMP.

#### Mapeamento de valores de parâmetro do Visual FoxPro para tipos de dados remotos

Você pode mapear um valor de parâmetro do Visual FoxPro para um tipo de dados remoto específico formatando o parâmetro como uma expressão de caractere que usa a sintaxe para o tipo de dados remoto desejado. Por exemplo, se seu servidor fornece um tipo de dados DateTime, você pode criar seu parâmetro do Visual FoxPro como uma expressão de caractere no formato usado pelo seu servidor para representar dados DateTime. Quando seu servidor recebe o valor do parâmetro, ele tenta mapear os dados formatados para o tipo de dados DateTime.

> **Observação:** Ao enviar um parâmetro para o servidor remoto, certifique-se de que o tipo de dados na cláusula WHERE corresponda ao tipo de dados usado para a expressão do parâmetro.
