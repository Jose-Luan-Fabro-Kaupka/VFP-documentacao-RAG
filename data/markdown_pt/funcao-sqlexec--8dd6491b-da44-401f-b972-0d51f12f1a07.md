# Função SQLEXEC( )

Envia uma instrução SQL à fonte de dados, onde a instrução é processada.

```foxpro
SQLEXEC(nStatementHandle [, cSQLCommand [, cCursorName[, aCountInfo]]])
```

#### Parâmetros
 **nStatementHandle**
Especifica o identificador de instrução para a fonte de dados retornado pela função SQLCONNECT( ). Para obter mais informações, consulte SQLCONNECT( ) Function.
**cSQLCommand**
Especifica a instrução SQL passada à fonte de dados. A instrução SQL pode conter uma cláusula WHERE parametrizada, que cria uma view parametrizada. Você deve definir todos os parâmetros na cláusula WHERE antes de emitir SQLEXEC( ). Por exemplo, se os parâmetros são variáveis, as variáveis devem ser criadas e inicializadas antes que SQLEXEC( ) seja emitido. Para obter mais informações sobre views parametrizadas, consulte How to: Create Parameterized Views. Você pode incluir expressões na instrução SQL. O Visual FoxPro avalia todas as expressões na instrução SQL que você passa antes de enviá-las à fonte de dados. O Visual FoxPro pode avaliar nomes de variáveis de memória, chamadas de função e expressões entre parênteses como valores de parâmetro.
**cCursorName**
Especifica o nome do cursor do Visual FoxPro para o qual o conjunto de resultados é enviado. Se você não incluir um nome de cursor, o Visual FoxPro usa o nome padrão SQLRESULT. Para vários conjuntos de resultados, novos nomes de cursor são derivados acrescentando um número incrementado ao nome do primeiro cursor.
**aCountInfo**
Especifica o nome da matriz a preencher com informações de contagem de linhas. Se a matriz não existir, ela é criada. A matriz tem duas colunas: 1 – Alias, 2 –Count. Coluna Conteúdo da matriz Tipo de dados Descrição Alias 0 Character Indica que o comando SQL não retornou nenhum resultado. Nenhum registro foi retornado ou o comando SQL falhou antes que os resultados pudessem ser retornados. (chamada final de SQLMORERESULTS) ou a execução falhou antes que qualquer resultado pudesse ser processado. Pode estar somente na primeira linha. A coluna Count da linha contém o valor -1. Cadeia de caracteres em maiúsculas não vazia Character Alias do cursor – destino da operação de busca de registros. A coluna Count da linha contém o número de registros buscados ou -1 se a busca falhou. Se Count for -1, o cursor pode não ter sido criado. Durante a execução assíncrona, o processo de busca de um cursor pode ser dividido entre várias chamadas SQLMORERESULTS ou SQLEXEC; cada chamada retorna sua própria contagem de busca para o cursor. Cadeia de caracteres vazia Character Indica que o comando SQL (INSERT, UPDATE ou DELETE) não retornou um conjunto de resultados. Count Número de registros afetados ou buscados. Integer Indica o número de registros afetados conforme retornado pela função ODBC SQLRowCount. Retorna -1 se o número de registros não estiver disponível.

# Valor de retorno

Tipo de dados Numeric. SQLEXEC( ) retorna o número de conjuntos de resultados se houver mais de um. SQLEXEC( ) retorna 0 se ainda estiver executando e retorna 1 quando terminar a execução. SQLEXEC( ) retorna –1 se ocorrer um erro no nível da conexão.

# Observações

Se a instrução SQL que você deseja passar é bastante longa, verifique se ela excede o comprimento máximo de um literal de cadeia de caracteres no Visual FoxPro, que é de 255 caracteres. Cadeias de caracteres mais longas causarão um erro "Command contains unrecognized phrase/keyword". No entanto, você pode passar instruções SQL longas se as dividir em vários literais concatenados. Por exemplo:

```foxpro
lnRetVal = SQLEXEC(lnHandle, "SELECT <long list of fields> " + ;
   "FROM <several tables> " + ;
   "WHERE <complex filter expression>")
```

