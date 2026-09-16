# Classe base ReportListener HTML Foundation

HtmlListener fornece a implementação padrão do Report Output Application para ListenerType 5 (saída HTML) e a implementação padrão de Genhml.prg para saída HTML de arquivos de relatório e etiqueta (tabelas frx e lbx).

| Categoria | Reporting |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Output\Report Listeners |
| Classe | HtmlListener |
| Classe base | ReportListener |
| Biblioteca de classes | _REPORTLISTENER.vcx |
| Classe pai | XmlDisplayListener ( ReportListener XML Display-Style Foundation Class ) |

# Observações

HtmlListener aproveita a capacidade do XmlListener de aplicar um documento de transformação XSLT ao formato XML base de relatório VFP automaticamente ao final da execução de um relatório. Para obter informações sobre as capacidades de processamento XSLT do XmlListener, consulte ReportListener XML Foundation Class.

HtmlListener não adiciona novas propriedades ou métodos à sua classe pai, XmlDisplayListener. Ele define a extensão do arquivo de saída como `"HTM"` e sua propriedade ApplyUserTransform como `.T.` e amplia o método interno XmlListener, getDefaultUserXslt, para fornecer um documento de transformação XSLT apropriado para produção HTML.

O documento XSLT personalizado incluído em HtmlListener trata todos os detalhes de leitura do VFP-RDL para as informações originais do seu relatório ou layout e reproduz esse layout em HTML. A impressora do usuário em tempo de execução pode ter um tamanho de página imprimível diferente da impressora para a qual o relatório foi originalmente renderizado, e o navegador do usuário também pode adicionar cabeçalhos, rodapés e margens a esse layout de página. Como resultado, você não deve confiar nesse formato para imprimir com quebras de página apropriadas no navegador; ele foi projetado principalmente para exibição de página.

> **Dica:** Você pode usar a cláusula RANGE no comando REPORT FORM para fornecer dados HTML em uma base página por página, para que imprima corretamente no navegador. Observe que o documento XSLT padrão do HtmlListener suporta a cláusula RANGE apenas para relatórios únicos, não para vários relatórios usando a capacidade NOPAGEEJECT. Sem RANGE , o XSLT padrão do HtmlListener suporta vários relatórios em um único documento HTML.

Se você deseja cópias exatas e imprimíveis de página, pode usar o método OutputPage da classe ReportListener para fornecer arquivos de imagem de páginas individuais do relatório para fins de impressão. Consulte o Objeto ReportListener para obter mais informações.

No entanto, você não está limitado à reprodução fiel do design original do relatório. Você pode substituir a transformação XSLT padrão por qualquer outra renderização dos dados originais do relatório que lhe convier, personalizando um único resultado de relatório para diferentes usuários em diferentes dispositivos de destino. Basta armazenar uma referência a um documento de transformação XSLT diferente na propriedade XsltProcessorUser. O código de exemplo em ReportListener XML Foundation Class mostra como alterar o conteúdo do documento.

# Exemplo

Este exemplo define o arquivo de saída de destino do HtmlListener e a precisão de coordenadas numéricas, e especifica que quaisquer arquivos de imagem renderizados no relatório devem ser copiados para um subdiretório relativo ao seu arquivo de saída. Esta é uma abordagem apropriada se o relatório será publicado em um servidor Web.

> **Observação:** Este exemplo foi projetado para ser usado em um aplicativo distribuído; portanto, não inclui um caminho para a biblioteca de classes FFC. Se você deseja executá-lo como um programa na linha de comando, descomente a instrução SET PATH.

Após executar um relatório, o exemplo abre a saída HTML em uma janela de edição do Visual FoxPro para verificação e depois exibe o conteúdo atual do documento XsltProcessorUser como texto na tela do Visual FoxPro, para sua referência.

> **Dica:** Se você examinar o conteúdo do documento XSLT de perto, verá que a propriedade Stylesheet.xml ainda mostra o valor padrão numberPrecision pré-compilação, 5 , e os valores padrão para todos os outros parâmetros neste documento XSLT. Por exemplo, externalFileLocation é um parâmetro no documento XSLT, e o valor que você atribui no exemplo, ".\images" , não aparece no conteúdo Stylesheet.xml. O método applyXSLT do XMLListener aplica os valores de tempo de execução dos parâmetros à instância Stylesheet compilada, imediatamente antes de aplicar o documento de transformação compilado ao seu XML de origem.

```foxpro
LOCAL oHtml
* SET PATH TO (HOME() + "FFC") ADDITIVE
oHtml = NEWOBJECT("HtmlListener","_reportlistener.vcx")
oHtml.targetFileName = "c:\temp\myOutput.htm"
* The following lines of code set the precision of coordinates
* of most individual layout items as a number of decimal places
* (the XSLT's coordinates are in inches).
* The default number of decimal places is set in the XSLT to 5,
* but here the value is set to 6:
oHtml.xsltParameters = CREATEOBJECT("Collection")
oHtml.xsltParameters.Add(6,"numberPrecision")
* The following directory must exist *before*
* you assign the next property:
IF NOT DIRECTORY("c:\temp\images")
   MD c:\temp\images
ENDIF
* Assignment of the image directory as
* a relative reference ensures
* appropriate src attributes in the
* HTML document:
oHtml.externalFileLocation = ".\images"
oHtml.copyImageFilesToExternalFileLocation = .T.
REPORT FORM ? OBJECT oHtml
MODIFY FILE (oHtml.targetFileName)
ACTI SCREEN
? oHtml.XsltProcessorUser.Stylesheet.Xml
```
