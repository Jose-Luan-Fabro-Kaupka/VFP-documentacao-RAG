# Como: definir conexões a fontes de dados remotas

Você pode definir e armazenar uma conexão a uma fonte de dados remota em um banco de dados do Visual FoxPro para poder usar o nome da conexão ao criar e usar uma view remota.

Criar e armazenar uma conexão nomeada em seu banco de dados não usa nenhum recurso de rede ou remoto porque o Visual FoxPro não ativa a conexão até que você use a view remota. A conexão nomeada existe somente como uma definição de conexão armazenada como uma linha no arquivo de banco de dados (.dbc) até que a conexão seja ativada.

> **Observação:** Antes de poder criar uma conexão, você deve ter um banco de dados aberto. Para obter mais informações, consulte Como: abrir bancos de dados.

### Para definir uma conexão
- Execute uma das seguintes ações: Abra o banco de dados no Database Designer. -OU- Abra o projeto do seu aplicativo no Project Manager.
- No menu File, clique em New.
- Na caixa de diálogo New, clique em Connection e, em seguida, em New File.
- No Connection Designer, selecione as opções que correspondem aos requisitos do seu servidor.
- No menu File, clique em Save para abrir a caixa de diálogo Save.
- Na caixa Connection Name, digite um nome para a conexão e clique em OK.

Para obter mais informações, consulte Connection Designer.

### Para criar uma nova conexão programaticamente
- Abra o banco de dados ou o projeto que contém o banco de dados.
- Escolha uma das seguintes opções: Para criar uma conexão usando o Connection Designer, use o comando CREATE CONNECTION com um ponto de interrogação (?). -OU- Para criar uma conexão sem abrir o Connection Designer, use o comando CREATE CONNECTION com o nome da conexão e os parâmetros necessários.

Para obter mais informações, consulte Comando CREATE CONNECTION.

Por exemplo, o código a seguir abre um banco de dados chamado MyDatabase e cria uma conexão chamada Remote_01 a uma fonte de dados remota chamada SQLRemote:

```foxpro
OPEN DATABASE MyDatabase
CREATE CONNECTION Remote_01 ;
   DATASOURCE SQLRemote USERID myUserID PASSWORD myPassword
```
