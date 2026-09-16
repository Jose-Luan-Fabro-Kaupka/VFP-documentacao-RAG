# Como: exibir código herdado para objetos, eventos e métodos

Você pode visualizar código herdado de classes pai, se existir para objetos, eventos e métodos, facilitando decidir se deseja usar ou substituir o código herdado.

> **Observação:** Os recursos View Parent e View Inherited Code suportam apenas a visualização de código pai, não a edição. Para editar código de classe pai para uma subclasse, use o Class Browser. Para obter mais informações, consulte Como: visualizar código de definição de classe e Operating the Class Browser.

### Para visualizar código herdado usando a janela de código
- Execute uma das seguintes ações: No formulário, clique duas vezes no objeto desejado. - OU - Na lista de propriedades da janela Properties, clique duas vezes em um evento ou método. Uma janela de código abre para o objeto, evento ou método.
- Na janela de código, clique em View Parent Code para exibir a lista de todas as classes pai. Observação View Parent Code está disponível na janela de código apenas quando há pelo menos uma classe pai que contém código. Quando o código-fonte existe, as classes pai aparecem em negrito. Dica Você também pode clicar em View Parent Code na janela de código pressionando ALT+I.
- Selecione a classe pai. Uma janela de edição abre e exibe o código pai.

Se código herdado existir para um método ou evento, o nome da classe pai e as bibliotecas de classes das quais o método ou evento herda código aparecem na lista de propriedades da janela Properties da seguinte forma:

```foxpro
        Inherited cClassname ClassLibrary
```

O Visual FoxPro exibe apenas as classes pai do controle selecionado. Se uma lista de classes pai estiver disponível, as classes pai aparecem em ordem da classe pai mais imediata ou superior à mais próxima da classe base, percorrendo a árvore pai. A classe base não aparece.

Se código herdado da classe pai imediata existir e a classe pai for membro de uma classe de contêiner, o Visual FoxPro exibe a classe de contêiner seguida de um separador e, em seguida, as classes na árvore pai. Outras classes que percorrem a hierarquia de contêineres podem conter código, mas não são exibidas na lista.

Visualizar código herdado usando a lista de propriedades na janela Properties percorre a árvore pai ou de contêiner para alcançar a classe pai herdada.
