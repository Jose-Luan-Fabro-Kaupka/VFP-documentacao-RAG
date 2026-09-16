# Classe base Graph By Record Foundation

Esta classe de contêiner cria gráficos no nível do registro, diferentemente da classe AutoGraph, que cria gráficos a partir de um cursor inteiro do Visual FoxPro. A classe também inclui um conjunto de botões para navegar entre registros e atualizar o gráfico dinamicamente.

| Categoria | Automation |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Automation |
| Classe | _graphbyrec |
| Classe base | Container |
| Biblioteca de classes | _utility.vcx |
| Classe pai | _container |
| Exemplo | ...\Samples\Solution\Ffc\automate.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho Item da Component Gallery, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário em um ambiente de dados, o Visual FoxPro abre um construtor para que você possa especificar os valores nChartType e cLblField para os pontos de dados do gráfico e os rótulos dos eixos. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade cLblField | Especifica a legenda para o rótulo do registro. Padrão: "" |
| Propriedade nChartType | Especifica o tipo de gráfico. Os valores válidos são: 1 = Area2 = Area 3D3 = Bar4 = Bar 3D5 = Column6 = Column 3D7 = Pie8 = Pie 3D9 = Line10 = Line 3D Padrão: 4 |
| Propriedade lSeriesByRow | Especifica se uma série deve ser plotada por linha. Padrão: .T. |
| Propriedade aDataFields[1] | Especifica a matriz de campos de dados a serem grafados. Padrão: .F. |
| Método SetupGraph | Inicializa os controles do gráfico. Sintaxe: SetupGraph( ) Retorno: nenhum Argumentos: nenhum |
| Método RefreshGraph | Atualiza o gráfico quando o ponteiro de registro é movido. Sintaxe: RefreshGraph( ) Retorno: nenhum Argumentos: nenhum |
