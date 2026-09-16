# Tratamento de erros de classes e objetos

Você pode tratar erros que ocorrem em objetos em tempo de execução adicionando código de tratamento de erros ao evento Error de um objeto ou definição de classe. Se você quiser que um objeto tenha seu próprio comportamento de tratamento de erros, adicione código de tratamento de erros ao evento Error do objeto. O comportamento de tratamento de erros que você especificar se aplica apenas a esse objeto específico.

Se você quiser que todos os objetos baseados em uma classe específica usem o mesmo comportamento de tratamento de erros, adicione código do evento Error à definição da classe, por exemplo, para uma classe personalizada ou subclasse. Todos os objetos instanciados da classe contêm o mesmo comportamento de tratamento de erros. Se a classe ou subclasse não contiver código do evento Error, ela herda o comportamento de tratamento de erros da classe pai. Se o código do evento Error não existir na classe pai, o Visual FoxPro pesquisa código do evento Error em outra classe na hierarquia de classes. Você também pode usar o comando NODEFAULT e a função DODEFAULT( ) para substituir ou chamar código da classe pai. Para obter mais informações, consulte Overriding and Calling Parent Class Code.

Se e quando um erro ocorrer no objeto em tempo de execução, o Visual FoxPro pesquisa código do evento Error no evento Error do objeto, no evento Error da classe base ou na hierarquia de classes desse objeto, e executa esse código, se existir. Outros manipuladores de erro podem afetar como o Visual FoxPro trata erros. Para obter mais informações, consulte Error Handler Priority.

# Tratamento de erros para objetos em containers

Para objetos membro instanciados dentro de outro objeto ou container, por exemplo, controles em um formulário, você pode especificar o tratamento de erros para cada objeto membro adicionando código do evento Error para cada objeto membro. No entanto, se o código do evento Error não existir para o objeto membro, ele não herda automaticamente o código do evento Error do objeto container. Se você quiser que o evento Error do objeto container trate erros para seus objetos membro, pode passar informações de erro do evento Error do objeto membro para o evento Error do container usando o seguinte código no evento Error do objeto membro:

```foxpro
LPARAMETERS nError, cMethod, nLine
THIS.Parent.Error(nError, cMethod, nLine)
```

Você pode adicionar código no evento Error do objeto container para processar as informações de erro passadas pelos parâmetros especificados neste código.

Por exemplo, a classe Vcr na biblioteca de classes de exemplo do Visual FoxPro, Buttons.vcx, localizada no diretório Visual FoxPro ...\Samples\Classes, é baseada na classe Container do Visual FoxPro. O container possui quatro botões de comando que navegam em uma tabela movendo o ponteiro de registro.

No entanto, quando um usuário clica em um botão quando uma tabela não está aberta, um erro pode ocorrer. O Visual FoxPro tenta gravar valores em buffer em uma tabela quando o ponteiro de registro se move; portanto, se o buffer de linha otimista estiver habilitado e outro usuário alterou um valor no registro em buffer, outro erro também pode ocorrer.

Esses erros podem ocorrer quando o usuário escolhe qualquer botão; portanto, você não precisa escrever quatro rotinas de tratamento de erros separadas para cada botão. Em vez disso, o evento Error de cada botão de comando contém código para passar informações de erro para uma única rotina de tratamento de erros no evento Error da classe Vcr.

Você também pode incluir outros manipuladores de erro, como os comandos TRY...CATCH...FINALLY e ON ERROR, em definições de classe e objetos. Para obter mais informações sobre a ordem e a prioridade em que os manipuladores de erro operam, consulte Error Handler Priority.
