# Como: executar tarefas com comandos

Quando um menu ou item de menu é selecionado, ele executa uma tarefa, como exibir um formulário, uma toolbar ou outro sistema de menu. Para executar uma tarefa, um menu ou item de menu deve executar um comando do Visual FoxPro. O comando pode estar contido em uma linha ou pode ser uma chamada de procedure.

> **Dica:** Se você espera usar um conjunto de comandos em vários lugares, escreva uma procedure. A procedure deve ser explicitamente nomeada e escrita no código de limpeza do menu, ou em algum lugar onde possa ser referenciada por qualquer menu ou objeto. Para mais informações, consulte Como: executar tarefas com procedures .

Um comando pode ser qualquer comando válido do Visual FoxPro, incluindo uma chamada a um programa que existe em seu caminho ou uma procedure definida na opção Cleanup da caixa de diálogo General Options. Para mais informações, consulte Como: personalizar um sistema de menu.

### Para atribuir um comando a um menu ou item de menu
- Na coluna Prompt, selecione o título de menu ou item de menu apropriado.
- Na caixa Result, selecione Command .
- Na caixa à direita da caixa Result, digite o comando apropriado:

Se o comando chama uma procedure no código de limpeza do menu, use o comando DO Command com a seguinte sintaxe:

```foxpro
DO procname IN menuname
```

Nesta sintaxe, menuname especifica o local da procedure. Este é o nome do arquivo de menu e deve ter a extensão .mpr. Se você não especificar o local em menuname, deve especificá-lo com SET PROCEDURE Command TO menuname.mpr, se a procedure estiver no código de limpeza do menu.

# Exibindo formulários e caixas de diálogo

De um menu ou item de menu, você pode exibir um formulário ou caixa de diálogo compilado chamando-o com um comando ou procedure.

### Para exibir um formulário ou caixa de diálogo
- Use o comando DO FORM com o nome do formulário.

Por exemplo, para exibir um formulário chamado "Orders," use o seguinte comando:

```foxpro
DO FORM Orders
```

> **Dica:** Quando você cria um menu ou item de menu que exibe um formulário ou caixa de diálogo, coloque três pontos no final do prompt para indicar que mais entrada do usuário é necessária.

Se você criar uma toolbar personalizada para uma aplicação, pode exibi-la chamando-a de um menu ou item de menu. Para detalhes, consulte Creating Custom Toolbars.
