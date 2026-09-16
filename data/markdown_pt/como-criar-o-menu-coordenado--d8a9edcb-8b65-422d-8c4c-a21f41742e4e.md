# Como: criar o menu coordenado

Quando você coordena um menu com uma barra de ferramentas, os itens de menu realizam as mesmas tarefas que os botões associados da barra de ferramentas, e os itens de menu são desabilitados automaticamente quando o botão associado da barra de ferramentas é desabilitado.

### Para criar um menu coordenado com uma barra de ferramentas
- Nos Designers de menu e atalho , crie um submenu com um prompt descritivo para cada botão na barra de ferramentas.
- Na coluna de resultado para cada item de submenu, escolha Comando .
- Para cada item de submenu, chame o código associado ao evento Click do botão de comando apropriado da barra de ferramentas. Por exemplo, se o nome do botão na barra de ferramentas é cmdA , adicione a seguinte linha de código na caixa de edição para o comando do item de submenu: Formset.toolbar.cmdA.Click
- Clique no botão na coluna Opções para abrir a caixa de diálogo Opções do prompt e escolha Ignorar para .
- Na Caixa de diálogo Construtor de expressões , insira uma expressão que indica que a opção de menu deve ser ignorada quando o botão de comando da barra de ferramentas não estiver habilitado. Por exemplo, se o nome do botão na barra de ferramentas é cmdA , insira a seguinte expressão na caixa Ignorar para: NOT formset.toolbar.cmdA.Enabled
- Gere o menu.
- Adicione o menu ao conjunto de formulários com a barra de ferramentas e execute o conjunto de formulários.

Quando o usuário abre o menu, o Visual FoxPro avalia a condição Ignorar para, desabilitando o item de menu se o botão de comando associado da barra de ferramentas estiver desabilitado. Quando o usuário escolhe um item no menu, o código no evento Click do botão de comando associado da barra de ferramentas é executado.
