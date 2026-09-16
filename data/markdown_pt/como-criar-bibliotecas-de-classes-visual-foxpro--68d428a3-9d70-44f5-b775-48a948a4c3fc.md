# Como: criar bibliotecas de classes (Visual FoxPro)

Você pode criar bibliotecas de classes ao criar classes usando o IDE do Visual FoxPro ou bibliotecas de classes vazias programaticamente.

O Visual FoxPro armazena classes que você cria usando o Class Designer em arquivos de biblioteca de classes visual (.vcx). Essas classes incluem classes visuais e não visuais. Você também pode optar por armazenar definições de classe em arquivos de programa (.prg) ao usar o comando DEFINE CLASS para criar classes.

### Para criar uma biblioteca de classes ao criar uma classe
- Crie uma classe usando o IDE do Visual FoxPro.
- Na caixa Store In da caixa de diálogo New Class, digite o nome da biblioteca de classes.

Para obter mais informações sobre a criação de classes, consulte Como: criar classes e subclasses.

### Para criar bibliotecas de classes programaticamente
- Use o comando CREATE CLASSLIB para criar uma biblioteca de classes vazia. -OU-
- Inclua a cláusula OF no comando CREATE CLASS ao criar uma classe.

Por exemplo, a linha de código a seguir usa o comando CREATE CLASSLIB para criar uma biblioteca de classes vazia chamada MyClassLibrary:

```foxpro
CREATE CLASSLIB MyClassLibrary
```

A linha de código a seguir inclui a cláusula OF no comando CREATE CLASS para especificar o nome da biblioteca de classes que armazenará a classe MyClass, que é baseada na classe Form.

```foxpro
CREATE CLASS MyClass OF MyClassLibrary AS Form
```

Para obter mais informações, consulte Comando CREATE CLASSLIB.
