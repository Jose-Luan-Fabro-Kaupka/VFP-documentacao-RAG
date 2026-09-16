# Como: adicionar tabelas a visualizações

Você pode acessar dados armazenados em outras tabelas adicionando essas tabelas à sua visualização local ou remota e especificando condições de junção para as tabelas adicionadas.

Especificar condições de junção entre as tabelas que você adiciona ajuda a determinar quais registros das duas tabelas devem ser comparados e retornados. Para obter mais informações, consulte How to: Control Record Selection with Joins and Join Conditions for Tables, Queries, and Views.

> **Observação:** Quando você adiciona tabelas a uma visualização existente programaticamente, o comando CREATE SQL VIEW produz um produto cruzado.

### Para adicionar uma tabela a uma visualização local
- Abra a visualização no Project Manager ou Database Designer. O View Designer abre.
- No menu Query, clique em Add Tables.
- Na caixa de diálogo Add Table or View, selecione a tabela ou visualização que deseja adicionar. A tabela ou visualização selecionada aparece no View Designer.
- Na caixa de diálogo Join Condition, especifique a condição de junção desejada e clique em OK.
- Se desejar especificar um alias para cada tabela selecionada, digite-o na caixa Alias.
- Quando terminar, clique em Close.

Para obter mais informações, consulte Query and View Designers e Join Condition Dialog Box.

### Para adicionar uma tabela a uma visualização remota
- Abra a visualização no Project Manager ou Database Designer. O View Designer abre.
- No menu Query, clique em Add Tables.
- Na caixa de diálogo Open, clique em cada tabela que deseja adicionar e depois em Add. A tabela selecionada aparece no View Designer.
- Na caixa de diálogo Join Condition, especifique a condição de junção desejada e clique em OK.
- Se desejar especificar um alias para cada tabela selecionada, digite-o na caixa Alias.
- Quando terminar, clique em Close.

Para obter mais informações, consulte Query and View Designers, Select Connection or Data Source Dialog Box e Join Condition Dialog Box.

### Para adicionar uma tabela a visualizações programaticamente
- Nas instruções SQL SELECT especificadas pelo comando CREATE SQL VIEW, adicione nomes de tabelas e condições de junção para as tabelas adicionadas usando as cláusulas FROM e WHERE. O Visual FoxPro exibe uma caixa de diálogo de confirmação para substituir a visualização existente.
- Na caixa de diálogo de confirmação, clique em Yes.

Para obter mais informações, consulte CREATE SQL VIEW Command.
