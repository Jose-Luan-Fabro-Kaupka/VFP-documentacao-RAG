# Caixa de diálogo Configure Dynamic Properties (Report Builder)

Permite especificar configurações de fonte, estilo e tamanho que você pode aplicar em tempo de execução para controles de relatório. As opções nesta caixa de diálogo são diferentes se você estiver trabalhando com um campo ou com um objeto como bitmap, linha ou retângulo.

Você pode abrir esta caixa de diálogo selecionando uma condição e clicando em Edit na guia Dynamics da caixa de diálogo Report Control Properties.

How to: Dynamically Format Report Controls

# Opções de campo e objeto

Você pode usar as seguintes opções ao trabalhar com controles de campo ou objeto.
 **Condition Name**
Identifica a condição para a qual você está definindo propriedades dinâmicas. Condition Name é somente leitura.
**Apply when this condition is true**
Especifica a expressão lógica que determina se o controle aparece em tempo de execução com suas opções de formatação dinâmica. Clique no botão de reticências (...) para abrir a caixa de diálogo Expression Builder Dialog Box

# Opções de controle de campo

Você pode usar as seguintes opções somente se estiver trabalhando com um controle de campo.
 **Replace expression result with**
Permite especificar uma expressão ou função definida pelo usuário para aparecer no lugar do valor do campo em tempo de execução. Clique no botão de reticências (...) para abrir a caixa de diálogo Expression Builder. Você pode usar Replace expression result with para fornecer mais opções de exibição. Por exemplo, UPPER(table.field) ou table.field + ": IMPORTANT" .
**Font**
Exibe o nome da fonte, o tamanho da fonte e o estilo da fonte que serão aplicados ao seu controle quando a expressão de condição for avaliada como .T.. Clique no botão de reticências para abrir a caixa de diálogo Font Dialog Box se quiser especificar uma fonte diferente.
**Use font script**
Indica se você selecionou um script na caixa de diálogo Font. Use font script é somente leitura.
**Strikethrough**
Especifica se o texto aparecerá com uma linha horizontal através dele quando a expressão de condição for avaliada como .T..
**Underline**
Especifica se o texto será sublinhado quando a expressão de condição for avaliada como .T..
**Use default foreground (pen) color**
Indica se o controle aparece na cor padrão da caneta quando a expressão de condição for avaliada como .T.. Quando você desmarca esta caixa de seleção, pode clicar no botão de reticências (…) para abrir a caixa de diálogo Color Picker.
**Use default background (fill) color**
Indica se o controle aparece com a cor de preenchimento padrão quando a expressão de condição for avaliada como .T.. Quando você desmarca esta caixa de seleção, pode clicar no botão de reticências para abrir a caixa de diálogo Color Picker.
**Backstyle - Opaque**
Especifica que objetos que aparecem atrás do controle de relatório não são visíveis.
**Backstyle - Transparent**
Especifica que objetos que aparecem atrás do controle de relatório são visíveis.
**Alpha - Pen**
Especifica o quão transparente é o texto. Uma configuração de 255 indica que o texto é completamente opaco. Uma configuração de 0 indica que o texto é completamente transparente.
**Alpha - Fill**
Especifica o quão transparente é a área de preenchimento atrás do texto. Uma configuração de 255 indica que o preenchimento é completamente opaco. Uma configuração de 0 indica que o preenchimento é completamente transparente.
**Sample**
Exibe a aparência do texto

# Opções de controle de objeto

Você pode usar as seguintes opções somente se estiver trabalhando com propriedades de objeto.
 **Width expression**
Especifica a largura do objeto quando a expressão de condição for avaliada como .T.. O padrão de -1 indica que o objeto será impresso na largura especificada no Report Builder . As expressões Width e Height devem ser avaliadas como valores em unidades de 1/960 de polegada.
**Height expression**
Especifica a altura do objeto quando a expressão de condição for avaliada como .T.. O padrão de -1 indica que o objeto será impresso na altura especificada no Report Builder .
