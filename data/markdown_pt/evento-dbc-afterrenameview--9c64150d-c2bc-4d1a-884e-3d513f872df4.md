# Evento dbc_AfterRenameView

Ocorre antes de uma view ser renomeada. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_AfterRenameView(cPreviousName, cNewName)
```

```foxpro
PROCEDURE dbc_AfterRenameView
LPARAMETERS cPreviousName, cNewName
```

#### Parâmetros
 **cPreviousName**
Especifica o nome atual da view.
**cNewName**
Especifica o novo nome da view.

# Observações

Você pode usar o evento dbc_AfterRenameView para rastrear alterações no banco de dados quando views são renomeadas.
