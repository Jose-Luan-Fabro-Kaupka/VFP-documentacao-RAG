# Como: definir ações da barra de ferramentas

Depois de criar uma barra de ferramentas, você deve definir as ações associadas à barra de ferramentas e seus objetos. Por exemplo, você deve definir o que acontece quando o usuário clica na barra de ferramentas ou em um de seus botões.

### Para definir uma ação da barra de ferramentas
- Selecione o objeto para o qual deseja definir uma ação: a barra de ferramentas ou um de seus botões.
- Na Properties Window (Visual FoxPro), escolha a guia Methods.
- Edite o evento apropriado.
- Adicione o código que especifica a ação.

Além disso, você pode definir propriedades e métodos da barra de ferramentas e seus objetos.

# Coordenando menus e barras de ferramentas personalizadas

Se você criar uma barra de ferramentas, deve sincronizar os comandos de menu com seus botões correspondentes na barra de ferramentas. Por exemplo, se você habilitar um botão da barra de ferramentas, deve habilitar o comando de menu correspondente.

Você deve projetar e criar seu aplicativo para:
 - Executar as mesmas ações quando o usuário escolhe botões associados da barra de ferramentas e itens de menu.
- Coordenar a habilitação e desabilitação de botões associados da barra de ferramentas e itens de menu.

### Para coordenar itens de menu e botões da barra de ferramentas
- Crie uma barra de ferramentas definindo uma classe de barra de ferramentas, adicione botões de comando e inclua o código operacional nos métodos associados ao evento Click dos botões de comando.
- Crie o menu coordenado.
- Adicione a barra de ferramentas e o menu coordenados a um form set.
