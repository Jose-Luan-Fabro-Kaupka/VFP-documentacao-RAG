# Comando CREATE CONNECTION

Cria uma conexão nomeada e a armazena no banco de dados atual.

```foxpro
CREATE CONNECTION [ConnectionName | ?]   [DATASOURCE cDataSourceName]
   [USERID cUserID] [PASSWORD cPassWord]   [DATABASE cDatabaseName]
| CONNSTRING cConnectionString]
```

#### Parâmetros
 **ConnectionName**
Especifica o nome da conexão a criar.
**?**
Exibe o Connection Designer a partir do qual você pode criar e salvar uma conexão.
**DATASOURCE cDataSourceName**
Especifica o nome da fonte de dados ODBC para a conexão.
**USERID cUserID**
Especifica sua identificação de usuário para a fonte de dados ODBC.
**PASSWORD cPassWord**
Especifica sua senha para a fonte de dados ODBC.
**DATABASE cDatabaseName**
Especifica um banco de dados no servidor ao qual a conexão é feita.
**CONNSTRING cConnectionString**
Especifica uma cadeia de conexão para a fonte de dados ODBC. A cadeia de conexão pode ser usada em vez de incluir explicitamente a fonte de dados ODBC, a identificação de usuário e a senha.

# Observações

Se você omitir os argumentos opcionais, o Connection Designer aparece, permitindo que você crie uma conexão interativamente.

# Exemplo

O exemplo a seguir assume que uma fonte de dados ODBC chamada MyFoxSQLNT está disponível. O banco de dados `testdata` é aberto e uma conexão chamada `Myconn` é criada. DISPLAY CONNECTIONS é usado para exibir as conexões nomeadas no banco de dados. A conexão é então removida do banco de dados com DELETE CONNECTION.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'data\testdata')
CREATE CONNECTION Myconn DATASOURCE "MyFoxSQLNT" USERID "<userid>" PASSWORD "<password>"
CLEAR
DISPLAY CONNECTIONS  && Displays named connections in the database
DELETE CONNECTION Myconn  && Removes the connection just created
```
