# Evento dbc_AfterDropTable

Ocorre depois que uma tabela é removida do banco de dados e excluída do disco pelo comando DROP TABLE. Existem duas versões da sintaxe.

```foxpro
PROCEDURE dbc_AfterDropTable(cTableName, lRecycle)
```

```foxpro
PROCEDURE dbc_AfterDropTable
LPARAMETERS cTableName, lRecycle
```

#### Parâmetros
 **cTableName**
Especifica a tabela removida do banco de dados atual e excluída do disco.
**lRecycle**
Especifica se a tabela foi colocada na Lixeira do Windows em vez de ser excluída imediatamente do disco.

# Observações

Você pode usar o evento dbc_AfterDropTable para verificar um valor apropriado para cTableName, usar esses parâmetros em um procedimento para rastrear ou gerenciar o acesso ao banco de dados depois que uma tabela é removida do banco de dados e do disco.

Se você excluir uma tabela usando DELETE FILE ou o sistema operacional, nenhum evento ocorre.

# Exemplo

```foxpro
* Reports to the screen the event name, where it is called from, and
* the parameter values passed to it.
PROCEDURE dbc_AfterDropTable ;
         (cTableName, ;
          lRecycle)
? '>>   ' + PROGRAM()
?? ' in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1)
? '     cTableName = ' + TRANSFORM(cTableName) + ' - ' ;
                   + TYPE('cTableName ')
? '     lRecycle   = ' + TRANSFORM(lRecycle)   + ' - ' ;
                   + TYPE('lRecycle')+' /end/ '
ENDPROC
```
