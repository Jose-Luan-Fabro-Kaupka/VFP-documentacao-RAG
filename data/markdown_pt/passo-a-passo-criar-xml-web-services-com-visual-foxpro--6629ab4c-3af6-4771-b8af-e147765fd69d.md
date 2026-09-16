# Passo a passo: criar XML Web Services com Visual FoxPro

XML Web services são os blocos fundamentais de construção para computação distribuída na Internet. Um XML Web service é um objeto ou classe implantado na Internet e que você pode acessar programaticamente por meio de chamadas de método típicas. XML Web services fornecem funcionalidade e acesso a dados entre plataformas e em conexões diversas. O aspecto mais importante dos XML Web services é que, por causa de como usam HTTP e SOAP, a funcionalidade está disponível através de firewalls. Você pode chamar um XML Web service independentemente da plataforma em que está executando, porque HTTP e SOAP operam independentemente da plataforma do seu computador. Em alguns casos, isso pode fornecer funcionalidade que não estava disponível sob COM distribuído.

Você pode criar XML Web services ou acessá-los na Web de onde estiverem publicados. Você pode usar o Visual FoxPro para criar um XML Web service ou pode usar o Visual FoxPro para acessar um XML Web service criado em outras linguagens de programação.

Este passo a passo explica como criar um COM Server e publicá-lo como um XML Web service. Além disso, ele orienta você no uso do XML Web service recém-criado. O XML Web service fornece uma lista de clientes de uma tabela em que os clientes atendem a um determinado requisito. A lista é enviada como uma cadeia de caracteres XML que é então colocada em um cursor usando a classe XMLAdapter.

Este passo a passo contém as seguintes seções:
 - Pré-requisitos
- Internet Information Services
- Criando um COM Server
- Criando e publicando um XML Web Service
- Testando um XML Web Service
- Usando um XML Web Service

# Pré-requisitos

Este passo a passo requer o seguinte:
 - Microsoft Internet Information Services (IIS)
- SOAP
- Visual FoxPro COM Servers

O SOAP é instalado automaticamente quando você instala o Visual FoxPro. O IIS é um componente opcional para Windows 2000 e é instalado automaticamente no Windows 2000 Server. O IIS serve seus XML Web services do seu diretório virtual para usuários na Internet. Seu diretório virtual referencia o local no disco rígido onde você coloca seus XML Web services. Você usa o Visual FoxPro para criar objetos COM. Depois que seus objetos COM são criados, você pode usar o builder de XML Web Service do Visual FoxPro para publicá-los no seu diretório virtual.

# Internet Information Services

O IIS fornece a referência à localização do seu XML Web service para usuários que o acessam pela Internet. Para publicar um XML Web service, você deve criar um diretório virtual no IIS que contenha os arquivos Web Services Description Language (.wsdl) necessários. Esses arquivos são criados pelo Web Service Wizard a partir do seu componente COM.

### Para criar um diretório virtual
- No diretório principal do Visual FoxPro ..\Program Files\Microsoft Visual FoxPro VersionNumber , crie uma pasta chamada Web Services.
- No Painel de Controle do Windows, clique duas vezes em Administrative Tools e depois clique duas vezes em Internet Information Services . A janela Internet Information Services abre, exibindo um controle de árvore à esquerda que exibe uma lista de serviços de informações da Internet no seu computador.
- Clique com o botão direito no nó Default Web Site.
- Clique em New e depois clique em Virtual Directory para abrir o Virtual Directory Creation Wizard.
- Siga as instruções no assistente e especifique a pasta Web Services que você criou na etapa 1 como seu diretório virtual. Este diretório virtual referencia a pasta Web Services onde você armazenará todos os arquivos de XML Web service que criar.

# Criando um COM Server

