# Referência de objeto THIS

Fornece uma referência ao objeto atual em código de evento ou em uma definição de classe.

```foxpro
THIS.PropertyName | ObjectName
```

#### Parâmetros
 **PropertyName**
Especifica uma propriedade a definir ou obter para o objeto.
**ObjectName**
Especifica um objeto na classe.

# Observações

THIS fornece uma maneira conveniente de referenciar o objeto atual ao escrever programas de tratamento de eventos em um formulário. Por exemplo, este programa de evento Click para um command button define o caption do botão para a hora atual:

```foxpro
this.caption = time()
```

Usar THIS em vez de referenciar explicitamente o objeto atual pelo nome (por exemplo, `thisform.command1.caption`) torna o código do programa portável entre objetos, porque evita o nome do objeto e encapsula automaticamente a classe pai do objeto.

THIS também permite referenciar uma propriedade ou um objeto em uma definição de classe. Métodos em um bloco de definição de classe podem usar THIS para especificar uma propriedade ou objeto que existirá quando a classe for criada.

Como múltiplas instâncias de objetos compartilham o mesmo código de método, THIS sempre se refere à instância na qual o código está sendo executado. Se houver múltiplas instâncias de um objeto, e um dos métodos do objeto for chamado, THIS se refere ao objeto correto.

# Exemplo

O exemplo a seguir cria uma subclasse chamada `MyForm`, baseada na classe Form. Um método chamado ChangeBackColor é criado. ChangeBackColor usa THIS para referenciar `MyForm`.

```foxpro
DEFINE CLASS MyForm AS FORM
 CAPTION = "This Form"
 HEIGHT = 15
 WIDTH = 20
 PROCEDURE ChangeBackColor
 PARAMETER NewColor
  THIS.BACKCOLOR = NewColor
 ENDPROC
ENDDEFINE
```
