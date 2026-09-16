# Como: remover uma tabela de um banco de dados

Você pode remover uma tabela do banco de dados ou excluir a tabela do disco permanentemente. Remover uma tabela de um banco de dados não exclui a tabela automaticamente. No entanto, remove a tabela e as informações associadas do dicionário de dados do arquivo de banco de dados e também atualiza as informações de back link para refletir o novo status da tabela como tabela livre.

> **Observação:** Você deve primeiro fechar uma tabela antes de removê-la ou excluí-la. Se uma tabela de banco de dados tem um nome longo, remover a tabela do banco de dados também remove o nome longo. Para obter mais informações, consulte Como: nomear tabelas.

### Para remover ou excluir uma tabela em um banco de dados
- Abra o banco de dados no Database Designer.
- No Database Designer, clique na tabela que deseja remover.
- No menu Database, clique em Remove. O Visual FoxPro solicita que você remova a tabela do banco de dados ou a exclua do disco.
- Na caixa de diálogo de confirmação, execute uma das seguintes ações: Para remover a tabela, clique em Remove. -OU Para excluir a tabela do disco, clique em Delete.

### Para remover ou excluir uma tabela de um banco de dados em um projeto
- Abra o projeto no Project Manager.
- No Project Manager, expanda o nó Data, o nó Databases e, em seguida, o nó Tables.
- Clique na tabela que deseja remover e, em seguida, em Remove. O Visual FoxPro solicita que você remova a tabela do banco de dados ou a exclua do disco.
- Na caixa de diálogo de confirmação, execute uma das seguintes ações: Para remover a tabela, clique em Remove. -OU Para excluir a tabela do disco, clique em Delete.

### Para remover ou excluir uma tabela do banco de dados atual programaticamente
- Execute uma das seguintes ações: Para remover a tabela do banco de dados, use o comando REMOVE TABLE. -OU- Para excluir a tabela do disco, use o comando DROP TABLE ou use o comando REMOVE TABLE com a cláusula DELETE.

Para obter mais informações, consulte o comando REMOVE TABLE e o comando DROP TABLE.

Por exemplo, o código a seguir abre um banco de dados chamado MyDatabase sem abrir o Database Designer e remove uma tabela chamada MyTable:

```foxpro
OPEN DATABASE MyDatabase
REMOVE TABLE MyTable
```

O código a seguir abre um banco de dados chamado MyDatabase sem abrir o Database Designer e exclui uma tabela chamada MyTable do disco:

```foxpro
OPEN DATABASE MyDatabase
REMOVE TABLE MyTable DELETE
```

O código a seguir abre um banco de dados chamado MyDatabase sem abrir o Database Designer e exclui uma tabela chamada MyTable do disco sem mover o arquivo para a Lixeira do Windows:

```foxpro
OPEN DATABASE MyDatabase
DROP TABLE MyTable NORECYCLE
```

> **Cuidado:** Não use o comando ERASE com tabelas associadas a um banco de dados. ERASE não atualiza o back link para o banco de dados e pode causar erros de acesso à tabela.
