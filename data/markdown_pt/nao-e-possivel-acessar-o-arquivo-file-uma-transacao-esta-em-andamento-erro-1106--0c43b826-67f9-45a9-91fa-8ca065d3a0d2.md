# Não é possível acessar o arquivo "file"; uma transação está em andamento. (Erro 1106)

O Visual FoxPro não pode acessar a tabela, o índice ou o arquivo memo porque uma transação em andamento ainda não foi concluída.

As funções FLOCK( ) e RLOCK( ) geralmente não impedem que outros usuários leiam as informações bloqueadas. Esta mensagem, que se desloca da esquerda para a direita para indicar que o Visual FoxPro ainda está ativo, oferece compatibilidade com o sistema de rastreamento de transações (TTS) da Novell.
