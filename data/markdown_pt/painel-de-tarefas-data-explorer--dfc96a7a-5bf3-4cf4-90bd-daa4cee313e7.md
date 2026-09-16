# Painel de tarefas Data Explorer

O Painel de tarefas Data Explorer é usado para abrir conexões de dados e fazer logon em servidores e explorar seus bancos de dados. Você pode clicar com o botão direito nos nós para executar várias ações nos elementos de dados representados por esses nós. Você pode arrastar nós do Data Explorer e soltá-los em designers e editores do Visual FoxPro. Isso cria novos controles de dados em formulários ou código pré-configurado para referenciar o item solto.

Para acessar o Painel de tarefas Data Explorer, selecione Task Pane no menu Tools para abrir o Task Pane Manager. Escolha o Painel de tarefas Data Explorer na caixa de listagem suspensa Task Panes na parte superior.

O Data Explorer também é um aplicativo autônomo e pode ser executado fora do gerenciador Task Pane. Para executar o Data Explorer como um aplicativo separado, execute o seguinte comando na janela Command.

```foxpro
DO HOME() + DATAEXPLORER.APP
```

> **Observação:** O Data Explorer armazena suas conexões e configurações em uma tabela chamada DataExplorer.dbf, que é armazenada no seu diretório de dados do usuário (consulte HOME(7) ).

# Usando o Data Explorer

O Data Explorer é muito fácil de usar. Tem uma interface simples que facilita a visualização e o trabalho com dados remotos. A operação básica do Data Explorer é a seguinte:
 - Você cria uma conexão com seus dados remotos, como um banco de dados SQL Server. Isso é feito usando o botão Add Connection.
- A conexão aparece como um nó sob o nó raiz Connections e é persistida para uso futuro.
- Você pode expandir nós e visualizar todos os componentes da sua conexão de dados. Quando você seleciona um nó, informações detalhadas sobre esse nó são mostradas no painel de descrição na parte inferior.
- Você pode clicar com o botão direito em nós individuais para executar ações como navegar em uma tabela, examinar uma definição de view ou editar um procedimento armazenado.
- Você pode arrastar e soltar nós em editores do Visual FoxPro e ter código adicionado para esse nó específico. Você também pode arrastar e soltar em um form designer e ter um controle apropriado solto para representar o nó.

Use o Data Explorer para executar diferentes ações com seus dados remotos. A seguir está uma lista de algumas das ações mais comuns:
 **Adicionar uma nova conexão**
