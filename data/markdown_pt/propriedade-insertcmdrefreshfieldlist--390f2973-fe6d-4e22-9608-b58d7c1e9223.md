# Propriedade InsertCmdRefreshFieldList

Especifica os campos no cursor a serem atualizados após a execução de um comando Insert. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.InsertCmdRefreshFieldList[ = cExpr]
```

# Valor de retorno

| Termo | Definição |
| --- | --- |
| cExpr | A expressão de caractere cExpr é uma lista separada por vírgulas dos campos no cursor que são atualizados. |

# Observações

Aplica-se a: classe CursorAdapter

A propriedade InsertCmdRefreshFieldList determina quais campos no cursor são atualizados automaticamente após a emissão de um comando Insert.

> **Observação:** A propriedade AllowInsert deve ser definida como True (.T.) para permitir operações de inserção em uma fonte de dados.

Para obter mais informações sobre como o Visual FoxPro atualiza dados remotos usando um CursorAdapter, consulte Data Access Management Using CursorAdapters.
