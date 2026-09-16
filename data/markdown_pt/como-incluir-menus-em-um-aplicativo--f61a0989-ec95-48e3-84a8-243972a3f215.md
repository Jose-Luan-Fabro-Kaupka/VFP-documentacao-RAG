# Como: incluir menus em um aplicativo

Quando você cria um sistema de menus, pode incluí-lo em seu aplicativo.

### Para incluir um sistema de menus em seu aplicativo
- Adicione o arquivo .mnx ao seu projeto e então compile o aplicativo a partir do projeto. Para obter mais informações sobre compilar seu aplicativo, consulte Compilando um aplicativo .

Quando você cria e gera um menu de atalho, pode anexá-lo a um controle. Menus de atalho normalmente aparecem quando um usuário clica com o botão direito em um controle. Você pode anexar um menu de atalho a um controle específico inserindo uma pequena quantidade de código no evento right-click do controle.

### Para anexar menus de atalho a controles
- Selecione o controle ao qual deseja anexar o menu de atalho.
- Na janela Properties, escolha a guia Methods e selecione Right Click Event .
- Na janela de código, digite DO menu .MPR , onde menu é o nome do menu de atalho. Observação Certifique-se de usar a extensão .mpr ao referenciar menus de atalho.

### Anexando menus SDI a formulários

Quando você cria um menu SDI, pode anexá-lo a um formulário SDI. Além disso, você deve:
 - Definir a propriedade ShowWindow do formulário.
- Adicionar uma instrução DO ao evento Init do formulário.

### Para anexar um menu SDI a um formulário
- No Form Designer , defina a propriedade ShowWindow do formulário como 2 – As Top Level Form .
- No evento Init do formulário, chame o menu. Por exemplo, se seu menu se chama SDIMENU.MPR , adicione este código: DO SDIMENU.MPR WITH THIS,.T.
