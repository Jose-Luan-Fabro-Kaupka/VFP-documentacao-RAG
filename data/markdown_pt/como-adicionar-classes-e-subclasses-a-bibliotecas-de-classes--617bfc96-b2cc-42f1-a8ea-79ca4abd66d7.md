# Como: adicionar classes e subclasses a bibliotecas de classes

Quando você cria uma classe ou subclasse de forma interativa ou programática, a classe é armazenada na biblioteca de classes que você especifica. Se a biblioteca de classes existir, a classe é adicionada à biblioteca de classes.

### Para adicionar uma classe a uma biblioteca de classes
- Abra a biblioteca de classes no Class Browser . Para obter mais informações sobre como abrir bibliotecas de classes, consulte Como: abrir bibliotecas de classes .
- Na lista de classes do Class Browser , selecione a biblioteca de classes para a qual deseja adicionar uma classe.
- No Class Browser , clique no botão New Class. A caixa de diálogo New Class abre para que você possa especificar informações para a nova classe.
- Siga as etapas para criar uma classe ou subclasse. Para obter mais informações, consulte Como: criar classes e subclasses .

Quando você termina de criar e salvar a classe, a classe aparece na biblioteca de classes exibida no Class Browser.

### Para adicionar uma subclasse a uma biblioteca de classes
- Abra a biblioteca de classes no Class Browser . Para obter mais informações sobre como abrir bibliotecas de classes, consulte Como: abrir bibliotecas de classes .
- Na lista de classes do Class Browser , selecione a classe da qual deseja criar uma subclasse.
- No Class Browser , clique no botão New Class. A caixa de diálogo New Class abre para que você possa especificar informações para a nova classe. A classe selecionada aparece por padrão na caixa Based On.
- Siga as etapas para criar uma classe ou subclasse. Para obter mais informações, consulte Como: criar classes e subclasses .

Quando você termina de criar e salvar a subclasse, a subclasse aparece na biblioteca de classes exibida no Class Browser.

### Para adicionar classes a bibliotecas de classes programaticamente
- Use o comando ADD CLASS.

Por exemplo, a seguinte linha de código adiciona a classe MyClass a MyClassLibrary:

```foxpro
ADD CLASS MyClass TO MyClassLibrary2
```

Para obter mais informações, consulte Comando ADD CLASS.
