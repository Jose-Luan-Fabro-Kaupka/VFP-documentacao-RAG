# Passo a passo: recuperar dados de diferentes fontes de dados

Você pode recuperar dados usando vários tipos de conexão de fonte de dados. Você pode então criar cursors ou cursor adapters do Visual FoxPro usando os dados recuperados. Cursor adapters podem recuperar dados de uma gama mais ampla de fontes de dados do que é possível com cursors convencionais.

Este passo a passo explica como construir um ambiente de dados para um formulário do Visual FoxPro configurando uma fonte de dados e, se necessário, um tipo de conexão que se aplica a todos os cursor adapters no ambiente de dados usando o DataEnvironment Builder. Você pode então criar cursors no ambiente de dados que tenham propriedades específicas para acessar dados usando o CursorAdapter Builder.

Este passo a passo contém as seguintes seções:
 - Pré-requisitos
- Abrindo o ambiente de dados de um formulário
- Definindo tipos de fonte de dados e fontes de dados
- Recuperando dados para cursor adapters
- Usando o cursor adapter no formulário

Para obter mais informações sobre cursor adapters, consulte Data Access Management Using CursorAdapters, CursorAdapter Class, DataEnvironment Builder e CursorAdapter Builder.

# Pré-requisitos

Este passo a passo requer o seguinte:
 - Fontes de dados usando os seguintes tipos de conexão: Native Use o banco de dados de exemplo Northwind incluído com o Visual FoxPro e localizado no diretório ...\Samples\Northwind. ODBC ou ADO Configure o acesso a um servidor SQL local ou remoto (SQL Server 7 ou 2000) com o banco de dados Northwind instalado. XML Use o arquivo DataSet GetCustomers.XML incluído com o Visual FoxPro e localizado no diretório ...\Samples\Solution\Toledo.
- Um formulário do Visual FoxPro baseado na classe FrmSolution incluída com a biblioteca de classes Solution.vcx, que está localizada na pasta ...\Samples\Solution. Um formulário baseado na classe FrmSolution é semelhante aos formulários usados nos exemplos Solution.

Você pode criar um formulário baseado na classe FrmSolution criando uma categoria na Toolbox, adicionando a classe FrmSolution à Toolbox e criando um formulário baseado nessa classe.

### Para criar o formulário usado neste passo a passo
- No menu Tools, clique em Toolbox .
- Clique com o botão direito na Toolbox e clique em Add Category .
- Na caixa Category name, digite um nome de categoria. A categoria que você criou aparece na Toolbox.
- Na Toolbox, clique com o botão direito na categoria e clique em Add Class Library .
- Na caixa de diálogo Add Class Library, clique no botão de reticências (...) e navegue até a pasta ...\Samples\Solution e selecione Solution.vcx. As classes na biblioteca de classes Solution.vcx aparecem na categoria que você criou na Toolbox.
- Na Toolbox, clique com o botão direito em frmsolution (SOLUTION) e clique em Create Form .

# Abrindo o ambiente de dados de um formulário

Quando você cria um formulário, o Visual FoxPro cria um objeto DataEnvironment como contêiner para objetos Cursor, CursorAdapter e Relation associados ao formulário, a um form set ou a um relatório. Você precisa abrir e definir o ambiente de dados do formulário para o tipo de fonte de dados e fonte de dados apropriados para recuperar dados.

Antes de selecionar o tipo de fonte de dados e a fonte de dados da qual recuperar dados, abra o ambiente de dados do formulário.

### Para abrir o ambiente de dados do formulário
- Abra o formulário.
- No Form Designer, clique com o botão direito no formulário e clique em DataEnvironment para abrir o ambiente de dados. Para um formulário com ambiente de dados vazio, a caixa de diálogo Open aparece.
- Na caixa de diálogo Open, clique em Cancel .
- Para abrir o DataEnvironment Builder, clique com o botão direito na superfície do Data Environment e clique em Builder . O DataEnvironment Builder abre e exibe as seguintes guias: Data Source e Cursors .

Para obter mais informações sobre objetos DataEnvironment, consulte DataEnvironment Object.

# Definindo tipos de fonte de dados e fontes de dados

Defina o tipo de fonte de dados e configure a fonte de dados apropriada da qual você deseja recuperar dados definindo opções na guia Data Source no DataEnvironment Builder.

### Para selecionar o tipo de fonte de dados do ambiente de dados do formulário
- No DataEnvironment Builder, clique na guia Data Source.
- Na guia Data Source, selecione o tipo de fonte de dados apropriado: ADO, Native, ODBC ou XML.

