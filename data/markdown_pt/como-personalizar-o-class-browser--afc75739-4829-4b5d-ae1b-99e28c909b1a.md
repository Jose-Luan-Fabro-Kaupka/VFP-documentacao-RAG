# Como: personalizar o Class Browser

Você pode personalizar o Class Browser alterando os valores de suas propriedades e usando seus métodos e eventos. Você pode realizar operações adicionais, como especificar bibliotecas de classes padrão para abrir no Class Browser, usando métodos do Class Browser. Para obter mais informações, consulte Class Browser Properties, Class Browser Methods e Class Browser Object Members

Quando você abre o Class Browser, a variável pública `_oBrowser` é criada automaticamente. Você pode usar esta variável para referenciar ou manipular o Class Browser como faria com qualquer objeto de formulário.

### Para definir propriedades do Class Browser
- Na Command window, use a sintaxe a seguir para definir as propriedades do Class Browser que deseja alterar: _oBrowser. Property = newValue

Por exemplo, após abrir o Class Browser, você pode usar as linhas de código a seguir para definir a propriedade Caption do Class Browser como "My Class Browser" e a propriedade Left como 10:

```foxpro
_OBROWSER.Caption = "My Class Browser"
_OBROWSER.Left = 10
```

### Para especificar a biblioteca de classes padrão para abrir no Class Browser
- Abra a biblioteca de classes no Class Browser.
- Na lista de classes do Class Browser, selecione a biblioteca de classes.
- Na Command window, digite o código a seguir: _oBrowser.SetDefaultFile

Isso redefine quaisquer bibliotecas padrão especificadas anteriormente.

Você pode especificar bibliotecas de classes para abrir por padrão além da biblioteca padrão.

### Para especificar bibliotecas adicionais para abrir com o Class Browser
- No Class Browser, clique no botão View Additional File.
- Na lista de classes do Class Browser, selecione a biblioteca de classes.
- Na Command window, digite o código a seguir: _oBrowser.SetDefaultFile(.T.)

### Para remover bibliotecas de classes da lista do Class Browser
- Na lista de classes do Class Browser, selecione a biblioteca de classes.
- Na Command window, digite o código a seguir: _oBrowser.ResetDefaultFile

### Para remover todas as bibliotecas da lista do Class Browser
- Na Command window, digite o código a seguir: _oBrowser.ResetDefaultFile(.T.)
