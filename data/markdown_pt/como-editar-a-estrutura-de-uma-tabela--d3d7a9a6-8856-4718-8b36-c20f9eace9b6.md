# Como: editar a estrutura de uma tabela

Você pode editar a estrutura de uma tabela, que define os campos e seus atributos, bem como os índices da tabela.

### Para editar a estrutura de uma tabela livre
- No menu File, clique em Open.
- Na caixa de diálogo Open, navegue até e selecione o arquivo de tabela (.dbf) que você deseja abrir e clique em OK.
- No menu View, clique em Table Designer. O Table Designer abre para que você possa alterar atributos de campos, índices e da tabela.

Para obter mais informações, consulte Table Designer (Visual FoxPro).

### Para editar a estrutura de uma tabela de banco de dados
- Abra o banco de dados no Database Designer.
- No Database Designer, clique na tabela que você deseja editar.
- No menu Database, clique em Modify.

O Table Designer abre para que você possa alterar atributos de campos, índices e da tabela.

### Para editar a estrutura de uma tabela em um projeto
- Abra o projeto no Project Manager.
- No Project Manager, expanda o nó Data.
- Escolha uma das seguintes opções: Expanda o nó Databases, o nó do banco de dados que contém a tabela, depois o nó Tables, e clique na tabela cuja estrutura você deseja editar. -OU- Expanda o nó Free Tables e clique na tabela cuja estrutura você deseja editar.
- No Project Manager, clique em Modify. O Table Designer abre para que você possa alterar atributos de campos, índices e da tabela.

Para obter mais informações, consulte Table Designer (Visual FoxPro).

### Para editar a estrutura de uma tabela programaticamente
- Abra a tabela com o comando USE.
- Escolha uma das seguintes opções: Para editar a estrutura abrindo o Table Designer, use o comando MODIFY STRUCTURE. -OU- Para editar a estrutura sem abrir o Table Designer, use o comando SQL ALTER TABLE.

Para obter mais informações, consulte USE Command, MODIFY STRUCTURE Command e ALTER TABLE - SQL Command.
