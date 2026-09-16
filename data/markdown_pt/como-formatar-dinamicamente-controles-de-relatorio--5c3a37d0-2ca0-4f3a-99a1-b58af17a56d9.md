# Como: formatar dinamicamente controles de relatório

Ao projetar um relatório, você pode especificar as propriedades de exibição dos controles de relatório. Suas especificações determinam como seus relatórios serão impressos em tempo de execução. Por exemplo, você pode especificar cor, fonte e tamanho. Você também pode alterar dinamicamente as propriedades dos controles de relatório em tempo de execução, de modo que a exibição do controle possa ser diferente dependendo se sua condição resulta em .T. ou .F. cada vez que o controle é impresso.

### Para adicionar formatação dinâmica a um controle de campo
- Clique com o botão direito em um controle de campo no Report Builder e clique em Properties .
- Clique na guia Dynamics.
- Clique em Add para abrir a Add Dynamic Style Condition Dialog Box (Report Builder) .
- Insira um nome para sua condição e clique em OK . O nome que você inserir aparece na lista de condições após criar a condição.
- Na Configure Dynamic Properties Dialog Box (Report Builder) , especifique uma condição na caixa Apply when this condition is true. A condição precisa resultar em um valor lógico .T. ou .F.. Por exemplo, orders.requiredate < DATE() ou orderdetail.quantity > 5.
- Se você deseja substituir o texto por conteúdo novo ou modificado, adicione o novo texto ou expressão na caixa Replace expression result with. Por exemplo, se seu campo está vinculado a orders.requiredate e sua expressão de condição é orders.requiredate < DATE() , você poderia substituir o valor da expressão pela expressão DTOC( orders.requiredate) + " LATE ORDER" no relatório impresso.
- Opcionalmente, defina configurações de Font para a exibição do texto no relatório. A área Sample na parte inferior da caixa de diálogo exibe a aparência do texto quando sua condição resulta em .T..
- Opcionalmente, defina configurações de Color para a exibição do texto. Você precisa desmarcar as caixas de seleção Use default foreground (pen) color e Use default background (fill) color para alterar as respectivas configurações de cor.
- Opcionalmente, defina configurações de opacidade e alfa para o texto.
- Clique em Ok para retornar à guia Dynamics. Se você tiver várias condições definidas, pode alterar a ordem em que são avaliadas arrastando-as para um novo local na lista.

### Para adicionar dimensionamento dinâmico a um objeto
- Clique com o botão direito em um objeto (por exemplo, um retângulo ou um objeto OLE) no Report Builder e clique em Properties .
- Clique na guia Dynamics.
- Clique em Add para abrir a caixa de diálogo Add Dynamic Style Condition.
- Insira um nome para sua condição e clique em Ok . O nome que você inserir aparece na lista de condições após criar a condição.
- Na caixa de diálogo Configure Dynamic Properties, especifique uma condição na caixa Apply when this condition is true. A condição precisa resultar em um valor lógico .T. ou .F. .
- Especifique a Height ou Width do controle. Insira -1, o padrão, para manter as dimensões criadas no Report Builder . Insira um valor em unidades de 1/960 de polegada para redimensionar seu controle quando sua condição resultar em .T.. Por exemplo, se você definir Width como 960 e Height como 960, seu objeto será impresso como um quadrado de 1 polegada.
- Clique em Ok para retornar à guia Dynamics. Se você tiver várias condições definidas, pode alterar a ordem em que são avaliadas arrastando-as para um novo local na lista.
