# Evento dbc_BeforeCloseTable

Ocorre antes que a tabela ou a view seja fechada. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_BeforeCloseTable(cTableName)
```

```foxpro
PROCEDURE dbc_BeforeCloseTable
LPARAMETERS cTableName
```

#### Parâmetros
 **cTableName**
Especifica o nome da tabela ou da view que está sendo fechada.

# Observações

Você pode usar o evento dbc_BeforeCloseTable para rastrear o acesso ao banco de dados antes que uma tabela seja fechada no banco de dados atual.

Retorne .F. deste procedimento para impedir que a tabela seja fechada.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameter passed.
PROCEDURE dbc_BeforeCloseTable ;
         (cTableName)
? '>>   ' + PROGRAM()
?? ' in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1)
? '     cTableName = ' + TRANSFORM(cTableName) + ' - ' ;
                   + TYPE('cTableName')+' /end/ '
ENDPROC
```
