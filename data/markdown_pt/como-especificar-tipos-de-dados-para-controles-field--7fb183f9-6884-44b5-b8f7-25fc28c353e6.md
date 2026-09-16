# Como: especificar tipos de dados para controles Field

Você pode especificar o tipo de dados para a saída gerada por controles Field em relatórios ou etiquetas. O tipo de dados que você escolhe determina as opções de formato disponíveis para a saída gerada pelo controle Field; no entanto, sua seleção não altera o tipo de dados do campo na tabela de origem.

Você pode especificar a formatação para a saída de um controle Field dependendo do tipo de dados da saída construindo uma expressão de formato. Por exemplo, você pode especificar formatação em maiúsculas para saída de caractere, inserir vírgulas ou pontos decimais em saída numérica, exibir saída numérica em formato de moeda ou converter um formato de data em outro. Para obter mais informações, consulte Format Expressions for Field Controls.

### Para especificar o tipo de dados e suas configurações de formato em um controle Field
- Abra o relatório ou a etiqueta no designer apropriado.
- No designer, clique duas vezes no controle Field desejado. A caixa de diálogo Field Properties é aberta. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo Report Expression é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte _REPORTBUILDER System Variable , Report Expression Dialog Box , e Format (Field) Dialog Box .
- Na caixa de diálogo Field Properties, clique na guia Format se ela não estiver selecionada.
- Na caixa Format expression, digite a expressão de formato desejada, que pode incluir códigos de formato e caracteres de modelo.
- Na guia Format, clique no tipo de dados desejado para o controle Field.
- Na área Format options, selecione os códigos de formato desejados dentre os disponíveis para o tipo de dados selecionado. Dica Ao usar uma combinação de códigos de formato e caracteres de modelo de formato, preceda a lista de caracteres de modelo de formato com a lista de códigos de formato.
- Quando terminar, clique em OK .

Para obter mais informações, consulte Format Tab, Report Control Properties Dialog Box (Report Builder).
