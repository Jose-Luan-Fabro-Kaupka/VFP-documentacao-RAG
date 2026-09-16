# Classe base Foundation Output Object

Este é um objeto de relatório genérico que fornece uma variedade de opções de origem e destino de relatório a partir de relatórios e etiquetas ou diretamente de uma fonte de dados.

| Categoria | Reporting |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Output |
| Classe | _output |
| Classe base | Container |
| Biblioteca de classes | _reports.vcx |
| Classe pai | _container |
| Amostra | ...\Samples\Solution\Ffc\output.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do item do Component Gallery, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro coloca a classe no formulário. Você pode então especificar os valores de propriedade apropriados e fornecer quaisquer objetos de entrada e saída necessários. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Diretrizes para usar classes base Foundation do Visual FoxPro para obter mais informações sobre o uso de classes base Foundation.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| propriedade aDestinations[1,2] | O array de destinos. Padrão: .F. |
| propriedade aOptions[1,2] | O array de opções de saída de destino. Padrão: .F. |
| propriedade cAlias | Especifica a fonte de dados usada para formatos de saída que não são relatório/etiqueta. Esta propriedade usa por padrão o alias atual, se houver. Padrão: "" |
| propriedade cDestination | Especifica uma lista de destinos disponíveis que muda dinamicamente, dependendo se cReport , cAlias ou ambos contêm valores. A lista de destinos disponíveis é armazenada no array aDestinations. Padrão: "PRINTREPORT" |
| propriedade cDisplayFontName | Especifica uma fonte na tela para saída; por exemplo, quando você emite BROWSE ou quando a classe _Showtext é instanciada para exibição de texto. Padrão: Courier New |
| propriedade cFieldList | Especifica uma lista delimitada por vírgulas de campos ou expressões. Afeta apenas fontes de dados diretas (BROWSEs e LISTs). Padrão: "" |
| propriedade cHtmlClass | Especifica uma classe HTML opcional e biblioteca de classes passada a _GENHTML. Padrão: "" |
| propriedade cHtmlstyleid | Especifica um estilo HTML opcional passado a _GENHTML. Padrão: "" |
| propriedade cOption | Especifica a lista de opções disponíveis que muda dinamicamente para se adequar ao cDestination atual. Padrão: WINDEFAULT |
| propriedade cReport | Especifica um formulário de etiqueta ou relatório adequado para saída formatada do Visual FoxPro. Padrão: "" |
| propriedade cScope | Especifica uma cadeia de caracteres expandida por macro a ser adicionada ao comando que executa a saída real. Deve ser um escopo válido como "FOR l Expression ". Padrão: "" |
| propriedade cTextfile | Especifica o nome do arquivo para todos os destinos de saída que vão para disco, que incluem arquivos de texto, arquivos de imagem de impressora e formatos de exportação. Padrão: "" |
| propriedade cVFPPrinterName | Especifica o nome da impressora padrão atual do Visual FoxPro, distinta da impressora padrão do Windows. Padrão: "" |
| propriedade lAddSourceNameToDropdown | Especifica se alguns destinos são exibidos no array aDestinations. Padrão: .T. |
| propriedade lPreventSourceChanges | Impede alterações de origem para cAlias ou cReport . Padrão: .F. |
| método CopyTable | Exporta uma tabela. Sintaxe: CopyTable( ) Retorno: nenhum Argumentos: nenhum |
| método GenHTML | Gera código HTML chamando o programa Genhtml.prg. Sintaxe: GenHTML( ) Retorno: nenhum Argumentos: nenhum |
| método Output | Especifica o método principal que é chamado para gerar saída com base nas configurações. Sintaxe: Output(liSelect) Retorno: nenhum Argumentos: liSelect especifica o destino de saída. |
| método OutputToScreen | Envia saída para a tela. Sintaxe: OutputToScreen( ) Retorno: nenhum Argumentos: nenhum |
| método SetDestinations | Avalia o ambiente atual para popular um array de destinos de saída. Sintaxe: SetDestinations( ) Retorno: lSuccess Argumentos: nenhum |
| método SetOptions | Avalia o ambiente atual para popular um array de opções para destinos de saída. Sintaxe: SetOptions( ) Retorno: lSuccess Argumentos: nenhum |
| método cAlias_assign | Interno à classe. |
| método cDestination_assign | Interno à classe. |
| método cDisplayFontName_assign | Interno à classe. |
| método cOption_assign | Interno à classe. |
| método cReport_assign | Interno à classe. |
| método cScope_assign | Interno à classe. |
| método cVFPPrinterName_access | Interno à classe. |
| método lPreventSourceChanges_assign | Interno à classe. |
| método PrintList | Interno à classe. |
| método PrintReport | Interno à classe. |
| método SetOutputPrinter | Interno à classe. |
| método SetVFPPrinter | Interno à classe. |
