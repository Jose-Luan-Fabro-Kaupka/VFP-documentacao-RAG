# Como: criar bancos de dados

Você pode usar um assistente para criar um banco de dados e adicionar tabelas, ou pode criar um contêiner de banco de dados vazio. Um assistente ajuda a criar um banco de dados usando suas respostas a uma série de perguntas. O assistente também fornece modelos para tabelas e exibições, índices, chaves primárias e relações que você pode escolher ou editar.

Quando você cria um banco de dados, é criado um arquivo de banco de dados (.dbc) com um arquivo de memorando de banco de dados (.dct) e um arquivo de índice de banco de dados (.dcx) associados.

### Para criar um banco de dados usando um assistente
- No menu File, clique em New.
- Na caixa de diálogo New, clique em Database e depois em Wizard.
- Siga as instruções nas telas do assistente.

Para obter mais informações, consulte Database Wizard.

Você também pode iniciar o assistente a partir de um projeto no Project Manager expandindo o nó Data, selecionando o nó Databases, clicando em New e depois em Database Wizard. Para obter mais informações, consulte Janela Project Manager.

### Para criar um contêiner de banco de dados vazio
- No menu File, clique em New.
- Na caixa de diálogo New, clique em Database e depois em New file.
- Na caixa de diálogo Create, navegue até o local em que deseja salvar o banco de dados, digite um nome para ele e clique em Save. O Database Designer será aberto e exibirá um banco de dados vazio.

Para obter mais informações, consulte Database Designer (Visual FoxPro).

### Para criar um banco de dados em um projeto
- Abra o projeto no Project Manager.
- No Project Manager, expanda o nó Data e clique no nó Databases.
- Clique em New e depois em New Database.

Para obter mais informações, consulte Janela Project Manager.

### Para criar um banco de dados programaticamente
- Use o comando CREATE DATABASE. O exemplo a seguir cria e abre exclusivamente um banco de dados chamado Sample: CREATE DATABASE Sample

Para obter mais informações, consulte Comando CREATE DATABASE.

> **Observação:** Usar o comando CREATE DATABASE não adiciona automaticamente o banco de dados a um projeto, mesmo quando o Project Manager está aberto. Para obter mais informações, consulte Como: adicionar bancos de dados a projetos.
