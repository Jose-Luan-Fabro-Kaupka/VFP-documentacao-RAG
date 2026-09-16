# Evento dbc_PackData

Ocorre antes da execução do comando PACK DATABASE.

```foxpro
PROCEDURE dbc_PackData()
```

# Observações

Você pode usar o evento dbc_PackData para rastrear o acesso ao banco de dados antes de um PACK DATABASE ser executado.

Retorne .F. deste procedimento para impedir que o banco de dados seja compactado. Você receberá um erro "File access denied" ao tentar compactar o banco de dados ao retornar .F..

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameter passed.
PROCEDURE dbc_PackData
 ? '  -  ' + PROGRAM()
 ??' in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1)
 ? '     Current DBC: ' + SUBSTR(DBC(),RAT('\',DBC())+1)+' /end/ '
ENDPROC
```
