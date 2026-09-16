# Como: Atribuir Teclas de Acesso e Atalhos de Teclado

Ao criar um sistema de menus, você deve considerar a facilidade de acesso ao sistema e deve atribuir tarefas ao sistema. Você deve dar a menus e itens de menu tarefas a executar, como exibir formulários, barras de ferramentas e outros sistemas de menus. Você deve definir teclas de acesso para permitir a entrada no sistema de menus. Você também pode adicionar atalhos de teclado e habilitar ou desabilitar itens de menu para mais controle.

# Atribuindo Teclas de Acesso

Menus bem projetados possuem teclas de acesso para acesso rápido por teclado à funcionalidade do menu. A tecla de acesso é representada pela letra sublinhada no título do menu ou item de menu. Por exemplo, o menu File do Visual FoxPro usa "F" como sua tecla de acesso.

Se você não atribuir uma tecla de acesso a um título de menu ou item de menu, o Visual FoxPro atribui automaticamente a primeira letra como tecla de acesso. Por exemplo, o menu Customer criado anteriormente não tinha uma tecla de acesso definida. Portanto, o Visual FoxPro atribuiu a primeira letra (C) como tecla de acesso.

### Para especificar a tecla de acesso para um menu ou item de menu
- Digite \< à esquerda da letra que deseja como tecla de acesso. Por exemplo, para definir a tecla de acesso como "u" no título do menu Customer, substitua Customer por C\<ustomer na coluna Prompt. Observação Se uma tecla de acesso para seu sistema de menus não funcionar, procure teclas de acesso duplicadas.

# Atribuindo Atalhos de Teclado

Além de atribuir teclas de acesso, você pode especificar atalhos de teclado para menus ou itens de menu. Assim como as teclas de acesso, os atalhos de teclado permitem escolher um menu ou item de menu mantendo pressionada uma tecla enquanto pressiona outra. A diferença entre teclas de acesso e atalhos de teclado é que você pode usar um atalho de teclado para escolher um item de menu sem primeiro exibir seu menu.

Os atalhos de teclado para itens de menu do Visual FoxPro são combinações da tecla CTRL ou ALT e outra tecla. Por exemplo, você pode criar um novo arquivo no Visual FoxPro pressionando CTRL+N.

### Para especificar um atalho de teclado para um menu ou item de menu
- Na coluna Prompt, selecione o título ou item de menu apropriado.
- Escolha o botão na coluna Options para exibir a caixa de diálogo Prompt Options.
- Na caixa Key Label, pressione uma combinação de teclas para criar um atalho de teclado. Se um item de menu não possui um atalho de teclado, o Visual FoxPro exibe "(press the key)" na caixa Key Label.
- Na caixa Key Text, adicione o texto que deseja exibir ao lado do item de menu. Por padrão, o Visual FoxPro repete o atalho de teclado da caixa Key Label na caixa Key Text. No entanto, você pode alterar o texto na caixa Key Text se desejar que seu aplicativo exiba texto diferente. Por exemplo, se tanto Key Label quanto Key Text fossem CTRL+R, você poderia alterar o valor Key Text para ^R. Observação CTRL+J é um atalho de teclado inválido porque é usado para fechar determinadas caixas de diálogo no Visual FoxPro.
