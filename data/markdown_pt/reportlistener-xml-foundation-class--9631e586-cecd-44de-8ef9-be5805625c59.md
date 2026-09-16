# ReportListener XML Foundation Class

XmlListener fornece a implementação padrão do Report Output Application de ListenerType 4 (saída XML). Suas propriedades incluem numerosas configurações que você pode usar para ajustar o VFP Report XML Schema e adaptar sua saída para diferentes propósitos. Por exemplo, se você enviar a saída XML do seu relatório para outro aplicativo, para importação em um banco de dados, pode não precisar da saída das bandas Page Header e Page Footer no seu relatório. Essas porções do relatório são renderizadas em intervalos com base no tamanho físico da página de layout original do relatório e podem não se relacionar diretamente com linhas de dados no relatório.

VFP Report XML inclui dados que descrevem as informações de layout do arquivo de relatório ou etiqueta original (a tabela frx ou lbx), bem como as configurações do comando REPORT FORM em tempo de execução, instruções da impressora, tabelas abertas e relacionamentos. Esta seção da estrutura XML é conhecida como VFP-RDL, ou Visual FoxPro Report Definition Language. Os elementos de esquema para estes itens são diferentes dos elementos gerados para as expressões em tempo de execução, linhas e outros controles de layout de relatório conforme o Report Engine renderiza cada registro durante um comando REPORT FORM.

Para informações completas sobre o VFP Reporting XML Schema, consulte Using VFP Report Output XML.

| Category | Reporting |
| --- | --- |
| Default Catalog | Visual FoxPro Catalog\Foundation Classes\Output\Report Listeners |
| Class | XmlListener |
| Base Class | ReportListener |
| Class Library | _REPORTLISTENER.vcx |
| Parent Class | UtilityReportListener ( ReportListener Utility and File-handling Foundation Class ) |

# XmlListener e continuação de relatório

XmlListener respeita a palavra-chave NOPAGEEJECT em comandos REPORT FORM executados em sequência, para que um único documento VFP Report XML possa incluir detalhes sobre várias execuções de relatório.

A palavra-chave nativa NOPAGEEJECT está disponível apenas de dentro de programas (não tem efeito quando você emite um comando REPORT FORM na janela Command). Você pode usar a propriedade noPageEject do XmlListener, em vez da palavra-chave padrão, se quiser experimentar esta capacidade interativamente.

> **Importante:** Você deve observar as mesmas restrições ao aplicar continuação à geração de XML que usaria ao imprimir. Você é responsável por emitir um REPORT FORM final sem uma cláusula NOPAGEEJECT para dizer ao XmlListener para parar de gravar no arquivo, assim como precisaria do comando REPORT FORM final para fechar a fila de impressão. No entanto, se você esquecer de fazer isso, o método Destroy da classe encerrará o trabalho de saída e fechará o arquivo.

XmlListener manipula a cláusula RANGE do comando REPORT FORM. No entanto, em documentos de relatório contendo vários relatórios por meio do recurso de continuação, ele só manipula RANGE se você não usar também a cláusula NORESET.

# Processo de geração XML do XmlListener

XmlListener usa uma combinação de técnicas para fornecer seus resultados XML. A classe Visual FoxPro XMLAdapter fornece a porção do esquema que descreve metadados FRX e de tempo de execução do relatório (o VFP-RDL). Também usa objetos MSXML diretamente para aprimorar os nós VFP-RDL. A classe gera a porção de dados do esquema usando um processo de saída "raw" que envia dados para um arquivo usando as funções de arquivo de baixo nível do Visual FoxPro e aproveitando plenamente outras capacidades nativas de manipulação de cadeias de caracteres para lidar com tarefas normais de codificação.

