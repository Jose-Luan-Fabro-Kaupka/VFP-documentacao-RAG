# Evento dbc_AfterRemoveTable

Ocorre após a conclusão da remoção de uma tabela. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_AfterRemoveTable(cTableName, lDelete, lRecycle)
```

```foxpro
PROCEDURE dbc_AfterRemoveTable
LPARAMETERS cTableName, lDelete, lRecycle
```

#### Parâmetros
 **cTableName**
Especifica o nome da tabela removida do banco de dados.
**lDelete**
Especifica se a tabela foi excluída em vez de convertida em uma tabela livre.
**lRecycle**
Especifica se a tabela foi colocada na Lixeira do Windows em vez de excluída imediatamente do disco. Alguns dados, como propriedades disponíveis apenas para tabelas contidas em um banco de dados, são perdidos mesmo que a tabela seja somente enviada à Lixeira.

# Observações

Você pode usar dbc_AfterRemoveTable para acompanhar o acesso ao banco de dados depois que uma tabela for removida dele e do disco.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameters passed.
PROCEDURE dbc_AfterRemoveTable ;
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