Dependendo da sua seleção, as opções apropriadas aparecem. Os procedimentos a seguir demonstram como definir o ambiente de dados para tabelas nativas do Visual FoxPro, ODBC, ADO e XML.

Para obter mais informações, consulte Data Source Tab, DataEnvironment Builder.

### Especificando fontes de dados nativas do Visual FoxPro

Para especificar fontes de dados nativas do Visual FoxPro, use o seguinte procedimento:

### Para usar tabelas nativas do Visual FoxPro
- Depois de selecionar Native na guia Data Source, clique no botão de reticências (...) à direita da caixa Database
- Navegue até o diretório ...\Samples e selecione o banco de dados Northwind.

Para continuar este passo a passo, consulte Recuperando dados para cursor adapters.

### Especificando fontes de dados usando ODBC

Para especificar fontes de dados ODBC, use o seguinte procedimento:

### Para usar fontes de dados ODBC
- Depois de selecionar ODBC na guia Data Source, clique em Use connection string .
- Digite a cadeia de conexão para conectar ao banco de dados Northwind no seu SQL Server local ou remoto. Por exemplo: Driver={Sql Server};Server=localhost;Database=Northwind;Int Security=yes; Observação Você deve ter acesso a um SQL Server local ou remoto (SQL Server 7 ou 2000) com o banco de dados Northwind instalado. Se o seu SQL Server não é local, você pode alterar o valor do parâmetro Server= na cadeia de conexão para o nome do servidor remoto.
- Clique em Test Connection para testar a conexão.

Se a conexão for bem-sucedida, você pode continuar e recuperar dados da fonte de dados.

Para continuar este passo a passo, consulte Recuperando dados para cursor adapters.

### Especificando fontes de dados usando ADO

Para usar fontes de dados ADO, use o seguinte procedimento:

### Para usar fontes de dados ADO
- Depois de selecionar ADO na guia Data Source, clique em Use connection string .
- Digite a cadeia de conexão para conectar ao banco de dados Northwind no seu SQL Server local ou remoto. Por exemplo: Provider=SQLOLEDB.1;Integrated Security=SSPI;Initial Catalog=Northwind;Data Source=localhost Observação Você deve ter acesso a um SQL Server local ou remoto (SQL Server 7 ou 2000) com o banco de dados Northwind instalado. Se o seu SQL Server não é local, você pode alterar o valor do parâmetro Data Source= na cadeia de conexão para o nome do servidor remoto.
- Clique em Test Connection para testar a conexão. Se a conexão for bem-sucedida, você pode continuar e recuperar dados da fonte de dados.

Se você deseja construir uma cadeia de conexão em vez de digitar uma na guia Data Source, clique em Build para abrir a caixa de diálogo Data Link Properties no Visual FoxPro OLE DB Provider. Para obter mais informações, consulte OLE DB Provider for Visual FoxPro.

Para continuar este passo a passo, consulte Recuperando dados para cursor adapters.

### Especificando fontes de dados XML

Neste passo a passo, o método para criar cursor adapters a partir de XML demonstra apenas um exemplo de como você pode acessar uma fonte de dados XML, mais especificamente, um arquivo XML DataSet gerado a partir do ADO.NET. O código real pode variar dependendo das suas necessidades específicas.

### Para usar fontes de dados XML
- Depois de selecionar XML na guia Data Source, clique na guia Cursors.

Você também pode usar cursor adapters com cursors gerados a partir de XML com XML adapters ou objetos XMLAdapter. Você pode usar essa combinação para acessar recursos mais avançados do ambiente de design e vincular controles em um formulário a campos no cursor adapter. O XML adapter realiza o trabalho real em tempo de execução.

Quando você cria um cursor adapter a partir de XML, pode usar o CursorAdapter Builder para definir as propriedades do CursorAdapter. No entanto, você precisa criar um objeto XMLAdapter para carregar o XML em sua coleção Tables. Depois de criar o XML adapter, você pode carregar um arquivo XML no XML adapter, definir o comando Select do cursor adapter para a referência de objeto XMLTable desejada na coleção Tables do XMLAdapter e então chamar o método CursorFill do CursorAdapter para preencher o cursor com dados XML.

Para continuar este passo a passo, consulte Recuperando dados para cursor adapters.

Para obter mais informações sobre como cursor adapters funcionam com XML adapters, consulte Create a Cursor from an XML DataSet Sample como exemplo de como acessar um arquivo XML e gerar XML DiffGrams e XML Functionality Using XMLAdapters.

Para obter mais informações sobre XML adapters e cursor adapters, consulte XMLAdapter Class e CursorAdapter Class.

# Recuperando dados para cursor adapters

