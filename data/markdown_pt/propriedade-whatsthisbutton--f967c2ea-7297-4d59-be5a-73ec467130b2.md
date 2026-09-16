# Propriedade WhatsThisButton

Especifica se o botão What's This aparece na barra de título de um formulário. Somente leitura em tempo de execução.

```foxpro
Form.WhatsThisButton[ = lExpr]
```

# Valor de retorno
 **lExpr**
Um dos seguintes: Configuração Descrição True (.T.) Ativa a exibição do botão What's This. False (.F.) (Padrão) Desativa a exibição do botão What's This.

# Observações

Aplica-se a: Form Object

O botão What's This não é exibido na barra de título do formulário se a propriedade WhatsThisButton estiver definida como true (.T.) e qualquer uma das seguintes condições for verdadeira:
 - A propriedade WhatsThisHelp do formulário estiver definida como false (.F.).
- A propriedade BorderStyle do formulário estiver definida como 0 (None).
- A propriedade MinButton do formulário estiver definida como true (.T.).
- A propriedade MaxButton do formulário estiver definida como true (.T.).
