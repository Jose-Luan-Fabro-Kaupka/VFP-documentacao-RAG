# Propriedade IntegralHeight

Especifica que a altura de um controle EditBox ou ListBox é ajustada automaticamente para que o último item no controle seja exibido corretamente. Especifica que a altura de um controle TextBox é ajustada para acomodar uma linha de texto. Disponível em tempo de design; somente leitura em tempo de execução.

```foxpro
Object.IntegralHeight[ = lExpr]
```

# Valor de retorno
 **lExpr**
Um dos seguintes: lExpr Descrição True (.T.) A altura de um controle EditBox ou ListBox é ajustada conforme necessário para que o último item no controle seja exibido corretamente. A altura de um TextBox é ajustada para acomodar uma linha de texto. False (.F.) (Padrão) A altura de um EditBox ou ListBox não é ajustada, permitindo que o último item no controle seja exibido incorretamente. A altura de um TextBox não é ajustada para acomodar uma linha de texto.

# Observações

Aplica-se a: Controle EditBox | Controle ListBox | Controle TextBox (Visual FoxPro)

A última linha de texto em um controle EditBox ou ListBox pode ser exibida parcialmente se o controle não tiver a altura adequada. Por exemplo, a altura do controle pode ser tal que apenas a metade superior do último item seja exibida no controle. Defina IntergralHeight como true (.T.) para ajustar automaticamente a altura do controle para que o último item no controle seja sempre exibido corretamente.

Para um TextBox, defina IntergralHeight como true (.T.) para garantir que o controle ajuste automaticamente sua altura quando sua propriedade FontSize é alterada.

Quando a propriedade IntegralHeight está definida como true (.T.), o valor da propriedade Height pode não corresponder à altura real do controle.
