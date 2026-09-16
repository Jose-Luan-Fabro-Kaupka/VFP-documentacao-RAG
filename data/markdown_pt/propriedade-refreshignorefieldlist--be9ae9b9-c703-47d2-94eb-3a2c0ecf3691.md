# Propriedade RefreshIgnoreFieldList

Especifica uma lista de campos ignorados pelo processo de atualização quando o método RecordRefresh é executado. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.RefreshIgnoreFieldList [ = cExpr]
```

#### Parâmetros

| Termo | Definição |
| --- | --- |
| cExpr | A expressão de caractere cExpr é uma lista delimitada por vírgulas dos campos no cursor que são ignorados pelo processo de atualização. |

# Observações

Aplica-se a: CursorAdapter Class

Você pode definir esta propriedade no evento BeforeRecordRefresh.
