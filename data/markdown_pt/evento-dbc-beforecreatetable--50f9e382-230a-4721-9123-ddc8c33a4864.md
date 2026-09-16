# Evento dbc_BeforeCreateTable

Ocorre antes de uma tabela ser criada no banco de dados ativo. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_BeforeCreateTable(cTableName, cLongTableNameT)
```

```foxpro
PROCEDURE dbc_BeforeCreateTable
LPARAMETERS cTableName, cLongTableName
```

#### Parâmetros
 **cTableName**
Especifica o nome da tabela sendo criada.
**cLongTableName**
Especifica o nome longo a ser dado à tabela.

# Observações

Este evento não ocorre quando você cria uma tabela livre.

Você pode usar o evento dbc_BeforeCreateTable para verificar valores apropriados para cTableName ou cLongTableName. Use esses parâmetros em um procedimento para rastrear ou gerenciar o acesso antes de uma tabela ser criada no banco de dados.

Retorne .F. deste procedimento para impedir que a tabela seja criada.

# Exemplo

```foxpro
PROCEDURE dbc_BeforeCreateTable ;
         (cTableName, ;
          cLongTableName)
? '     cTableName     = ' + TRANSFORM(cTableName)     + ' - ' ;
                       + TYPE('cTableName ')
? '     cLongTableName = ' + TRANSFORM(cLongTableName) + ' - ' ;
                       + TYPE('cLongTableName ')+' /end/ '
ENDPROC
```
