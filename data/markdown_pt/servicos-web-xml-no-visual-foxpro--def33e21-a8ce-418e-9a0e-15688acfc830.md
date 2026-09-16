# Serviços Web XML no Visual FoxPro

Serviços Web XML são classes ou objetos disponíveis na Web que você pode usar em seus aplicativos programaticamente como chamadas orientadas a objetos normais. Você também pode publicar COM Servers (OLEPUBLIC) do Visual FoxPro como serviços Web XML para disponibilizar informações a outros clientes na Internet.

Por exemplo, você pode usar um serviço Web XML em seu aplicativo que retorna o clima de uma determinada cidade quando você chama um método que retorna a temperatura ao receber o nome da cidade.

O suporte do Visual FoxPro para serviços Web XML é tratado por meio de SOAP usando uma implementação da Web Services Description Language (WSDL) compatível com a versão 1.1 do WSDL. O Visual FoxPro inclui o Microsoft SOAP Toolkit versão 3.0, que fornece suporte para serviços Web XML por meio de um conjunto de extensões, e também está disponível no site da Microsoft. O Visual FoxPro amplia a funcionalidade do Toolkit; portanto, quaisquer alterações futuras na especificação WSDL pelo W3C se propagam diretamente ao Visual FoxPro quando você atualiza para uma versão mais recente do Toolkit.

> **Observação:** Você deve ter o Microsoft SOAP Toolkit instalado para usar serviços Web XML. Se você planeja publicar serviços Web XML a partir de COM Servers do Visual FoxPro, deve ter o Microsoft Internet Information Services (IIS) instalado.

O SOAP Toolkit também fornece objetos que você pode usar para chamar serviços Web XML em níveis baixos que interagem diretamente com as mensagens SOAP reais. No entanto, esses objetos não são suportados diretamente pelas extensões do Visual FoxPro.

Para obter mais informações sobre plataformas suportadas, SOAP, WSDL ou o Toolkit, consulte a documentação online do Toolkit ou o site SOAP Developer Resources em http://msdn.microsoft.com/soap/.

# Nesta seção
 **Como: acessar serviços Web XML**
Descreve como localizar, registrar e usar serviços Web XML em aplicativos do Visual FoxPro.
**Como: distribuir serviços Web XML**
Descreve como especificar um local padrão para publicar serviços Web XML, publicar COM Servers do Visual FoxPro como serviços Web XML, incluir componentes para implantar serviços Web XML e gerar arquivos de suporte a serviços Web XML automaticamente quando seu COM Server é recompilado.
**Testando e recompilando COM Servers para serviços Web XML**
Descreve como gerar arquivos de suporte a serviços Web XML automaticamente ao testar e recompilar servidores COM.
**Implantando serviços Web XML (Visual FoxPro)**
Descreve os arquivos que você precisa incluir para implantar serviços Web XML.

# Seções relacionadas
 **Serviços Web e componentes**
Discute como você pode permitir que um aplicativo do Visual FoxPro funcione para vários usuários aproveitando controles ActiveX e aplicativos habilitados para automação e adicionando recursos internacionais.
**Automação e COM Servers**
Descreve como você pode ampliar a funcionalidade de seus aplicativos do Visual FoxPro sem muito tempo extra de codificação usando automação e COM Servers.
**Passo a passo: criando serviços Web XML com o Visual FoxPro**
Explica como criar e publicar um COM Server do Visual FoxPro como um serviço Web XML.
**Interoperabilidade e a Internet**
Explica como usar OLE drag-and-drop para desenvolver aplicativos para que você possa mover dados entre aplicativos baseados no Microsoft Windows e dentro de um aplicativo do Visual FoxPro. Crie documentos para uso na Internet ou use um dos dois tempos de execução diferentes do Visual FoxPro para criar componentes COM (servidores de automação) como aplicativos normais ou multithread.
