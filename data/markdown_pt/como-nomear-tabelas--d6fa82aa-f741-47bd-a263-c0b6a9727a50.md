# Como: nomear tabelas

Quando você cria uma tabela, precisa especificar um nome para o arquivo de tabela (.dbf) criado para armazenar a tabela. Tanto tabelas de banco de dados quanto tabelas livres exigem nomes de arquivo de tabela. Os nomes de tabela devem começar com uma letra ou sublinhado e podem consistir em letras, dígitos ou sublinhados.

Se sua tabela está em um banco de dados, você pode especificar um nome longo de tabela, que pode conter até 128 caracteres, além do nome do arquivo de tabela. Você pode usar nomes longos de tabela em vez de nomes de arquivo convencionais para identificar a tabela em um banco de dados mais facilmente. O Visual FoxPro exibe nomes longos de tabela quando a tabela aparece na interface do Visual FoxPro, por exemplo no Project Manager, Database Designer, Query Designer e View Designer, bem como na barra de título de uma janela de navegação.

> **Observação:** Se você remover uma tabela de um banco de dados, a tabela mantém seu nome de arquivo, mas não seu nome longo.

### Para atribuir um nome longo de tabela a uma tabela de banco de dados
- Abra a tabela de banco de dados no Table Designer.
- No Table Designer, clique na guia Table.
- Na caixa Name, digite um nome longo para a tabela.

### Para atribuir um nome longo de tabela a uma tabela de banco de dados programaticamente
- Inclua a cláusula NAME ao criar uma tabela de banco de dados com o comando SQL CREATE TABLE.

Para obter mais informações, consulte Table Designer (Visual FoxPro) e CREATE TABLE - SQL Command.

# Renomeando tabelas

Você pode renomear os nomes longos de tabelas de banco de dados e os nomes de arquivo de tabelas de banco de dados e tabelas livres. Você pode renomear os nomes longos de tabelas de banco de dados usando o Table Designer porque está alterando o nome longo, não o nome do arquivo de tabela. Você pode renomear tabelas livres apenas programaticamente porque tabelas livres não têm nomes longos.

### Para alterar o nome longo de uma tabela de banco de dados
- Abra o banco de dados no Database Designer.
- Encontre e torne ativa a tabela que deseja renomear.
- No menu Database, clique em Modify.
- No Table Designer, clique na guia Table.
- Na caixa Name, digite um novo nome para a tabela.

Para obter mais informações, consulte Database Designer (Visual FoxPro) e Table Designer (Visual FoxPro).

### Para renomear uma tabela de banco de dados programaticamente
- Defina o banco de dados que contém a tabela que deseja renomear como o banco de dados atual.
- Use o comando RENAME TABLE.

Para obter mais informações, consulte RENAME TABLE Command.

### Para renomear uma tabela livre programaticamente
- Use o comando RENAME. Cuidado Não use o comando RENAME em tabelas de banco de dados. RENAME não atualiza o back link da tabela ao banco de dados e pode causar erros ao acessar a tabela. Use o comando RENAME TABLE em vez disso.

Para obter mais informações, consulte RENAME Command.
