# Funções SQL Pass-Through do Visual FoxPro

A tabela a seguir lista as funções SQL do Visual FoxPro que suportam trabalho com fontes de dados remotas, agrupadas por tarefa.

| Tarefa | Função | Finalidade |
| --- | --- | --- |
| Gerenciamento de conexão | SQLCONNECT( ) | Conecta a uma fonte de dados para operações SQL pass-through. |
| SQLSTRINGCONNECT( ) | Conecta a uma fonte de dados usando sintaxe de cadeia de conexão ODBC. | |
| SQLDISCONNECT( ) | Interrompe uma conexão com uma fonte de dados ODBC, tornando o identificador de conexão especificado obsoleto. | |
| SQLIDLEDISCONNECT( ) | Permite que uma conexão ou conexões SQL pass-through sejam temporariamente desconectadas. | |
| Execução e controle de instruções SQL | SQLCANCEL( ) | Cancela uma consulta SQL executando assincronamente em uma conexão ativa. |
| SQLEXEC( ) | Executa uma consulta SQL pass-through em uma conexão ativa; retorna o número de conjuntos de resultados gerados, ou 0 se SQLEXEC( ) ainda estiver executando (processamento assíncrono). | |
| SQLMORERESULTS( ) | Coloca outro conjunto de resultados em um cursor. Retorna 0 se a instrução que cria o conjunto de resultados ainda estiver executando. | |
| SQLPREPARE( ) | Pré-compila a instrução SQL na fonte de dados e vincula os parâmetros do Visual FoxPro, ou seja, salva as expressões de parâmetro reais para todos os parâmetros na instrução SQL. | |
| SQLCOMMIT( ) | Solicita um commit de transação. | |
| SQLROLLBACK( ) | Solicita um rollback de transação. | |
| Informações da fonte de dados | SQLCOLUMNS( ) | Armazena uma lista de nomes de colunas e informações sobre cada uma em um cursor. Retorna 1 se a função for bem-sucedida, ou 0 se a função ainda estiver executando. |
| SQLTABLES( ) | Armazena os nomes das tabelas na fonte em um cursor. Retorna 1 se a função for bem-sucedida, ou 0 se a função ainda estiver executando. | |
| Controle diverso | SQLGETPROP( ) | Obtém uma propriedade de conexão de uma conexão ativa. |
| SQLSETPROP( ) | Define uma propriedade de uma conexão ativa. | |

As instruções SQLEXEC( ), SQLMORERESULTS( ), SQLTABLES( ) e SQLCOLUMNS( ) podem ser canceladas no modo síncrono pressionando ESC se SET ESCAPE estiver definido como ON. Você pode cancelar essas instruções a qualquer momento no modo assíncrono emitindo SQLCANCEL( ). Todas as outras instruções SQL pass-through funcionam de forma síncrona e não são interrompíveis.
