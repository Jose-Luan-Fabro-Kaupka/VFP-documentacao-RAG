# Como: criar menus e submenus

Você pode criar menus personalizando o sistema de menus existente do Visual FoxPro ou desenvolvendo seu próprio sistema de menus. Para começar com o sistema de menus existente do Visual FoxPro, use o recurso Quick Menu.

### Para criar um sistema de menus com Quick Menu
- Na janela Project Manager, selecione a guia Other, selecione Menus e depois New.
- Selecione Menu. O Menu Designer é exibido.
- No menu Menu, escolha Quick Menu. O Menu Designer agora contém informações sobre os menus principais do Visual FoxPro.
- Personalize o sistema de menus adicionando ou alterando itens de menu. Por exemplo, insira um menu Customer antes do menu Help escolhendo o botão mover associado ao menu Help, escolhendo o botão Insert e digitando Customer na coluna Prompt. O resultado é semelhante a isto: Um sistema de menus personalizado Dica Arraste os botões mover para alterar a posição dos menus na barra de menus. Se você precisar de um menu Help, coloque-o como o último menu na barra de menus para que os usuários possam encontrá-lo rapidamente.
- No menu Menu, escolha Generate. O Visual FoxPro solicita que você salve o sistema de menus em um arquivo com extensão .mnx. Este arquivo é uma tabela que armazenará todas as informações sobre o sistema de menus. Depois de salvar o sistema de menus, o Visual FoxPro solicita um arquivo de saída com extensão .mpr. Este arquivo conterá o programa de menu gerado.

# Criando menus SDI

Menus SDI são menus que aparecem em janelas de interface de documento único (SDI). Para criar um menu SDI, você deve indicar que o menu será usado em um formulário SDI enquanto estiver criando o menu. Além disso, o processo de criação de um menu SDI é o mesmo que o de um menu normal.

### Para criar um menu SDI
- Enquanto o Menu and Shortcut Designers estiver aberto, escolha General Options no menu View e selecione Top-Level Form.

> **Observação:** Menus em formulários SDI (ShowWindow = 2) não são suportados se a propriedade HalfHeightCaption do formulário estiver definida como True (.T.).

# Criando submenus

Para cada item de menu, você pode criar um submenu contendo itens de menu adicionais.

### Para criar um submenu
- Na coluna Prompt, selecione o item de menu ao qual deseja adicionar um submenu.
- Na caixa Result, selecione Submenu. Um botão Create aparece à direita da lista. Se um submenu já existir, um botão Edit aparece em vez disso.
- Selecione Create ou Edit.
- Na coluna Prompt, digite os nomes dos novos itens de menu.

### Para adicionar menus programaticamente
- Use os comandos DEFINE PAD, DEFINE POPUP ou DEFINE BAR.

Embora você normalmente crie menus e itens de menu usando o Menu Designer, também pode criá-los usando comandos do Visual FoxPro. Por exemplo, você pode criar um menu usando DEFINE PAD Command, um submenu usando DEFINE POPUP Command e itens no submenu usando uma série de comandos DEFINE BAR Command. Você também pode usar DEFINE BAR Command para personalizar menus de formas como adicionar imagens, atribuir fontes e exibir mensagens ao usuário.
