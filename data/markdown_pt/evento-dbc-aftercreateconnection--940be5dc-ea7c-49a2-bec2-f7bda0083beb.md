# Evento dbc_AfterCreateConnection

Ocorre depois que uma conexão foi criada. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_AfterCreateConnection
(cConnectionName, cDataSourceName, cUserID, cPassWord, cConnectionString)
```

```foxpro
PROCEDURE dbc_AfterCreateConnection
LPARAMETERS cConnectionName, cDataSourceName, cUserID, cPassWord,
 cConnectionString
```

#### Parâmetros
 **cConnectionName**
Especifica o nome da conexão que foi criada.
**cDataSourceName**
Especifica o nome da fonte de dados ODBC.
**cUserID**
Especifica sua identificação de usuário para a fonte de dados ODBC.
**cPassWord**
Especifica sua senha para a fonte de dados ODBC.
**cConnectionString**
Especifica uma cadeia de caracteres de conexão para a fonte de dados ODBC. Você pode usar a cadeia de caracteres de conexão em vez de incluir explicitamente a fonte de dados ODBC, a identificação de usuário e a senha.

# Observações

Você pode usar o evento dbc_AfterCreateConnection para rastrear tentativas de acesso ao banco de dados após uma conexão ser criada.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameters passed.
PROCEDURE dbc_AfterCreateConnection ;
         (cConnectionName, ;
          cDataSourceName, ;
          cUserID, ;
          cPassword, ;
          cConnectionString)
? '>>   ' + PROGRAM()
?? ' in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1)
? '     cConnectionName    = ' + TRANSFORM(cConnectionName)   + ' - ' ;
                           + TYPE('cConnectionName ')
? '     cDataSourceName    = ' + TRANSFORM(cDataSourceName)   + ' - ' ;
                           + TYPE('cDataSourceName ')
? '     cUserID            = ' + TRANSFORM(cUserID)           + ' - ' ;
                           + TYPE('cUserID ')
? '     cPassword          = ' + TRANSFORM(cPassword)         + ' - ' ;
                           + TYPE('cPassword ')
? '     cConnectionString  = ' + TRANSFORM(cConnectionString) + ' - ' ;
                           + TYPE('cConnectionString ')+' /end/ '
ENDPROC
```
