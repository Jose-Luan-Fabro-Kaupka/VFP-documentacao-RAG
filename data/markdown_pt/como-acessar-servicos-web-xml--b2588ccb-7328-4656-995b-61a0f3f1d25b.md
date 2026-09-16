# Como: acessar serviços Web XML

O suporte para serviços Web XML no Visual FoxPro fornecido pelo Microsoft SOAP Toolkit torna possível acessar serviços Web XML da Web. As extensões fornecidas pelo SOAP Toolkit 3.0 fornecem acesso a serviços Web XML usando o objeto SoapClient do Toolkit. Esta arquitetura de acesso de associação tardia de alto nível torna possível chamar um método de serviço Web XML diretamente usando apenas algumas linhas de código de objeto simples.

A classe base WSHandler, que está incluída com a biblioteca de classes _WS3Client.vcx na pasta ...\Ffc, é a classe de serviço Web XML usada para todas as chamadas de serviço Web XML do Visual FoxPro.

# Registrando serviços Web XML

Antes de usar um serviço Web XML em seu aplicativo, você deve registrá-lo no Visual FoxPro. Você pode então selecionar o serviço Web XML no Toolbox do Visual FoxPro e usar chamadas de operação ou método desse serviço Web XML para retornar resultados. Ao chamar o serviço Web XML, você pode definir os resultados em uma propriedade de um controle especificado, como a propriedade Value do TextBox.

> **Observação:** Você não precisa registrar um serviço Web XML para acessá-lo; no entanto, registrar um serviço Web XML permite que o Visual FoxPro forneça IntelliSense para os métodos do serviço Web XML e seus parâmetros.

### Para registrar um serviço Web XML
- No menu Tools, clique em Task Pane.
- Na barra de ferramentas do Task Pane Manager, clique em More Panes e, em seguida, clique em XML Web Services.
- No painel XML Web Services, clique em Register an XML Web Service.
- Na caixa de diálogo Visual FoxPro XML Web Services Registration, digite a URL WSDL (Web Services Description Language) para o serviço Web XML e clique em Register.

Você também pode abrir a caixa de diálogo Visual FoxPro XML Web Services Registration programaticamente conforme mostrado no código a seguir:

```foxpro
DO (_wizard) WITH "project",,"Web","IntelliSense"
```

Para obter mais informações sobre as configurações que você precisa definir, consulte Visual FoxPro XML Web Services Registration Dialog Box.

# Chamando serviços Web XML

Depois de registrar um serviço Web XML no Visual FoxPro, você pode chamar e associar o serviço Web XML a um controle ou objeto em um formulário. Você pode então processar resultados do serviço Web XML em seu aplicativo. Você pode chamar e associar serviços Web XML usando o XML Web Service Builder ou em código. O builder fornece capacidades extensivas de associação sem que você precise escrever código. Para obter mais informações, consulte XML Web Service Builder.

As etapas a seguir ilustram como chamar o serviço Web XML em seu programa usando código.

### Para chamar um serviço Web XML usando código
- No menu Tools, clique em Toolbox.
- No Toolbox, clique em My XML Web Services.
- Abra uma janela de edição no local em seu programa ou código onde deseja chamar o serviço Web XML.
- Arraste e solte o serviço Web XML na janela de edição. O código para o serviço Web XML aparece na janela de edição.

Você também pode digitar os caracteres ws na janela de edição. A caixa de diálogo Select aparece para que você possa selecionar um serviço Web XML e quaisquer opções adicionais e inserir código para o serviço Web XML na janela de edição. Para obter mais informações, consulte Select Dialog Box (Visual FoxPro).

Você pode usar IntelliSense para ver os métodos e parâmetros disponíveis para o serviço Web XML. Por exemplo, IntelliSense exibe uma lista de métodos disponíveis para o serviço Web XML quando você digita a linha de código a seguir na janela de edição:

```foxpro
? YourXMLWebService.
```

> **Observação:** Certifique-se de substituir MyXMLWebService pelo objeto de serviço Web XML fornecido no código.

Você pode selecionar um método e continuar digitando conforme a seguir para especificar parâmetros para o método:

```foxpro
? MyXMLWebService.WSMethod(
```

> **Observação:** Substitua WSMethod pelo método de serviço Web XML que você selecionar.

IntelliSense exibe os possíveis parâmetros e o tipo de retorno para esse método.

Você também pode portar o código para o serviço Web XML para outro computador que não tenha o serviço Web XML registrado. O Visual FoxPro pode detectar que o serviço Web XML não está registrado e solicita que você o registre. Se você não deseja registrar o serviço Web XML, pode remover a linha que contém a referência WSDL, por exemplo:

```foxpro
* __VFPWSDef__: lofoxtypes=http://mywebserver/foxws/foxtypes.wsdl
```

Para obter mais detalhes sobre o acesso a serviços Web XML usando chamadas de alto e baixo nível, consulte a documentação do SOAP Toolkit 3.0.

# Associando serviços Web XML a controles

Você pode associar um serviço Web XML a um controle ou objeto em um formulário do Visual FoxPro e atribuir os resultados do serviço Web XML a propriedades do controle ou objeto.

### Para associar um serviço Web XML a um controle
- Crie um formulário ou classe novo ou abra um existente.
- No menu Tools, clique em Toolbox.
- Em My XML Web Services no Toolbox, arraste e solte o controle Generic Handler ou o serviço Web XML registrado em um formulário ou classe. O XML Web Service Builder aparece para que você possa associar o serviço Web XML a controles ou objetos no formulário. Se o builder não aparecer, clique com o botão direito no controle de serviço Web XML e selecione Builder.

Para obter mais informações, consulte XML Web Service Builder.

> **Observação:** É recomendado que você salve um formulário recém-criado antes de soltar um serviço Web XML porque o builder precisa acessar controles no formulário usando o caminho do contêiner.
