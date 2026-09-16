# Como: especificar expressões em controles Field

Você pode exibir os resultados de expressões em relatórios e etiquetas especificando expressões em controles Field. Por exemplo, você pode incluir expressões e funções comumente usadas para exibir valores como os seguintes:
 - Exibição da data atual
- Exibição de números de página

Depois de adicionar controles Field com expressões que contêm campos à página, eles podem não ser exibidos da forma desejada devido a espaçamento indesejado. Para remover espaçamento indesejado, você pode aparar e concatenar expressões que contêm campos em uma única expressão. Para obter mais informações, consulte Aparar e concatenar expressões.

# Exibição da data atual

Você pode exibir a data atual na página usando um controle Field.

### Para exibir a data atual na página
- Abra o relatório ou etiqueta no designer apropriado.
- No designer, adicione um controle Field ao layout de página. A caixa de diálogo Field Properties é aberta. Dica Você também pode clicar duas vezes no controle de relatório no Report Designer ou Label Designer para abrir a caixa de diálogo de propriedades do controle de relatório. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo Report Expression é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER e Caixa de diálogo Report Expression.
- Na caixa de diálogo Field Properties, clique na guia General se ela não estiver selecionada.
- Na caixa Expression na guia General, digite DATE() e clique em OK.

Para obter mais informações, consulte Função DATE( ) e Guia General, caixa de diálogo Report Control Properties (Report Builder).

Você pode visualizar a data visualizando o relatório. Para obter mais informações, consulte Como: visualizar relatórios.

# Exibição de números de página

A banda Page Header ou Page Footer normalmente contém um número de página. Você pode exibir números de página usando um controle Field.

> **Observação:** Se você usar um assistente ou a funcionalidade Quick Report, um número de página é inserido automaticamente na banda Page Footer.

### Para exibir números de página na página
- Abra o relatório ou etiqueta no designer apropriado.
- No designer, adicione um controle Field ao layout de página. A caixa de diálogo Field Properties é aberta. Dica Você também pode clicar duas vezes no controle de relatório no Report Designer ou Label Designer para abrir a caixa de diálogo de propriedades do controle de relatório. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo Report Expression é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER e Caixa de diálogo Report Expression.
- Na caixa de diálogo Field Properties, clique na guia General se ela não estiver selecionada.
- Na caixa Expression na guia General, digite _pageno e clique em OK.

Para obter mais informações, consulte Variável de sistema _PAGENO.

Você pode visualizar os números de página visualizando o relatório. Para obter mais informações, consulte Como: visualizar relatórios.