> **Dica:** Você pode recompilar a classe para ajustar os objetos MSXML que o XmlListener usa, e também pode optar por usar objetos MSXML consistentemente em vez do método "raw" que usa por padrão para fornecer as porções de dados da saída. Usar objetos MSXML em todo o processamento pode facilitar alguns cenários em que a saída do seu relatório requer codificação especializada de dados binários. Para ajustar o processo de geração, altere os valores definidos no arquivo de cabeçalho do XmlListener, REPORTLISTENERS.H. Os valores padrão são mostrados abaixo:

```foxpro
#DEFINE OUTPUTXML_RAW             0
#DEFINE OUTPUTXML_DOM             1
#DEFINE XMLOUTPUT      OUTPUTXML_RAW
#DEFINE OUTPUTXML_DOMDOCUMENTOBJECT ;
  "Msxml2.FreeThreadedDOMDocument.4.0"
#DEFINE OUTPUTXML_DOMFREETHREADED_DOCUMENTOBJECT ;
  "Msxml2.FreeThreadedDOMDocument.4.0"
#DEFINE OUTPUTXML_XSLT_PROCESSOROBJECT ;
  "Msxml2.XSLTemplate.4.0"
```

# XmlListener e XSLT

Depois de gerar um documento XML, você frequentemente precisa movê-lo de um formato para outro. XmlListener fornece recursos para Extensible Stylesheet Language Transformations (XSLT). Você pode carregar documentos XSLT e solicitar que o XmlListener forneça o resultado final da transformação escolhida, em vez de seu documento de esquema VFP Report XML nativo.

# XmlListener e sua tabela de configuração

Como sua superclasse, UtilityReportListener, XmlListener aproveita a mesma estrutura de tabela de configuração do Report Output Application. Reserva um intervalo de valores em OBJTYPE (1100 a 1199) como forma de consultar nomes de nós XML para vários elementos de relatório. Usar a estrutura de configuração para armazenar nomes de nós é uma forma de localizar os elementos XML para legibilidade. Por exemplo, o valor padrão de `PH` como nome de nó para bandas Page Header pode não ser intuitivo para um desenvolvedor que não trabalha em inglês, ou o desenvolvedor pode preferir uma notação menos concisa. Como XmlListener pode ler seus valores preferidos em tempo de execução, o esquema VFP Report Xml deve ser considerado um modelo estrutural; os nomes de nós reais em tempo de execução podem ser diferentes.

XmlListener armazena estas informações na tabela de configuração de acordo com o esquema que você vê na tabela a seguir.

| Field | Usage |
| --- | --- |
| OBJTYPE | Armazena o valor OBJTYPE original da tabela FRX para o tipo de banda ou objeto de layout que o elemento XML descreve, mais um deslocamento de 1100. Por exemplo, um controle de layout Picture em um FRX tem OBJTYPE 17, então um registro que armazena o nome do nó XML para um controle de layout Picture tem o valor 1117. |
| OBJCODE | Tem o mesmo valor que um registro do mesmo tipo no FRX. Por exemplo, um registro que armazena o nome do nó XML para uma banda Detail Footer tem o mesmo OBJCODE que um registro de banda DetailFooter no FRX. |
| OBJNAME | Não usado pelo XmlListener |
| OBJVALUE | Armazena o nome do nó. |
| OBJINFO | Armazena um valor descritivo para o tipo de registro FRX. Por exemplo, Detail Footer Band nodename . |

Se XMLListener for a subclasse de UtilityReportListener que gera a tabela de configuração em tempo de execução, ou se não conseguir encontrar seus registros necessários na tabela de configuração preexistente, incluirá registros apropriados para todos os elementos de que precisa. Também adiciona as chaves de índice especializadas de que precisa à tabela de configuração, se necessário.

# Observações

XmlListener adiciona as seguintes propriedades e métodos públicos à sua classe pai, UtilityReportListener.

