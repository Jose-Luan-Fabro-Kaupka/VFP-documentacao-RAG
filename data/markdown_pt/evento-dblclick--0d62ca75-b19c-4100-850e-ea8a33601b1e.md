# Evento DblClick

Ocorre quando o usuário pressiona e solta o botão do mouse duas vezes em rápida sucessão.

```foxpro
PROCEDURE Object.DblClick
```

# Observações

Aplica-se a: controle CheckBox | controle ComboBox | controle CommandGroup | objeto Container | objeto Control (Visual FoxPro) | controle EditBox | objeto Form | controle Grid | objeto Header | controle Image (Visual FoxPro) | controle Label (Visual FoxPro) | controle Line | controle ListBox | controle OptionButton | controle OptionGroup | objeto Page | controle PageFrame | controle Shape | controle Spinner | controle TextBox (Visual FoxPro) | objeto ToolBar

O evento DblClick também ocorre quando você seleciona um item em uma caixa de listagem ou combinação e pressiona ENTER.

Se DblClick não ocorrer dentro do limite de tempo de clique duplo do sistema, o objeto reconhecerá outro evento Click. Portanto, ao associar procedimentos a esses eventos relacionados, verifique se suas ações não entram em conflito. Controles que não recebem eventos DblClick podem receber dois cliques simples em vez de um clique duplo.

> **Observação:** Se o mouse tiver mais de um botão, você poderá distinguir os botões esquerdo, direito e central usando os eventos MouseDown e MouseUp.