Adicione uma nova conexão à sua fonte de dados remota clicando em Add Connection ou clicando com o botão direito no nó raiz Connections e selecionando o item de menu Add Connection…. Quando a caixa de diálogo Add Connection aparecer, selecione um tipo de conexão. Depois de escolher um tipo de conexão, você será solicitado a fornecer mais detalhes sobre sua fonte de dados. Se você selecionar um tipo de conexão SQL ou ADO, será solicitado com uma caixa de diálogo Connection Properties.
**Acessar um SQL Server existente**
O nó raiz SQL Servers é uma maneira conveniente de explorar e acessar SQL Servers disponíveis na sua rede. Basta clicar no nó raiz para expandir e visualizar todos os servidores disponíveis. Observação Muitas vezes é mais conveniente criar uma conexão separada para um banco de dados SQL Server específico do que acessá-lo pelo nó raiz SQL Servers. Uma conexão separada também fornecerá acesso mais rápido.
**Modificar uma conexão existente**
Depois que a conexão é adicionada ao Data Explorer, ela é persistida para que esteja disponível na próxima vez que você iniciar o Visual FoxPro. Você pode fazer modificações na conexão clicando com o botão direito no nó de conexão e selecionando o item de menu Properties.
**Trabalhar com bancos de dados**
Se você selecionar um tipo de conexão SQL Server, os nós abaixo da conexão serão bancos de dados. Com bancos de dados, você pode expandir o nó para ver vários itens, incluindo tabelas, views, procedimentos armazenados e funções. Se estiver usando uma conexão SQL ou ADO, você pode arrastar e soltar um nó de banco de dados em um programa e o código será inserido que trata a conexão e configura um objeto CursorAdapter para recuperar dados.
**Trabalhar com tabelas**
Você pode expandir o nó Tables para ver uma lista de todas as tabelas na sua fonte de dados. Informações sobre essa tabela, como o proprietário ou localização, são exibidas no painel de descrição. Você pode expandir ainda mais um nó de tabela para visualizar seus campos. Para visualizar os dados, você pode clicar com o botão direito no nó de tabela desejado e selecionar o menu Browse. Para executar uma consulta mais avançada, selecione o menu Run Query. Se você estiver trabalhando com uma tabela Fox, pode clicar com o botão direito e selecionar Design para abrir o Table Designer. Observação Por meio da arquitetura de extensibilidade, você pode adicionar suporte de design para fontes de dados remotas, como SQL Server. Quando você arrasta e solta uma tabela em um form ou class designer, um controle Grid para essa tabela é adicionado. Observação Você ainda precisará adicionar código ou objetos de ambiente de dados para conectar à fonte de dados remota. Quando você arrasta e solta uma tabela em uma janela de edição, o código é inserido para visualizar essa tabela: Se você arrastar de uma tabela Fox, uma instrução SELECT simples é inserida. Se você arrastar de uma conexão SQL ou ADO, o código também é inserido que trata a conexão e configura um objeto CursorAdapter para recuperar dados.
**Trabalhar com views**
Você pode expandir o nó Views para ver uma lista de todas as views na sua fonte de dados. Informações sobre essa view, como o proprietário, são exibidas no painel de descrição. Você pode expandir ainda mais um nó de view para ver seus campos. Para visualizar os dados, você pode clicar com o botão direito no nó desejado e selecionar o menu Browse. Para executar uma consulta mais avançada, selecione o menu Run Query. Para ver a definição dessa view, selecione o menu View Definition. Observação Certos tipos de conexão, como uma conexão ADO para SQL Server, podem não exibir esta opção. Se você estiver trabalhando com uma view Fox, pode clicar com o botão direito e selecionar Design para abrir o View Designer. Observação Por meio da arquitetura de extensibilidade, você pode adicionar suporte de design para fontes de dados remotas, como SQL Server. Quando você arrasta e solta uma view em um form ou class designer, um controle Grid para essa view é adicionado. Observação Você ainda precisará adicionar código ou objetos de ambiente de dados para conectar à fonte de dados remota. Quando você arrasta e solta uma view em uma janela de edição, o código é inserido para navegar nessa view: Se você arrastar de uma view Fox, uma instrução SELECT simples é inserida. Se você arrastar de uma conexão SQL ou ADO, o código também é inserido que trata a conexão e configura um objeto CursorAdapter para recuperar dados.
**Trabalhar com campos**
Você pode expandir um nó Table ou View para ver uma lista de seus campos. Informações sobre esse campo, como o tipo de dados, são exibidas no painel de descrição. Se Column Info estiver marcado para essa conexão, o tipo de dados é exibido no nó de campo. Observação Certos tipos de conexão podem não oferecer suporte à exibição de detalhes de campo. Para executar uma consulta, selecione o menu Run Query. Quando você arrasta e solta um campo em um form ou class designer, um controle Textbox para esse campo é adicionado. Observação Você ainda precisará adicionar código ou objetos de ambiente de dados para conectar à fonte de dados remota. Quando você arrasta e solta um campo em uma janela de edição, o código é inserido para navegar nesse campo: Se você arrastar de um campo Fox, uma instrução SELECT simples é inserida. Se você arrastar de uma conexão SQL ou ADO, o código também é inserido que trata a conexão e configura um objeto CursorAdapter para recuperar dados.
**Trabalhando com procedimentos armazenados**
Você pode expandir o nó Stored Procedures para ver uma lista de todos os procedimentos armazenados na sua fonte de dados. Informações sobre o procedimento armazenado, como o proprietário, são exibidas no painel de descrição. Você pode expandir ainda mais um nó de procedimento armazenado individual para ver seus parâmetros. Observação Certos tipos de conexão podem não oferecer suporte a esta opção. Para executar o procedimento armazenado, você pode clicar com o botão direito nesse nó e selecionar o menu Run Stored Procedure. Se o procedimento armazenado requer parâmetros, uma caixa de diálogo solicita que você insira parâmetros. Os resultados são exibidos na janela Run Query, onde você pode modificar e executar seu procedimento novamente. Para executar seu procedimento com mais controle sobre a sintaxe de chamada, selecione o menu Run Query. Para ver a definição do procedimento, selecione o menu View Definition. Para editar um procedimento, selecione o menu Edit Procedure. Para excluir um procedimento, selecione o menu Delete Procedure. Para adicionar um novo procedimento, selecione o menu New Procedure. Você pode arrastar e soltar um procedimento armazenado de conexão SQL ou ADO em uma janela de edição. Ao fazer isso, o código é inserido que trata a conexão e chama o procedimento. Para procedimentos de conexão SQL, o código também inclui a configuração de um objeto CursorAdapter para recuperar dados do procedimento armazenado.
**Trabalhar com funções**
Você pode expandir o nó Functions para ver uma lista de todas as funções na sua fonte de dados. Informações sobre a função, como o proprietário, são exibidas no painel de descrição. Você pode expandir ainda mais um nó de função individual para ver seus parâmetros. Observação Certos tipos de conexão, como uma conexão Fox, podem não oferecer suporte a esta opção. Para chamar a função, você pode clicar com o botão direito no nó desejado e selecionar o menu Run Stored Procedure. Se o procedimento armazenado requer parâmetros, uma caixa de diálogo solicita que você insira parâmetros. Os resultados são exibidos na janela Run Query, onde você pode modificar e executar seu procedimento novamente. Para executar sua função com mais controle sobre a sintaxe de chamada, selecione o menu Run Query. Para ver a definição da função, selecione o menu View Definition. Para editar um procedimento, selecione o menu Edit Function. Para excluir um procedimento, selecione o menu Delete Function. Para adicionar um novo procedimento, selecione o menu New Function. Você pode arrastar e soltar uma função de conexão SQL ou ADO em uma janela de edição. Ao fazer isso, o código é inserido que trata a conexão e chama a função.
**Usar a janela Run Query**
Quando você seleciona o item de menu Run Query, a janela Run Query é exibida e contém comandos relevantes para o nó selecionado. Por exemplo, se você abrir a janela Run Query para uma tabela, a caixa de edição contém uma instrução SELECT para essa tabela. Se você escolher um procedimento armazenado, uma instrução EXEC (aplicável a SQL) será mostrada. Com a janela Run Query, você pode digitar uma consulta, executá-la para ver os resultados e executar tarefas adicionais de add-in, como copiar os resultados para a área de transferência. Para executar uma consulta, insira um comando de consulta, como uma instrução SELECT ou EXEC, e clique no botão Run. Os resultados serão exibidos na parte inferior da janela.
**Definir um filtro**
Você pode selecionar o menu Filter para definir um filtro que exiba somente nós filhos que correspondam ou não correspondam aos critérios especificados. Por exemplo, você pode querer filtrar todas as tabelas que começam com "sys" para excluir tabelas do sistema.
**Atualizar nós de dados**
Se você clicar com o botão direito em um nó, pode selecionar o menu Refresh para que todos os nós filhos sejam atualizados.

