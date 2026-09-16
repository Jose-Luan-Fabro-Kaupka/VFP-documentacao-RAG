# Guia Data, caixa de diálogo Pane Customization

A guia Data contém os dados nos quais os painéis Web Page, HTML e XML são baseados.
 **Source**
Especifica o tipo de fonte de dados para o painel. Os cinco tipos de fonte de dados são explicados na tabela a seguir. Tipo de fonte de dados Descrição Static Text Especifica que os dados são XML bem formado. O texto estático padrão para o tipo XML Pane é: <VFPData> <!-- CONTENT --> </VFPData> Você pode digitar dados XML bem formados em vez do comentário. Se o painel raiz tem subseções, o texto estático padrão pode permanecer porque o Visual FoxPro concatena e coloca os dados XML da subseção aqui. Se você precisa envolver seu subconteúdo em XML para que as seções de conteúdo possam ser transformadas adicionalmente pela raiz antes de finalmente exibir no painel, use a seguinte sintaxe na seção de conteúdo raiz. <VFPData> <!-- XMLCONTENT --> </VFPData> Isso envolve cada subconteúdo em seções CDATA XML com o conteúdo entre tags <HTMLText>. Por exemplo, um painel com dois registros de subconteúdo pode parecer com o exemplo a seguir: <VFPData> <PaneContent id="uniqueid1"> <PaneTitle>Content Title goes here</PaneTitle> <HTMLText><![CDATA[Transformed sub-content is placed here]]> </HTMLText> </PaneContent> <PaneContent id="uniqueid2"> <PaneTitle>Content Title goes here</PaneTitle> <HTMLText><![CDATA[Transformed sub-content is placed here]]> </HTMLText> </PaneContent> </VFPData> A transformação da seção de conteúdo raiz então determina se deve tratar a transformação destes dados XML ou distribuir um arquivo XML na seção de arquivos. URL Os dados estão contidos em um arquivo na Internet. Você pode então enviar conteúdo dinâmico ao painel a partir de um arquivo na Internet. Script Especifica código Visual FoxPro para gerar dados XML. O código retorna uma cadeia de caracteres XML a ser usada como dados e aceita um objeto de parâmetro para expor opções definidas para o painel ao código. LPARAMTERS oContent O objeto expõe as seguintes propriedades e métodos: CacheDir O diretório do cache de painel do usuário ContentTitle O nome da seção de conteúdo selecionada Unique ID O ID exclusivo da seção de conteúdo selecionada TaskPaneID O ID exclusivo do painel ao qual a seção de conteúdo pertence User Dados do usuário contidos no campo User na tabela PaneContent GetOption(cOptionName , xDefaultValue) Retorna o valor da opção especificada. Você pode opcionalmente especificar o valor padrão a ser retornado se a opção estiver vazia. Todos os valores de opção são retornados como cadeias de caracteres, a menos que xDefaultValue especifique um tipo de dados diferente. File Especifica um arquivo local como fonte de dados. Este arquivo é adicionado à lista de arquivos associados para o painel e copiado para o diretório de cache do painel. Web Service Especifica que os dados são obtidos por meio de um serviço Web XML na Internet.
**Modify**
Abre uma janela para modificar o código Visual FoxPro ou dados XML.
**Edit Box**
Exibe código Visual FoxPro ou dados XML.
**Source of this content is from the Internet**
Especifica que um script de código Visual FoxPro está baixando conteúdo da Internet. Isso habilita a opção Check for New Internet Content para o painel.
**File**
Especifica o nome do arquivo de dados.
**Reticências (...)**
Solicita que você selecione um arquivo de dados.
**WSDL URL**
Especifica a URL do arquivo Web Services Description Language (WSDL) para o serviço Web XML que fornece os dados para o painel. O WSDL descreve os serviços oferecidos pelo servidor.
**Method**
Especifica o método do serviço Web XML a ser chamado. Os parâmetros apropriados para o método também devem ser especificados. Para especificar opções de painel, use os delimitadores ##. Por exemplo, GetPaneXML(##daysold##) referencia o método do serviço Web XML GetPaneXML e usa a opção DaysOld para um painel como parâmetro.
**Service**
Especifica o serviço no arquivo WSDL que contém a operação especificada na solicitação Simple Object Access Protocol (SOAP). Se esta opção estiver em branco, o primeiro serviço no arquivo WSDL especificado é usado ao inicializar o objeto SoapClient. (Opcional)
**Port**
Especifica o nome da porta no arquivo WSDL que contém a operação especificada na solicitação SOAP. Se esta opção estiver em branco, a primeira porta no serviço especificado é usada ao inicializar o objeto SoapClient. (Opcional)
**WSML**
Especifica a URL do arquivo Web Services Meta Language (WSML). Este é um parâmetro obrigatório apenas ao usar mapeadores de tipo personalizados. Para obter mais informações sobre mapeadores de tipo personalizados, consulte a documentação do SOAP Toolkit distribuída com o Visual FoxPro.
