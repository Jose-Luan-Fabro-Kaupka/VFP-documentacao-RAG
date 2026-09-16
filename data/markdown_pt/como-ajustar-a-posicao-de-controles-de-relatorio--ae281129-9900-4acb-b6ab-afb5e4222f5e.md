# Como: ajustar a posição de controles de relatório

Você pode mover ou especificar uma posição para controles de relatório no Report Designer. Você também pode especificar que controles de relatório ajustem a posição automaticamente na saída quando a parte inferior de controles de relatório posicionados acima deles expande verticalmente ou quando a banda do relatório altera a altura.

Por exemplo, a parte inferior de controles de relatório como controles Field e Picture/OLE Bound pode expandir verticalmente quando exibidos, o que afeta o posicionamento de outros controles que aparecem abaixo deles no layout. Você pode especificar que os controles afetados ajustem a posição automaticamente.

### Para ajustar manualmente a posição de um controle de relatório
- Abra o relatório ou etiqueta no designer apropriado.
- No designer, arraste o controle de relatório para a posição desejada.

### Para especificar uma posição para um controle de relatório
- Abra o relatório ou etiqueta no designer apropriado.
- No designer, clique duas vezes no controle de relatório que deseja reposicionar. A caixa de diálogo de propriedades do controle de relatório é aberta. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo do controle de relatório ou outra caixa de diálogo pode ser exibida. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER .
- Na caixa de diálogo de propriedades do controle de relatório, clique na guia General se ela não estiver selecionada.
- Nas caixas From page top e From left na área Size and position in layout, digite ou selecione os valores de posição desejados.
- Quando terminar, clique em OK .

Para obter mais informações, consulte Guia General, Caixa de diálogo Propriedades do controle de relatório (Report Builder).

### Para ajustar automaticamente a posição de um controle de relatório
- Abra o relatório ou etiqueta no designer apropriado.
- No designer, clique duas vezes no controle de relatório que deseja reposicionar automaticamente. A caixa de diálogo de propriedades do controle de relatório é aberta. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo do controle de relatório ou outra caixa de diálogo pode ser exibida. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER .
- Na caixa de diálogo de propriedades do controle de relatório, clique na guia General se ela não estiver selecionada.
- Na área Object position, escolha uma das seguintes opções: Para especificar que o controle de relatório se mova em relação à altura dos controles acima dele, clique em Float . Para especificar que o controle de relatório permaneça em posição em relação ao topo da banda, clique em Fix relative to top of band . Para especificar que o controle de relatório permaneça em posição em relação à parte inferior da banda, clique em Fix relative to bottom of band .
- Quando terminar, clique em OK .

Para obter mais informações, consulte Guia General, Caixa de diálogo Propriedades do controle de relatório (Report Builder).
