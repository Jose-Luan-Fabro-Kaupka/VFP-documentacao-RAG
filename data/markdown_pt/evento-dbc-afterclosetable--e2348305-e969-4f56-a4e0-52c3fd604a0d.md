# Evento dbc_AfterCloseTable

Ocorre depois que uma tabela ou view é fechada. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_AfterCloseTable(cTableName)
```

```foxpro
PROCEDURE dbc_AfterCloseTable
LPARAMETERS cTableName
```

#### Parâmetros
 **cTableName**
Especifica o nome da tabela ou view sendo fechada.

# Observações

Você pode usar o evento dbc_AfterCloseTable para rastrear o acesso ao banco de dados depois que uma tabela é fechada no banco de dados atual.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameter passed.
PROCEDURE dbc_AfterCloseTable ;
         (cTableName)
? '>>   ' + PROGRAM()
?? ' in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1)
? '     cTableName = ' + TRANSFORM(cTableName) + ' - ' ;
                   + TYPE('cTableName')+' /end/ '
ENDPROC
```
