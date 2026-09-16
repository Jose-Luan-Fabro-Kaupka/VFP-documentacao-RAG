# Evento RangeHigh

Para um spinner ou caixa de texto, ocorre quando o controle perde o foco. Para uma caixa de combinação ou caixa de listagem, ocorre quando o controle recebe o foco.

```foxpro
PROCEDURE Object.RangeHigh
```

# Observações

Aplica-se a: Controle ComboBox | Controle ListBox | Controle Spinner | Controle TextBox (Visual FoxPro)

Um evento RangeHigh pode retornar um valor numérico ao Microsoft Visual FoxPro por meio de uma instrução RETURN. Para um spinner ou uma caixa de texto com um valor numérico, se o valor retornado ao Visual FoxPro for menor que o valor digitado no controle, o controle mantém o foco. Para uma caixa de combinação ou caixa de listagem, o valor retornado ao Visual FoxPro especifica qual item no controle é selecionado inicialmente. Por exemplo, se 2 é retornado ao Visual FoxPro, o segundo item no controle é selecionado inicialmente.
