# Evento dbc_AfterDeleteConnection

Ocorre depois que uma conexão é excluída. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_AfterDeleteConnection(cConnectionName)
```

```foxpro
PROCEDURE dbc_AfterConnection
LPARAMETERS cConnectionName
```

#### Parâmetros
 **cConnectionName**
Especifica o nome da conexão sendo excluída.

# Observações

Você pode usar o evento dbc_AfterDeleteConnection para rastrear o acesso ao banco de dados depois que uma conexão é excluída do banco de dados.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameter passed.
PROCEDURE dbc_AfterDeleteConnection ;
          cItemName)
 ? '>>   ' + PROGRAM()
 ?? ' in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1)
 ? '     cConnectionName    = ' + TRANSFORM(cConnectionName)        + ' - ' ;
                      + TYPE('cConnectionName ')+' /end/ '
ENDPROC
```
