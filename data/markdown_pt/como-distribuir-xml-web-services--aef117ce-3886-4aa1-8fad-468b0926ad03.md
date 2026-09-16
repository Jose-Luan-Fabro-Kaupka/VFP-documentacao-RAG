# Como: distribuir XML Web Services

O suporte a XML Web services no Visual FoxPro fornecido pelo Microsoft SOAP Toolkit permite publicar Visual COM Servers (OLEPUBLIC) como XML Web services que podem ser acessados pela Web. As extensões e objetos disponíveis no SOAP Toolkit fornecem capacidades de publicação para XML Web services. Para obter informações sobre a publicação de COM Servers do Visual FoxPro como XML Web services, consulte Walkthrough: Creating XML Web Services with Visual FoxPro.

# Especificando um local padrão para XML Web Services

Antes de publicar um XML Web service, você pode especificar um local padrão para publicação. Este local é um Uniform Resource Locator (URL) de servidor Web local ou um diretório virtual que você usa para armazenar arquivos de suporte a XML Web service, como listeners ASP e arquivos WSDL. Embora este local seja opcional, ele pode simplificar o processo de publicação de XML Web services.

> **Observação:** A caixa de diálogo Visual FoxPro XML Web Service Location aparece na primeira vez que você seleciona Web Services no menu Wizards. Se você não fornecer um local padrão, o Visual FoxPro solicitará o local padrão cada vez que publicar um novo XML Web service. Você pode alterar o local posteriormente clicando em Advanced na caixa de diálogo Visual FoxPro XML Web Services Publisher.

Para obter mais informações, consulte Visual FoxPro XML Web Service Location Dialog Box e Visual FoxPro XML Web Services Publisher Dialog Box.

### Para especificar um local padrão para um XML Web service
- No menu Tools, aponte para Wizards e clique em Web Services.
- Na caixa de diálogo que aparece, clique em OK.
- Na caixa de diálogo Visual FoxPro XML Web Service Location, para selecionar um local existente para publicar seu XML Web service, clique em Existing e selecione um local na caixa Select Location (Virtual Directory). -ou- Para selecionar um novo local, clique em New, selecione um local na caixa Select Location (Virtual Directory), clique no botão Ellipsis (...) para especificar um caminho de saída de arquivo, se desejar, e digite um nome para o diretório na caixa New Virtual Directory Name.

As configurações de cada XML Web service são preservadas para que você possa atualizar facilmente o XML Web service, por exemplo, se o conteúdo do WSDL mudar. Essas configurações são armazenadas na tabela FoxWS3.dbf no mesmo diretório da tabela FoxCode.dbf (_FOXCODE).

# Publicando XML Web Services

Você pode publicar um Visual FoxPro COM Server como um XML Web service para torná-lo disponível na Web.

> **Observação:** A publicação de XML Web services por meio da caixa de diálogo Visual FoxPro Web Services Publisher é suportada somente para gerar arquivos WSDL contendo um único serviço e porta ou classe. Se você deseja selecionar várias classes, deve usar o assistente disponível no SOAP Toolkit.

### Para publicar um XML Web service
- No menu Tools, clique em Task Pane.
- Na barra de ferramentas do Task Pane Manager, clique em More Panes.
- No painel XML Web Services, clique em Publish Your XML Web Service.
- Na caixa de diálogo Visual FoxPro XML Web Services Publisher, clique no botão Ellipsis (...) para procurar e selecionar o Visual FoxPro COM Server desejado.

Você também pode publicar seu COM Server clicando em Web Services no menu Wizards, clicando com o botão direito em um projeto COM Server aberto, clicando em Builder no menu de atalho e selecionando Web Services Publisher na caixa de diálogo Wizard Selection. Você também pode abrir a caixa de diálogo Visual FoxPro XML Web Services Publisher usando o código a seguir:

```foxpro
DO (_wizard) WITH "project",,"Web"
```

Para obter mais informações, consulte Visual FoxPro XML Web Services Publisher Dialog Box.
