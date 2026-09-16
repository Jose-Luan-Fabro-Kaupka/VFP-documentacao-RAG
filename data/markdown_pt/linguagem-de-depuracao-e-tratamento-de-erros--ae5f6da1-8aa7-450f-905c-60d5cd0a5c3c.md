# Linguagem de depuração e tratamento de erros

A tabela a seguir lista a linguagem que permite realizar operações de depuração e tratamento de erros em programas Visual FoxPro.
 Linguagem de depuração
| Use | Para |
| --- | --- |
| Comando * | Indicar o início de uma linha de comentário. |
| Comando && | Indicar o início de um comentário inline. |
| Comandos CLEAR | Liberar o item ou itens especificados da memória. |
| Comando DEBUG | Abrir o Visual FoxPro Debugger. |
| Comando DEBUGOUT | Direcionar o resultado de uma ou mais expressões para a janela Debug Output. |
| Comando SET DEVELOPMENT | Determinar se a janela Trace é aberta quando ocorre um erro em um formulário em execução. |
| Comando SET TALK | Determinar se o Visual FoxPro exibe os resultados dos comandos. |
| Comando SET TRBETWEEN | Habilitar ou desabilitar o rastreamento entre pontos de interrupção na janela Trace. |
| Comando WAIT | Exibir uma mensagem e pausar a execução do Visual FoxPro até que o usuário pressione uma tecla ou clique no mouse. |
 Linguagem de tratamento de erros
| Use | Para |
| --- | --- |
| Função AERROR( ) | Armazenar informações de erro em uma matriz. |
| Função COMRETURNERROR( ) | Armazenar informações de erro na estrutura de exceção COM. |
| Comando DEBUG ou Comando SET STEP | Abrir o Debugger ou a janela Trace. |
| Comando ERROR | Gerar um erro específico do Visual FoxPro para testar seu tratamento de erros. |
| Função ERROR( ) | Retornar um número de erro. |
| Função LINENO( ) | Retornar uma linha de programa em execução. |
| Função MESSAGE( ) | Retornar uma cadeia de mensagem de erro. |
| Comando ON ERROR | Executar um comando quando ocorre um erro. |
| Função ON( ) | Retornar comandos atribuídos a comandos de tratamento de erros. |
| Comando ON SHUTDOWN | Executa um comando ao sair do Visual FoxPro ou do Windows. |
| Função PROGRAM( ) OU SYS(16) - Nome do arquivo de programa em execução | Retornar o nome do programa atualmente em execução. |
| Comando RETRY | Executar o comando executado mais recentemente. |
| Comando SET AUTOINCERROR | Gerar um erro ao tentar atualizar ou inserir valores em um campo de autoincremento. |
| SYS(2018) - Parâmetro de mensagem de erro | Retornar qualquer parâmetro de mensagem de erro atual. |
| SYS(2410) - Manipulador de erros | Retornar o tipo de manipulador de erros para um erro. |
| Comando TRY...CATCH...FINALLY | Tratar erros e exceções que podem ocorrer ao executar um bloco de código. |