Como um XML Web service é uma biblioteca de vínculo dinâmico (.dll) ou arquivo executável (.exe), você deve usar um COM Server como base para seu XML Web service. Um COM Server no Visual FoxPro é um arquivo com extensão .dll ou .exe, contendo uma classe personalizada baseada no objeto Session. A classe personalizada é especificada como OLEPUBLIC quando é definida. Isso expõe funcionalidade que pode ser usada e reutilizada por outros aplicativos por meio de automação.

Para este exemplo de COM Server, você cria uma classe personalizada que relata algumas informações básicas. Você grava um programa que cria uma classe com um método, compila o projeto que a contém em um COM Server e depois a publica como um XML Web service.

### Para criar um COM Server
- No menu Arquivo no Visual FoxPro, clique em New .
- Na caixa de diálogo New, clique em Project e depois clique em New file . Salve o projeto como myWServ1 .
- Na guia All do Project Manager, expanda Code , clique em Programs e depois clique em New .
- Copie o código a seguir para a janela Editing. DEFINE CLASS ShowCustomers AS Session OLEPUBLIC PROCEDURE CustomersInGermany AS String LOCAL loXMLAdapter AS XMLAdapter LOCAL lcXMLCustomers AS String loXMLAdapter = CREATEOBJECT("XMLAdapter") OPEN DATABASE "C:\Program Files\Microsoft Visual FoxPro 9\" ; + "Samples\Northwind\northwind.dbc" USE customers SELECT * ; FROM customers ; WHERE country LIKE "Germany%" ; INTO CURSOR curCustomers loXMLAdapter.AddTableSchema("curCustomers") loXMLAdapter.UTF8Encoded = .T. loXMLAdapter.ToXML("lcXMLCustomers") CLOSE DATABASES ALL RETURN lcXMLCustomers ENDPROC ENDDEFINE Este programa define uma classe, ShowCustomers, que tem um método, CustomersInGermany.
- No menu Arquivo, clique em Save .
- Na caixa de diálogo Save As, nomeie o programa myWServ1 e clique em Save .
- Feche a janela Editing.
- No Project Manager, clique em Build .
- Selecione Multi-threaded COM server (dll) e clique em OK . Na caixa de diálogo Save As, localize o diretório Web Services que você criou no diretório principal do Visual FoxPro. Salve a DLL como myWServ1.dll no diretório Web Services.

> **Observação:** Se a DLL for salva em um diretório que o IIS/SOAP não pode acessar, as chamadas ao WebService resultam no erro SOAP "Class not registered."

O Visual FoxPro agora compila o arquivo myWServ1 em um COM Server chamado myWServ1.dll. Você pode publicá-lo como um XML Web service.

# Criando e publicando um XML Web Service

Do arquivo myWServ1.dll, criado no procedimento anterior, um novo arquivo Web Services Description Language (.wsdl) é gerado quando você publica o XML Web service. O arquivo .wsdl é um arquivo XML que descreve o XML Web service e as classes que ele contém.

Para adicionar os componentes necessários para transformar seu COM Server em um XML Web service, você deve compilar o COM Server como um XML Web service. Depois de especificar as configurações no Web Services Publisher, o Visual FoxPro cria os arquivos SOAP necessários para transformar seu COM Server em um XML Web service, publica-os no seu diretório virtual e registra seu novo XML Web service no IntelliSense.

### Para compilar e publicar um XML Web service
- No menu Tools, clique em Task Pane .
- No Task Pane Manager , clique em XML Web Services .
- Em XML Web Service Tools , selecione Publish Your XML Web Service .
- Se o arquivo myWServ1.dll não estiver listado no campo COM Server, clique no botão de reticências ( ... ) e selecione myWServ1.dll .
- Clique em Advanced para exibir a caixa de diálogo Visual FoxPro XML Web Services Publisher.
- Certifique-se de que a caixa Listener URI exiba seu diretório virtual. Se não exibir, clique no botão de reticências ( ... ) e selecione seu diretório virtual.
- Clique na guia Methods e certifique-se de que CustomersInGermany está selecionado.
- Clique na tabela Namespaces, substitua tempuri.org pelo seu domínio em todos os campos e clique em OK . Se você não tiver seu próprio domínio, pode deixar tempuri.org para este exemplo.
- Clique em OK para fechar a caixa de diálogo Visual FoxPro XML Web Services Publisher.
- Clique em Generate . O Visual FoxPro gera os arquivos de XML Web service. Após a conclusão, a caixa de diálogo XML Web Services Publishing Results aparece, exibindo uma lista de arquivos gerados, arquivo .wsdl, listener ISAPI ou ASP e se o arquivo foi gerado corretamente.

