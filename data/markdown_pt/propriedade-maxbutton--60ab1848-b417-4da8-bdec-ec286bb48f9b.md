# Propriedade MaxButton

Especifica se um formulário tem um botão Maximizar. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.MaxButton[ = lExpr]
```

# Valor de retorno
 **lExpr**
As configurações da propriedade MaxButton são: Configuração Descrição True (.T.) (Padrão) O formulário tem um botão Maximizar. False (.F.) O formulário não tem um botão Maximizar.

# Observações

Aplica-se a: Objeto Form | Variável de sistema _SCREEN

Um botão Maximizar permite que o usuário amplie um formulário para o tamanho da tela inteira.

Um botão Maximizar torna-se automaticamente um botão Restaurar quando uma janela é maximizada. Minimizar ou restaurar uma janela altera automaticamente o botão Restaurar de volta para um botão Maximizar.

As configurações que você especifica para MaxButton, MinButton, BorderStyle e ControlBox não são refletidas na aparência do formulário até o tempo de execução.

Maximizar um formulário em tempo de execução dispara o evento Resize.

> **Observação:** A propriedade WindowState reflete o estado atual da janela. Se você definir a propriedade WindowState como 2 (Maximizada), o formulário é maximizado independentemente das configurações em vigor para as propriedades MaxButton e BorderStyle.
