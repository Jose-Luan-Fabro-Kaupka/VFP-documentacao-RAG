# Evento dbc_BeforeDeleteConnection

Ocorre antes que uma conexão seja excluída. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_BeforeDeleteConnection(cConnectionName)
```

```foxpro
PROCEDURE dbc_BeforeDeleteConnection
LPARAMETERS cConnectionName
```

#### Parâmetros
 **cConnectionName**
Especifica o nome da conexão.

# Observações

Você pode usar o evento dbc_BeforeDeleteConnection para rastrear tentativas de acesso ao banco de dados antes que conexões sejam excluídas.

Retorne .F. deste procedimento para impedir que a conexão seja excluída.
