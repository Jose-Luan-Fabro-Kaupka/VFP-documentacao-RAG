# Classe base Graph Object Foundation Class

| Categoria | Automation |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Automation |
| Classe | autograph |
| Classe base | Custom |
| Biblioteca de classes | autograph.vcx |
| Classe pai | automation |
| Amostra | ...\Samples\Solution\Ffc\Automate.scx |

# Observações

Esta classe customizada gera um gráfico automatizando o MS Graph usando o mecanismo principal do Graph Wizard.

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do Component Gallery Item, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro abre um builder para que você possa especificar os valores cOutputfile, nChartType, lAddLegend e lSeriesByRow. Você também pode usar a classe autograph e fornecer valores para campos, tipo de gráfico, o formulário de visualização e o nome padrão em código de programa. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para obter mais informações sobre o uso de classes base.

| Properties, Events, Methods | Descrição |
| --- | --- |
| propriedade aDataFields[1,1] | Especifica o nome de um campo numérico na tabela de destino (o valor do eixo "Y"). Padrão: .F. |
| propriedade cCategoryField | Especifica um campo na tabela de destino (o eixo "X"). Padrão: .F. |
| propriedade cOutFile | Nome do arquivo de saída, se houver. Padrão: "" |
| propriedade cTitle | Legenda do título do gráfico. Padrão: "" |
| propriedade lCurrRec | Especifica se deve manter o número do registro atual, se estiver grafando apenas um registro. Padrão:.F. |
| propriedade lAddedData | Sinaliza se os dados já foram adicionados para desempenho. Padrão: .F. |
| propriedade lAddLegend | Adiciona uma legenda ao gráfico. Padrão: .T. |
| propriedade lAddTitle | Adiciona um título ao gráfico. Padrão: .T. |
| propriedade lGraphRecord | Especifica se deve grafar o registro atual. O padrão grafará o cursor inteiro. Padrão: .F. |
| propriedade lKeepForm | Especifica se deve usar o formulário e o controle OLE fornecidos pelo usuário. Padrão: .F |
| propriedade lSeriesByRow | Plota uma série por linha ou coluna. Padrão: .T. |
| propriedade lShowNulls | Exibe valores null no gráfico. Padrão: .T. |
| propriedade lShowWhenDone | Especifica se deve exibir uma visualização do formulário. Padrão: .T. |
| propriedade lUse8Type | Especifica se deve usar a propriedade nChartType. Padrão: .F. |
| propriedade lUseAutoformat | Usa a galeria de autocharting do MS Graph. Padrão: .F. |
| propriedade nAction | Especifica o tipo de ação de saída: 0 = preview1 = save to form2 = save to table3 = save to query Padrão: 1 |
| propriedade nChartAutoformat | Formato de gráfico para autoformat. Padrão: 2 |
| propriedade nChartAutoGallery | Formato de gráfico da galeria para autoformat. Padrão: 1 |
| propriedade nChartSubType | Subtipo de gráfico. Padrão: 1 |
| propriedade nChartType | Especifica o tipo de gráfico. Os valores válidos são: 1 = Area2 = Bar3 = Column4 = Line5 = Pie6 = Doughnut7 = Radar8 = Scatter9 = Area 3D10 = Bar 3D11 = Column 3D12 = Line 3D13 = Pie 3D -4102 = Pie 3D Padrão: 1 |
| propriedade nGraphVersion | Versão do Graph em uso. Padrão: 5 |
| propriedade cDefNewField | Interno à classe. |
| propriedade cGraphDBF | Interno à classe. |
| propriedade cGraphField | Interno à classe. |
| propriedade cGraphFldCol | Interno à classe. |
| propriedade cGraphFldRow | Interno à classe. |
| propriedade cGraphPrevClass | Interno à classe. |
| propriedade cLastDataCol | Interno à classe. |
| propriedade cLastDataRow | Interno à classe. |
| propriedade cOLEServer | Interno à classe. |
| propriedade cOpenAlias | Interno à classe. |
| propriedade cOutGenField | Interno à classe. |
| propriedade GraphPreview | Interno à classe. |
| propriedade lAutograph | Interno à classe. |
| propriedade lDontStripLegend | Interno à classe. |
| propriedade lHadPreview | Interno à classe. |
| propriedade lReplaceDBF | Interno à classe. |
| propriedade lStripExcessLegend | Interno à classe. |
| propriedade nDataCount | Interno à classe. |
| propriedade nDataSeries | Interno à classe. |
| propriedade nLastAction | Interno à classe. |
| propriedade nTotalDataFlds | Interno à classe. |
| propriedade oGraphRef | Interno à classe. |
