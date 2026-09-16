# Usando a tecnologia SQL pass-through

Usar views remotas é o método mais fácil e mais comum para acessar e atualizar dados remotos. A tecnologia SQL pass-through permite enviar instruções SQL diretamente ao servidor e, como as instruções são executadas no servidor, é uma forma poderosa de melhorar o desempenho de sua aplicação cliente/servidor.

Os tópicos a seguir fornecem informações sobre como usar a tecnologia SQL pass-through em suas aplicações.

# Nesta seção
 **How to: Access Stored Procedures on Remote Servers with SQL Pass-Through Functions**
Descreve como usar stored procedures do servidor. Stored procedures do servidor podem melhorar significativamente o desempenho de instruções SQL e lotes.
**How to: Use SQL Pass-Through Functions**
Explica como sua aplicação cliente/servidor pode acessar dados remotos com SQL pass-through. Também é fornecida uma comparação entre views remotas e tecnologias SQL pass-through.
**Visual FoxPro SQL Pass-Through Functions**
Fornece uma lista de funções SQL Pass-Through.
**Using Result Sets**
Explica como o Visual FoxPro trata conjuntos de resultados retornados por funções SQL Pass-Through.
**How to: Return Multiple Result Sets**
Explica como recuperar vários conjuntos de resultados, como aqueles de uma stored procedure que contém instruções SELECT nativas do servidor.
**How to: Create a Parameterized Query**
Explica como criar uma consulta parametrizada com a tecnologia SQL pass-through.
**Using SQL Server Input/Output Parameters**
Descreve como usar parâmetros de entrada e saída para passar valores entre o SQL Server e o Visual FoxPro.
**Execution of ODBC Extensions to SQL**
Fornece informações sobre como executar extensões ODBC para SQL.
**Managing Connections with SQL Pass-Through**
Descreve como gerenciar suas conexões de servidor, fornecendo uma visão geral das várias propriedades de ambiente e conexão e como defini-las.
**Sharing Connections for Remote Data**
Descreve como o Visual FoxPro permite compartilhar um identificador de conexão para uma conexão de dados remota, o que é útil para reduzir o número de conexões ao gerenciar conexões do SQL Server e recursos do servidor.
**How to: Use Automatic Transaction Mode**
Descreve como configurar o Visual FoxPro para encapsular automaticamente cada operação de gravação de dados enviada a um servidor remoto em uma transação.
**How to: Control Transactions Manually**
Descreve como controlar transações manualmente com um servidor remoto.
**Selecting the Right Methods**
Descreve e contrasta as melhores práticas para o uso de views remotas e tecnologia SQL pass-through em sua aplicação cliente/servidor.

# Seções relacionadas
 **Working with Remote Data Using SQL Pass-Through**
Explica como você pode visualizar e controlar as propriedades de um cursor de conjunto de resultados de consulta SQL pass-through usando as funções Microsoft Visual FoxPro CURSORGETPROP( ) e CURSORSETPROP( ).
**Working with Data**
Descreve como criar aplicações eficazes com índices, tabelas e bancos de dados baseados em seus requisitos de dados.
**Handling SQL Pass-Through Errors**
Explica como recuperar informações sobre o erro para examinar o erro e determinar sua causa.
