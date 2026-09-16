# Como: personalizar um sistema de menu

Depois de criar um sistema de menu básico, você pode personalizá-lo. Por exemplo, você pode criar mensagens da barra de status, definir localizações de menu ou definir procedimentos padrão.

# Exibindo mensagens da barra de status

Quando um menu ou item de menu é selecionado, você pode exibir uma mensagem da barra de status descrevendo a escolha. Essa mensagem ajuda o usuário ao adicionar informações sobre a escolha do menu.

### Para exibir uma mensagem quando um menu ou item de menu é selecionado
- Na coluna Prompt, selecione o título de menu ou item de menu apropriado.
- Escolha o botão na coluna Options para exibir a caixa de diálogo Prompt Options.
- Selecione Message . A caixa de diálogo Expression Builder aparece.
- Na caixa Message, digite a mensagem apropriada. Dica Coloque cadeias de caracteres entre aspas.

# Definindo a localização dos títulos de menu

Você pode personalizar a localização dos títulos de menu definidos pelo usuário em seus aplicativos. Você pode personalizar a localização em relação ao sistema de menu ativo escolhendo opções na caixa de diálogo General Options. Além disso, você pode especificar a localização dos títulos de menu quando o usuário edita um objeto visualmente.

### Para especificar uma localização relativa para títulos de menu definidos pelo usuário
- No menu View, escolha General Options .
- Escolha a opção Location apropriada: Replace , Append , Before ou After .

O Visual FoxPro realoca todos os títulos de menu que você definiu. Se desejar realocar alguns, mas não todos, arraste os botões mover ao lado dos títulos de menu apropriados nos Designers de Menu e Atalho.

Além disso, você pode especificar a localização dos títulos de menu quando o usuário edita um objeto em seu aplicativo. Se você incluir um objeto e o usuário ativá-lo, seus títulos de menu não aparecerão na barra de menu resultante, a menos que você indique que deseja que eles apareçam lá.

### Para controlar a localização do título de menu durante a edição visual de objetos
- Na coluna Prompt, selecione o título de menu apropriado.
- Escolha o botão na coluna Options para exibir a caixa de diálogo Prompt Options.
- Marque a caixa de seleção Negotiate.
- Escolha um dos seguintes botões de opção: None não coloca o título de menu na barra de menu. Escolher None é o mesmo que não escolher nenhuma opção. Left coloca o título de menu no grupo esquerdo de títulos de menu na barra de menu. Middle coloca o título de menu no grupo central de títulos de menu na barra de menu. Right coloca o título de menu no grupo direito de títulos de menu na barra de menu.

Se você não escolher Left, Middle ou Right, o título de menu não aparecerá na barra de menu quando o usuário editar um objeto. Para obter mais informações sobre edição visual de objetos, consulte Compartilhamento de informações e adição de OLE.

# Salvando e restaurando menus

Você pode salvar e restaurar menus na pilha empurrando e desempilhando-os, o que pode ser útil quando deseja remover um menu temporariamente, substituí-lo por outro e depois restaurar o original. O número de menus que você salva na memória é limitado apenas pela quantidade de memória disponível.

> **Dica:** Verifique a memória disponível com a função SYS(1016). Por exemplo, para verificar quanta memória seu sistema de menu usa, chame SYS(1016), empurre o menu na pilha e chame SYS(1016) novamente.

### Para salvar ou restaurar menus
- Use os comandos PUSH MENU ou POP MENU.

# Criando um procedimento padrão para um sistema de menu

Você pode criar um procedimento global que se aplica a todo o seu sistema de menu. Esse procedimento é executado sempre que um menu sem procedimento atribuído é escolhido.

Por exemplo, suponha que você esteja desenvolvendo um aplicativo para o qual alguns menus ainda não têm submenus, procedimentos e assim por diante. Para esses menus, você pode criar um stub de código que é executado quando os menus são escolhidos. Por exemplo, você poderia criar um procedimento geral que inclua esta função:

```foxpro
MESSAGEBOX("Feature not available")
```

### Para criar um procedimento padrão
- Abra o sistema de menu que você está criando.
- No menu View, escolha General Options .
- Atribua o procedimento fazendo uma das seguintes opções: Escreva ou chame um procedimento na caixa Procedure. -OU- Selecione Edit e depois OK para abrir uma janela de edição separada e escrever ou chamar um procedimento.

# Configurando o menu do sistema

Você pode manipular menus que usam o sistema de menu do Visual FoxPro. Você pode desabilitar seus menus, adicionar e remover itens de seus menus, restaurar os menus padrão do Visual FoxPro e controlar o acesso aos seus menus durante a execução do programa.

### Para manipular menus
- Use o Comando SET SYSMENU .
