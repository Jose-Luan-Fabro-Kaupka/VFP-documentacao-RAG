# MODIFY CONNECTION Comando

Mostra o Designer de Conexões, tornando possível que você modifique interativamente uma conexão existente chamada armazenada no banco de dados atual.

```foxpro
MODIFY CONNECTION [ConnectionName | ?]
```

Parâmetros
** ConexãoName
Especifica o nome da ligação a modificar.
**?
Mostra a caixa de diálogo Abrir na qual você pode escolher uma conexão com o nome existente para modificar.

Observações

Se você omitir os argumentos opcionais, a caixa de diálogo Abrir é exibida, permitindo que você especifique uma conexão com o nome existente para modificar. O Designer de Conexões é exibido após você escolher uma conexão nomeada para modificar.

Exemplo

The following example assumes an ODBC data source called MyFoxSQLNT is available. The `testdata` database is opened, and a connection named `Myconn` is created. MODIFY CONNECTION is used to displays the Connection Designer so you can modify the connection.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'data\testdata')
CREATE CONNECTION Myconn DATASOURCE "MyFoxSQLNT" USERID "<userid>" PASSWORD "<password>"
MODIFY CONNECTION Myconn && Displays named connections in the database
```

Veja também
- CREATE CONNECTION Command
- DELETE CONNECTION Command
- OPEN DATABASE Command
- RENAME CONNECTION Command
- Commands (Visual FoxPro)
