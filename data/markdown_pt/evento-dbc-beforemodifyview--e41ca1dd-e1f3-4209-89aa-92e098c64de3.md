# Evento dbc_BeforeModifyView

Ocorre antes de uma view ser modificada. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_BeforeModifyView(cViewName)
```

```foxpro
PROCEDURE dbc_BeforeModifyView
LPARAMETERS cViewName
```

#### Parâmetros
 **cViewName**
Especifica o nome da view modificada.

# Observações

Você pode usar o evento dbc_BeforeModifyView para rastrear tentativas de acesso ao banco de dados antes de as views serem modificadas.

Retorne .F. deste procedimento para impedir que a view seja modificada.
