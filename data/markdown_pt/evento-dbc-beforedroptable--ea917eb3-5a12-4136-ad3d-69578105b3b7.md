# Evento dbc_BeforeDropTable

Ocorre antes de a tabela especificada ser removida do banco de dados ativo e excluída do disco com o comando DROP TABLE. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_BeforeDropTable(cTableName, lRecycle)
```

```foxpro
PROCEDURE dbc_BeforeDropTable
LPARAMETERS cTableName, lRecycle
```

#### Parâmetros
 **cTableName**
Especifica a tabela sendo removida do banco de dados atual e excluída do disco.
**lRecycle**
Especifica se a tabela deve ser colocada na Lixeira do Microsoft Windows em vez de ser excluída imediatamente do disco. Alguns dados, como as propriedades de tabela disponíveis apenas em tabelas contidas em um banco de dados, são perdidos mesmo se a tabela for apenas reciclada em vez de removida e excluída.

# Observações

Você pode usar o evento dbc_BeforeDropTable para verificar um valor apropriado para cTableName e usar esses parâmetros em uma procedure para rastrear ou gerenciar o acesso ao banco de dados antes que a tabela seja removida do banco de dados e do disco.

Se você excluir uma tabela usando DELETE FILE ou o sistema operacional, nenhum evento ocorre.

Retorne .F. desta procedure para impedir que a tabela seja removida.

# Exemplo

```foxpro
* Reports the name of the method, where it came from and what the
* parameter values were.
PROCEDURE dbc_BeforeDropTable ;
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
