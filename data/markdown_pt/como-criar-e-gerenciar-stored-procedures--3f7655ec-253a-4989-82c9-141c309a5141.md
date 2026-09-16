# Como: criar e gerenciar stored procedures

Você pode criar, editar, copiar e excluir stored procedures no seu banco de dados. Uma stored procedure é código Visual FoxPro armazenado no arquivo de banco de dados (.dbc) e que opera especificamente sobre dados no banco de dados.

### Para criar uma stored procedure
- Abra o banco de dados no Database Designer .
- No menu Database, clique em Edit Stored Procedures .

Uma janela de edição abre para que você possa escrever código para a stored procedure.

### Para criar uma stored procedure para um banco de dados em um projeto
- Abra o projeto no Project Manager .
- No Project Manager , expanda o nó Data, o nó Databases e, em seguida, o nó do banco de dados no qual deseja adicionar uma stored procedure.
- Clique no nó Stored Procedures e depois em New .

Uma janela de edição abre para que você possa escrever código para a stored procedure.

### Para criar uma stored procedure programaticamente
- Use o comando MODIFY PROCEDURE.

Para obter mais informações, consulte MODIFY PROCEDURE Command.

### Para editar uma stored procedure
- Execute uma das seguintes ações: Para editar uma stored procedure no Database Designer, no menu Database, clique em Edit Stored Procedures . -OU- Para editar uma stored procedure no Project Manager , clique no nó Stored Procedures e depois em Modify . -OU- Use o comando MODIFY PROCEDURE.

Uma janela de edição abre para que você possa editar o código da stored procedure.

### Para copiar e anexar stored procedures a um arquivo de texto
- Use os comandos COPY PROCEDURES e APPEND PROCEDURES.

Para obter mais informações, consulte COPY PROCEDURES Command e APPEND PROCEDURES Command.

### Para excluir uma stored procedure
- Abra a janela de edição da stored procedure.
- Na janela de edição, selecione o código que deseja excluir.
- Pressione a tecla DELETE.
