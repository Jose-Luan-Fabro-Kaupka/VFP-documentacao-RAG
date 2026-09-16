# Evento When

Ocorre antes de um controle receber o foco.

```foxpro
PROCEDURE Control.When
```

# Observações

Aplica-se a: Controle CheckBox | Controle ComboBox | Controle CommandButton | Controle CommandGroup | Controle EditBox | Controle Grid | Controle ListBox | Controle OptionButton | Controle OptionGroup | Controle Spinner | Controle TextBox (Visual FoxPro)

Se o evento When retornar true (.T.), o controle padrão recebe o foco. Se o evento When retornar false (.F.), o controle não recebe o foco. A ordem dos eventos quando um controle ganha o foco é:
 - Evento When
- Evento GotFocus

Para controles ListBox, o evento When ocorre cada vez que um usuário move o foco entre itens na lista clicando nos itens ou movendo a seleção com as teclas de seta.

> **Observação:** O controle Grid não possui um evento GotFocus, portanto apenas When é disparado.

Para todos os outros controles, o evento When ocorre quando é feita uma tentativa de mover o foco para o controle.
