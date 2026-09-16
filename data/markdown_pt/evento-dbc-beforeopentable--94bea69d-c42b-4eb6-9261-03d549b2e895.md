# Evento dbc_BeforeOpenTable

Ocorre antes que uma tabela ou view contida no banco de dados seja aberta. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_BeforeOpenTable(cTableName)
```

```foxpro
PROCEDURE dbc_BeforeOpenTable
LPARAMETERS cTableName
```

#### Parâmetros
 **cTableName**
Especifica o nome da tabela ou view sendo aberta.

# Observações

Você pode usar código de método no evento dbc_BeforeOpenTable para rastrear tentativas de acesso antes que uma tabela seja aberta no banco de dados. Este evento ocorre sempre que uma tabela ou view no banco de dados é aberta explicitamente pelo comando USE ou implicitamente por outros comandos, como SELECT.

Se as tabelas subjacentes não estiverem abertas quando uma view for aberta, este evento ocorre tanto para as tabelas quanto para a view. O evento dbc_BeforeOpenTable recebe o nome da tabela como parâmetro e não o nome do cursor.

Retorne .F. deste procedimento para impedir que a tabela seja aberta.

# Exemplo

```foxpro
* Reports the method name, where it is called from and the
* value of the paramater cTableName.
PROCEDURE dbc_BeforeOpenTable ;
         (cTableName)
? '>>   ' + PROGRAM()
?? ' in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1)
? '     cTableName = ' + TRANSFORM(cTableName) + ' - ' ;
                    + TYPE('cTableName')+' /end/ '
ENDPROC
```
