# Como: copiar classes entre bibliotecas de classes

Você pode copiar classes entre bibliotecas de classes. Você pode copiar classes usando o Class Browser, o Project Manager quando as bibliotecas de classes fazem parte de projetos, embora não necessariamente do mesmo projeto, ou programaticamente.

### Para copiar uma classe entre bibliotecas de classes
- Abra a biblioteca de classes que contém a classe que você deseja copiar no Class Browser. Para obter mais informações sobre como abrir bibliotecas de classes, consulte How to: Open Class Libraries.
- Abra a biblioteca de classes de destino em outra instância do Class Browser.
- No Class Browser que contém a biblioteca de classes de origem, selecione a classe que você deseja copiar.
- Pressione e mantenha pressionada a tecla CTRL enquanto arrasta o ícone da classe acima da lista de classes para a biblioteca de classes de destino. Um sinal de mais (+) aparece acima do cursor quando você arrasta o ícone da classe para a biblioteca de classes de destino.

> **Dica:** Para mover uma classe de uma biblioteca de classes para outra, não pressione e mantenha pressionada a tecla CTRL ao arrastar o ícone da classe.

### Para copiar uma classe entre bibliotecas de classes em projetos
- Abra o projeto ou projetos que contêm as bibliotecas de classes.
- No Project Manager, selecione a guia Classes.
- Expanda a biblioteca de classes que contém a classe que você deseja copiar e a biblioteca de classes de destino.
- Arraste a classe para a biblioteca de destino. O ponteiro do mouse se transforma em um ícone de biblioteca de classes quando você o move sobre uma biblioteca de destino válida.

### Para copiar classes entre bibliotecas de classes programaticamente
- Use o comando ADD CLASS com a cláusula OF.

Por exemplo, a linha de código a seguir copia a classe MyClass de MyClassLibrary1 para MyClassLibrary2.

```foxpro
ADD CLASS MyClass OF MyClassLibrary1 TO MyClassLibrary2
```

Para obter mais informações, consulte ADD CLASS Command.