Depois de definir o ambiente de dados do formulário no DataEnvironment Builder para a fonte de dados que você deseja usar, crie objetos CursorAdapter no ambiente de dados do formulário para recuperar dados da fonte de dados. Você pode criar objetos CursorAdapter definindo opções na guia Cursors do CursorAdapter Builder.

### Para criar um novo cursor adapter
- No DataEnvironment Builder, clique na guia Cursors para torná-la visível.
- Na guia Cursors, clique em New para abrir o CursorAdapter Builder.

O CursorAdapter Builder aparece, exibe as guias Properties, Data Access e Auto-Update e cria um novo cursor adapter chamado Cursor1.

Para obter mais informações, consulte Cursors Tab, DataEnvironment Builder.

### Definindo propriedades para cursor adapters

Defina propriedades para um novo cursor adapter editando configurações na guia Properties do CursorAdapter Builder.

### Para definir propriedades para um novo cursor adapter
- No CursorAdapter Builder, clique na guia Properties para torná-la visível, se ainda não estiver visível.
- Na guia Properties, edite o nome de Cursor1 se desejar; renomeie o alias do cursor adapter para Customer. Observação Geralmente, você digita o nome e o alias que deseja para o cursor adapter.
- Clique em Use DataEnvironment data source para usar a fonte de dados definida anteriormente para o ambiente de dados do formulário.

Para obter mais informações, consulte Properties Tab, CursorAdapter Builder.

### Especificando como cursor adapters recuperam dados

Depois de criar um novo cursor adapter, especifique como o cursor adapter recupera dados da fonte de dados definindo opções na guia Data Access do CursorAdapter Builder.

Se você está usando o tipo de fonte de dados Native, ODBC ou ADO, use as instruções a seguir para construir o comando Select para recuperar dados da fonte de dados. Se você está usando o tipo de fonte de dados XML, siga as instruções para especificar um arquivo XML bem formado que contenha schema.

### Para construir o comando Select para fontes de dados usando Native, ODBC e ADO
- No CursorAdapter Builder, clique na guia Data Access para torná-la visível.
- Na guia Data Access, clique em Build para abrir a caixa de diálogo Select Command Builder.
- Na caixa de diálogo Select Command Builder, selecione a tabela CUSTOMERS na lista Table. Os campos que a tabela CUSTOMERS contém aparecem na lista no lado esquerdo da caixa de diálogo Select Command Builder.
- Na lista à esquerda, clique em CUSTOMERS.* para incluir a tabela CUSTOMERS e todos os seus campos no comando Select. Observação Geralmente, se você deseja selecionar campos individuais na tabela para o comando Select, clique em tableName . fieldName para adicionar cada campo separadamente à lista de campos selecionados que aparece no lado direito da caixa de diálogo Select Command Builder.
- Clique na seta simples para a direita ( > ) para adicionar CUSTOMERS.* à lista de campos selecionados e então clique em OK . O comando Select construído aparece na caixa Select command, e o schema do cursor adapter aparece na caixa Schema.

Você pode definir opções adicionais para recuperação de dados. No entanto, este passo a passo usa as configurações padrão para essas opções.

> **Observação:** Neste passo a passo, o modo de buffer do cursor adapter é definido como optimistic row buffering por padrão na guia Data Access para tipos de fonte de dados Native, ODBC e ADO. Portanto, quando você faz alterações em uma linha de grade no formulário e move para outra linha, essas alterações são enviadas à tabela Customer.dbf na fonte de dados através do tipo de conexão apropriado. Para obter mais informações sobre modos de buffer, consulte BufferModeOverride Property .

Para obter mais informações sobre opções adicionais que você pode definir, consulte Data Access Tab, CursorAdapter Builder.

### Para especificar um arquivo XML para fontes de dados XML
- No CursorAdapter Builder, clique na guia Data Access para torná-la visível.
- Na guia Data Access, clique em Build localizado acima da caixa Schema para exibir a caixa de diálogo Open.
- Navegue até a pasta ...\Samples\Solution\Toledo\ e selecione o arquivo GetCustomers.XML. O schema do cursor adapter aparece na caixa Schema.
- Na caixa Buffer mode override, selecione Optimistic table buffering . Observação Neste passo a passo, o modo de buffer do cursor adapter é definido como optimistic table buffering na guia Data Access para tipos de fonte de dados XML para permitir que o XML adapter crie XML DiffGrams. Para obter mais informações sobre configurações de modo de buffer, consulte BufferModeOverride Property .
- Clique em OK para fechar o CursorAdapter Builder e então clique em OK novamente para fechar o DataEnvironment Builder. O novo cursor adapter, agora chamado Customer , aparece no Data Environment do formulário e contém todos os campos do arquivo GetCustomer.xml.

