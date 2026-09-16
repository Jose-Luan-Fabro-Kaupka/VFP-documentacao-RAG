# Evento dbc_BeforeCreateConnection

Ocorre antes de uma nova conexão ser criada.

```foxpro
PROCEDURE dbc_BeforeCreateConnection()
```

# Observações

Você pode adicionar código no evento dbc_BeforeCreateConnection para rastrear tentativas de acesso ao banco de dados antes de uma conexão ser criada, ou para impedir a criação de uma conexão.

Retorne .F. deste procedimento para impedir que a conexão seja criada.

# Exemplo

```foxpro
* Reports to the screen Event name and where it is called from.
PROCEDURE dbc_BeforeCreateConnection
? '>>   ' + PROGRAM()
?? ' in ' + SUBSTR(SYS(16),RAT('\\',SYS(16))+1)
RETURN .F.    && Prevents user from creating a connection.
ENDPROC
```
