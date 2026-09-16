# Acessando dados remotos usando views

Você pode acessar e recuperar informações em fontes de dados remotas criando views remotas. Views remotas são semelhantes a views locais, exceto que você especifica o nome ou o nome da conexão para uma fonte de dados remota. Esta fonte de dados remota é tipicamente uma fonte de dados Open Database Connectivity (ODBC). Views remotas usam a sintaxe SQL da fonte de dados remota.

O processo geral para acessar dados remotos usando views remotas aparece da seguinte forma:
 - Estabeleça uma conexão funcional a uma fonte de dados remota válida. Uma fonte de dados remota válida é tipicamente um servidor remoto para o qual você instalou um driver ODBC e configurou um nome de fonte de dados ODBC. Para obter mais informações, consulte Como: configurar uma fonte de dados ODBC.
- No Visual FoxPro, defina a fonte de dados ou uma conexão nomeada a usar ao criar a view. Você pode definir uma conexão a uma fonte de dados e armazenar a definição em um banco de dados do Visual FoxPro para poder usar a definição de conexão ao criar uma view remota. Quando você abre a view remota, o Visual FoxPro usa a conexão nomeada associada à view para conectar à fonte de dados remota e solicitar dados da fonte de dados remota.
- Crie a view remota selecionando tabelas e campos que deseja usar da fonte de dados remota.
- Defina quaisquer propriedades que desejar para a conexão nomeada para otimizar a comunicação entre o Visual FoxPro e a fonte de dados remota.
