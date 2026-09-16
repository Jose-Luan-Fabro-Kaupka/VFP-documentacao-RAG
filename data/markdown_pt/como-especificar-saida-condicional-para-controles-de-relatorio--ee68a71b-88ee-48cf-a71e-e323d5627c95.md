# Como: especificar saída condicional para controles de relatório

Você pode especificar uma condição lógica que é avaliada pelo mecanismo de relatório para determinar se a saída de um controle deve ser renderizada. Se a expressão for avaliada como False (.F.), a saída do controle não é exibida.

Para exemplos de expressões de saída, consulte os relatórios de exemplo Colors.frx e Ledger.frx no diretório Visual FoxPro ...\Samples\Solution\Reports.

### Para adicionar uma expressão de saída a um controle de relatório
- Abra o relatório ou etiqueta no designer apropriado.
- No designer, clique duas vezes no controle desejado. A caixa de diálogo de propriedades do controle de relatório é aberta. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo do controle de relatório ou outra caixa de diálogo pode ser exibida. Na caixa de diálogo do controle de relatório, clique em Print When para abrir a caixa de diálogo Print When. Para obter mais informações, consulte _REPORTBUILDER System Variable e Print When Dialog Box.
- Na caixa de diálogo de propriedades do controle de relatório, clique na guia Print when se ela não estiver selecionada.
- Na caixa Print only when expression is true, digite uma expressão ou crie uma clicando no botão de reticências ( … ) para abrir o Expression Builder.
- Quando terminar, clique em OK.

Para obter mais informações, consulte Print When Tab, Report Control Properties Dialog Box (Report Builder) e Expression Builder Dialog Box.
