# Evento dbc_BeforeAddTable

Ocorre antes de uma tabela livre existente ser adicionada ao banco de dados ativo.

Você pode usar o evento dbc_BeforeAddTable para executar código antes que a tabela seja adicionada a um banco de dados. Isso é útil para necessidades de programação como controlar se ou sob quais condições uma tabela é adicionada ao banco de dados ou para registrar a adição da tabela. Há duas versões da sintaxe.

> **Observação:** Este evento não ocorre quando você cria uma tabela no banco de dados.

```foxpro
PROCEDURE dbc_BeforeAddTable(cTableName, cLongTableName)
```

```foxpro
PROCEDURE dbc_BeforeAddTable
LPARAMETERS [cTableName, cLongTableName]
```

#### Parâmetros
 **cTabl eName,**
Especifica o nome da tabela sendo adicionada.
**cLongTableName**
Especifica o nome longo a ser dado à tabela.

# Observações

Para impedir que a tabela seja adicionada ao banco de dados, retorne um valor False (.F.) deste procedimento.

# Exemplo

```foxpro
PROCEDURE dbc_BeforeAddTable ;
         (cTableName, ;
          cLongTableName)
? '     cTableName     = ' + TRANSFORM(cTableName)     + ' - ' ;
                       + TYPE('cTableName ')
? '     cLongTableName = ' + TRANSFORM(cLongTableName) + ' - ' ;
                       + TYPE('cLongTableName ')
userID      = SUBSTR(SYS(0),AT('#',SYS(0))+2)
IF UPPER(userID) = 'MYALIAS'   && only one user can add tables.
   RETURN .T.
ENDIF
   RETURN .F.
ENDIF
ENDPROC
```
