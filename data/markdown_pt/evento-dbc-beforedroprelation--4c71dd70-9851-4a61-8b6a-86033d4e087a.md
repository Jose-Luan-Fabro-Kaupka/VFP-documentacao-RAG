# Evento dbc_BeforeDropRelation

Ocorre antes que uma relação seja removida de um banco de dados. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_BeforeDropRelation(cRelationID, cTableName, cRelatedChild,
   cRelatedTable, cRelatedTag)
```

```foxpro
PROCEDURE dbc_BeforeDropRelation
LPARAMETERS [cRelationID, cTableName, cRelationChild, cRelatedTable,
   cRelatedTag]
```

#### Parâmetros
 **cRelationID**
Especifica o ID da relação armazenado no banco de dados.
**cTableName**
Especifica o nome da tabela pai.
**cRelatedChild**
Especifica o nome da coluna vinculada na tabela filha.
**cRelatedTable**
Especifica a tabela filha que contém a coluna vinculada.
**cRelatedTag**
Especifica a tag de índice da tabela pai.

# Observações

Você pode usar o evento dbc_BeforeDropRelation para verificar valores apropriados para cRelationID e os outros parâmetros em um procedimento que rastreia ou gerencia o acesso ao banco de dados antes que uma relação seja removida do banco de dados.

Retorne .F. deste procedimento para impedir que a relação seja removida.