# Caixa de diálogo Add Connection

O botão Add Connection abre a caixa de diálogo Add Connection para que você possa criar uma nova conexão persistida. Você pode escolher entre fontes de dados SQL Server, Visual FoxPro ou ADO. Os seguintes tipos estão disponíveis nesta caixa de diálogo:

| Tipo de conexão | Descrição |
| --- | --- |
| SQL Server | Uma conexão a um SQL Server. O nó de conexão exibirá nós separados para cada banco de dados nesse servidor. |
| SQL Database | Uma conexão a um banco de dados SQL Server. |
| FoxPro Directory | Uma conexão a um diretório. O nó de conexão exibe nós separados para cada banco de dados Visual FoxPro (.dbc). |
| FoxPro Database | Uma conexão a um banco de dados Visual FoxPro. |
| FoxPro Table | Uma conexão a uma tabela Visual FoxPro. |
| ADO Connection | Uma conexão a uma fonte de dados ADO. Observação Se você estiver criando conexões ADO para SQL Server, é recomendado usar um dos tipos de conexão SQL Server, pois há mais funcionalidade disponível, como itens adicionais de menu de atalho. |

# Caixa de diálogo SQL Connection Properties

A caixa de diálogo SQL Connection Properties é usada para especificar informações de conexão a um banco de dados SQL Server. Esta caixa de diálogo aparece quando você cria uma conexão SQL pela primeira vez para o tipo de conexão SQL Server ou SQL Database. Você pode abrir esta caixa de diálogo posteriormente e fazer alterações depois que a conexão é criada clicando com o botão direito no nó de conexão específico e selecionando o item de menu Properties.
 **Server Name**
