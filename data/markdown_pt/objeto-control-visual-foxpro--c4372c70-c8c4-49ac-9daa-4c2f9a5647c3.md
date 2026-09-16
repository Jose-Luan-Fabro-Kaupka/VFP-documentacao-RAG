# Objeto Control (Visual FoxPro)

Cria um objeto de controle que pode conter outros objetos protegidos.

```foxpro
Control
```

# Observações

Objetos Control podem conter outros objetos, mas, diferentemente de objetos container, não permitem acesso aos objetos contidos neles. Por exemplo, se você criar um objeto Control que consiste em dois ListBoxes e dois CommandButtons e depois adicionar o objeto Control a um formulário, os ListBoxes e CommandButtons não podem ser manipulados individualmente em tempo de design ou em tempo de execução.

Para obter mais informações sobre objetos Control e como eles diferem de outros objetos e controles, consulte Object-Oriented Programming.
