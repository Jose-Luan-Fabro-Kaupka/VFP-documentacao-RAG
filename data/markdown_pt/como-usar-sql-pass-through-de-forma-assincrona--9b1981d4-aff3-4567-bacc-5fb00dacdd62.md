# Como: usar SQL Pass-Through de forma assíncrona

Seu aplicativo pode solicitar processamento assíncrono para as quatro funções que enviam solicitações a uma fonte de dados e recuperam dados: Função SQLEXEC( ), Função SQLMORERESULTS( ), Função SQLTABLES( ) e Função SQLCOLUMNS( ). Você habilita o processamento assíncrono definindo a propriedade Asynchronous da conexão com a função SQLSETPROP( ). Quando a comunicação assíncrona é estabelecida para a conexão, todas as quatro dessas funções operam de forma assíncrona.

### Para verificar a configuração da propriedade Asynchronous
- Use a Função SQLGETPROP( ) para visualizar a configuração da propriedade Asynchronous. No exemplo a seguir, nConnectionHandle representa o número do identificador da sua conexão ativa: ? SQLGETPROP(nConnectionHandle,'Asynchronous')

### Para habilitar o processamento assíncrono
- Use a Função SQLSETPROP( ) para especificar a propriedade Asynchronous: ? SQLSETPROP(nConnectionHandle,'Asynchronous', .T.)

No modo assíncrono, você deve chamar cada função repetidamente até que ela retorne um valor diferente de 0 (ainda executando). Enquanto a função ainda está executando, você pode cancelar o processamento da função pressionando a tecla ESC se a propriedade SET ESCAPE estiver definida como true (.T.).

Até que a função tenha terminado o processamento, o aplicativo pode usar um identificador de conexão somente com a Função SQLCANCEL( ) ou com as funções assíncronas — Função SQLEXEC( ), Função SQLMORERESULTS( ), Função SQLTABLES( ) ou Função SQLCOLUMNS( ) — originalmente associadas ao identificador. Você não pode chamar nenhuma das outras três funções assíncronas ou a Função SQLDISCONNECT( ) com o mesmo identificador de conexão até que a função tenha terminado.
