# Como: criar views locais

Views locais usam sintaxe SQL do Visual FoxPro para selecionar informações de tabelas ou views armazenadas localmente em seu computador. Você pode criar views locais das seguintes maneiras:
 - Usando o Local View Wizard. Um wizard é a maneira mais fácil de começar a criar uma view. Você pode selecionar campos de tabelas e views e filtrar e classificar os registros em sua view. Para obter mais informações, consulte Criando views locais usando um wizard.
- Usando o View Designer. O View Designer permite selecionar campos de tabelas ou views, especificar critérios para recuperar dados e condições de junção, e filtrar, classificar e agrupar registros para criar views ou personalizar views existentes. Para obter mais informações, consulte Criando views locais usando o View Designer.
- Criando views programaticamente. O comando CREATE SQL VIEW permite usar instruções SQL SELECT para criar views programaticamente. Para obter mais informações, consulte Criando views locais programaticamente.

Independentemente do método usado, o processo básico para criar uma view é geralmente o mesmo. Para obter mais informações, consulte Criação de view.

> **Observação:** Quando você cria ou usa uma view do Project Manager, o Project Manager abre o banco de dados automaticamente. No entanto, se você posteriormente usar uma view fora do projeto, deve abrir o banco de dados ou garantir que o banco de dados esteja no escopo antes de poder usar a view.

# Criando views locais usando um wizard

Você pode criar views locais facilmente usando um wizard. O wizard ajuda a selecionar tabelas ou views e cria uma consulta baseada em suas respostas a uma série de perguntas.

> **Observação:** As tabelas ou views que você deseja usar devem fazer parte de um projeto ou banco de dados antes de poder usar o Local View Wizard para criar uma view. Para obter mais informações, consulte Trabalhando com projetos e Desenvolvendo bancos de dados.

### Para iniciar o Local View Wizard
- Execute uma das seguintes opções: Abra um banco de dados no Database Designer. -OU- Abra o projeto de sua aplicação no Project Manager e clique em um banco de dados ou tabela.
- No menu Tools, aponte para Wizards e clique em All Wizards.
- Na caixa de diálogo Wizard Selection, clique em Local View Wizard e depois em OK.
- Siga as instruções nas telas do wizard.

Para obter mais informações, consulte Local View Wizard.

# Criando views locais usando o View Designer

Você pode usar o View Designer para criar views e especificar opções adicionais ou personalizar views existentes.

> **Observação:** As tabelas ou views que você deseja usar devem fazer parte de um projeto ou banco de dados antes de poder usar o View Designer para criar uma view. Para obter mais informações, consulte Trabalhando com projetos e Desenvolvendo bancos de dados.

### Para iniciar o View Designer
- Execute uma das seguintes opções: Abra um banco de dados no Database Designer. -OU- Abra o projeto de sua aplicação no Project Manager e clique em um banco de dados.
- No menu File, clique em New.
- Na caixa de diálogo New, clique em View e depois em New File. A caixa de diálogo Add Table or View é exibida.
- Na área Select da caixa de diálogo Add Table or View, clique em Tables para exibir tabelas disponíveis ou Views para exibir views disponíveis.
- Clique nas tabelas ou views que deseja usar e depois em Add. Dica Quando você adiciona mais de uma tabela ou view à sua view, a caixa de diálogo Join Condition é exibida. Você pode modificar o escopo dos registros resultantes especificando uma condição de junção para cada tabela ou view adicional. Dica Quando você seleciona a mesma tabela ou view mais de uma vez, o Visual FoxPro usa um alias gerado automaticamente para a tabela ou view. No entanto, você pode especificar um alias para cada tabela ou view selecionada digitando-o na caixa Alias na caixa de diálogo Add Table or View. As tabelas ou views selecionadas aparecem no View Designer e no Database Designer.
- Quando terminar, clique em Close.

Para obter mais informações sobre especificação de condições de junção, consulte Como: controlar seleção de registros com junções, Condições de junção para tabelas, consultas e views e Caixa de diálogo Join Condition.

Depois de selecionar tabelas ou views, você precisa selecionar os campos que contêm os dados que deseja recuperar para sua view. Para obter mais informações, consulte Como: selecionar campos para views.

# Criando views locais programaticamente

Você pode criar views locais programaticamente abrindo o View Designer ou especificando uma instrução SQL SELECT.

### Para criar uma view local programaticamente
- Abra o banco de dados ou projeto que contém as tabelas ou views que deseja selecionar.
- Escolha uma das seguintes opções: Para selecionar tabelas ou views e abrir o View Designer, use o comando CREATE SQL VIEW apenas com o nome da view que deseja criar. -OU- Para criar uma view local sem abrir o View Designer, use o comando CREATE SQL VIEW e a cláusula AS para especificar instruções SQL SELECT. Observação Para corresponder registros relacionados entre as tabelas, você deve especificar uma condição de junção na cláusula FROM ou WHERE da instrução SQL usada no comando CREATE SQL VIEW. Se existirem relações persistentes entre as tabelas, elas são usadas automaticamente como condições de junção. As tabelas ou views selecionadas aparecem no View Designer e no Database Designer. Pode ser necessário fechar e reabrir os designers para atualizá-los.

Para obter mais informações, consulte Comando CREATE SQL VIEW.
