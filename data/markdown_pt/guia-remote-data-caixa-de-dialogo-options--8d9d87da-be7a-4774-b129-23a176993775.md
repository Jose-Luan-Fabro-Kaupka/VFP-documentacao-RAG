# Guia Remote Data, caixa de diálogo Options

Contém opções para views remotas e configurações de conexão.

Quando você escolhe Set As Default — que aparece em cada guia da caixa de diálogo — o Visual FoxPro salva todas as opções em todas as guias.

# Padrões de view remota

As configurações na caixa Remote view defaults representam as configurações de cursor do Visual FoxPro para a sessão atual. Se você escolher Set As Default, as configurações tornam-se os padrões para sessões subsequentes. As opções nesta caixa correspondem às configurações que você faz ou obtém usando a função CURSORSETPROP( ) e a função CURSORGETPROP( ).
 **Share connection**
Especifica que o Visual FoxPro use uma conexão compartilhada, se uma estiver disponível. Se uma conexão compartilhada não estiver disponível, o Visual FoxPro cria uma conexão exclusiva quando a view é aberta e ela não pode ser compartilhada com outras views.
**Fetch memo**
Especifica que o Visual FoxPro não busque campos memo e general da fonte de dados até que um campo memo ou general seja ativado na saída da view. Desmarque esta opção para reduzir a quantidade de dados baixados inicialmente da tabela remota — isso resulta em desempenho mais rápido.
**SQL updates: Criteria**
Especifica quais campos o Visual FoxPro verifica em um servidor remoto para determinar se um registro foi alterado antes de você tentar atualizá-lo. A atualização falha se os dados nos campos especificados foram alterados.
**SQL updates: Method**
Especifica se o Visual FoxPro usa SQL UPDATE ou SQL DELETE e depois INSERT para atualizar informações no servidor remoto.
**Records to fetch at a time**
Especifica quantos registros o Visual FoxPro deve retornar por vez da fonte de dados remota. Escolha All para especificar que todos os registros devem ser retornados na primeira operação de busca. Esta configuração é limitada pelo valor especificado em Maximum records to fetch.
**Maximum records to fetch**
Especifica o número total de registros retornados por uma view, o que pode ajudar a evitar o download de uma quantidade excessiva de dados se você construiu uma consulta incorretamente. Escolha All para especificar que todos os registros devem ser retornados.
**Use memo for fields >=**
Especifica o comprimento máximo dos dados em campos Character longos. Se os dados de caracteres excederem o comprimento especificado, o Visual FoxPro os converte em um campo memo na saída da view. O padrão é 255, o tamanho máximo de um campo de caracteres no Visual FoxPro.
**Records to batch update**
Especifica o número de instruções de atualização enviadas de uma vez para views. O padrão é 1. Ajustar este valor pode aumentar muito o desempenho de atualização. Para obter mais informações, consulte o comando REPLACE e Scope Clauses.

# Padrões de conexão

As configurações na caixa Connection defaults representam as configurações padrão globais do Visual FoxPro para conexões. As opções nesta caixa correspondem às configurações que você faz ou obtém usando a função SQLSETPROP( ) e a função SQLGETPROP( ).
 **Asynchronous execution**
Especifica que o Visual FoxPro execute comandos SQL pass-through (usando a função SQLEXEC( ), a função SQLMORERESULTS( ), a função SQLTABLES( ) e a função SQLCOLUMNS( )) em segundo plano após retornar o controle à aplicação. Se você escolher esta opção, sua aplicação pode exibir informações de progresso e permitir que os usuários interrompam um comando com a tecla ESC se o comando SET ESCAPE Command foi definido como true. Você pode determinar o status de um comando SQL executando de forma assíncrona chamando uma das funções pass-through repetidamente até que ela informe que o comando foi concluído. O padrão é que esta opção esteja desabilitada (execução síncrona), o que especifica que o Visual FoxPro aguarda até que o comando SQL pass-through seja concluído antes de retornar o controle à aplicação.
**Display warnings**
Habilita a exibição de mensagens de aviso.
**Batch processing**
Especifica que, ao enviar várias instruções SQL pass-through usando a função SQLEXEC( ), o Visual FoxPro não retorna nenhum resultado até que todos os conjuntos de resultados individuais tenham sido recuperados. Corresponde à configuração de BatchMode na função SQLSETPROP( ). Se esta opção estiver desabilitada, você deve chamar a função SQLMORERESULTS( ) para determinar se há dados disponíveis.
**Automatic transactions**
Especifica que as transações são tratadas automaticamente pela conexão em tabelas remotas. Se você desmarcar esta opção, deve tratar o processamento de transações manualmente usando a função SQLCOMMIT( ) e a função SQLROLLBACK( ).
**Show login**
Especifica se exibir prompts de login quando uma conexão é ativada (se a conexão exigir que os usuários façam login). Por exemplo, Only When Necessary especifica que os prompts de login aparecem somente para informações de login não especificadas na definição da conexão ou da view.
**Connection timeout (sec)**
Especifica o número de segundos (entre 0 e 600) para aguardar o estabelecimento de uma conexão com o servidor remoto. Se a conexão não puder ser estabelecida no tempo especificado, o Visual FoxPro gera um erro. Especifique 0 para aguardar indefinidamente por uma conexão.
**Idle timeout (min)**
Especifica o número de minutos de tempo ocioso permitido antes que a conexão seja desativada. Se uma solicitação ao servidor não for feita no tempo especificado, o Visual FoxPro encerra a conexão. No entanto, o Visual FoxPro tenta reconectar automaticamente se uma solicitação ao servidor for feita após o timeout da conexão.
**Query timeout (sec)**
Especifica o número de segundos (entre 0 e 600) para aguardar a resposta do servidor a uma solicitação. Se o servidor demorar mais que o número de segundos especificado para processar a consulta, o Visual FoxPro gera um erro. Especifique 0 para aguardar indefinidamente pelos resultados da consulta.
**Wait time (ms)**
Especifica o número de milissegundos que decorrem antes que o Visual FoxPro verifique se a instrução SQL foi concluída.
