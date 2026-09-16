# Evento dbc_AfterOpenTable

Ocorre depois que uma tabela ou view é aberta. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_AfterOpenTable(cTableName)
```

```foxpro
PROCEDURE dbc_AfterOpenTable
LPARAMETERS cTableName
```

#### Parâmetros
 **cTableName**
Especifica o nome da tabela ou view que foi aberta.

# Observações

Você pode usar o evento dbc_AfterOpenTable para rastrear o acesso ao banco de dados depois que uma tabela é aberta no banco de dados.

Se as tabelas subjacentes não estiverem abertas quando uma view é aberta, este evento ocorre tanto para as tabelas quanto para a view.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameter passed.
PROCEDURE dbc_AfterOpenTable ;
         (cTableName)
 ? '>>   ' + PROGRAM()
 ?? ' in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1)
? '     cTableName = ' + TRANSFORM(cTableName) + ' - ' + TYPE('cTableName')+' /end/ '
ENDPROC
```
