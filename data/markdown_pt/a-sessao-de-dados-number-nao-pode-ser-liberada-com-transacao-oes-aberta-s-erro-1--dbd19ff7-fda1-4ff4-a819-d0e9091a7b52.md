# A sessão de dados #number não pode ser liberada com transação(ões) aberta(s) (Erro 1549)

Um objeto baseado em sessão de dados está sendo fechado enquanto há transações abertas. A sessão de dados permanecerá ativa.

Feche a sessão de dados emitindo SET DATASESSION Command number seguido do número apropriado de comandos END TRANSACTION Command ou ROLLBACK Command.
