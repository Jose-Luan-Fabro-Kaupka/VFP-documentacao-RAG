# Evento Activate (Visual FoxPro)

Ocorre quando um objeto Form, FormSet, Project ou Page se torna ativo, ou quando um objeto Toolbar é exibido.

```foxpro
PROCEDURE Object.Activate
```

# Observações

Aplica-se a: variável de sistema _SCREEN | objeto Form | objeto FormSet | objeto ProjectHook | objeto Page | objeto ToolBar

Os gatilhos deste evento dependem do tipo de objeto:
 - Form é ativado por uma ação do usuário, como clicar no formulário ou em um controle, ou quando seu método Show é chamado.
- FormSet é ativado quando um formulário do conjunto recebe foco ou quando Show é chamado.
- ProjectHook é ativado por ação do usuário, como clicar na janela Project, ou por um comando como ACTIVATE WINDOW project.
- Page é ativado por ação do usuário, como clicar em sua guia ou em um controle nela contido, ou quando ActivePage do quadro de página é definido como o número da página.
- ToolBar é ativado quando seu método Show é chamado.

Ao usar Show para um conjunto de formulários, todos os formulários com Visible definida como True (.T.) são exibidos. Activate é disparado primeiro para o conjunto, depois para o formulário e, por fim, para a página.