Neste ponto, você criou e publicou seu XML Web service. Qualquer pessoa que tenha acesso ao diretório virtual que você estabeleceu anteriormente pode usar HTTP para acessar o XML Web service que você publicou.

# Testando um XML Web Service

Depois de publicar seu novo XML Web service, você deve testá-lo para garantir que está funcionando corretamente. O Visual FoxPro fornece um mecanismo para testar XML Web services que está disponível no painel XML Web Service no Task Pane Manager. O mecanismo de teste exibe quaisquer resultados retornados do XML Web service, esquemas XML usados, feedback de erro.

### Para testar um XML Web service
- No menu Tools no Visual FoxPro, clique em Task Pane .
- No Task Pane Manager, clique em XML Web Services .
- Em Explore an XML Web Service , clique em ShowCustomers na caixa Service Name.
- Na caixa The following methods are supported by this XML web service, clique em CustomersInGermany . Esta caixa lista todos os métodos disponíveis no XML Web service.
- Clique em Test this XML Web Service .

Se o teste for bem-sucedido, a janela Web Service Test Results aparece. Ela exibe os resultados do XML Web service e você pode visualizar o arquivo .wsdl associado ao XML Web service. Se houver um erro no teste, a janela Web Service Test Results exibe informações sobre o erro.

# Usando um XML Web Service

Você usa um XML Web service da mesma forma que usaria qualquer COM Server: para expor a funcionalidade de um aplicativo a outro. No procedimento a seguir, você cria um arquivo de programa (.prg) para acessar seu XML Web service e usa a Toolbox para adicionar o código necessário que referencia o XML Web service corretamente.

### Para usar um XML Web service
- No menu Arquivo no Visual FoxPro, clique em New .
- Na caixa de diálogo New, selecione Project e clique em New file . Salve o projeto como wsTest .
- Na guia All do Project Manager, expanda Code , selecione Programs e depois clique em New No menu Tools, clique em Toolbox .
- Na Toolbox, clique em My XML Web Services .
- Clique e arraste o XML Web service ShowCustomers da Toolbox para a janela Editing. Isso adiciona o código adequado ao seu XML Web service.
- Na janela Editing, abaixo da linha que diz "Call your XML Web service here," insira o código a seguir. LOCAL lcXML, lcAlias AS String LOCAL loXMLAdapter AS XMLAdapter lcXML = loShowCustomers.CustomersInGermany loXMLAdapter = CREATEOBJECT("XMLAdapter") loXMLAdapter.LoadXML(lcXML) lcAlias = loXMLAdapter.Tables.Item(1).Alias loXMLAdapter.Tables.Item(1).ToCursor() SELECT(lcAlias) BROWSE CLOSE DATABASES ALL
- No menu Arquivo, clique em Save .
- Na caixa de diálogo Save As, nomeie o programa WebServiceTest e clique em Save .
- Feche a janela Editing.
- No Project Manager, selecione o arquivo de programa WebServiceTest e clique em Run . Uma janela de navegação aparece com todos os clientes da Alemanha selecionados no banco de dados Northwind. Este cursor foi preenchido a partir de XML fornecido pelo seu XML Web service usando a classe XMLAdapter.

Para obter mais informações sobre Web Services, consulte Web Services and Components. Para obter mais informações sobre COM Servers, consulte How to: Create Automation Servers.
