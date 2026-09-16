# Como: definir variáveis de relatório

Você pode definir variáveis no layout de relatório ou etiqueta para armazenar, manipular e exibir valores.

Variáveis de relatório são PUBLIC em escopo e permanecem disponíveis após uma execução de relatório (a menos que você especifique explicitamente que devem ser liberadas).

# Definindo variáveis de relatório

### Para definir uma variável de relatório
- Abra o relatório ou etiqueta no designer apropriado.
- No menu Report, clique em Variables . A caixa de diálogo Report Properties abre. Observação Se a variável de sistema _REPORTBUILDER não está definida para o Report Builder padrão ou está definida para um builder de terceiros, a caixa de diálogo Report Variables é exibida ou uma caixa de diálogo diferente pode ser exibida. Para mais informações, consulte Variável de sistema _REPORTBUILDER e Caixa de diálogo Report Variables .
- Na caixa de diálogo Report Properties, clique na guia Variables se ela não estiver selecionada.
- Na guia Variables, clique em Add .
- Na caixa de diálogo Report Variable, digite o nome da variável.
- Na caixa Value to store, digite uma expressão. Em qualquer momento durante a execução do relatório, a variável conterá os resultados avaliados da expressão.
- Para especificar um valor inicial para a variável, na caixa Initial value, digite uma expressão. O resultado avaliado desta expressão será atribuído à variável no início da execução do relatório. Observação Se você usar a variável de relatório em cálculos, certifique-se de inicializar a variável com um valor diferente de zero para evitar um erro de divisão por zero. Se você não especificar um valor inicial, o Visual FoxPro atribui um valor padrão de 0.
- Para especificar cálculos adicionais a serem executados nos resultados da expressão avaliada antes de atribuir um valor à variável, na lista Calculation type, selecione a operação de cálculo desejada.
- Para tipos de cálculo cumulativos, você também pode especificar o ponto em que o valor da variável é redefinido, alterando a configuração de Reset value based on . Para informações detalhadas sobre tipos de cálculo, consulte Guia Calculate, caixa de diálogo Report Control Properties (Report Builder) .
- Quando terminar, clique em OK . Agora você pode usar a variável em seu relatório ou etiqueta.

Para mais informações, consulte Guia Variables, caixa de diálogo Report Properties (Report Builder).

Por exemplo, considere uma tabela de informações de folha de ponto com campos para horários de entrada e saída armazenados nos campos `hour_in`, `min_in`, `hour_out` e `min_out`. A tabela a seguir mostra três variáveis de exemplo usadas em um relatório:

| Para armazenar este valor | Crie esta variável | Usando esta expressão |
| --- | --- | --- |
| Hora de chegada do funcionário | tArrive | hour_in + (min_in / 60) |
| Hora de saída do funcionário | tLeave | hour_out + (min_out / 60) |
| Tempo total de presença do funcionário | tDayTotal | tLeave - tArrive |

Você pode usar a variável `tDayTotal` em uma variedade de outros cálculos, como o número de horas trabalhadas em uma semana, um mês ou um ano; o número médio de horas trabalhadas por dia; e assim por diante.

Para exemplos de variáveis de relatório, consulte os relatórios de amostra Percent.frx e Invoice.frx no diretório Visual FoxPro ...\Samples\Solution\Reports.
