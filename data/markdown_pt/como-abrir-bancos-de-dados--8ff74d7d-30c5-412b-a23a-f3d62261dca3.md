# Como: abrir bancos de dados

Para adicionar, acessar e editar itens em um banco de dados, abra o banco de dados. Quando você abre um banco de dados, o Visual FoxPro o define como o banco de dados atual e adiciona o nome do banco de dados à lista de bancos de dados na barra de ferramentas padrão do Visual FoxPro. Por padrão, os itens que você cria ou adiciona ao banco de dados são associados ao banco de dados atual, e comandos ou funções que manipulam bancos de dados abertos operam no banco de dados atual. Você também pode definir outro banco de dados aberto como o banco de dados atual. Para mais informações, consulte Como: definir o banco de dados atual.

> **Observação:** Abrir um novo banco de dados não fecha nenhum banco de dados atualmente aberto. No entanto, o banco de dados aberto mais recentemente torna-se o banco de dados atual.

Você pode ter vários bancos de dados abertos ao mesmo tempo. Por exemplo, você pode abrir e usar vários bancos de dados ao executar vários aplicativos, cada um usando um banco de dados diferente. Você também pode querer abrir vários bancos de dados para usar informações, como controles personalizados, em um banco de dados separado do banco de dados do seu aplicativo.

> **Observação:** O Visual FoxPro pode abrir um ou mais bancos de dados automaticamente quando você executa uma consulta ou um formulário que exige a abertura de bancos de dados. Para garantir que você está trabalhando com o banco de dados correto, defina o banco de dados atual explicitamente antes de usar quaisquer comandos que operem no banco de dados atual. Para mais informações, consulte Como: definir o banco de dados atual .

Abrir o banco de dados no Database Designer permite que você visualize o esquema do banco de dados, uma representação visual do banco de dados, e trabalhe com as tabelas associadas a ele, as relações entre essas tabelas e outros itens no banco de dados. Para visualizar a estrutura do próprio arquivo de banco de dados (.dbc), consulte Como: visualizar a estrutura do banco de dados.

### Para abrir um banco de dados no Database Designer
- No menu Arquivo, clique em Abrir .
- Na caixa de diálogo Abrir, procure e selecione o arquivo de banco de dados (.dbc) que deseja abrir.
- Clique em OK . O banco de dados selecionado abre no Database Designer, que exibe todos os itens que ele contém e quaisquer relações entre eles.

Para mais informações, consulte Database Designer (Visual FoxPro).

### Para abrir um banco de dados em um projeto
- Abra o projeto no Project Manager .
- No Project Manager , expanda o nó Data, depois o nó Databases.
- Clique no nome do banco de dados que deseja abrir.
- Execute uma das seguintes opções: Para abrir o banco de dados sem abrir o Database Designer , clique em Abrir ou expanda o nó do banco de dados. -OU- Para abrir o banco de dados no Database Designer , clique em Modificar . O banco de dados selecionado abre no Database Designer, que exibe todos os itens que ele contém e quaisquer relações entre eles.

Para mais informações, consulte Janela Project Manager.

### Para abrir um banco de dados programaticamente
- Execute uma das seguintes opções: Para abrir o banco de dados sem abrir o Database Designer , use o comando OPEN DATABASE. -OU- Para abrir o banco de dados no Database Designer , use o comando MODIFY DATABASE.

Para mais informações, consulte Comando OPEN DATABASE e Comando MODIFY DATABASE.
