# Como: personalizar a aparência de aplicativos

Você pode alterar a aparência do aplicativo sem modificar seu código:
 - Altere o sistema de menus padrão. Crie e adicione menus e opções personalizados com o Menu Designer. Caso contrário, o ambiente de execução exibirá o menu padrão do Visual FoxPro.
- Altere o título padrão do aplicativo. Por padrão, ele é executado na janela principal e exibe "Microsoft Visual FoxPro" na barra de título.
- Altere o ícone padrão do aplicativo. Ao compilar, o ícone padrão aparece no Windows Explorer ou no menu Start. Você pode usar o ícone genérico fornecido ou seu próprio ícone.

### Para alterar o título do aplicativo
- No arquivo de configuração, inclua a instrução a seguir e substitua MyProgramTitle pelo título apropriado: TITLE = MyProgramTitle. Dica: para incluir uma função do Visual FoxPro, por exemplo um número de versão, inclua a linha a seguir para definir Caption da janela principal: COMMAND=_SCREEN.Caption="MyProgramTitle " + FunctionName()

Para obter mais informações, consulte Termos especiais para arquivos de configuração.

### Para alterar o ícone padrão do aplicativo
- Abra o projeto.
- No Project Manager, selecione o arquivo principal.
- No menu Project, clique em Project Info.
- Na caixa Project Information, clique na guia Project.
- Clique em Attach icon.
- Na caixa Open, selecione um arquivo de ícone (.ico).
- Clique em OK.

Para obter mais informações, consulte Janela Project Manager e Caixa de diálogo Project Information.
