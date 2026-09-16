# Linguagem de manipulação de banco de dados

A tabela a seguir lista comandos e funções que permitem manipular bancos de dados.

| Uso | Para |
| --- | --- |
| ADATABASES( ) Function | Coloca os nomes e caminhos de todos os bancos de dados abertos em uma matriz. |
| ADD TABLE Command | Adiciona uma tabela livre ao banco de dados atual. |
| APPEND PROCEDURES Command | Anexa stored procedures em um arquivo de texto às stored procedures no banco de dados atual. |
| AUSED( ) Function | Coloca aliases de tabela e áreas de trabalho de uma sessão de dados em uma matriz de variáveis. |
| CLOSE Commands | Fecha vários tipos de arquivo. |
| COMPILE Command | Compila os arquivos de origem especificados e cria um arquivo de objeto para cada um. |
| COPY PROCEDURES Command | Copia stored procedures no banco de dados atual para um arquivo de texto. |
| CREATE CONNECTION Command | Cria uma conexão nomeada e a armazena no banco de dados atual. |
| CREATE DATABASE Command | Cria um banco de dados e o abre. |
| CREATE SQL VIEW Command | Exibe o View Designer, onde você pode criar uma SQL view. |
| CREATE TRIGGER Command | Cria um trigger Delete, Insert ou Update para uma tabela. |
| CREATEOFFLINE( ) Function | Coloca uma view existente offline. |
| DROPOFFLINE( ) Function | Descarta todas as alterações feitas em uma view offline e coloca a view offline online novamente. |
| CURSORGETPROP( ) Function | Recupera as configurações atuais de propriedade de uma tabela ou cursor do Visual FoxPro. |
| CURSORSETPROP( ) Function | Especifica configurações de propriedade para uma tabela ou cursor do Visual FoxPro. |
| CURVAL( ) Function | Retorna valores de campo diretamente do disco para uma tabela ou fonte de dados remota. |
| DATETIME( ) Function | Retorna a data e hora atuais como um valor DateTime, ou cria um valor DateTime compatível com o ano 2000. |
| DBC( ) Function | Retorna o nome e o caminho do banco de dados atual. |
| DBGETPROP( ) Function | Recupera o valor de uma propriedade do banco de dados atual ou de campos, conexões nomeadas, tabelas ou views no banco de dados atual. |
| DBSETPROP( ) Function | Define uma propriedade do banco de dados atual ou de campos, conexões nomeadas, tabelas ou views no banco de dados atual. |
| DBUSED( ) Function | Retorna true (.T.) se o banco de dados especificado estiver aberto. |
| DELETE - SQL Command | Marca registros para exclusão. |
| DELETE CONNECTION Command | Exclui uma conexão nomeada do banco de dados atual. |
| DELETE DATABASE Command | Exclui um banco de dados do disco. |
| DELETE TRIGGER Command | Remove um trigger de uma tabela do banco de dados atual. |
| DELETE VIEW Command | Exclui uma SQL view do banco de dados atual. |
| DISPLAY CONNECTIONS Command | Exibe informações sobre as conexões nomeadas no banco de dados atual. |
| DISPLAY DATABASE Command | Exibe informações sobre o banco de dados atual ou campos, conexões nomeadas, tabelas ou views no banco de dados atual. |
| DISPLAY PROCEDURES Command | Exibe os nomes de procedures armazenadas no banco de dados atual. |
| DISPLAY TABLES Command | Exibe nomes e informações sobre todas as tabelas contidas no banco de dados atual. |
| DISPLAY VIEWS Command | Exibe informações sobre SQL views no banco de dados atual. |
| FREE TABLE Command | Remove uma referência de banco de dados de uma tabela. |
| GETFLDSTATE( ) Function | Retorna um valor numérico indicando o status de um campo em uma tabela ou cursor. |
| GETNEXTMODIFIED( ) Function | Retorna o número do registro do próximo registro modificado em uma tabela ou cursor com buffer. |
| INDBC( ) Function | Retorna se um objeto de banco de dados especificado está no banco de dados atual. |
| ISEXCLUSIVE( ) Function | Retorna se um banco de dados especificado foi aberto exclusivamente. |
| LIST CONNECTIONS Command | Exibe informações sobre as conexões nomeadas no banco de dados atual. |
| LIST DATABASE Command | Exibe informações sobre o banco de dados atual. |
| LIST PROCEDURES Command | Display the names of stored procedures in the current database. |
| LIST TABLES Command | Exibe as informações de tabela contidas no banco de dados atual. |
| LIST VIEWS Command | Display the information about SQL views in the current database. |
| MODIFY CONNECTION Command | Exibe o Connection Designer. |
| MODIFY DATABASE Command | Exibe o Database Designer. |
| MODIFY PROCEDURE Command | Abre o editor de texto do Visual FoxPro. |
| MODIFY VIEW Command | Exibe o View Designer. |
| OLDVAL( ) Function | Retorna valores originais de campos que foram modificados, mas não atualizados. |
| OPEN DATABASE Command | Abre um banco de dados. |
| PACK DATABASE Command | Remove registros marcados para exclusão do banco de dados atual. |
| REFRESH( ) Function | Atualiza dados em uma SQL view remota ou local atualizável ou cursor CursorAdapter. |
| REMOVE TABLE Command | Remove uma tabela do banco de dados atual. |
| RENAME CONNECTION Command | Renomeia uma conexão nomeada no banco de dados atual. |
| RENAME TABLE Command | Renomeia uma tabela no banco de dados atual. |
| RENAME VIEW Command | Renomeia uma SQL view no banco de dados atual. |
| REQUERY( ) Function | Recupera dados novamente para uma SQL view. |
| SET DATABASE Command | Especifica o banco de dados atual. |
| SET DATASESSION Command | Ativa a sessão de dados do formulário especificado. |
| SETFLDSTATE( ) Function | Atribui um valor de estado de modificação ou exclusão de campo a um campo ou registro em uma tabela ou cursor. |
| SQLCANCEL( ) Function | Solicita o cancelamento de uma instrução SQL em execução. |
| SQLCOLUMNS( ) Function | Armazena informações de coluna de uma tabela de fonte de dados especificada em um cursor. |
| SQLCOMMIT( ) Function | Confirma uma transação. |
| SQLCONNECT( ) Function | Estabelece uma conexão com uma fonte de dados. |
| SQLDISCONNECT( ) Function | Encerra uma conexão com uma fonte de dados. |
| SQLEXEC( ) Function | Envia uma instrução SQL para a fonte de dados, onde a instrução é processada. |
| SQLGETPROP( ) Function | Recupera as configurações atuais de uma conexão ativa. |
| SQLMORERESULTS( ) Function | Copia outro conjunto de resultados para um cursor do Visual FoxPro se mais conjuntos de resultados estiverem disponíveis. |
| SQLROLLBACK( ) Function | Cancela quaisquer alterações feitas durante a transação atual. |
| SQLSETPROP( ) Function | Especifica configurações para uma conexão ativa. |
| SQLSTRINGCONNECT( ) Function | Estabelece uma conexão com uma fonte de dados usando uma cadeia de conexão. |
| SQLTABLES( ) Function | Armazena os nomes de tabelas em uma fonte de dados em um cursor do Visual FoxPro. |
| TABLEREVERT( ) Function | Descarta alterações feitas em uma linha com buffer, tabela com buffer ou cursor. |
| TABLEUPDATE( ) Function | Confirma alterações feitas em uma linha com buffer, tabela com buffer, cursor ou cursor adapter. |
| _TRIGGERLEVEL System Variable | Contém um valor numérico somente leitura que indica o nível de aninhamento atual de procedure de trigger. |
| VALIDATE DATABASE Command | Garante que as localizações de tabelas e índices no banco de dados atual estejam corretas. |
