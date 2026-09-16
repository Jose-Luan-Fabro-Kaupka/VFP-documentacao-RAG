# Objeto Application

Um objeto criado para cada instância do Visual FoxPro que expõe um conjunto de propriedades e métodos do Visual FoxPro.

```foxpro
Application.PropertyName[ = eValue]
-or-
Application.Method
```

#### Parâmetros
 **PropertyName**
Especifica uma propriedade do objeto de aplicação.
**eValue**
Especifica um valor para a propriedade.
**Method**
Especifica um método a ser executado para o objeto de aplicação.

# Observações

Aplica-se a: coleção Projects (Visual FoxPro)

O Visual FoxPro é um servidor de automação, permitindo que outras aplicações, como o Microsoft Excel ou o Visual Basic, iniciem e manipulem remotamente o Visual FoxPro por meio de propriedades e métodos. O objeto Application também está disponível dentro de uma instância do Visual FoxPro.

A sintaxe usada por uma aplicação para criar uma instância de um servidor de automação como o Visual FoxPro é normalmente exclusiva da aplicação. Consulte a documentação da aplicação para obter a sintaxe adequada para criar uma instância de um servidor de automação e manipular a instância por meio das propriedades e métodos.

A coleção Objects pode ser acessada por meio do objeto Application.

# Exemplo

Você pode iniciar outra instância do Visual FoxPro a partir do Visual FoxPro com o comando a seguir:

```foxpro
oNewInstance = CREATEOBJECT('VisualFoxPro.Application')
```

Uma nova instância do Visual FoxPro não é visível quando é criada; o comando a seguir torna a nova instância visível:

```foxpro
oNewInstance.Visible = .T.
```
