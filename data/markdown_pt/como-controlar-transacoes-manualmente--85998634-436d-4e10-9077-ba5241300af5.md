# Como: controlar transações manualmente

Se você deseja controlar transações manualmente, pode definir a propriedade Transactions como 2, ou DB_TRANSMANUAL. Com tratamento manual de transações, o Visual FoxPro inicia automaticamente uma transação para você quando você emite a primeira instrução SQL de gravação de dados, mas você deve enviar as funções SQLCOMMIT( ) ou SQLROLLBACK( ) do Visual FoxPro para encerrar a transação. Para o objeto CursorAdapter, você pode definir a propriedade UseTransactions como false (.F.) e o CursorAdapter não usa transações para enviar comandos Insert, Update ou Delete.

### Para usar o modo de transação manual
- Use a função DBSETPROP( ) para definir a propriedade Transactions na conexão como 2 ou DB_TRANSMANUAL. -ou-
- Use a função SQLSETPROP( ) para definir a propriedade Transactions na conexão ativa como 2 ou DB_TRANSMANUAL.

O processamento de transações é tratado manualmente por meio da função SQLCOMMIT( ) e da função SQLROLLBACK( ).

Depois de confirmar ou reverter a transação anterior, o Visual FoxPro inicia automaticamente uma nova transação quando você emite a próxima instrução SQL de gravação de dados. Para obter mais informações sobre transações, consulte Programming for Shared Access.

O Visual FoxPro suporta transações aninhadas até cinco níveis para dados locais. Um único nível de suporte a transações está integrado ao SQL pass-through.

Se seu servidor suporta múltiplos níveis de transações, você pode usar SQL pass-through para gerenciar níveis de transação explicitamente. O gerenciamento explícito de transações é complexo, no entanto, porque pode ser difícil controlar a interação entre a transação integrada e o momento das transações do servidor remoto. Para obter mais informações sobre gerenciamento explícito de transações, consulte a documentação ODBC.
