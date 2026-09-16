# Comando DELETE CONNECTION

Exclui uma conexão nomeada do banco de dados atual.

```foxpro
DELETE CONNECTION ConnectionName
```

#### Parâmetros
 **ConnectionName**
Especifica o nome da conexão nomeada a ser excluída do banco de dados atual.

# Observações

Excluir uma definição de conexão nomeada não fecha nenhuma conexão ativa.

DELETE CONNECTION requer uso exclusivo do banco de dados. Para abrir um banco de dados para uso exclusivo, inclua EXCLUSIVE em OPEN DATABASE.

# Exemplo

O exemplo a seguir assume que uma fonte de dados ODBC chamada MyFoxSQLNT está disponível. O banco de dados `testdata` é aberto e uma conexão chamada `Myconn` é criada. DISPLAY CONNECTIONS é usado para exibir as conexões nomeadas no banco de dados. A conexão é então removida do banco de dados com DELETE CONNECTION.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
CREATE CONNECTION Myconn DATASOURCE "MyFoxSQLNT" USERID "<userid>" PASSWORD "<password>"
DISPLAY CONNECTIONS    && Displays named connections in the database
DELETE CONNECTION Myconn  && Removes the connection just created
```
