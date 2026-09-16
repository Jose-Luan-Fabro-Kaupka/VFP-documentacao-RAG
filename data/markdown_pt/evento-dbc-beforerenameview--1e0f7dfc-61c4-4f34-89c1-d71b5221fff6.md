# Evento dbc_BeforeRenameView

Ocorre antes que uma view seja renomeada. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_BeforeRenameView(cPreviousName, cNewName)
```

```foxpro
PROCEDURE dbc_BeforeRenameView
LPARAMETERS cPreviousName, cNewName
```

#### Parâmetros
 **cPreviousName**
Especifica o nome atual da view.
**cNewName**
Especifica o novo nome da view.

# Observações

Use dbc_BeforeRenameView para controlar tentativas de acesso ao banco antes que views sejam renomeadas.

Retorne .F. desse procedimento para impedir a renomeação.
