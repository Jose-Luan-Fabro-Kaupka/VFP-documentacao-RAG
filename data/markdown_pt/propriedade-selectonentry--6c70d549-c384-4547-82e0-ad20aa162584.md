# Propriedade SelectOnEntry

Especifica se o texto em uma célula de coluna, caixa de edição ou caixa de texto é selecionado quando o usuário move o foco para ele. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.SelectOnEntry[ = lExpr]
```

# Valor de retorno

As configurações da propriedade SelectOnEntry são:

| Configuração | Descrição |
| --- | --- |
| True (.T.) | (Padrão para colunas) O texto é selecionado. |
| False (.F.) | (Padrão para caixas de edição e de texto) O texto não é selecionado. |

# Observações

Aplica-se a: Column Object | EditBox Control | TextBox Control (Visual FoxPro)

Se a propriedade Highlight estiver definida como verdadeiro (.T.), você pode usá-la em conjunto com a propriedade SelectOnEntry para determinar se todo o texto aparece selecionado. Se você definir a propriedade Highlight como falso (.F.), a propriedade SelectOnEntry é ignorada.
