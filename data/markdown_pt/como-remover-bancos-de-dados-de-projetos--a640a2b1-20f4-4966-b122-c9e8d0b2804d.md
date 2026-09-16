# Como: remover bancos de dados de projetos

Você pode remover um banco de dados de um projeto ou excluí-lo do disco permanentemente. Remover um banco de dados não exclui automaticamente o banco de dados. Excluir o banco de dados usando as etapas descritas permite que o Visual FoxPro remova as informações de back link nas tabelas do banco de dados.

> **Observação:** Usar outros métodos, como procurar os arquivos do banco de dados e excluí-los usando o Windows Explorer, não remove as informações de back link.

### Para remover ou excluir um banco de dados de um projeto
- Abra o projeto na janela Project Manager .
- No Project Manager , expanda o nó Data e, em seguida, o nó Databases.
- Clique no banco de dados que deseja remover e, em seguida, Remove . O Visual FoxPro solicita que você remova o banco de dados do projeto ou o exclua do disco.
- Na caixa de diálogo de confirmação, execute uma das seguintes ações: Para remover o banco de dados do projeto, clique em Remove . -OU- Para excluir o banco de dados do disco, clique em Delete .

### Para excluir um banco de dados programaticamente
- Use o comando DELETE DATABASE. Observação DELETE DATABASE não exclui tabelas de banco de dados do disco. Em vez disso, as tabelas de banco de dados tornam-se free tables. Dica Para excluir um banco de dados e suas tabelas associadas do disco, use o comando DELETE DATABASE com a cláusula DELETETABLES.

Para obter mais informações, consulte DELETE DATABASE Command.

Por exemplo, o código a seguir exclui um banco de dados chamado MyDatabase do disco:

```foxpro
DELETE DATABASE MyDatabase
```
