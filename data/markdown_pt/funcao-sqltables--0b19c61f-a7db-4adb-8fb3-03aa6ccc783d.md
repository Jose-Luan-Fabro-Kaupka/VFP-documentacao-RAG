# Função SQLTABLES( )

Armazena os nomes das tabelas de uma fonte de dados em um cursor do Visual FoxPro.

```foxpro
SQLTABLES(nStatementHandle [, cTableTypes] [, cCursorName])
```

#### Parâmetros
**nStatementHandle**
Especifica o identificador de instrução da fonte de dados retornado por SQLCONNECT( ).
**cTableTypes**
Especifica um ou mais tipos de tabela. Os tipos de tabela válidos são 'TABLE', 'VIEW', 'SYSTEM TABLE' ou qualquer identificador de tipo de tabela válido e específico da fonte de dados. Se você incluir uma lista de tipos de tabela, separe-os por vírgulas. Todos os nomes de tabela da fonte de dados serão selecionados se cTableTypes for omitido ou for uma cadeia de caracteres vazia. O tipo de tabela especificado deve estar delimitado por aspas simples. O exemplo a seguir demonstra como especificar os tipos de tabela 'VIEW' e 'SYSTEM TABLE' como um literal de cadeia de caracteres. ? SQLTABLES(handle, "'VIEW', 'SYSTEM TABLE'", "mydbresult")
**cCursorName**
Especifica o nome do cursor do Visual FoxPro para o qual o conjunto de resultados é enviado. Se você não incluir um nome de cursor, o Visual FoxPro usará o nome padrão SQLRESULT. A estrutura dos resultados depende da função SQLTABLES( ) interna para o identificador ODBC.

# Valor de retorno

Numérico. SQLTABLES( ) retorna 1 se o cursor for criado com êxito, 0 se SQLTABLES( ) ainda estiver em execução, – 1 se ocorrer um erro no nível da conexão e – 2 se ocorrer um erro no nível do ambiente.

# Observações

SQLTABLES( ) é uma das quatro funções que podem ser executadas de forma síncrona ou assíncrona. A configuração da opção assíncrona de SQLSETPROP( ) determina se essas funções são executadas de forma síncrona ou assíncrona. No modo assíncrono, você deve chamar SQLTABLES( ) repetidamente até que ela retorne um valor diferente de False (.F.), o que indica que a função ainda está em execução.

# Exemplo

O exemplo a seguir pressupõe que uma fonte de dados ODBC chamada MyFoxSQLNT esteja disponível. SQLCONNECT( ) é emitida e seu valor de retorno é armazenado em uma variável chamada `gnHandle`.

Se não for possível conectar-se à fonte de dados, SQLCONNECT( ) retornará um número negativo e uma mensagem será exibida.

Se a conexão com a fonte de dados for bem-sucedida, SQLCONNECT( ) retornará um número positivo e uma caixa de diálogo será exibida. SQLTABLES( ) é usada para criar um cursor chamado `mycursor`, que contém informações sobre as tabelas da fonte de dados. LIST é usado para exibir informações sobre as tabelas.

```foxpro
STORE SQLCONNECT('MyFoxSQLNT', '<userid>', '<password>') TO gnConnHandle
IF gnConnHandle < 0
   = MESSAGEBOX('Cannot make connection', 16, 'SQL Connect Error')
ELSE
   = MESSAGEBOX('Connection made', 48, 'SQL Connect Message')
   STORE SQLTABLES(gnConnHandle, 'TABLE', 'mycursor') TO nTables
   IF nTables = 1
      SELECT mycursor
      LIST
   ENDIF
ENDIF
```
