# Assistente Graph

O assistente Graph cria um gráfico a partir de uma tabela do Visual FoxPro usando o Microsoft Graph. Você desejará usar um gráfico de um tipo ou outro para facilitar a exibição visual ou a avaliação de dados contidos em tabelas grandes ou relatados em planilhas densas.

Quanto maior sua tabela, mais tempo o assistente levará para processar seu gráfico. Você pode considerar limitar o escopo de registros em uma tabela grande criando uma view antes de executar o assistente Graph. Para obter mais informações, consulte Como: criar consultas (Visual FoxPro).

 Para acessar o assistente Graph
 - No menu Tools, escolha Wizards e clique em Query.
- Na caixa de diálogo Wizard Selection, escolha Graph Wizard.

# Etapa 1 – Select Fields

Nesta etapa, você pode escolher uma tabela livre ou uma tabela dentro de um banco de dados como fonte para seu gráfico. Isso pode normalizar a entrada em formulários de entrada de dados e, assim, suas tabelas de dados. Você pode selecionar campos de apenas uma única tabela ou view. Esta seleção deve incluir pelo menos um campo numérico.

 Para selecionar os campos para seu gráfico
 - Use os controles Databases and Tables para localizar e selecionar a tabela que deseja usar.
- Na janela Available fields, selecione um ou mais campos que deseja usar da tabela selecionada e use os botões de seta para movê-los para a janela Selected fields. Observação Se você escolher um campo general ou automation nesta etapa, o campo não estará disponível na próxima etapa para definir o layout do gráfico.

# Etapa 2 – Define Layout

Nesta etapa, você especifica qual campo numérico é representado no gráfico e qual campo fornece as divisões ao longo das quais esses valores são representados. Arraste um ou mais dos campos numéricos disponíveis da janela Available fields para a janela Data series. Arraste outro campo da janela Available fields para a caixa Axis abaixo da imagem do gráfico. Por exemplo, em uma tabela contendo valores de salário como um campo numérico, você pode escolher o campo de salário e um campo de nome ou região para representar no gráfico.

# Etapa 3 - Select Graph Style

Nesta etapa, você seleciona um estilo de gráfico que apresenta efetivamente as informações. Cada estilo de gráfico representa os dados de maneira diferente. Observe as imagens nos botões para escolher um estilo que atenda às suas necessidades. A lista a seguir resume os tipos de gráfico disponíveis:
 **Area and 3D area**
Indica a importância relativa dos valores ao longo de um período de tempo e enfatiza a quantidade de mudança em vez da taxa de mudança.
**Bar and 3D bar**
Indica valores de elementos discretos em relação uns aos outros. Isso é semelhante a um gráfico de colunas, mas disposto verticalmente.
**Column and 3D column**
Indica variação ao longo de um período de tempo ou faz comparações entre itens discretos. A disposição horizontal de colunas sugere fluxo de tempo mais que um gráfico de barras.
**Pie and 3D pie**
Indica as relações ou proporções de partes em relação a um todo. Este tipo de gráfico sempre contém apenas uma série de dados.
**Line and ribbon (3D line)**
Indica tendências ou mudanças nos dados ao longo de um período de tempo. Isso é semelhante a um gráfico de área, mas enfatiza o fluxo de tempo e a taxa de mudança em vez da quantidade de mudança.
**Scatter (XY)**
Indica a relação ou grau de relação entre valores numéricos em diferentes grupos de dados. Este tipo de gráfico é útil para determinar padrões ou tendências e para determinar se variáveis são dependentes ou afetam umas às outras.

# Etapa 4 - Finish

Nesta etapa, você especifica a forma como o gráfico é gerado e se ele exibirá o nome do campo numérico selecionado e valores nulos. Você pode salvar o gráfico em um formulário, pode usar o gráfico em um relatório salvando-o em uma tabela ou pode criar uma consulta que gera o gráfico.

### Salvando em um formulário

Se você escolher salvar o gráfico em um formulário, o assistente cria um formulário contendo o gráfico e, opcionalmente, uma legenda do(s) valor(es) representado(s).

### Salvando em uma tabela

Se você escolher salvar o gráfico em uma tabela, o assistente cria uma tabela com um único registro contendo um campo General que armazena um objeto Automation para seu gráfico. Você pode então incluir este campo em um relatório. Depois que o assistente termina, ele deixa sua nova tabela aberta. Para visualizar o gráfico, navegue pela nova tabela e clique duas vezes no campo Olegraph.

### Criando uma consulta

Se você escolher criar uma consulta, o assistente salva uma consulta que envia seus resultados para o gráfico que você especificou. Depois que o assistente salva a consulta, você pode abri-la e modificá-la como qualquer outra consulta no Query designer.
 **Show null values check box**
Especifica que o gráfico represente quaisquer valores nulos, bem como todos os valores positivos e negativos. Por exemplo, pode ser importante para sua apresentação mostrar que nada aconteceu em dias específicos ou com clientes específicos.
**Add a legend to the graph check box**
Especifica que o gráfico inclua uma legenda nomeando o valor representado. Isso ajuda a tornar seu gráfico e seus dados mais legíveis.
**Preview button**
Permite visualizar o gráfico antes de salvá-lo em um formulário, tabela ou arquivo de consulta.
