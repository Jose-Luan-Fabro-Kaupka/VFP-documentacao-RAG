# Como: associar tabelas a um banco de dados

Depois de criar um banco de dados, você pode associar tabelas a um banco de dados criando-as no banco de dados ou adicionando tabelas existentes. As tabelas podem pertencer a apenas um banco de dados por vez; portanto, você pode associar qualquer tabela que não faça parte de outro banco de dados. Se você deseja associar uma tabela que pertence a outro banco de dados, deve remover essa tabela antes de poder adicioná-la a um banco de dados diferente. Você também pode usar dados de outra tabela de banco de dados sem removê-la. Para mais informações, consulte How to: Use Tables from Other Databases.

> **Observação:** Para associar tabelas livres a um banco de dados, você deve adicioná-las explicitamente. Modificar sua estrutura não associa tabelas livres a um banco de dados, mesmo se um banco de dados estiver aberto quando você modificar a estrutura.

Quando você adiciona uma tabela a um banco de dados, o Visual FoxPro modifica o registro de cabeçalho no arquivo de tabela para documentar o caminho e o nome do arquivo do banco de dados que agora contém a tabela. Essas informações de caminho e nome de arquivo são chamadas de back link porque vinculam a tabela de volta ao banco de dados proprietário.

Para criar tabelas de banco de dados, consulte How to: Create Database Tables.

### Para associar uma tabela a um banco de dados
- Abra o banco de dados no Database Designer. O menu Database aparece.
- No menu Database, clique em Add Table.
- Na caixa de diálogo Open, procure e selecione uma tabela e clique em OK. A tabela que você selecionou aparece no Database Designer.

### Para associar uma tabela a um banco de dados em um projeto
- Abra o projeto no Project Manager.
- No Project Manager, expanda o nó Data e, em seguida, o nó Databases.
- Clique no nó Tables e, em seguida, em Add.
- Na caixa de diálogo Select table name, procure e selecione o arquivo de tabela (.dbf) que deseja adicionar e clique em OK. A tabela que você selecionou aparece no nó Tables do Project Manager.

Para mais informações, consulte Project Manager Window.

### Para associar uma tabela ao banco de dados atual programaticamente
- Abra o banco de dados.
- Use o comando ADD TABLE. Por exemplo, o código a seguir abre um banco de dados chamado MyDatabase e adiciona uma tabela chamada MyTable: OPEN DATABASE MyDatabase ADD TABLE MyTable

Para mais informações, consulte ADD TABLE Command.