Você pode digitar o nome do SQL Server diretamente na caixa de combinação ou selecionar um na caixa de listagem suspensa. A caixa de listagem suspensa contém a mesma lista de servidores que aparecem sob o nó SQL Servers.
**Database**
Depois de escolher um SQL Server, você pode escolher um banco de dados para sua conexão. Esta opção está disponível somente para uma conexão SQL Database. Observação Você pode ser solicitado a inserir uma combinação Login/Password se a Trusted Connection atual não permitir acesso à lista de bancos de dados do servidor selecionado.
**Use Trusted Connection**
Selecione isto para usar suas credenciais de logon do Windows para conectar ao SQL Server.
**Login**
Se você desmarcar Use Trusted Connection , pode especificar um nome de logon SQL para usar na conexão.
**Password**
Se você desmarcar Use Trusted Connection , pode especificar uma senha de logon SQL para usar na conexão.
**Connection Timeout**
Especifica o tempo de espera (segundos) antes de retornar um erro de tempo limite de conexão. Se você especificar 0, a espera é indefinida e nenhum erro de tempo limite é retornado. O valor pode ser de 0 a 600. Observação Isso é equivalente a usar SQLSETPROP(0, "ConnectTimeOut", nTimeout) antes de estabelecer a conexão.
**Query Timeout**
Especifica o tempo de espera (segundos) antes de retornar um erro geral de tempo limite. Se você especificar 0, a espera é indefinida e nenhum erro de tempo limite é retornado. O valor pode ser de 0 a 600. Observação Isso é equivalente a usar SQLSETPROP(nHandle, "QueryTimeOut", nTimeout) antes de executar a consulta.
**Show Column Info**
Exibe o tipo e o comprimento da coluna ao lado do nome da coluna em cada nó de coluna.
**Sort Objects**
Ordena objetos abaixo da conexão por nome.

# Caixa de diálogo ADO Connection Properties

A caixa de diálogo ADO Connection Properties é usada para especificar informações de conexão a uma fonte de dados ADO (OLE DB Provider). Esta caixa de diálogo aparece quando você cria uma conexão ADO pela primeira vez. Você pode abrir esta caixa de diálogo posteriormente e fazer alterações depois que a conexão é criada clicando com o botão direito no nó de conexão específico e selecionando o item de menu Properties.
 **Use DSN**
Especifique uma conexão usando um DSN existente. Insira as informações necessárias do OLE DB Provider selecionando uma fonte de dados disponível na caixa de listagem suspensa e, opcionalmente, inserindo um User ID e Password.
**Use Connection String**
Insira uma cadeia de conexão válida. O botão Build está disponível para auxiliar na geração da cadeia de conexão. Este botão abre a caixa de diálogo padrão Data Link Properties, onde você pode escolher um OLE DB Provider registrado.
**Connection Timeout**
Especifica o tempo de espera (segundos) antes de retornar um erro de tempo limite de conexão. Se você especificar 0, a espera é indefinida e nenhum erro de tempo limite é retornado. O valor pode ser de 0 a 600. Observação Isso é equivalente a usar SQLSETPROP(0, "ConnectTimeOut", nTimeout) antes de estabelecer a conexão.
**Query Timeout**
Especifica o tempo de espera (segundos) antes de retornar um erro geral de tempo limite. Se você especificar 0, a espera é indefinida e nenhum erro de tempo limite é retornado. O valor pode ser de 0 a 600. Observação Isso é equivalente a usar SQLSETPROP(nHandle, "QueryTimeOut", nTimeout) antes de executar a consulta.
**Show Column Info**
Exibe o tipo e o comprimento da coluna ao lado do nome da coluna em cada nó de coluna.

# Janela Run Query

A janela Run Query é uma parte central do Data Explorer. Ela permite executar consultas no nó de dados selecionado. Você também pode executar procedimentos armazenados e funções. Para executar uma consulta, execute as seguintes etapas:
 - Clique com o botão direito em um nó de dados cujos dados você deseja consultar e selecione o menu Run Query.
