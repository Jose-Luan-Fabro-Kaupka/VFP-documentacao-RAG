# Propriedade TimestampFieldList

Especifica os campos de timestamp no cursor. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.TimestampFieldList [= cExpr]
```

# Valor de retorno

| Termo | Definição |
| --- | --- |
| cExpr | A expressão de caracteres cExpr é uma lista separada por vírgulas de campos de timestamp no cursor. |

# Observações

Aplica-se a: CursorAdapter Class

Use esta propriedade para especificar os campos de timestamp em um cursor em um objeto CursorAdapter. Se você especificar os campos de timestamp com esta propriedade e a propriedade CursorAdapter WhereType estiver definida como 4, o Visual FoxPro inclui os campos de timestamp na condição where para comandos UPDATE/DELETE para atualizações baseadas em Native, ODBC e ADODB.Command. Para atualizações baseadas em XML, os campos de timestamp são incluídos na seção <before> do UpdateGram.
