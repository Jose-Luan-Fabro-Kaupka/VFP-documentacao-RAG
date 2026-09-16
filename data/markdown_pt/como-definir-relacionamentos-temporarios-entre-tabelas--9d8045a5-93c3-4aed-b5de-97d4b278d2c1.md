# Como: definir relacionamentos temporários entre tabelas

Você pode definir relacionamentos temporários entre tabelas abertas para que, quando o ponteiro de registro em uma tabela se move, o ponteiro de registro na outra tabela acompanhe. Você também pode criar um relacionamento temporário em uma única tabela.

> **Dica:** Normalmente, você define um relacionamento temporário entre tabelas que têm um campo comum usando uma expressão relacional. A expressão relacional é tipicamente a expressão de índice do índice controlador na tabela filha.

Para obter mais informações, consulte Relacionamentos temporários entre tabelas.

### Para criar um relacionamento entre tabelas
- Abra as tabelas entre as quais deseja criar relacionamentos.
- No menu Janela, escolha Data Session . A janela Data Session é aberta.
- Na lista Aliases, clique no alias da tabela pai desejada e então Relations . A tabela que você selecionou aparece na lista Relations seguida de uma linha indicando o relacionamento com uma tabela filha que você seleciona na próxima etapa.
- Na lista Aliases, clique no alias da tabela filha desejada e então Relations . Observação Se uma ordem de índice não foi definida na tabela que você selecionou, a caixa de diálogo Set Index Order aparece. Para selecionar uma ordem de índice, clique na ordem de índice que deseja definir na tabela filha e então OK . O Expression Builder é aberto.
- No Expression Builder , digite ou construa uma expressão relacional entre a tabela pai e a tabela filha. Quando terminar, clique em OK .

Para obter mais informações, consulte Como: abrir tabelas em áreas de trabalho.

### Para criar um relacionamento um-para-muitos entre tabelas
- Depois de selecionar a tabela filha na janela Data Session, clique em 1 to many .
- Na caixa de diálogo Create One-to-Many Relationships, clique no alias da tabela filha desejada e então Move .
- Quando terminar, clique em OK .

### Para criar um relacionamento em uma única tabela
- Abra a tabela desejada em duas áreas de trabalho separadas.
- No menu Janela, escolha Data Session . A janela Data Session é aberta.
- Na lista Aliases, clique no alias da tabela pai desejada e então Relations .
- Na lista Aliases, clique no alias da tabela filha desejada e então Relations . Observação Se uma ordem de índice não foi definida na tabela que você selecionou, a caixa de diálogo Set Index Order aparece. Para selecionar uma ordem de índice, clique na ordem de índice que deseja definir na tabela filha e então OK . O Expression Builder é aberto.
- No Expression Builder , digite ou construa uma expressão relacional entre a tabela pai e a tabela filha. Quando terminar, clique em OK .

Para obter mais informações, consulte Como: abrir tabelas em áreas de trabalho.

### Para definir um relacionamento temporário entre tabelas programaticamente
- Use o comando SET RELATION.

Você também pode usar SET RELATION para estabelecer um relacionamento entre uma única tabela pai e várias tabelas filhas. Você também pode definir um relacionamento entre uma tabela aberta na área de trabalho atualmente selecionada e outra tabela aberta em outra área de trabalho usando o comando SET RELATION. Para obter mais informações, consulte Comando SET RELATION.
