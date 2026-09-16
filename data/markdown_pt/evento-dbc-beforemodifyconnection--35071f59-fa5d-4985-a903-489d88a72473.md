# Evento dbc_BeforeModifyConnection

Ocorre antes que uma conexão seja modificada. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_BeforeModifyConnection(cConnectionName)
```

```foxpro
PROCEDURE dbc_BeforeModifyConnection
LPARAMETERS cConnectionName
```

#### Parâmetros
 **cConnectionName**
Especifica o nome da conexão modificada.

# Observações

Você pode usar o evento dbc_BeforeModifyConnection para rastrear tentativas de acesso ao banco de dados antes que as conexões sejam modificadas.

Retorne .F. deste procedimento para impedir que a conexão seja modificada.
