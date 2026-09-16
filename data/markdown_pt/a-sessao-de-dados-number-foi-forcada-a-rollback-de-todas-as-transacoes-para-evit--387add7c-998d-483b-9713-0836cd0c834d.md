# A sessão de dados #number foi forçada a ROLLBACK de todas as transações para evitar deadlock (Erro 1599)

Um deadlock foi detectado de outra sessão de dados tentando bloquear um índice ou arquivo memo mantido pela sessão de dados #number. Um ROLLBACK forçado foi concluído, deixando a sessão de dados number em um estado de erro.

Emita o número apropriado de comandos ROLLBACK Command para limpar o estado de erro. Essas situações podem ser evitadas definindo SYS(3052) - Override SET REPROCESS Locking on para arquivos de índice e memo.