Você pode definir opções adicionais para recuperação de dados. No entanto, exceto pela configuração de modo de buffer para o cursor criado pelo cursor adapter no exemplo XML, este passo a passo usa as configurações padrão para essas opções. Para obter mais informações sobre essas opções, consulte Data Access Tab, CursorAdapter Builder.

Para continuar com o exemplo XML, consulte Usando o cursor adapter no formulário.

### Configurando atualização para cursor adapters

Depois de construir o comando Select para o cursor adapter recuperar dados, você pode especificar como o cursor adapter realiza atualizações na fonte de dados definindo opções na guia Auto-Update do CursorAdapter Builder.

### Para configurar como o cursor adapter atualiza a fonte de dados
- No CursorAdapter Builder, clique na guia Auto-Update.
- Na guia Auto-Update, selecione a caixa de seleção Auto-update. Selecionar a caixa de seleção Auto-update preenche a lista de campos na guia Auto-Update com os campos que você selecionou na guia Data Access e habilita a atualização automática para os campos especificados.
- Selecione a caixa de seleção Update all fields para designar todos os campos da tabela especificada para atualização automática. Uma marca de verificação aparece na coluna de atualização automática, indicada por um símbolo de lápis, para cada campo na lista de campos.
- Selecione a caixa de seleção na coluna key field, indicada por um símbolo de chave, para o campo CUSTOMERID para designá-lo como campo de chave primária.
- Desmarque a caixa de seleção na coluna de atualização automática para o campo CUSTOMERID para impedir que seja modificado como chave primária.
- Clique em OK para fechar o CursorAdapter Builder e então clique em OK novamente para fechar o DataEnvironment Builder. O novo cursor adapter, agora chamado Customer , aparece no Data Environment do formulário e contém todos os campos da tabela Customer conforme especificado.

Você pode definir opções adicionais para como o cursor adapter atualiza a fonte de dados. No entanto, este passo a passo usa as configurações padrão para essas opções.

Para obter mais informações, consulte Auto-Update Tab, CursorAdapter Builder.

# Usando o cursor adapter no formulário

Depois de criar o cursor adapter no ambiente de dados do formulário, você pode arrastar o cursor adapter para o formulário para criar uma grade.

### Para criar uma grade usando o cursor adapter criado
- No ambiente de dados do formulário, clique e arraste o cursor adapter Customer para o formulário para criar uma grade. Se você está usando o tipo de fonte de dados XML, digite o seguinte código no evento Init do formulário para criar e configurar o objeto XMLAdapter: LOCAL oXMLAdapter as XMLAdapter DODEFAULT() ThisForm.AddProperty('oXMLAdapter',CREATEOBJECT('XMLAdapter')) WITH ThisForm.oXMLAdapter .LoadXml(ThisForm.cRunPath+'getcustomers.xml',.T.) ENDWITH ThisForm.DataEnvironment.cursor1.SelectCmd="ThisForm.oXMLAdapter.Tables.Item(1)" ThisForm.DataEnvironment.cursor1.CursorFill() GO TOP ThisForm.BindControls = .T. ThisForm.grdCustomer.AutoFit()
- Na janela Properties, defina a propriedade BindControls do formulário como False (.F.).
- Salve o formulário na pasta ...\Samples\Solution\Toledo.
- Na barra de ferramentas do Visual FoxPro, clique no botão Run (!) para executar o formulário.

O formulário aparece e exibe uma grade que contém o seguinte:
 - Tipos de fonte de dados Native, ODBC e ADO: Dados dos campos na tabela CUSTOMER.
- Tipo de fonte de dados XML: Dados carregados do XML DataSet, GetCustomer.xml. Ao usar XML adapters com cursor adapters, você pode gerar XML DiffGrams usando o XML adapter criado. Por exemplo, o seguinte código cria uma cadeia de caracteres XML DiffGram em uma variável local chamada lcXML : LOCAL lcXML, llIncludeBefore, llChangesOnly, llIsFile, lcSchemaLocation WITH ThisForm.oXMLAdapter ...* Release XML document but preserve schema. ....ReleaseXML(.F.) ....UTF8Encoded = .T. && Indicates international characters. ....IsDiffgram = .T. && Generate XML DiffGram. ...llIncludeBefore = .T. && Include <diffgram:before> format. ...llChangesOnly = .T. && Generate only changes made. ...llIsFile = .F. && Sample XML is a stream. ...lcSchemaLocation = "" && Sample schema is inline. ....ToXML("lcXML",lcSchemaLocation,llIsFile,llIncludeBefore,llChangesOnly) ENDWITH
