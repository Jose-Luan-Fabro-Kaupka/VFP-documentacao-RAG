# Como: construir integridade referencial entre tabelas

Você pode criar um conjunto de regras para preservar os relacionamentos definidos entre tabelas de banco de dados ao adicionar, atualizar ou excluir registros. O processo de criar essas regras é chamado de construir integridade referencial.

### Para construir integridade referencial entre tabelas
- Abra o banco de dados no Database Designer.
- No Database Designer, crie um novo relacionamento persistente entre duas tabelas ou escolha um relacionamento existente clicando na linha de relacionamento.
- No menu Database, clique em Edit Referential Integrity.
- No Referential Integrity Builder, selecione as regras que deseja aplicar para atualizar, excluir ou inserir registros.
- Para salvar suas alterações, gerar código RI e sair do builder, clique em OK e depois em Yes.

Para obter mais informações, consulte Referential Integrity Builder.

Quando você usa o RI Builder, o Visual FoxPro gera código para aplicar regras de integridade referencial e o salva como triggers que referenciam stored procedures. Um trigger é uma expressão vinculada a uma tabela e invocada quando registros da tabela são modificados por comandos de manipulação de dados especificados. Você pode visualizar esse código abrindo o editor de texto de stored procedure do seu banco de dados. Para obter mais informações, consulte Uso de triggers e Como: criar e gerenciar stored procedures.

> **Cuidado:** Execute o RI Builder novamente quando fizer alterações em um banco de dados, como modificar tabelas de banco de dados ou alterar índices usados em um relacionamento persistente, antes de usar o banco de dados. Executar o RI Builder novamente atualiza o código de stored procedure e os triggers de tabela usados para aplicar integridade referencial. Se você não executar o RI Builder novamente, poderá receber resultados inesperados porque as stored procedures e os triggers não foram atualizados.
