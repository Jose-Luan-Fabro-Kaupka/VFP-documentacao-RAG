# Propriedade UpdateCmdRefreshKeyFieldList

Especifica os campos-chave no cursor usados para recuperar um registro depois que um comando Update é executado. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.UpdateCmdRefreshKeyFieldList[ = cExpr]
```

# Valor de retorno

| Termo | Definição |
| --- | --- |
| cExpr | A expressão de caracteres cExpr é uma lista separada por vírgulas dos campos-chave no cursor que são usados para recuperar um registro da fonte de dados. |

# Observações

Aplica-se a: CursorAdapter Class

> **Observação:** A propriedade AllowUpdate deve ser definida como True (.T.) para permitir operações de insert em uma fonte de dados.

Para obter mais informações sobre como o Visual FoxPro atualiza CursorAdapters, consulte Data Access Management Using CursorAdapters.
