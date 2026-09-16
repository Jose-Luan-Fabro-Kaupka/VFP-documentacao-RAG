# Como: remover classes de bibliotecas de classes

Você pode remover classes de bibliotecas de classes.

> **Cuidado:** Quando você remove uma classe de uma biblioteca de classes, você exclui a classe.

Você pode remover classes de bibliotecas de classes usando o Class Browser, o Project Manager quando a biblioteca de classes faz parte de um projeto ou programaticamente.

### Para remover uma classe de uma biblioteca de classes
- Abra a biblioteca de classes no Class Browser. Para obter mais informações sobre como abrir bibliotecas de classes, consulte Como: abrir bibliotecas de classes.
- Na lista de classes do Class Browser, clique com o botão direito na classe que deseja remover e escolha Remove.

### Para remover uma classe de um projeto
- Abra o projeto que contém a biblioteca de classes.
- No Project Manager, escolha a guia Classes.
- Expanda a biblioteca de classes que contém a classe que deseja remover.
- Selecione a classe que deseja remover e escolha Remove.

### Para remover classes de bibliotecas de classes programaticamente
- Use o comando REMOVE CLASS.

Por exemplo, a linha de código a seguir remove uma classe chamada MyClass da biblioteca de classes chamada MyClassLibrary:

```foxpro
REMOVE CLASS MyClass OF MyClassLibrary.vcx
```

Para obter mais informações, consulte o comando REMOVE CLASS.
