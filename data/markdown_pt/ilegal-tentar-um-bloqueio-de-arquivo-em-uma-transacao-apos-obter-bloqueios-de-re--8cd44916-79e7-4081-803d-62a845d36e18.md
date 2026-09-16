# Ilegal tentar um bloqueio de arquivo em uma transação após obter bloqueios de registro anteriores (Erro 1594)

Você tentou explicitamente (com a função FLOCK( )) ou implicitamente (com REPLACE Command (Visual FoxPro), por exemplo) obter um bloqueio de arquivo em uma transação. Isso é ilegal se quaisquer bloqueios de registro já foram obtidos explicitamente ou implicitamente neste nível de transação ou em qualquer nível de transação inferior. Isso é ilegal mesmo se esses bloqueios de registro foram liberados dentro da transação.

Você deve reverter todos os bloqueios de registro neste arquivo antes de tentar este bloqueio de arquivo. Para obter mais informações, consulte ROLLBACK Command.
