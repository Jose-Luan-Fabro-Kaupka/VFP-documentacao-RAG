# Evento dbc_BeforeRenameConnection

Ocorre antes de uma conexão ser renomeada. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_BeforeRenameConnection(cPreviousName,cNewName)
```

```foxpro
PROCEDURE dbc_BeforeRenameConnection
LPARAMETERS cPreviousName, cNewName
```

#### Parâmetros
 **cPreviousName**
Especifica o nome atual da conexão.
**cNewName**
Especifica o novo nome da conexão.

# Observações

Você pode usar o evento dbc_BeforeRenameConnection para rastrear tentativas de acesso ao banco de dados antes que as conexões sejam renomeadas.

Retorne .F. deste procedimento para impedir que a conexão seja renomeada.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameter passed.
PROCEDURE dbc_BeforeRenameConnection ;
         (cPreviousName, cNewName)
 ? '>>   ' + PROGRAM()
 ?? ' in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1)
 ? '     cPreviousName = ' + TRANSFORM(cPreviousName)    + ' - ' ;
                       + TYPE('cPreviousName ')
 ? '     cNewName      = ' + TRANSFORM(cNewName)         + ' - ' ;
                       + TYPE('cNewName ')+' /end/ '
ENDPROC
```