- Se houver texto na caixa de edição superior, você pode clicar no botão Run para executar a consulta. Se nenhum texto for exibido, insira uma consulta, como uma instrução SELECT, e clique em Run .
- Os resultados da sua consulta aparecerão na metade inferior da janela Run Query em uma grade. Se a consulta não foi bem-sucedida, um erro aparecerá no painel de resultados inferior. Você pode editar sua consulta para corrigir o problema e clicar em Run para consultar novamente.
- A janela Run Query também permite executar procedimentos armazenados e funções. Se estes retornarem conjuntos de resultados, como do SQL Server, serão exibidos em uma grade. Caso contrário, os resultados são armazenados no painel de resultados.
- A janela Run Query oferece suporte à extensibilidade de add-in que permite ações personalizadas na consulta ou nos resultados de dados. Add-ins gerenciados usando o Add-In Manager ( caixa de diálogo Options), aparecem como botões acima da caixa de edição de consulta e do painel de resultados. Você também pode acessar add-ins clicando com o botão direito na caixa de edição de consulta.

Os seguintes add-ins estão incluídos com o Visual FoxPro e podem ser modificados usando o Add-In Manager:

| Add-In | Descrição |
| --- | --- |
| Save Query | Você pode salvar o texto da consulta atual em um arquivo de texto com extensão .SQL. Este é um add-in de consulta. |
| Load Query | Você pode carregar uma consulta salva anteriormente de um arquivo de texto. Este é um add-in de consulta. |
| Format for VFP | Isso modifica a consulta atual para adicionar um caractere de continuação (;) ao final de todas as linhas, remover quaisquer linhas em branco e converter quaisquer comentários SQL "--" para "&&". Além disso, todos os colchetes ao redor de palavras são removidos. Isso é útil se você tem uma instrução SQL originalmente escrita para SQL Server e deseja executá-la em dados do Visual FoxPro. Por exemplo, a seguinte consulta: SELECT [au_lname] FROM [pubs] -- retrieve all last names é reformatada como: SELECT au_lname ; FROM pubs && retrieve all last names Este é um add-in de consulta. |
| Format for SQL | Isso modifica a consulta atual para remover quaisquer caracteres de continuação de fim de linha (;), converter quaisquer linhas de comentário VFP que começam com "*" em linhas de comentário SQL começando com "--", alterar aspas duplas para aspas simples e alterar duplo igual (==) para igual simples (=). Isso é útil se você está modificando uma consulta originalmente escrita para dados VFP para executar em dados SQL Server. Este é um add-in de consulta. |
| Clipboard to Variable | Copia a consulta para a área de transferência formatada com atribuição de variável. Este é um add-in de consulta. |
| Clipboard to TEXT/ENDT | Copia a consulta para a área de transferência formatada com o comando TEXT ... ENDTEXT . Este é um add-in de consulta. |
| Copy Results to Clipboard. | Os dados exibidos na grade são copiados para a área de transferência. Este é um add-in de resultado de dados. |

# Caixa de diálogo Options
 - A caixa de diálogo Options permite personalizar o Data Explorer e os comportamentos de conexão.
 **Font**
Define a fonte padrão usada pelo Data Explorer.
**Show Description Pane**
Exibe um painel de descrição na parte inferior do Data Explorer.
**Show Column Info**
Mostra informações de tipo de dados de coluna nos nós de coluna. Esta é a configuração padrão para novas conexões. Você pode alterar isso posteriormente na caixa de diálogo Connection Properties. Observação Se o painel de descrição estiver visível, as informações de tipo de dados de coluna são exibidas lá para a coluna selecionada.
**Manage Add-Ins**
Abre o Add-Ins Manager.
**Manage Menus**
Abre o Menu Manager.
**Manage DragDrop**
Abre o DragDrop Manager.
**Restore to Default**
Restaura o Data Explorer às suas configurações padrão. Um backup da tabela DataExplorer.dbf original é feito com o nome DataExplorerBackup_xx.dbf, onde xx é um número sequencial para que backups anteriores não sejam substituídos.

# Add-In Manager

A janela Run Query permite adicionar novos e personalizar add-ins existentes para trabalhar com suas consultas, bem como os resultados de dados da consulta. Esses add-ins aparecem na janela Run Query como botões. Add-Ins são armazenados na sua tabela de configurações DataExplorer.dbf.
 **Query Add-Ins**