Se SQLEXEC( ) for usado para executar uma instrução SQL preparada com SQLPREPARE( ), somente o argumento de identificador de conexão nStatementHandle é necessário. Os argumentos cSQLCommand e CursorName devem ser omitidos. Para obter mais informações, consulte SQLPREPARE( ) Function.

Se a instrução SQL gerar um conjunto de resultados, SQLEXEC( ) armazena o conjunto de resultados no cursor do Visual FoxPro especificado. Se a instrução SQL gerar dois ou mais conjuntos de resultados, você pode nomear cada conjunto de resultados definindo a propriedade BatchMode da conexão como False (.F.) usando a função SQLSETPROP( ) e alterando o nome do cursor cada vez que chamar a função SQLMORERESULTS( ). Caso contrário, SQLEXEC( ) nomeia cada conjunto de resultados acrescentando números sequenciais ao nome do primeiro.

SQLEXEC( ) é uma das quatro funções que você pode executar de forma síncrona ou assíncrona. A configuração Asynchronous de SQLSETPROP( ) determina se essas funções executam de forma síncrona ou assíncrona. No modo assíncrono, você deve chamar SQLEXEC( ) repetidamente até que retorne um valor diferente de 0 (ainda executando).

# Exemplo

O exemplo a seguir mostra várias maneiras de usar SQLEXEC( ) para executar consultas ad-hoc e chamar ou criar stored procedures:

```foxpro
CLEAR
LOCAL lnConn
LOCAL lnPercent AS Int  && Input parameters must be typed.
LOCAL lnOutput
lnPercent = 50
lnOutput = 0
* Make connection, assuming a local trusted connection.
lnConn = SQLCONNECT('local')
IF m.lnConn > 0  && Success.
   * Set the active database to PUBS.
   SQLEXEC(m.lnConn, 'use pubs')
   * Execute SELECT statement.
   SQLEXEC(m.lnConn, 'SELECT * FROM authors', 'PubAuthors')
   BROWSE

   * Execute INSERT statement, get value of identity field.
   SQLEXEC(m.lnConn, "INSERT INTO JOBS (job_desc, min_lvl, max_lvl);
       VALUES ('Developer',75,150)")
   SQLEXEC(m.lnConn, "SELECT SCOPE_IDENTITY()", "job_id")
   ? "ID for added Job is " + LTRIM(STR(job_id.exp))
   * Execute DELETE statement. Get number of records affected.
   SQLEXEC(m.lnConn, "DELETE FROM JOBS WHERE job_desc ='Developer'")
   SQLEXEC(m.lnConn, "SELECT @@ROWCOUNT", 'rowcount')
   ? rowcount.exp, "record(s) deleted"
   * Call a stored procedure with no parameters.
   SQLEXEC(m.lnConn, 'sp_who', 'activeusers')
   BROWSE
   * Execute stored procedure with an INPUT parameter.
   SQLEXEC(m.lnConn, 'exec byroyalty ?lnPercent','HalfOffAuthors')

   * Create temp stored procedure with OUTPUT parameter and call it.
   SQLEXEC(m.lnConn, "CREATE PROCEDURE #MyProc @outparam int OUTPUT AS;
      SELECT @outparam=100")
   SQLEXEC(m.lnConn, "exec #myProc ?@lnOutput")
   ? m.lnOutput

   * Create a temp stored procedure with INPUT and OUTPUT parameters
   * and call it.
    SQLEXEC(m.lnConn, "CREATE PROCEDURE #MyProc2 " + ;
                      "@inputparam INT, " + ;
                      "@outparam int OUTPUT " + ;
                      "AS SET @outparam=@inputparam*10")
    SQLEXEC(m.lnConn, "exec #myProc2 ?lnPercent, ?@lnOutput")
    ? m.lnOutput
   * Get version information.
   SQLEXEC(m.lnConn, 'SELECT @@VERSION','SQLVersion1')
   ? STRTRAN(SQLVersion1.Exp,CHR(0))
   * Disconnect.
   SQLDISCONNECT(m.lnConn)
ELSE
   ? "Unable to connect to SQL Server"
ENDIF
RETURN
```
