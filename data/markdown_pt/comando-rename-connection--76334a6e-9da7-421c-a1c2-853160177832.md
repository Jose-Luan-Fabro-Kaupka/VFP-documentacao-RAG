# Comando RENAME CONNECTION

Renomeia uma conexão nomeada no banco de dados atual.

```foxpro
RENAME CONNECTION ConnectionName1 TO ConnectionName2
```

#### Parâmetros
 **ConnectionName1**
Especifica o nome da conexão a ser renomeada.
**ConnectionName2**
Especifica o novo nome da conexão.

# Observações

O banco de dados que contém a conexão nomeada deve ser aberto de forma exclusiva e deve ser o atual antes que a conexão possa ser renomeada. Para abrir um banco de dados para uso exclusivo, inclua EXCLUSIVE em OPEN DATABASE.

# Exemplo

O exemplo a seguir assume que uma fonte de dados ODBC chamada MyFoxSQLNT está disponível. O banco de dados `testdata` é aberto e uma conexão chamada `Myconn1` é criada. DISPLAY CONNECTIONS é usado para exibir as conexões nomeadas no banco de dados.

RENAME CONNECTION é então usado para alterar o nome da conexão recém-criada para `Myconn2`. DISPLAY CONNECTIONS é usado novamente para exibir a conexão com seu novo nome. A conexão recém-renomeada é então removida do banco de dados com DELETE CONNECTION.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
CREATE CONNECTION Myconn1 DATASOURCE "MyFoxSQLNT" USERID "<userid>" PASSWORD "<password>"
CLEAR
DISPLAY CONNECTIONS  && Displays named connections in the database
RENAME CONNECTION Myconn1 TO Myconn2
DISPLAY CONNECTIONS  && Displays connection with new name
DELETE CONNECTION Myconn2  && Removes the connection just renamed
```