Add-Ins que aparecem na parte superior da janela Run Query e se aplicam à consulta.
**Data Results Add-Ins**
Add-Ins que aparecem na parte inferior da janela Run Query e se aplicam aos resultados que aparecem depois que a consulta é executada.
**Add-In List**
Lista de todos os Add-Ins registrados. Quando você seleciona um add-in, seus detalhes aparecem nos controles à direita.
**New**
Cria um novo add-in.
**Delete**
Remove um add-in.
**Move Up/Move Down**
Use as setas para mover um add-in selecionado para cima ou para baixo na ordem da lista. Isso controla a posição em que o add-in aparece na janela Run Query.
**Add-In**
Especifica o nome descritivo completo do add-in.
**Abbreviated Name**
Especifica como o add-in é exibido na barra de menu.
**Select Image**
Selecione a imagem a ser associada ao add-in atualmente selecionado.
**Script Code Editbox**
Especifica o código a executar quando o add-in é selecionado. O script deve aceitar um parâmetro, que é um objeto contendo o texto da consulta, uma referência ao objeto de gerenciamento de dados e uma referência ao mecanismo DataExplorer.
**Modify**
Abre a janela do editor para modificar o script se você desejar uma janela de edição maior.

# Menu Manager

O Menu Manager permite personalizar itens de menus de atalho disponíveis para nós específicos. Menus são armazenados na sua tabela de configurações DataExplorer.dbf.
 **Menu List**
Lista de todos os menus registrados. Quando você seleciona um menu, seus detalhes aparecem nos controles à direita.
**New**
Cria um novo item de menu de atalho.
**Copy**
Cria um novo item de menu de atalho usando a definição do item selecionado.
**Delete**
Exclui um item de menu de atalho.
**Move Up/Move Down**
Use as setas para mover um menu selecionado para cima ou para baixo na ordem da lista. Isso controla a posição em que o item de menu aparece no menu de atalho de um nó.
**Caption**
Especifica o nome do menu personalizado conforme aparece no menu de contexto do nó. Use "\-" para criar um separador de menu.
**Additional Info**
Permite categorizar facilmente itens de menu. Isso é exibido como a segunda coluna na lista de itens de menu.
**Template**
Modelo opcional de código que pode ser referenciado no código de script do menu. Clique no botão Modify para abrir o código em uma janela de edição.
**Display Only**
Esta página permite controlar quais nós exibirão o menu. A caixa de texto Display only… permite incluir uma lista separada por vírgulas de nomes de nós (classes) que podem exibir o menu. Você pode especificar um asterisco no final de qualquer nome de nó para especificar quaisquer nós que comecem com o texto.
**Code to Determine…**
Código que é executado para classes de nós especificadas incluídas na caixa de texto Display Only que pode ser usado adicionalmente para filtrar se um menu é exibido ou não. Isso é particularmente útil se você deseja limitar um menu a apenas certos Providers com conexões ADO. O código deve aceitar um único parâmetro de objeto contendo informações sobre o nó. Clique no botão Modify para abrir o código em uma janela de edição.
**Script To Run**
Código a executar quando o item de menu é selecionado. O código deve aceitar um único parâmetro de objeto contendo informações sobre o nó. Clique no botão Modify para abrir o código em uma janela de edição.

# DragDrop Manager

O DragDrop Manager permite personalizar o comportamento de arrastar e soltar para nós especificados. Ações de arrastar e soltar são armazenadas na sua tabela de configurações DataExplorer.dbf.
 **DragDrop Item List**
Lista de todas as ações de arrastar e soltar registradas. Quando você seleciona um item, seus detalhes aparecem nos controles à direita.
**New**
Cria um novo item de arrastar e soltar.
**Copy**
Cria um novo item de arrastar e soltar usando a definição do item selecionado.
**Delete**
Exclui um item de arrastar e soltar.
**Move Up/Move Down**
Use as setas para mover um item selecionado para cima ou para baixo na ordem da lista. Isso controla a ordem em que o código da ação é executado.
**Caption**
Especifica o nome do item de arrastar e soltar para referência futura.
**Template**
Modelo opcional de código que pode ser referenciado no código de script. Clique no botão Modify para abrir o código em uma janela de edição.
**Execute Only**
Especifica uma lista separada por vírgulas de nomes de nós para aplicar a ação de arrastar e soltar. Se isso for deixado em branco, a verificação de nó não é executada. Você pode incluir um asterisco no final de qualquer nome de nó para especificar quaisquer nós que comecem com o texto.
**Script To Run**
Código a executar quando você arrasta e solta de um nó para uma janela de edição. O código deve aceitar um único parâmetro de objeto contendo informações sobre o nó. Se você deseja especificar texto a inserir, precisa definir a propriedade DropText do objeto de parâmetro. Clique no botão Modify para abrir o código em uma janela de edição.

