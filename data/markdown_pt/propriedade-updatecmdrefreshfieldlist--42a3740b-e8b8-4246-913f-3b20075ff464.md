# Propriedade UpdateCmdRefreshFieldList

Especifica os campos no cursor a serem atualizados após a execução de um comando Update. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.UpdateCmdRefreshFieldList[ = cExpr]
```

# Valor de retorno

| Termo | Definição |
| --- | --- |
| cExpr | A expressão de caractere cExpr é uma lista separada por vírgulas dos campos na fonte de dados que são atualizados. |

# Observações

Aplica-se a: CursorAdapter Class

A propriedade UpdateCmdRefreshFieldList determina quais campos no cursor são automaticamente atualizados após a emissão de um comando Update.

> **Observação:** A propriedade AllowUpdate Property deve estar definida como True (.T.) para permitir operações de atualização em uma fonte de dados.

Para obter mais informações sobre como o Visual FoxPro atualiza CursorAdapters, consulte Data Access Management Using CursorAdapters.
