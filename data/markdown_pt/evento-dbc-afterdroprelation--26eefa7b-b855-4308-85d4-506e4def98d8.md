# Evento dbc_AfterDropRelation

Ocorre depois que uma relação é removida com êxito de um banco de dados. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_AfterDropRelation(cRelationID, cTableName, cRelatedChild, cRelatedTable, cRelatedTag)
```

```foxpro
PROCEDURE dbc_AfterDropRelation
LPARAMETERS cRelationID, cTableName, cRelatedChild, cRelatedTable, cRelatedTag
```

#### Parâmetros
 **cRelationID**
Especifica o ID da relação armazenado no banco de dados.
**cTableName**
Especifica o nome da tabela pai.
**cRelatedChild**
Especifica o nome da coluna vinculada na tabela filha.
**cRelatedTable**
Especifica a tabela que contém a coluna vinculada.
**cRelatedTag**
Especifica a tag de índice da tabela pai.

# Observações

Use dbc_AfterDropRelation para verificar os parâmetros em um procedimento que rastreia ou gerencia o acesso ao banco de dados após a remoção de uma relação.

Retorne .F. para impedir que a relação seja removida.
