# Evento dbc_BeforeAddRelation

Ocorre antes que uma relação seja adicionada ao banco de dados. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_BeforeAddRelation(cRelationID, cTableName, cRelatedChild,
   cRelatedTable, cRelatedTag)
```

```foxpro
PROCEDURE dbc_BeforeAddRelation
LPARAMETERS cRelationID, cTableName, cRelatedChild, cRelatedTable,
   cRelatedTag
```

#### Parâmetros
 **cRelationID**
Especifica o número de ID da relação armazenado no banco de dados.
**cTableName**
Especifica o nome da tabela pai.
**cRelatedChild**
Especifica o nome da coluna vinculada.
**cRelatedTable**
Especifica a tabela que contém a coluna vinculada.
**cRelatedTag**
Especifica a tag de índice da tabela pai.

# Observações

Use dbc_BeforeAddRelation para verificar valores apropriados dos parâmetros em um procedimento que controla ou gerencia o acesso ao banco antes da adição da relação.

Retorne .F. desse procedimento para impedir a adição.
