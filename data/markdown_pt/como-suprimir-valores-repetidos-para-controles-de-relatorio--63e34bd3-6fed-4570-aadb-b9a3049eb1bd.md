# Como: suprimir valores repetidos para controles de relatório

Você pode suprimir a exibição de valores repetidos em registros consecutivos para que o valor apareça uma vez para o primeiro registro, mas não para registros subsequentes até que o valor seja alterado. Você também pode suprimir a exibição repetida de controles de relatório.

Por exemplo, suponha que você tenha uma fatura com campos de tabela subjacentes que contêm a data da transação. Você pode especificar que a data apareça apenas uma vez para transações que ocorreram na mesma data.

Você também pode escolher repetir valores somente quando uma nova página ou coluna começa, quando o grupo de dados é alterado ou quando uma banda Detail continua com a próxima página ou coluna.

### Para suprimir valores ou controles de relatório repetidos
- Abra o relatório ou etiqueta no designer apropriado.
- No designer, clique duas vezes no controle de relatório desejado. A caixa de diálogo de propriedades do controle de relatório é aberta. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um construtor de terceiros, a caixa de diálogo do controle de relatório é exibida ou uma caixa de diálogo diferente pode ser exibida. Na caixa de diálogo do controle de relatório, clique em Imprimir Quando para abrir a caixa de diálogo Imprimir Quando. Para obter mais informações, consulte Variável de Sistema _REPORTBUILDER e Caixa de Diálogo Imprimir Quando .
- Na caixa de diálogo de propriedades do controle de relatório, clique na guia Imprimir quando se ela não estiver selecionada.
- Na área Imprimir valores repetidos, clique em Não , e depois OK .

Para obter mais informações, consulte Guia Imprimir Quando, Caixa de Diálogo Propriedades do Controle de Relatório (Report Builder).

### Para repetir valores ou controles de relatório sob condições específicas
- Abra o relatório ou etiqueta no designer apropriado.
- No designer, clique duas vezes no controle de relatório desejado. A caixa de diálogo de propriedades do controle de relatório é aberta. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um construtor de terceiros, a caixa de diálogo do controle de relatório é exibida ou uma caixa de diálogo diferente pode ser exibida. Na caixa de diálogo do controle de relatório, clique em Imprimir Quando para abrir a caixa de diálogo Imprimir Quando. Para obter mais informações, consulte Variável de Sistema _REPORTBUILDER e Caixa de Diálogo Imprimir Quando .
- Na caixa de diálogo de propriedades do controle de relatório, clique na guia Imprimir quando se ela não estiver selecionada.
- Na área Imprimir valores repetidos na guia Imprimir quando, clique em Não .
- Na área Também imprimir, escolha uma das seguintes opções: Para repetir valores ou o controle de relatório somente para uma nova página ou coluna, clique Na primeira banda inteira da nova página/coluna . Para repetir valores ou o controle de relatório somente quando o grupo de dados é alterado, clique Quando esta expressão de grupo de dados é alterada . Selecione o grupo de dados apropriado na lista suspensa. Para repetir valores ou o controle de relatório somente quando a banda continua com a próxima página ou coluna, clique Quando o conteúdo da banda transborda para nova página/coluna e Na primeira banda inteira da nova página/coluna .
- Quando terminar, clique em OK .

Para obter mais informações, consulte Guia Imprimir Quando, Caixa de Diálogo Propriedades do Controle de Relatório (Report Builder).
