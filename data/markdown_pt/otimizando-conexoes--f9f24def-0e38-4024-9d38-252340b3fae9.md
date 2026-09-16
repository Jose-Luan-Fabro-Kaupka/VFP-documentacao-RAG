# Otimizando conexões

Estabelecer uma conexão usa tempo e memória tanto no cliente quanto no servidor. Ao otimizar conexões, você equilibra sua necessidade de alto desempenho com os requisitos de recursos do seu aplicativo.

O número de conexões usadas pelo Visual FoxPro depende de você forçar o fechamento de conexões não utilizadas e de como você define o comprimento do tempo limite de inatividade da conexão.

# Usando conexões compartilhadas

Você pode usar conexões exclusivamente ou compartilhar uma conexão. Cada método tem seus benefícios. Quando você usa uma conexão exclusivamente, seu aplicativo não experimenta contenções por recursos de conexão depois que uma conexão é estabelecida. Se cada conjunto de resultados usar uma conexão exclusiva, você também pode intercalar processamento assíncrono em múltiplos conjuntos de resultados.

Quando você usa uma conexão compartilhada, você tem uma conexão para múltiplos conjuntos de resultados. Você deve serializar operações de manipulação de dados nos conjuntos de resultados que compartilham a mesma conexão e projetar o aplicativo para testar a conexão quanto a ocupação sempre que conflitos possam ocorrer. Para obter informações sobre compartilhamento de conexão, consulte Como: compartilhar conexões para múltiplas views remotas.

# Controlando tempos limite de conexão

Se seu aplicativo não realizar nenhuma ação por muito tempo, você pode reduzir o uso de conexão definindo a propriedade IdleTimeout na conexão. A propriedade IdleTimeout controla o intervalo de tempo que as conexões podem ficar inativas antes de serem fechadas pelo Visual FoxPro. Por padrão, as conexões aguardam indefinidamente e não são desativadas até serem fechadas especificamente pelo usuário.

Você define o tempo de inatividade para uma definição de conexão com a propriedade IdleTimeout da função DBSETPROP( ); você pode definir a propriedade IdleTimeout para uma conexão ativa com a função SQLSETPROP( ).

O Visual FoxPro fecha conexões mesmo se janelas Browse e formulários exibindo dados remotos ainda estiverem abertos e, em seguida, reconecta automaticamente quando a conexão for necessária novamente. No entanto, o Visual FoxPro não pode fechar uma conexão se:
 - Resultados de uma consulta do servidor estiverem pendentes.
- A conexão estiver em modo de transação manual. Você deve confirmar ou reverter a transação e mudar para o modo de transação automática antes que a conexão possa ser fechada.

Você define o modo de transação para uma definição de conexão com a propriedade Transactions da função DBSETPROP( ); você pode definir o modo de transação para uma conexão ativa com a função SQLSETPROP( ).

# Liberando conexões

Você pode melhorar o desempenho fechando conexões que seu aplicativo não está mais usando. As conexões são fechadas automaticamente para você quando você fecha uma view. Se a conexão for compartilhada por múltiplas views, o Visual FoxPro fecha a conexão quando a última view que usa a conexão é fechada.

Você pode controlar a conexão para uma consulta manualmente se não quiser atualizar os dados em um cursor. Use uma consulta SQL pass-through para selecionar os dados necessários em um cursor local e, em seguida, feche a conexão.
