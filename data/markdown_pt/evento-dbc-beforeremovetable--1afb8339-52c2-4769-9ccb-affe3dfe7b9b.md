# Evento dbc_BeforeRemoveTable

Ocorre antes que uma tabela seja removida do banco de dados. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_BeforeRemoveTable(cTableName, lDelete, lRecycle)
```

```foxpro
PROCEDURE dbc_BeforeRemoveTable
LPARAMETERS cTableName, lDelete, lRecycle
```

#### Parâmetros
 **cTableName**
Especifica o nome da tabela que está sendo removida do banco de dados.
**lDelete**
Especifica se a tabela será excluída em vez de convertida em uma tabela livre.
**lRecycle**
Especifica se a tabela será colocada na Lixeira do Windows em vez de ser excluída imediatamente do disco. Alguns dados, como as propriedades de tabela disponíveis somente em tabelas contidas em um banco de dados, são perdidos mesmo que a tabela seja apenas enviada à Lixeira em vez de removida e excluída.

# Observações

Você pode usar o evento dbc_BeforeRemoveTable para acompanhar ou gerenciar o acesso ao banco de dados antes que uma tabela seja removida do banco de dados e do disco.

Retorne .F. deste procedimento para impedir que a tabela seja removida.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameter passed.
PROCEDURE dbc_BeforeRemoveTable ;
         (cTableName, ;
          lDelete, ;
          lRecycle)
? '>>   ' + PROGRAM()
?? ' in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1)
? '     cTableName = ' + TRANSFORM(cTableName) + ' - ' ;
                   + TYPE('cTableName ')
? '     lDelete    = ' + TRANSFORM(lDelete)    + ' - ' ;
                   + TYPE('lDelete')
? '     lRecycle   = ' + TRANSFORM(lRecycle)   + ' - ' ;
                   + TYPE('lRecycle')+' /end/ '
ENDPROC
```
