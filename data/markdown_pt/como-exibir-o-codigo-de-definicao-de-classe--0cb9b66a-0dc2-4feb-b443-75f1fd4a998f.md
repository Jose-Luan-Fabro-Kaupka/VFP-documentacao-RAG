# Como: exibir o código de definição de classe

Você pode exibir o código das definições de classe, de parâmetros específicos ou da classe pai para métodos definidos pelo usuário usando o Class Browser. Também é possível salvar o código da definição de classe em outra biblioteca de classes.

### Para exibir o código de definição de classe
- No Class Browser, abra a biblioteca de classes desejada. Para obter informações sobre como abrir o Class Browser, consulte Como: executar o Class Browser.
- Na lista de classes, selecione a classe desejada.
- No Class Browser, clique no botão View Class Code.

O Visual FoxPro exibe o código de definição da classe em um arquivo de programa (.prg) somente leitura. A definição de classe exibida inclui todas as configurações de propriedades e o código de métodos e eventos.

> **Observação:** O código é exibido somente para visualização. Em muitos casos, você pode salvá-lo em um programa e executá-lo diretamente; contudo, código com contêineres aninhados gera erros. Para exibir informações da biblioteca de tipos, use a janela Object Browser.

Você pode usar uma seleção limitada de comandos de edição, como Find, Copy e Select All, no menu Edit.

Se houver código da classe pai disponível para um método definido pelo usuário, você poderá exibi-lo.

### Para exibir o código da classe pai de um método definido pelo usuário
- No Class Browser, clique duas vezes em uma classe ou membro de classe. A classe ou o membro será aberto no Class Designer ou no Form Designer. Se nenhuma janela de código estiver aberta, escolha Code no menu View.
- Na barra de ferramentas do Visual FoxPro, clique no botão Edit ParentClass Method.
