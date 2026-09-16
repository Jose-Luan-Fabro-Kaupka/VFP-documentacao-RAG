# Propriedade PageCount

Especifica o número de páginas contidas em um page frame. Disponível em tempo de design e em tempo de execução.

```foxpro
PageFrame.PageCount[ = nPages]
```

# Valor de retorno
 **nPages**
Especifica o número de páginas contidas em um page frame.

# Observações

Aplica-se a: Controle PageFrame

O valor mínimo para a configuração da propriedade PageCount é 0, e o valor máximo é 99.

> **Cuidado:** Se você diminuir a configuração da propriedade PageCount (por exemplo, se alterar a configuração de 3 para 2), todas as páginas que excedem a nova configuração e os objetos que elas contêm são perdidos.
