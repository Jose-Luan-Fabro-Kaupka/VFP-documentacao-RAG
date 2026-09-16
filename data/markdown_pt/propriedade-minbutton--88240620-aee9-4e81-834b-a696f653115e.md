# Propriedade MinButton

Especifica se um formulário tem um botão Minimizar. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.MinButton[ = lExpr]
```

# Valor de retorno
 **lExpr**
As configurações da propriedade MinButton são: Configuração Descrição True (.T.) (Padrão) O formulário tem um botão Minimizar. False (.F.) O formulário não tem um botão Minimizar.

# Observações

Aplica-se a: Objeto Form | Variável de sistema _SCREEN

Um botão Minimizar permite que os usuários minimizem uma janela Form para um ícone.

As configurações que você especificar para MaxButton, MinButton, BorderStyle e ControlBox não são refletidas na aparência do Form até o tempo de execução.

No Microsoft Windows versão 3.0 ou posterior, um formulário filho MDI é exibido com um botão Minimizar independentemente da configuração de MinButton. No entanto, se MinButton estiver definido como false (.F.), ele é desabilitado e o comando Minimizar correspondente não está no menu Controlbox do formulário.

Minimizar um formulário para um ícone em tempo de execução gera um evento Resize. A propriedade WindowState reflete o estado atual da janela. Se você definir a propriedade WindowState como 1 (Minimized), o Form é minimizado independentemente das configurações em vigor para as propriedades MinButton e BorderStyle.
