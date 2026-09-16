# Como: criar tabelas livres

Você pode criar tabelas livres usando um assistente ou como uma tabela vazia. Um assistente ajuda você a criar uma tabela usando suas respostas a uma série de perguntas.

Quando você cria uma tabela, um arquivo de tabela (.dbf) é criado para armazenar o arquivo da tabela. Para obter informações sobre como nomear tabelas, consulte Como: nomear tabelas.

### Para criar uma tabela livre usando um assistente
- No menu File, clique em New .
- Na caixa de diálogo New, clique em Table e depois em Wizard .
- Siga as instruções nas telas do assistente.

Para obter mais informações, consulte Table Wizard.

Você também pode iniciar o assistente a partir de um projeto no Project Manager expandindo o nó Data, clicando no nó Free Tables e depois em New. Na caixa de diálogo New Table, clique em Table Wizard. Para obter mais informações, consulte Project Manager Window.

### Para criar uma tabela livre vazia
- No menu File, clique em New .
- Na caixa de diálogo New, clique em Table e depois em New file .
- Na caixa de diálogo Create, selecione o local onde deseja salvar a tabela do banco de dados e digite um nome para a tabela.
- Clique em Save . O Table Designer é aberto para que você possa especificar campos, itens e outros atributos da tabela.

Para obter mais informações, consulte Table Designer (Visual FoxPro).

### Para criar uma tabela livre em um projeto
- Abra o projeto no Project Manager .
- No Project Manager , expanda o nó Data.
- Clique no nó Free Tables e depois em New .
- Na caixa de diálogo New Table, clique em New Table .
- Na caixa de diálogo Create, selecione o local onde deseja salvar a tabela do banco de dados e digite um nome para a tabela.
- Clique em Save . O Table Designer é aberto para que você possa especificar campos, itens e outros atributos da tabela.

Para obter mais informações, consulte Project Manager Window e Table Designer (Visual FoxPro).

### Para criar uma tabela livre programaticamente
- Execute uma das seguintes opções: Para criar uma tabela abrindo o Table Designer , feche quaisquer bancos de dados abertos e use o comando CREATE. -OU- Para criar uma tabela sem abrir o Table Designer , use o comando SQL CREATE TABLE. Se um banco de dados estiver aberto, inclua a palavra-chave FREE.

Para obter mais informações, consulte o comando CREATE e o comando CREATE TABLE - SQL.
