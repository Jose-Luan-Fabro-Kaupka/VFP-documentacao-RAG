# Evento dbc_BeforeRenameTable

Ocorre antes que uma tabela seja renomeada. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_BeforeRenameTable(cPreviousName, cNewName)
```

```foxpro
PROCEDURE dbc_BeforeRenameTable
LPARAMETERS cPreviousName, cNewName
```

#### Parâmetros
 **cPreviousName**
Especifica o nome atual da tabela.
**cNewName**
Especifica o novo nome da tabela.

# Observações

Você pode usar o evento dbc_BeforeRenameTable para acompanhar tentativas de acesso ao banco de dados antes que uma conexão seja renomeada ou para impedir a renomeação de uma tabela.

Retorne .F. deste procedimento para impedir que a tabela seja renomeada.

# Exemplo

```foxpro
PROCEDURE dbc_BeforeRenameTable;
   (cPreviousName, ;
    cNewName)
 ? '>>   ' + PROGRAM()
 ?? 'in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1
 ? '     Current DBC:    ' + SUBSTR(DBC(),RAT('\',DBC())+1
 ? '     cPreviousName = ' + TRANSFORM(cPreviousName)     + ' – ' +
TYPE('cPreviosName ')+' /end/ '
ENDPROC
```