| Properties and methods | Description |
| --- | --- |
| applyUserTransform Property | Indica se XMLListener deve aplicar automaticamente uma transformação XSLT definida pelo usuário na conclusão de uma execução de relatório. Padrão .F. Observações: Quando você define esta propriedade como .T. , o método assign associado verifica se você já preencheu a propriedade xsltProcessorUser com um objeto processador apropriado. Se não, executa um método interno, getDefaultUserXslt, para carregar a propriedade xsltProcessorUser. Este método interno fornece um gancho para subclasses fornecerem seu documento XSLT preferido para uso sem exigir um procedimento de carregamento externo. |
| applyXslt Method | Fornece recursos genéricos para aplicar XSLT a XML. Sintaxe: applyXslt (vSource, vProcessor [, vParamCollection]) Valores de retorno: cXmlResult Parâmetros: vSource pode ser o nome de um arquivo contendo o documento XML de origem, uma cadeia contendo o documento XML ou um objeto de documento DOM. vProcessor pode ser o nome de um arquivo contendo o documento do processador XSLT, uma cadeia contendo o documento XSLT ou um objeto processador XSLT. vParamCollection é um objeto opcional do tipo Collection. Se estiver disponível, este método adiciona os membros da coleção à instância do processador XSLT como parâmetros globais antes de aplicar a transformação XSLT ao documento de origem. Usa as chaves da coleção como nomes de parâmetros e os valores correspondentes da coleção como valores de parâmetros. XmlListener fornece uma propriedade, xsltParameters, que você pode usar para manter a coleção que constrói para manter estes parâmetros entre chamadas. Observações: Tanto os tipos de objeto de origem XML quanto de processador XSLT são definidos em REPORTLISTENERS.H. Você pode editar este arquivo de cabeçalho e recompilar a classe para escolher objetos de processamento diferentes. |
| contAttr Property | Fornece o nome do atributo usado para mostrar o tipo de continuação para um objeto de layout que pode abranger bandas ou páginas. Padrão "c" |
| currentDocument Property | Contém informações sobre o documento XML para o qual a saída está sendo gerada atualmente durante uma execução de relatório. Padrão .NULL. |
| heightAttr Property | Fornece o nome do atributo XML usado para mostrar a altura de um objeto de layout. Padrão "h" |
| idAttribute Property | Fornece o nome do atributo XML usado para fornecer o número de registro FRX de um objeto de layout ou número de página de um objeto de banda de formatação (coluna ou página). Padrão "id" |
| idrefAttribute Property | Fornece o nome do atributo XML usado para fornecer a página atual de um objeto de layout ou número de registro FRX de um objeto de banda de formatação (coluna ou página). Padrão "idref" |
| includeBandsWithNoObjects Property | Indica se informações de nível de banda para bandas sem conteúdo devem ser incluídas no XML. Padrão .F. |
| includeBreaksInData Property | Determina se bandas de formatação (página e colunas) devem ser incluídas na saída e, em caso afirmativo, usando qual estrutura. Valor Significado 0 Fornece nós de banda de página posicionados junto com outras bandas no fluxo de dados, onde quer que ocorram 1 Sem informações de quebra de página, sem informações de cabeçalho e rodapé de página 2 Fornece coleção de páginas com dados de cabeçalhos e rodapés de página Padrão 0 |
| includeDataSourcesInVfpRdl Property | Indica se informações sobre as tabelas de origem, relações, índices, etc. devem ser incluídas na seção de metadados VFPRDL do XML do relatório. Padrão .F. |
| includeFormattingInLayoutObjects Property | Indica se informações de formatação, como atributos de posicionamento, devem ser incluídas no XML do relatório. Padrão .F. |
| leftAttr Property | Fornece o nome do atributo XML usado para mostrar a posição mais à esquerda de um objeto de layout. Padrão "l" |
| noPageEject Property | Indica se o XML Listener deve considerar a execução de relatório atual como continuada. Pode ser usado sem NOPAGEEJECT no comando REPORT FORM. Padrão .F. |
| resetDocument Method | Redefine o documento XML após uma execução de relatório. Sintaxe: resetDocument() Valores de retorno: nenhum Parâmetros: nenhum |
| topAttr Property | Fornece o nome do atributo XML usado para mostrar a posição mais alta de um objeto de layout. Padrão "t" |
| verifyNCName Method | Fornece método genérico para validar cadeias como NCNames padrão XML . Sintaxe: verifyNCName ( cName ) Valores de retorno: lValid Parâmetros: cName é a cadeia que você está verificando quanto à validade como valor NCName. Observações: Em XML, um NCName ou nome não colonizado é um valor legal para o namespace ou o nome (local) não prefixado de um nó. Por exemplo, no nome de nó xsl:template , tanto xsl quanto template são NCNames. |
| widthAttr Property | Fornece o nome do atributo XML usado para mostrar a largura de um objeto de layout. Padrão "w" |
| xmlMode Property | Determina quais partes do esquema VFP Report XML são incluídas na saída. Valor Significado 0 Somente dados 1 Somente VFP-RDL 2 Dados e VFP-RDL Padrão 2 |
| xsltParameters Property | Contém uma coleção de parâmetros opcional passada ao método ApplyXSLT quando XmlListener aplica automaticamente uma transformação XSLT do usuário na conclusão de uma execução de relatório. Padrão .NULL. Observações: O exemplo de código em ReportListener HTML Foundation Class usa xsltParameters explicitamente, para definir numberPrecision , um parâmetro de sua transformação padrão. O código da classe define vários outros parâmetros da transformação HTML padrão usando xsltParameters. Se você criar xsltParameters como um objeto de coleção você mesmo, conforme mostrado nesse exemplo, a classe HtmlListener usará este objeto, adicionando quaisquer chaves e valores necessários após verificar se já existem. |
| xsltProcessorRdl Property | Contém um objeto processador específico de Report Definition Language (RDL). Padrão .NULL. Observações: Reservado para uso futuro. Você pode carregar um objeto processador XSLT nesta propriedade usando as mesmas técnicas descritas para a propriedade xslProcessorUser. |
| xsltProcessorUser Property | Contém um objeto processador definível pelo usuário que, se preenchido e disponível no fim de uma execução, pode ser usado automaticamente pelo XML Listener para transformar o documento XML bruto conforme os requisitos. Padrão .NULL. Observações: Para alterar este documento, você tem várias opções: Armazene um nome de arquivo na propriedade, conforme mostrado no exemplo abaixo. Armazene um documento XSLT contido em uma variável de cadeia na propriedade. Armazene um objeto processador XSLT, com sua folha de estilo já carregada, na propriedade. Os tipos de objeto apropriados são definidos no arquivo de cabeçalho do XmlListener, REPORTLISTENERS.H . Se você armazenar o documento como cadeia ou nome de arquivo, XmlListener cria o objeto processador para você e carrega a folha de estilo. |

# Exemplo

Neste exemplo, o código ajusta as propriedades do XmlListener para atender a um cenário particular de transferência de dados (uma lista de clientes sendo transferida entre um aplicativo Visual FoxPro e um aplicativo CRM hospedado em um ambiente diferente).

O código fornece à propriedade xsltProcessUser do objeto um documento de transformação XSLT adequado, usando um dos três métodos descritos na tabela acima para carregar o objeto processador. Instrui o objeto a aplicar a transformação XSLT automaticamente após a execução do relatório. Em seguida, executa o relatório. O XSLT resultante atende aos requisitos do aplicativo CRM e pode ser importado sem alterações adicionais.

```foxpro
oXml = NEWOBJECT("XmlListener","_REPORTLISTENER")
WITH oXml
  .xmlMode = 0 && data only,
               && no RDL is needed for this
               && particular transform
  .xsltProcessorUser = "Customer.xslt"
  .applyUserTransform = .T.
ENDWITH
REPORT FORM Customer OBJECT oXml
MODIFY FILE (oXml.TargetFileName)
```
