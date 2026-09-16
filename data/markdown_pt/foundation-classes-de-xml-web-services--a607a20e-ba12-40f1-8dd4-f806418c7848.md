# Foundation Classes de XML Web Services

As bibliotecas de classes foundation de XML Web Service, _WS3Utils.vcx e _WS3Client.vcx, contêm uma coleção de classes que servem como extensões de XML Web service do Visual FoxPro para o Microsoft SOAP Toolkit versão 3.0. Use essas classes para registrar XML Web services em conformidade com os suportados pelo Toolkit. Você também pode publicar COM Servers (.dll files) do Visual FoxPro como XML Web services usando essas extensões.
 Biblioteca de classes _WS3Utils.vcx
| Classe | Descrição |
| --- | --- |
| Olecontrols | Controle tree view usado pelo XML Web Service Builder. |
| Wsbasebuilder | Classe de formulário base usada pelo XML Web Service Builder. |
| Wsbuilder | Caixa de diálogo inicial do XML Web Service Builder. |
| Wsbuilder1 | Caixa de diálogo XML Web Service – Operation Detail. |
| Wsbuilder2 | Caixa de diálogo XML Web Service – Client Detail. |
| Wsbuilder3 | Caixa de diálogo XML Web Service – Complex Types. |
| Wsbuilder4 | Caixa de diálogo XML Web Service – Parameter Values. |
| Wsconfig | Caixa de diálogo usada pelo Web Services Publisher para especificar um local de URL para arquivos WSDL. |
| Wsfoxcode | Classe usada para lidar com IntelliSense para um XML Web service ao acessar na janela de edição de um programa. |
| Wsmanager | Classe chamada pelo painel XML Web Services no Task Pane Manager para gerenciar XML Web services. |
| Wsphook | Classe project hook usada pelo XML Web Services Publisher para regenerar arquivos WSDL quando o projeto é recompilado. |
| Wspicker | Caixa de diálogo para selecionar uma classe de XML Web service para inserir código proxy. Esta caixa de diálogo abre quando você digita os caracteres ws na janela de edição de um programa. |
| Wsproxy | Classe usada para gerar código proxy quando uma classe de XML Web service é arrastada e solta da Toolbox para uma janela de edição de um programa ou chamada digitando os caracteres ws na janela de edição. |
| Wspub | Caixa de diálogo Visual FoxPro XML Web Services Publisher. |
| Wsreg | Caixa de diálogo Visual FoxPro XML Web Services Registration. |
| Wstest | Caixa de diálogo chamada do painel XML Web Services no Task Pane Manager para testar um XML Web service. |
| Wstool | Caixa de diálogo Visual FoxPro XML Web Services Publisher Advanced. |
| Wsuddi | Caixa de diálogo Visual FoxPro XML Web Services Registration UDDI Search. |
| _webservices | Classe de motor central para publicar e registrar XML Web services. |
 Biblioteca de classes _WS3Client.vcx
| Classe | Descrição |
| --- | --- |
| Wshandler | Classe cliente central usada para comunicar com um XML Web service. Esta classe é usada no código proxy gerado na janela de edição de um programa e ao vincular visualmente controles a XML Web services em um formulário. |
| Colbase | Classe da qual as classes de coleção de XML Web service são derivadas. |
| Colclient | Classe adicionada à coleção de clientes ColClients. |
| Colclients | Classe de coleção de clientes de operação. |
| Coloperation | Classe adicionada à coleção de operações Coloperations. |
| Coloperations | Classe de coleção de operações. |
| Colparm | Classe adicionada à coleção de parâmetros Colparms. |
| Colparms | Classe de coleção de parâmetros de operação |
| Wsparms | Caixa de diálogo que solicita ao usuário que insira parâmetros para a chamada de operação do XML Web service. |
| Wsparmzoom | Caixa de diálogo Zoom usada pela caixa de diálogo de parâmetros de entrada. |

# Observações

Na biblioteca de classes _WS3Utils.vcx, a classe de motor central, _WebServices, comunica-se diretamente com o Toolkit. A classe _WebServices contém métodos para publicar XML Web services, incluindo aqueles que leem informações de biblioteca de tipos do seu servidor e aqueles que geram os arquivos de suporte de XML Web service necessários, por exemplo, arquivos de listener ASP e de descrição de serviço WSDL. Você também pode registrar um XML Web service externo usando os métodos fornecidos.

A biblioteca de classes _WS3Utils.vcx contém outras classes de suporte para trabalhar com XML Web services. Essas classes são essencialmente classes de formulário que auxiliam o usuário a coletar informações para registrar e publicar XML Web services. Elas funcionam em conjunto com a classe _WebServices.

Na biblioteca de classes _WS3Client.vcx, a classe central para usar um XML Web service é WSHandler. Esta classe lida com todas as chamadas às classes SOAP Client do SOAP Toolkit 3.0 que se conectam a um XML Web service e chamam operações.

Para obter mais informações sobre como usar foundation classes, consulte Guidelines for Using Visual FoxPro Foundation Classes.
