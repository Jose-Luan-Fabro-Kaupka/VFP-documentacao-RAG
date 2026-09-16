# Como: atualizar links de tabelas e bancos de dados

Quando você move arquivos de banco de dados (.dbc, .dct e .dcx) ou uma tabela de banco de dados, os caminhos relativos mudam e podem quebrar links diretos e links inversos que o Visual FoxPro usa para associar arquivos de banco de dados e tabelas. Você pode restabelecer links e atualizar as informações de caminho relativo para refletir o novo local do arquivo.

> **Dica:** Se você quiser abrir uma tabela sem restabelecer links para todas as tabelas no banco de dados, use o comando USE. O Visual FoxPro exibe a caixa de diálogo Open para que você possa localizar o banco de dados que possui a tabela ou excluir os links. Para obter mais informações, consulte Comando USE.

Você também pode remover a referência ao banco de dados, ou link inverso, de uma tabela.

### Para atualizar links entre um banco de dados e suas tabelas
- Use o comando VALIDATE DATABASE com a cláusula RECOVER

Para obter mais informações, consulte Comando VALIDATE DATABASE.

Por exemplo, o código a seguir abre um banco de dados chamado MyDatabase e exibe caixas de diálogo para ajudá-lo a localizar aquelas tabelas que não estão nos locais armazenados pelo banco de dados:

```foxpro
OPEN DATABASE MyDatabase
VALIDATE DATABASE RECOVER
```

### Para remover o link inverso de uma tabela
- Use o comando FREE TABLE. Cuidado Não use FREE TABLE para remover uma tabela de um banco de dados se o banco de dados existir no disco; use REMOVE TABLE em vez disso. Se o banco de dados existir no disco, FREE TABLE pode tornar o banco de dados inutilizável.

Para obter mais informações, consulte Comando FREE TABLE.
