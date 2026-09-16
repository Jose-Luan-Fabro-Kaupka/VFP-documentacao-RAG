# Como: exibir registros em tabelas

Você pode exibir os registros de uma tabela abrindo-a em uma janela de navegação. Uma janela de navegação exibe os dados de uma tabela como linhas (registros) e colunas (campos) pelas quais você pode rolar. Para obter mais informações, consulte Janela Browse.

### Para navegar pelos dados de uma tabela livre
- No menu File, clique em Open.
- Na caixa de diálogo Open, navegue até o local da tabela que deseja exibir.
- Na caixa Files of type, selecione o tipo de arquivo Table (*.dbf) para exibir somente arquivos de tabela.
- Selecione o arquivo de tabela que deseja exibir.
- No menu View, clique em Browse. A tabela selecionada será aberta em uma janela de navegação.

### Para navegar pelos dados de uma tabela de banco de dados
- Abra o banco de dados no Database Designer.
- Selecione a tabela desejada.
- No menu Database, clique em Browse. A tabela será aberta em uma janela de navegação.

### Para navegar pelos dados de uma tabela a partir de um projeto
- Abra o projeto no Project Manager.
- Expanda o nó Data e escolha uma das opções a seguir: para navegar por uma tabela de banco de dados, expanda o nó Databases e depois o nó Tables. -OU- Para navegar por uma tabela livre, expanda o nó Free Tables.
- Clique na tabela que deseja exibir e depois em Browse. A tabela selecionada será aberta em uma janela de navegação.

### Para navegar por uma tabela programaticamente
- Abra a tabela com o comando USE.
- Após USE, use o comando BROWSE. Dica: para impedir que os usuários adicionem registros a uma tabela durante a navegação, inclua a cláusula NOAPPEND no comando BROWSE.

Para obter mais informações, consulte Comando USE e Comando BROWSE.
