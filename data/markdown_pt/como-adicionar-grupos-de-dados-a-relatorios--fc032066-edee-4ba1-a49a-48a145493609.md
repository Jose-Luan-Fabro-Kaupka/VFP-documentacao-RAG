# Como: adicionar grupos de dados a relatórios

Você pode adicionar um ou mais grupos de dados a um relatório ou etiqueta e aninhar grupos até um máximo de 74 níveis. As bandas Group Header e Group Footer acompanham os grupos de dados automaticamente.

> **Observação:** Os registros na fonte de dados devem ser classificados e ordenados de acordo com a ordem em que você deseja que os registros apareçam em cada grupo de dados.

> **Dica:** Controles de campo usados para agrupamento na banda Detail geralmente são movidos para a banda Group Header.

### Para adicionar um grupo de dados
- Abra o relatório ou etiqueta no designer apropriado.
- No menu Report, clique em Data Grouping . A caixa de diálogo Report Properties é aberta. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo Data Grouping é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER e Caixa de diálogo Data Grouping .
- Na caixa de diálogo Report Properties, clique na guia Data Grouping se ela não estiver selecionada.
- Na guia Data Grouping, clique em Add . Uma expressão de grupo de dados aparece na lista Grouping nesting order.
- Na caixa Group on, digite a expressão desejada. Para construir uma expressão, clique no botão de reticências ( … ) para abrir o Expression Builder .
- Na área Group starts on, selecione as configurações de saída desejadas para o grupo de dados.
- Para adicionar outro grupo de dados, clique em Add e repita as etapas 4 a 5 para cada expressão de grupo de dados. Para remover um grupo de dados, clique em Remove . Dica As expressões aparecem na lista Group nesting order na ordem em que são adicionadas inicialmente. No entanto, você pode alterar a ordem das expressões de grupo. Para alterar a ordem das expressões, arraste o botão mover à esquerda da expressão que deseja mover para a posição desejada.
- Quando terminar, clique em OK . As bandas Group Header e Group Footer aparecem para cada grupo de dados e envolvem todas as bandas Detail no layout. Cada banda Group Header e Group Footer exibe o número do grupo de dados e a expressão do grupo de dados. As bandas Group Header e Group Footer com o número mais alto aparecem mais próximas da banda Detail.

Para obter mais informações, consulte Guia Data Grouping, caixa de diálogo Report Properties (Report Builder) e Caixa de diálogo Expression Builder.
