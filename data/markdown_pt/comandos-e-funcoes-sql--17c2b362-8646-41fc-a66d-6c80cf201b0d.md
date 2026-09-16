# Comandos e funções SQL

O Visual FoxPro suporta comandos e funções Structured Query Language (SQL). Os comandos SQL do Visual FoxPro utilizam a tecnologia Rushmore Query Optimization para otimizar o desempenho, e um único comando SQL pode ser usado para substituir múltiplos comandos do Visual FoxPro.

O Visual FoxPro suporta o seguinte:
 **Comando ALTER TABLE - SQL**
Modifica uma tabela existente. Você pode modificar o nome, tipo, precisão, escala, suporte a valores nulos e regras de integridade referencial para cada campo na tabela.
**Função ASQLHANDLES( )**
Armazena referências numéricas a todos os handles de instrução de conexão SQL ativos em um array.
**Comando CREATE CURSOR - SQL**
Cria uma tabela temporária. Cada campo na tabela temporária é definido com um nome, tipo, precisão, escala, suporte a valores nulos e regras de integridade referencial. Essas definições podem ser obtidas do próprio comando ou de um array.
**Comando CREATE SQL VIEW**
Exibe o View Designer, permitindo que você crie uma view SQL.
**Comando CREATE TABLE - SQL**
Cria uma tabela. Cada novo campo da tabela é definido com um nome, tipo, precisão, escala, suporte a valores nulos e regras de integridade referencial. Essas definições podem ser obtidas do próprio comando ou de um array.
**Comando DELETE - SQL**
Marca registros em uma tabela para exclusão usando sintaxe SQL.
**Comando INSERT - SQL**
Anexa um novo registro ao final de uma tabela existente. O novo registro contém dados listados no comando INSERT ou de um array.
**Comando SELECT - SQL**
Especifica os critérios nos quais uma consulta é baseada e emite a consulta. O Visual FoxPro interpreta a consulta e recupera os dados especificados da(s) tabela(s). O comando SELECT está integrado ao Visual FoxPro como qualquer outro comando do Visual FoxPro. Você pode criar uma consulta do comando SELECT nestas áreas: Na Janela de Comando. Em um programa Visual FoxPro (como qualquer outro comando do Visual FoxPro). No Query Designer.
**Classe base SQL Pass Through**
Torna possível executar stored procedures em um banco de dados host como o Microsoft SQL Server.
**Função SQLCANCEL( )**
Solicita o cancelamento de uma instrução SQL em execução
**Função SQLCOLUMNS( )**
Armazena uma lista de nomes de colunas e informações sobre cada coluna para a tabela de fonte de dados especificada em um cursor do Visual FoxPro.
**Função SQLCOMMIT( )**
Confirma uma transação.
**Função SQLCONNECT( )**
Estabelece uma conexão com uma fonte de dados.
**Função SQLDISCONNECT( )**
Encerra uma conexão com uma fonte de dados.
**Função SQLEXEC( )**
Envia uma instrução SQL para a fonte de dados, onde a instrução é processada.
**Função SQLGETPROP( )**
Retorna configurações atuais ou padrão para uma conexão ativa.
**Função SQLIDLEDISCONNECT( )**
Permite que uma conexão SQL pass-through seja temporariamente desconectada.
**Função SQLMORERESULTS( )**
Copia outro conjunto de resultados para um cursor do Visual FoxPro se mais conjuntos de resultados estiverem disponíveis.
**Função SQLPREPARE( )**
Prepara uma instrução SQL para execução remota por SQLEXEC( ).
**Função SQLROLLBACK( )**
Cancela quaisquer alterações feitas durante a transação atual.
**Função SQLSETPROP( )**
Especifica configurações para uma conexão ativa.
**Função SQLSTRINGCONNECT( )**
Estabelece uma conexão com uma fonte de dados por meio de uma cadeia de conexão.
**Função SQLTABLES( )**
Armazena os nomes das tabelas em uma fonte de dados em um cursor do Visual FoxPro.
**Comando UPDATE - SQL**
Atualiza registros em uma tabela. Os registros podem ser atualizados com base nos resultados de uma instrução SELECT - SQL.
