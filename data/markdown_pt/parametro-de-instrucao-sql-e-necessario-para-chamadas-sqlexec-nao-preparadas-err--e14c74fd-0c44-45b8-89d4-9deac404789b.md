# Parâmetro de instrução SQL é necessário para chamadas SqlExec( ) não preparadas (Erro 1472)

Você deve usar a Função SQLPREPARE( ) primeiro ou incluir uma instrução SQL na chamada à Função SQLEXEC( ).
 - SQLPREPARE( ) não foi chamado. Inclua uma instrução SQL diretamente em SQLEXEC( ) ou chame SQLPREPARE( ) antes de chamar SQLEXEC( ).
- O estado preparado foi limpo porque SQLEXEC( ) foi chamado com um argumento cSQLCommand ou porque SQLPREPARE( ) foi chamado. Chame SQLPREPARE( ) novamente.
