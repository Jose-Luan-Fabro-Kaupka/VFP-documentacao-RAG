# Evento dbc_AfterModifyProc

Ocorre após modificações terem sido feitas e o editor de stored procedure do banco de dados ter sido fechado.

```foxpro
PROCEDURE dbc_AfterModifyProc()
```

# Observações

Você pode usar o evento dbc_AfterModifyProc para rastrear o acesso ao banco de dados após a stored procedure ser modificada.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called.
PROCEDURE dbc_AfterModifyProc
 ? '>>   ' + PROGRAM()
 ?? ' in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1)
 ? '     Current DBC:    ' + SUBSTR(DBC(),RAT('\',DBC())+1)+' /end/ '
ENDPROC
```
