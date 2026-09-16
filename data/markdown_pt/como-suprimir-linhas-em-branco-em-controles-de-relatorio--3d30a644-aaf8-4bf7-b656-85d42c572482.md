# Como: suprimir linhas em branco em controles de relatório

Seu relatório pode incluir registros que não contêm valores para todos os campos do relatório. Por padrão, o Visual FoxPro deixa a área desse campo em branco. Para reduzir o "espaço em branco" na saída renderizada do relatório, você pode especificar que o mecanismo de relatório contraia verticalmente a saída do relatório nos casos em que todos os controles em uma linha horizontal no layout são renderizados como vazios.

### Para suprimir linhas em branco em um controle de relatório
- Abra o relatório ou etiqueta no designer apropriado.
- No designer, clique duas vezes no controle de relatório desejado. A caixa de diálogo de propriedades do controle de relatório é aberta. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo do controle de relatório é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte a variável de sistema _REPORTBUILDER e a caixa de diálogo Print When .
- Na caixa de diálogo de propriedades do controle de relatório, clique na guia Print when se ela não estiver selecionada.
- Na guia Print when, clique em Remove line if blank e depois em OK .

Para obter mais informações, consulte a guia Print When, Report Control Properties Dialog Box (Report Builder).

> **Observação:** Quando um campo em uma faixa de relatório está em branco ou o campo na tabela subjacente está vazio, o Visual FoxPro verifica a faixa de relatório em busca de outros controles de relatório. Se não existirem outros controles na faixa de relatório, o Visual FoxPro remove a linha inteira. Você pode escolher se a faixa de relatório se ajusta para linhas em branco suprimidas. Para obter mais informações, consulte Como: configurar a saída para faixas de relatório .
