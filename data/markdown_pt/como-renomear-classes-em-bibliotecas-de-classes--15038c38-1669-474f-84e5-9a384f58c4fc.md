# Como: renomear classes em bibliotecas de classes

Você pode renomear classes em bibliotecas de classes usando o Class Browser, o Project Manager quando a biblioteca fizer parte de um projeto, ou programaticamente.

> **Cuidado:** Ao renomear uma classe, formulários que a contêm e subclasses em outras bibliotecas continuam fazendo referência ao nome original e deixam de funcionar corretamente.

> **Dica:** Se você renomear uma classe com o Class Browser enquanto todas as subclasses e formulários associados estiverem abertos nele, o novo nome será referenciado automaticamente em todos os itens afetados.

### Para renomear uma classe em uma biblioteca de classes
- Abra a biblioteca no Class Browser. Para obter mais informações, consulte Como: abrir bibliotecas de classes.
- Na lista de classes do Class Browser, selecione a classe a renomear e clique no botão Rename.
- Na caixa de diálogo Rename, digite o novo nome e clique em Rename. A lista do Class Browser exibirá a classe renomeada.

Para obter mais informações, consulte Janela Class Browser.

### Para renomear uma classe em um projeto
- Abra o projeto que contém a biblioteca com a classe a renomear.
- No Project Manager, selecione a guia Classes.
- Expanda a biblioteca de classes que contém a classe.
- Clique com o botão direito na biblioteca e escolha Rename.
- Na caixa To: da caixa de diálogo Rename File, digite um novo nome para a classe.
- Clique em OK.

### Para renomear classes programaticamente
- Use o comando RENAME CLASS.

Por exemplo, a linha a seguir altera o nome da classe MyClass na biblioteca MyClassLibrary para YourClass:

```foxpro
RENAME CLASS MyClass OF MyClassLibrary TO YourClass
```

Para obter mais informações, consulte Comando RENAME CLASS.
