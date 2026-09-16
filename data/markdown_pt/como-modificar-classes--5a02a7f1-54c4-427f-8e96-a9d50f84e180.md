# Como: modificar classes

Depois de criar uma classe, você pode fazer alterações nela. As alterações que você faz na classe se propagam para todas as subclasses e objetos baseados na classe. Por exemplo, suponha que você adicione um aprimoramento a uma classe ou corrija um bug na classe. Todas as subclasses e objetos baseados na classe herdam a alteração.

> **Cuidado:** Se a classe estiver sendo usada em qualquer outro componente da aplicação, não altere a propriedade Name da classe. Caso contrário, o Visual FoxPro não conseguirá localizar a classe quando ela for necessária.

Você pode modificar classes abrindo o Class Designer pela IDE do Visual FoxPro, pelo Class Browser, pelo Project Manager se a classe faz parte de um projeto ou programaticamente.

### Para modificar uma classe
- No menu Arquivo, escolha Abrir.
- Na caixa Arquivos do tipo na caixa de diálogo Abrir, selecione a biblioteca de classes que deseja abrir e clique em OK. Uma caixa de diálogo Abrir aparece para você selecionar uma classe da biblioteca de classes que você abriu.
- Na lista Nome da classe da caixa de diálogo Abrir, selecione uma classe e clique em Abrir. A classe selecionada abre no Class Designer. -OU-
- No Class Browser, abra a biblioteca de classes desejada. Para obter informações sobre como abrir bibliotecas de classes, consulte Como: abrir bibliotecas de classes.
- Na lista de classes, clique com o botão direito na classe e escolha Modificar. A classe selecionada abre no Class Designer.

### Para modificar uma classe em um projeto
- Abra o projeto que contém a classe desejada.
- No Project Manager, selecione a classe desejada e clique em Modificar. A classe selecionada abre no Class Designer.

Você também pode modificar classes em arquivos de biblioteca de classes visual (.vcx) usando o comando MODIFY CLASS para abrir o Class Designer.

Por exemplo, digitar a linha a seguir na janela Command abre a classe MyClass, que está armazenada na biblioteca de classes MyClassLibrary, no Class Designer para que você possa modificá-la:

```foxpro
MODIFY CLASS MyClass OF MyClassLibrary
```

Para obter mais informações, consulte Comando MODIFY CLASS.
