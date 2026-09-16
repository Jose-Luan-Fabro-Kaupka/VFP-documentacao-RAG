# Como: adicionar controles Field a relatórios

Controles Field são como você renderiza dados de variáveis, expressões e campos em tabelas e views em um relatório ou etiqueta. Esses valores podem mudar para cada registro percorrido pelo mecanismo de relatório ao processar o relatório.

Se o layout do relatório tem um data environment associado, você pode adicionar campos de tabelas e views diretamente do data environment do relatório.

### Para adicionar um controle Field à página
- Abra o relatório ou etiqueta no designer apropriado.
- No menu Report, aponte para Insert Control e clique em Field . A caixa de diálogo Field Properties é aberta. Dica Você também pode clicar duas vezes no controle de relatório no Report Designer ou Label Designer para abrir a caixa de diálogo de propriedades do controle de relatório. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo Report Expression é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte _REPORTBUILDER System Variable e Report Expression Dialog Box .
- Na caixa de diálogo Field Properties, clique na guia General se ela não estiver selecionada.
- Na caixa Expression, digite a expressão, variável ou campo de tabela desejado. Para construir uma expressão, clique no botão de reticências ( … ) para abrir o Expression Builder .
- Quando terminar no Expression Builder , clique em OK .
- Na caixa de diálogo Field Properties, especifique as configurações de formatação desejadas e clique em OK . Dica Para especificar que a parte inferior do controle de relatório Field se expande para acomodar os resultados da expressão quando o controle é preenchido, clique em Stretch with overflow . Um controle Field para a variável, expressão ou campo aparece na banda Page Header do relatório por padrão. Dica Você pode adicionar controles de relatório Field na posição desejada selecionando-os na barra de ferramentas Report Controls e desenhando-os. Quando você especifica uma expressão em um controle de relatório Field, redimensione o controle de relatório Field para a quantidade mínima de espaço que a expressão requer. Se mais espaço for necessário, você pode definir o controle para expandir para valores maiores, mas não pode definir para reduzir de tamanho se menos espaço for necessário.

Para obter mais informações, consulte How to: Specify Expressions in Field Controls, General Tab, Report Control Properties Dialog Box (Report Builder) e Expression Builder Dialog Box.

Você também pode especificar os tipos de dados e opções de formato de saída para os valores armazenados no controle Field. Para obter mais informações, consulte How to: Specify Data Types for Field Controls.

### Para adicionar um controle Field diretamente do data environment
- Abra o relatório ou etiqueta no designer apropriado.
- No menu View, clique em Data Environment para abrir o data environment do relatório.
- Arraste o campo desejado da tabela ou view para a posição desejada no designer. Um controle de relatório Field para o campo aparece na banda Page Header por padrão. Após adicionar o controle, você pode movê-lo arrastando-o para a posição desejada.
