# Como: implementar a ajuda "What's This?"

A ajuda "What's This?" é semelhante à ajuda sensível ao contexto, pois fornece ajuda relacionada a um objeto ou controle específico em um formulário que tem foco. A ajuda "What's This?" é útil para fornecer descrições ou definições breves no estilo de dicas para controles específicos. Você pode implementar a ajuda "What's This?" adicionando o botão "What's This?" (?) aos formulários. Os usuários acessam a ajuda "What's This?" clicando no botão "What's This?" (?) na barra de título do formulário, o que altera o ponteiro do mouse para um ponto de interrogação e, em seguida, clicando nos objetos no formulário.

Quando você configura sua aplicação para usar arquivos WinHelp, clicar no botão "What's This?" abre uma janela pop-up que exibe texto de ajuda, que desaparece quando você clica em outro lugar na tela. Quando você configura sua aplicação para usar arquivos HTML Help, clicar no botão "What's This?" abre o arquivo de ajuda e exibe o tópico de ajuda no visualizador HTML Help.

> **Dica:** Mantenha os tópicos de ajuda "What's This?" breves e concisos para que a janela pop-up não obscureça o recurso que descreve.

### Para implementar a ajuda "What's This?"
- Abra o formulário desejado no Form Designer.
- No menu Window, clique em Properties Window.
- Na janela Properties, defina a propriedade WhatsThisHelp do formulário como True (.T.).
- Para exibir um botão de ajuda "What's This?" (?) na barra de título do formulário, defina a propriedade WhatsThisButton do formulário como True (.T.). Defina a propriedade MaxButton do formulário como False (.F.) e a propriedade MinButton como False (.F.).
- Para associar um tópico de ajuda ao formulário, defina a propriedade WhatsThisHelpID do formulário para um número de ID correspondente ao tópico apropriado no arquivo de ajuda.
- Para associar um tópico de ajuda a um controle específico no formulário, selecione o controle e defina sua propriedade WhatsThisHelpID para um número de ID correspondente ao tópico apropriado no arquivo de ajuda.

Você também pode usar o método WhatsThisMode para exibir o ponto de interrogação da ajuda "What's This?" para que os usuários possam clicar em objetos para exibir tópicos de ajuda "What's This?".

Para obter mais informações, consulte WhatsThisHelp Property, WhatsThisButton Property, WhatsThisHelpID Property e WhatsThisMode Method.
