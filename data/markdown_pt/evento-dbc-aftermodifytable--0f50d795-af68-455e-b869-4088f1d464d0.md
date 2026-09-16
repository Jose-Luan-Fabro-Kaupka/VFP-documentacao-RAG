# Evento dbc_AfterModifyTable

Ocorre depois que uma tabela é modificada. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_AftermodifyTable(cTableName, lChanged)
```

```foxpro
PROCEDURE dbc_AfterModifyTable
LPARAMETERS cTableName, lChanged
```

#### Parâmetros
 **cTableName**
Especifica o nome da tabela modificada.
**lChanged**
Especifica se uma modificação foi salva no Designer de Tabelas.

# Observações

Você pode usar o evento dbc_AfterModifyTable para acompanhar o acesso ao banco de dados depois que tabelas são modificadas.
