# Evento dbc_AfterCreateTable

Ocorre após uma tabela ser criada no banco de dados ativo. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_AfterCreateTable(cTableName, cLongTableName)
```

```foxpro
PROCEDURE dbc_AfterCreateTable
LPARAMETERS cTableName, cLongTableName
```

#### Parâmetros
 **cTableName**
Especifica o nome da tabela que foi criada.
**cLongTableName**
Especifica o nome longo da tabela que foi criada.

# Observações

Este evento não ocorre quando você cria uma tabela livre.

Você pode usar o evento dbc_AfterCreateTable para verificar valores apropriados para cTableName ou cLongTableName, usar esses parâmetros em um procedimento para rastrear ou gerenciar o acesso ao banco de dados após uma tabela ser criada no banco de dados.

# Exemplo

```foxpro
PROCEDURE dbc_AfterCreateTable ;
         (cTableName, ;
          cLongTableName)
? '     cTableName      = ' + TRANSFORM(cTableName)     + ' - ' ;
                        + TYPE('cTableName ')
? '     cLongTableName  = ' + TRANSFORM(cLongTableName) + ' - ' ;
                        + TYPE('cLongTableName ')+' /end/ '
ENDPROC
```
