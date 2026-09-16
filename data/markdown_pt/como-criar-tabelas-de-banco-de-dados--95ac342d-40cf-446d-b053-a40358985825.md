# Como: criar tabelas de banco de dados

Você pode usar um assistente para ajudá-lo a criar uma tabela de banco de dados ou pode criar uma tabela de banco de dados vazia. Um assistente ajuda você a criar uma tabela usando suas respostas a uma série de perguntas.

> **Observação:** Quando você cria uma tabela de banco de dados com um banco de dados aberto, a tabela de banco de dados é associada automaticamente ao banco de dados aberto. Se vários bancos de dados estiverem abertos, a tabela é associada ao banco de dados aberto definido como banco de dados atual. A associação da tabela com o banco de dados é armazenada como um back link no registro de cabeçalho da tabela. Para obter mais informações, consulte Databases in Visual FoxPro e How to: Open Databases .

Quando você cria uma tabela, um arquivo de tabela (.dbf) é criado para armazenar o arquivo da tabela. Para informações sobre como nomear tabelas, consulte How to: Name Tables.

### Para criar uma tabela de banco de dados usando um assistente
- Abra o banco de dados no qual deseja criar uma tabela.
- No menu Database, clique em Create Table .
- Na caixa de diálogo New Table, clique em Table Wizard .
- Siga as instruções nas telas do assistente.

Para obter mais informações, consulte Table Wizard.

Você também pode iniciar o assistente a partir de um projeto no Project Manager expandindo o nó Data, o nó Databases e, em seguida, o nó do seu banco de dados. Clique no nó Tables e, em seguida, em New. Na caixa de diálogo New Table, clique em Table Wizard. Para obter mais informações, consulte Project Manager Window.

### Para criar uma tabela de banco de dados vazia
- Abra o banco de dados no qual deseja criar uma tabela.
- No menu Database, clique em Create Table .
- Na caixa de diálogo New Table, clique em New Table .
- Na caixa de diálogo Create, selecione o local onde deseja salvar a tabela de banco de dados e digite um nome para a tabela.
- Clique em Save . O Table Designer abre para que você possa especificar campos da tabela, itens e outros atributos.

Para obter mais informações, consulte Table Designer (Visual FoxPro).

### Para criar uma tabela de banco de dados em um projeto
- Abra o projeto com o banco de dados no Project Manager .
- No Project Manager , expanda o nó Data, o nó Databases e, em seguida, o nó do seu banco de dados.
- Clique no nó Tables, New e, em seguida, New Table .
- Na caixa de diálogo Create, selecione o local onde deseja salvar a tabela de banco de dados e digite um nome para a tabela.
- Clique em Save . O Table Designer abre para que você possa especificar campos da tabela, itens e outros atributos.

Para obter mais informações, consulte Project Manager Window e Table Designer (Visual FoxPro).

### Para criar uma tabela de banco de dados programaticamente
- Abra o banco de dados para o qual deseja criar uma tabela.
- Execute uma das seguintes ações: Para criar uma tabela abrindo o Table Designer , use o comando CREATE. -OU- Para criar uma tabela sem abrir o Table Designer , use o comando SQL CREATE TABLE.

Para obter mais informações, consulte CREATE Command e CREATE TABLE - SQL Command.
