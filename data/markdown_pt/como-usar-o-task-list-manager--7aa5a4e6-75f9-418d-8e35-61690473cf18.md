# Como: usar o Task List Manager

Você pode acompanhar tarefas usando o Task List Manager, que armazena tarefas no arquivo de tabela FoxTask.dbf. Você pode criar os seguintes tipos de tarefas:
 - Shortcut Referencia uma linha específica de código que você pode querer editar ou visualizar depois.
- User-defined Especifica um item de tarefa ou informação que você pode querer acompanhar. Eles são adicionados manualmente.
- Other Uma tarefa personalizada. Você deve adicionar este tipo de tarefa programaticamente em seu aplicativo. Observação Certifique-se de definir o campo Type da tarefa personalizada como "O" no arquivo FoxTask.dbf, que é referenciado pela variável de sistema _FOXTASK. Para obter mais informações, consulte _FoxTask System Variable .

### Para abrir o Task List Manager
- No menu Tools, clique em Task List .

Para obter mais informações, consulte Task List Manager Window.

Você pode executar muitas ações no Task List Manager, como adicionar, editar, priorizar, definir status e excluir tarefas.

### Adicionando tarefas

Você pode adicionar tarefas shortcut e user-defined no Task List Manager.

### Para adicionar uma tarefa shortcut
- Abra o arquivo de programa no qual deseja criar o shortcut.
- Na janela de edição de código, selecione a linha de código que deseja criar como shortcut.
- No menu Edit, aponte para Bookmarks e clique em Toggle Task List Shortcut .

Você também pode adicionar um shortcut fazendo um dos seguintes após selecionar a linha de código:
 - Clique com o botão direito no código selecionado e clique em Add Task List Shortcut .
- Pressione ALT+F2 para adicionar ou remover o shortcut.
- Pressione e segure a tecla CTRL e depois clique duas vezes na Selection Margin do Editor .

Tarefas shortcut são indicadas por um ícone de seta na coluna de tipo de tarefa.

### Para adicionar uma tarefa user-defined
- Na janela Tasks, clique em Click here to add a new task na coluna Contents. Um cursor aparece na caixa de texto.
- Digite informações sobre a tarefa que deseja executar.
- Quando terminar, pressione RETURN ou clique fora da caixa de texto. A tarefa é adicionada ao final da lista para que você possa inserir informações adicionais.

Tarefas user-defined são indicadas por um ícone de pessoa/tarefa na coluna de tipo de tarefa.

### Editando tarefas

Você pode editar uma tarefa diretamente no Task List ou usando a caixa de diálogo Task Properties. A caixa de diálogo Task Properties contém as guias Task e Fields, que exibem informações para todos os campos disponíveis, mesmo se não estiverem mostrados na janela Tasks.

> **Observação:** Clicar duas vezes em uma tarefa shortcut na janela Tasks abre a janela de edição apropriada e move diretamente para esse shortcut.

### Para editar uma tarefa na caixa de diálogo Task Properties
- Na coluna de tipo de tarefa (terceira coluna da esquerda), clique duas vezes no ícone ao lado da tarefa.
- Na caixa de diálogo Task Properties, clique na guia Task.
- Edite os campos e configurações desejados.

Você também pode abrir a caixa de diálogo Task Properties clicando com o botão direito na tarefa e clicando em Open Task.

### Priorizando tarefas

Você pode definir e organizar prioridades para tarefas.

### Para definir uma prioridade para uma tarefa
- Na coluna de prioridade, indicada por um ponto de exclamação (!), clique na caixa da tarefa desejada
- Na lista, selecione uma prioridade.

Você pode organizar tarefas por prioridade clicando no cabeçalho da coluna de prioridade. Você também pode inserir uma data de vencimento para uma tarefa.

### Marcando tarefas

Você pode marcar tarefas para indicar seu status como lidas ou completas no Task List Manager.

Tarefas que ainda não foram lidas aparecem em negrito. Você pode marcar tarefas como lidas quando terminar de ler sobre a tarefa.

### Para marcar uma tarefa como lida
- Clique com o botão direito na tarefa e clique em Mark as Read . Quando uma tarefa é lida, ela não aparece mais em negrito.

Você também pode marcar uma tarefa como lida abrindo a caixa de diálogo Task Properties, clicando na guia Task e selecionando a caixa de seleção Read.

Você pode marcar tarefas como completas quando terminar a tarefa.

### Para marcar uma tarefa como completa
- Na coluna da lista de tarefas, ou segunda coluna da esquerda, selecione a caixa de seleção da tarefa que deseja completar. Quando uma tarefa está completa, ela aparece como texto tachado.

Você também pode marcar uma tarefa como completa clicando com o botão direito na tarefa e clicando em Mark as Complete ou abrindo a caixa de diálogo Task Properties, clicando na guia Task e selecionando a caixa de seleção Complete.

### Excluindo tarefas

Você pode excluir tarefas no Task List Manager.

> **Observação:** Tarefas shortcut são excluídas automaticamente quando você remove o shortcut na janela de edição.

### Para excluir uma tarefa
- Clique com o botão direito na tarefa e clique em Delete Task .

### Adicionando arquivos a tarefas user-defined

Tarefas shortcut têm um arquivo automaticamente associado a elas. Você pode adicionar associações de arquivo a tarefas user-defined ou other, embora não seja obrigatório.

### Para adicionar uma associação de arquivo
- No campo File Name da tarefa, digite o caminho completo e o nome do arquivo e qualquer informação adicional necessária, como linha ou método.

Você também pode adicionar uma associação de arquivo abrindo a caixa de diálogo Task Properties e inserindo o nome do arquivo no campo File Name.

### Abrindo arquivos para edição

Você pode abrir e editar arquivos associados a tarefas.

### Para abrir e editar um arquivo associado a uma tarefa
- Clique duas vezes na tarefa na janela Tasks.

Você também pode clicar com o botão direito em tarefas shortcut ou tarefas user-defined que tenham associações de arquivo e clicar em Open File.

### Editando campos personalizados

Você pode editar campos personalizados que existem no Task List Manager.

### Para editar campos personalizados
- Na coluna de tipo de tarefa (terceira coluna da esquerda), clique duas vezes no ícone ao lado da tarefa.
- Na caixa de diálogo Task Properties, clique na guia Fields. Uma lista de campos personalizados disponíveis aparece.

### Limpando e editando a tabela Task List

Você pode limpar a tabela Task List e editar a estrutura da tabela de colunas definidas pelo usuário.

### Para limpar a tabela Task List
- Clique com o botão direito na janela Tasks e clique em Options .
- Na caixa de diálogo Tasklist Options, clique em Clean Up FoxTask .

### Para editar a estrutura da tabela de colunas definidas pelo usuário
- Clique com o botão direito na janela Tasks e clique em Options .
- Na caixa de diálogo Tasklist Options, clique em Edit Structure .

Você também pode personalizar o Task List manager classificando ou filtrando tarefas e selecionando ou adicionando campos personalizados. Para obter mais informações, consulte Customizing the Task List Manager.
