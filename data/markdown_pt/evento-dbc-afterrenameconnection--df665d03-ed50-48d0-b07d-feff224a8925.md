# Evento dbc_AfterRenameConnection

Ocorre antes de uma conexão ser renomeada. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_AfterRenameConnection(cConnectionName, cNewName)
```

```foxpro
PROCEDURE dbc_AfterRenameConnection
LPARAMETERS cPreviousName, cNewName
```

#### Parâmetros
 **cPreviousName**
Especifica o nome anterior da conexão.
**cNewName**
Especifica o novo nome da conexão.

# Observações

Você pode usar o evento dbc_AfterRenameConnection para rastrear alterações no banco de dados conforme as conexões são renomeadas.

Retorne .F. deste procedimento para impedir que a conexão seja renomeada.