# Extendendo o Data Explorer

O Data Explorer fornecido com o Visual FoxPro inclui suporte para muitas necessidades centrais de dados remotos. Com a arquitetura de extensibilidade, você pode adicionar capacidades adicionais não disponíveis atualmente, como a capacidade de modificar tabelas ou views remotas por meio de um designer personalizado. Além disso, você pode adicionar suporte para novas fontes de dados remotas conforme ficarem disponíveis no futuro (como novas versões do SQL Server).

O Data Explorer pode ser extendido adicionando, removendo ou substituindo classes de nó ou classes de gerenciador de conexão. Cada uma delas é definida na tabela DataExplorer, que está localizada no diretório de dados do usuário (consulte Função HOME( )). Se a tabela não for encontrada, ela é criada automaticamente usando a tabela DataExplorerDefault.dbf que está vinculada ao aplicativo DataExplorer.

> **Observação:** Se você deseja fazer modificações ou aprimoramentos no Data Explorer, pode encontrar a origem em XSource.zip contido na pasta Tools\XSource.
 **DataExplorer.dbf**
Grande parte da extensibilidade do Data Explorer é tratada por meio desta tabela para que você não precise fazer modificações no arquivo DataExplorer.app. Todas as personalizações definidas pelos vários gerenciadores na caixa de diálogo Options são armazenadas nesta tabela. A tabela a seguir contém detalhes sobre a extensão da tabela de configurações do Data Explorer:

| Fieldname | Type | Descrição |
| --- | --- | --- |
| UniqueID | C(25) | Um ID exclusivo para o registro criado. Deve estar no formato: vendor.id Por exemplo: microsoft.textscraps |
| DefType | C(1) | A definição do registro: R = Root S = Data Source C = Connection M = Menu P = Picture T = Template Q = Query Add-in Z = Data Add-in E = Expanded Info Y = Drop Action, Code Window V = Drop Action, Design Surface |
| ConnType | C(25) | Tipo de conexão para uma conexão criada pelo usuário. |
| ConnName | C(100) | Nome da conexão. |
| ConnInfo | M | Informações de conexão. |
| ClassName | M | Nome da classe. |
| ClassLib | M | Nome e localização da biblioteca de classes. |
| ScriptCode | M | Código de script a executar. |
| DisplayOrd | I | Ordem de exibição. |
| Options | M | Dados opcionais para registro DefType específico. |
| OptionData | M | Contém configurações de nó que podem ser personalizadas pelo usuário. Isso se aplica a nós Connection e Root. Para conexões, propriedades de conexão são armazenadas neste campo. |
| Template | M | Pode ser usado por add-ins. |
| WhenNodes | M | Lista separada por vírgulas de nós aos quais um add-in de menu se aplica. |
| WhenCode | M | Código de script a executar ao determinar se um add-in de menu deve ser exibido. |
| AddinImage | W | Imagem a exibir para o add-in. |
| Inactive | L | Se definido como TRUE (.T.), o registro é ignorado. |
| User | M | Definido pelo usuário. |
| Modified | T | Última modificação. |

A tabela a seguir contém detalhes sobre os diferentes valores do campo DefType na tabela Data Explorer:

