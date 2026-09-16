# dbc_BeforeModifyTable Evento

Ocorre antes de uma tabela ser modificada. Existem duas versões da sintaxe.

```foxpro
PROCEDURE dbc_BeforeModifyTable(cTableName)
```

```foxpro
PROCEDURE dbc_BeforeModifyTable
LPARAMETERS cTableName
```

#### Parâmetros
 **cTableName**
Especifica o nome da tabela modificada.

# Observações
Você pode usar o evento dbc_BeforeModifyTable para rastrear tentativas de acesso ao banco de dados antes que as tabelas sejam modificadas.

Retorne .F. deste procedimento para evitar que a tabela seja modificada.
