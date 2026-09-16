# Propriedade ContinuousScroll

Especifica se a rolagem dentro de um formulário é contínua ou se a rolagem ocorre somente quando uma caixa de rolagem é liberada. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.ContinuousScroll[ = lExpression]
```

# Valor de retorno
 **lExpression**
As configurações para lExpression são: Configuração Descrição True (.T.) (Padrão) A rolagem é contínua dentro do formulário. O formulário rola continuamente conforme as caixas de rolagem são movidas. O evento Scrolled ocorre continuamente conforme o formulário é rolado. False (.F.) A rolagem ocorre somente quando uma caixa de rolagem é liberada. O formulário permanece estático até que uma caixa de rolagem seja liberada e então o formulário é redesenhado em sua nova posição. O evento Scrolled ocorre depois que o formulário é redesenhado.

# Observações

Aplica-se a: objeto Form

A propriedade Scrollbars determina se um formulário tem barras de rolagem.