| Valor DefType | Descrição |
| --- | --- |
| R | Root. Contém detalhes sobre o nó raiz. Data Connections e SQL Servers são os nós raiz predefinidos. |
| S | Data Source. Especifica um tipo de conexão válido que pode ser feito. As seguintes colunas são utilizadas: ConnName - nome amigável da fonte de dados, como "SQL Server." ClassName - nome da classe responsável por representar o nó. Esta classe deve derivar de IConnectionNode de TreeNodes.prg. ClassLib - nome e localização da biblioteca de classes onde ClassName pode ser encontrada. |
| C | Connection. Contém uma conexão criada pelo usuário. |
| M | Menu. Especifica uma opção de menu de clique com o botão direito disponível para um nó. ConnName - nome da opção de menu conforme aparece no menu de clique com o botão direito. ScriptCode - código a executar quando esta opção de menu é selecionada. WhenNodes - lista separada por vírgulas de nós aos quais o add-in de menu se aplica. WhenCode - código a executar para determinar se o menu deve ser exibido (chamado somente se passar no teste WhenNodes). Template - informações adicionais que podem ser usadas pelo item de menu. DisplayOrd - ordem relativa em que o item de menu deve ser exibido no menu de atalho. Se a primeira palavra de ScriptCode for 'THIS.', então o DataExplorer assume que é um método da classe de gerenciamento de dados e será executado somente se encontrar o nome do método especificado como membro desse objeto. Se o DataExplorer encontrar um método chamado <MethodName>Okay() , então o DataExplorer chama este método primeiro para determinar se a opção de menu deve ser visível ou não (e retorna TRUE se deve ser incluída). Se a primeira palavra de ScriptCode não for 'THIS.' então o código é executado normalmente. |
| P | Picture. Contém imagem usada para representar um determinado nó. ConnInfo - localização relativa da imagem, como "bitmaps\column.bmp." |
| T | Template (reservado para o futuro). |
| Q | Query Add-In. Este é um add-in de consulta da janela Run Query que aparece como um botão na parte superior da janela ou no menu de atalho. Os seguintes campos são usados. ConnName - nome da opção de menu conforme aparece no menu de clique com o botão direito e na barra de add-in. ConnInfo - nome descritivo do add-in conforme aparece em uma dica de ferramenta. ScriptCode - código a executar quando esta opção de menu é selecionada. DisplayOrd - ordem relativa em que o add-in deve ser exibido no menu. |
| Z | Data Add-In. Este é um add-in de dados da janela Run Query que aparece como um botão na parte inferior da janela. Consulte Query Add-In acima para mais detalhes sobre os campos usados. |
| E | Expanded Info (reservado para o futuro). Armazena quais nós estão expandidos quando o Data Explorer é fechado para que os mesmos nós possam ser expandidos quando reiniciado. Esta informação é armazenada na coluna OptionData. |
| Y | DragDrop Action for Code Window. ConnName - nome da ação DragDrop conforme aparece no DragDrop Manager. ScriptCode - código a executar para a ação DragDrop. WhenNodes - lista separada por vírgulas de nós aos quais a ação DragDrop se aplica. Template - informações adicionais que podem ser usadas pela ação DragDrop. DisplayOrd - ordem relativa em que a ação DragDrop é executada. |
| V | DragDrop Action for Design Surface. Consulte o item anterior para detalhes. |
 **Personalizando conexões ADO**
O Data Explorer contém suporte para tratamento genérico de conexão ADO. No entanto, você pode querer personalizar para um tipo de conexão específico. Na verdade, o Data Explorer contém um exemplo disso usando Oracle. Aqui estão as etapas que você precisa fazer para adicionar este tipo de personalização: Crie uma nova classe baseada na classe central ADO Data Management. Aqui está um exemplo do Oracle em Datamgmt_Oracle.prg: DEFINE CLASS OracleDatabaseMgmt AS ADODatabaseMgmt OF DataMgmt_ADO.prg Nesta classe, você pode especificar comportamentos como como popular nós ou funcionalidade de menu de clique com o botão direito. Você pode recompilar o DataExplorer.app com sua nova classe ou apenas deixá-la externa. Você precisa referenciar esta classe em seu DataExplorer.dbf para que possa ser usada. Para fazer isso: Abra a tabela DataExplorer.dbf do seu local HOME(7) e localize o registro ADO Connection (Deftype="S"). Abra o campo memo ScriptCode Adicione outra instrução CASE ao código existente (abaixo) para seu provedor específico junto com as informações da classe personalizada. LPARAMETERS oParam, oConn IF TYPE("oConn") == 'O' AND !ISNULL(oConn) DO CASE CASE ATC("ORACLE", oConn.DBMSName) > 0 oParam.DataMgmtClass = "OracleDatabaseMgmt" oParam.DataMgmtClassLibrary = "DataMgmt_Oracle.prg" oParam.ProviderName = "ORACLE" CASE ATC("SQL Server", oConn.DBMSName) > 0 oParam.ProviderName = "SQLSERVER" CASE ATC("FOXPRO", oConn.DBMSName) > 0 oParam.ProviderName = "FOXPRO" ENDCASE ENDIF Para adicionar funcionalidade personalizada de menu de clique com o botão direito e arrastar e soltar, use os gerenciadores específicos disponíveis na caixa de diálogo Options. Para dicas, dê uma olhada nos itens existentes nos vários gerenciadores.
