# Evento dbc_BeforeModifyProc

Ocorre antes que os procedimentos armazenados no banco de dados aberto sejam modificados.

```foxpro
PROCEDURE dbc_BeforeModifyProc()
```

# Observações

Você pode usar o evento dbc_BeforeModiProc para rastrear tentativas de acesso ao banco de dados antes que os procedimentos armazenados sejam modificados.

Retorne .F. deste procedimento para impedir que os procedimentos armazenados sejam modificados.

# Exemplo

```foxpro
* Reports to the screen Event name, and where it is called from.
PROCEDURE dbc_BeforeModifyProc
 ? '>>   ' + PROGRAM()
 ?? ' in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1)
? DBC()
RETURN .F. && prevents modification of stored procedures.
ENDPROC
```
