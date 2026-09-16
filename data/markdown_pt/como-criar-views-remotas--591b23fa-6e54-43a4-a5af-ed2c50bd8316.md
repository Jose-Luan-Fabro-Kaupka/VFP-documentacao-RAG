# Como: criar views remotas

Você pode criar views remotas especificando o nome de uma fonte de dados válida ou uma conexão que você definiu anteriormente. Para obter mais informações sobre como definir conexões, consulte Como: definir conexões com fontes de dados remotas.

> **Observação:** Se você criar uma view remota usando apenas o nome da fonte de dados, o Visual FoxPro usa as informações Open Database Connectivity (ODBC) sobre a fonte de dados para criar e ativar uma conexão com a fonte de dados. Quando você fecha a view, a conexão é fechada.

Você pode criar views remotas das seguintes maneiras:
 - Usando o Remote View Wizard. Um assistente é a maneira mais fácil de começar a criar uma view. Você pode selecionar campos de tabelas e filtrar e ordenar os registros na sua view remota. Para obter mais informações, consulte Creating Remote Views Using a Wizard .
- Usando o View Designer. O View Designer permite selecionar campos de tabelas, especificar critérios para recuperar dados e condições de junção, e filtrar, ordenar e agrupar registros para criar views ou personalizar views existentes. Para obter mais informações, consulte Creating Remote Views Using the View Designer .
- Criando views remotas programaticamente. O comando CREATE SQL VIEW permite especificar uma fonte de dados remota ou nome de conexão para que você possa criar views remotas programaticamente.

Independentemente do método que você usar, o processo básico para criar uma view é geralmente o mesmo. Para obter mais informações, consulte View Creation.

> **Observação:** Quando você cria ou usa uma view do Project Manager, o Project Manager abre o banco de dados automaticamente. No entanto, se você usar uma view fora do projeto posteriormente, deve abrir o banco de dados ou garantir que o banco de dados esteja no escopo antes de poder usar a view.

# Criando views remotas usando um assistente

Você pode criar views remotas facilmente usando um assistente. O assistente ajuda você a selecionar conexões ou fontes de dados e cria uma consulta com base nas suas respostas a uma série de perguntas.

### Para criar uma view remota com um assistente
- Execute uma das seguintes ações: Abra o banco de dados no Database Designer . -OU- Abra o projeto do seu aplicativo no Project Manager .
- No menu Tools, aponte para Wizards e clique em All Wizards .
- Na caixa de diálogo Wizard Selection, clique em Remote View Wizard e, em seguida, OK .
- Siga as instruções nas telas do assistente.

Para obter mais informações, consulte Remote View Wizard.

# Criando views remotas usando o View Designer

Você pode usar o View Designer para criar views e especificar opções adicionais ou personalizar views existentes.

> **Observação:** Para views remotas, se você unir duas ou mais tabelas no View Designer, o designer usa junções internas e coloca a condição de junção na cláusula WHERE da instrução SQL gerada pela view. Se você deseja usar uma junção externa, o View Designer fornece somente junções externas à esquerda usando a sintaxe suportada pelo ODBC. Se você precisar de junções externas à direita ou completas ou deseja usar sintaxe nativa para uma junção externa à esquerda, crie a view programaticamente.

### Para criar uma view remota
- Execute uma das seguintes ações: Abra o banco de dados no Database Designer . -OU- Abra o projeto do seu aplicativo no Project Manager .

Para obter mais informações, consulte Query and View Designers e a caixa de diálogo Select Connection or Data Source.

Depois de selecionar tabelas, você precisa selecionar os campos que contêm os dados que deseja recuperar para sua view. Para obter mais informações, consulte Como: selecionar campos para views.

# Criando views remotas programaticamente

Você pode criar views remotas programaticamente abrindo o View Designer ou especificando uma instrução SQL SELECT.

### Para criar uma view remota programaticamente
- Abra o banco de dados ou projeto ao qual deseja adicionar a view remota.
- Escolha uma das seguintes opções: Para selecionar uma fonte de dados ou nome de conexão, escolher tabelas e abrir o View Designer, use o CREATE SQL VIEW somente com a cláusula REMOTE. -OU- Para criar uma view remota sem abrir o View Designer, use o CREATE SQL VIEW com uma cláusula CONNECTION e a cláusula AS para especificar a instrução SQL SELECT que deseja usar. Observação Para corresponder registros relacionados entre as tabelas, você deve especificar uma condição de junção na cláusula FROM ou WHERE da instrução SQL usada no comando CREATE SQL VIEW. Se existirem relacionamentos persistentes entre as tabelas, eles são automaticamente usados como condições de junção. As tabelas que você seleciona aparecem no View Designer e no Database Designer . Você pode precisar fechar e reabrir os designers para atualizá-los.

Para obter mais informações, consulte o comando CREATE SQL VIEW.

Você pode visualizar conexões disponíveis usando o comando DISPLAY CONNECTIONS. Para obter mais informações, consulte o comando DISPLAY CONNECTIONS.

Por exemplo, o código a seguir abre um banco de dados chamado MyDatabase em um servidor remoto e cria uma view remota de uma tabela chamada MyRemoteTable usando uma conexão predefinida chamada Remote_01:

```foxpro
OPEN DATABASE MyDatabase
CREATE SQL VIEW MyRemoteTable_Remote_View ;
   CONNECTION Remote_01 AS SELECT * FROM MyRemoteTable
```

Você também pode especificar um nome de fonte de dados em vez de nome de conexão.
