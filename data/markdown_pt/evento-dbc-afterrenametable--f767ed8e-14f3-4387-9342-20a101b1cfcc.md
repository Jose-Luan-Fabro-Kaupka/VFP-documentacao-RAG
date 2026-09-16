# Evento dbc_AfterRenameTable

Ocorre antes de uma tabela ser renomeada. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_AfterRenameTable(cPreviousName, cNewName)
```

```foxpro
PROCEDURE dbc_AfterRenameTable
LPARAMETERS cPreviouName, cNewName
```

#### Parâmetros
 **cPreviousName**
Especifica o nome atual da tabela.
**cNewName**
Especifica o novo nome da tabela.

# Observações

Você pode usar o evento dbc_AfterRenameTable para rastrear alterações no banco de dados conforme as tabelas são renomeadas.

# Exemplo

```foxpro
PROCEDURE dbc_AfterRenameTable;
   (cPreviousName, ;
    cNewName)
 ? '>>   ' + PROGRAM()
 ?? 'in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1
 ? '     Current DBC:    ' + SUBSTR(DBC(),RAT('\',DBC())+1
 ? '     cPreviousName = ' + TRANSFORM(cPreviousName)    + ' – ' + TYPE('cPreviousName ')+' /end/ '
ENDPROC
```
