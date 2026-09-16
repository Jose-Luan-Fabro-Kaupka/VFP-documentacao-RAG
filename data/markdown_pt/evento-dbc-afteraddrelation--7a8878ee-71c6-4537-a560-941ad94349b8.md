# Evento dbc_AfterAddRelation

Ocorre após uma relação ser adicionada com sucesso ao banco de dados. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_AfterAddRelation(cRelationID, cTableName, cRelatedChild, cRelatedTable, cRelatedTag)
```

```foxpro
PROCEDURE dbc_AfterAddRelation
LPARAMETERS cRelationID, cTableName, cRelatedChild, cRelatedTable, cRelatedTag
```

#### Parâmetros
 **cRelationID**
Especifica o número de ID da relação armazenado no banco de dados.
**cTableName**
Especifica o nome da tabela pai.
**cRelatedChild**
Especifica o nome da coluna vinculada na tabela filha.
**cRelatedTable**
Especifica a tabela que contém a coluna vinculada.
**cRelatedTag**
Especifica a tag de índice da tabela pai.

# Observações

Você pode usar o evento dbc_AfterAddRelation para verificar valores apropriados para cRelationID e os outros parâmetros em um procedimento que rastreia ou gerencia o acesso ao banco de dados após uma relação ser adicionada ao banco de dados.
