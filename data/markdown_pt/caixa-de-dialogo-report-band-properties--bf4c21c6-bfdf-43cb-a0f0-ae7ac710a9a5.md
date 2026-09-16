# Caixa de diálogo Report Band Properties

Permite definir propriedades e opções para uma banda em um layout de página de relatório ou etiqueta.

Esta caixa de diálogo aparece quando você escolhe Properties no menu de contexto de um separador de banda de relatório; quando você clica duas vezes em um separador de banda de relatório; ou quando você clica duas vezes no nome da banda na caixa de diálogo Edit Bands.

> **Observação:** Dependendo da configuração da variável de sistema _REPORTBUILDER, esta caixa de diálogo pode ser substituída por uma interface de usuário alternativa. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER.

# Opções de layout de banda de relatório
 **Height**
Especifica a altura da banda. A altura da banda de relatório determina a quantidade de espaço que cada banda de relatório usa na página dentro das margens da página. Ao selecionar um valor de altura clicando nas setas Height, os valores mudam em incrementos de 0,05 na unidade de medida definida para a régua/grade. Para obter mais informações, consulte Como: configurar a grade de layout de página para relatórios. Por exemplo, se a banda Title estiver definida em meia polegada, as informações na banda Title aparecem na primeira meia polegada da página após a margem superior. Dica Ao adicionar itens a uma banda de relatório, talvez seja necessário alterar a altura da banda de relatório para acomodar seu conteúdo. Como guia para determinar a altura, use a régua à esquerda da banda. A medida da régua é específica para a altura da banda e não inclui as margens da página. Observação Ao reduzir a altura de uma banda, você não pode tornar uma banda mais curta que a altura dos controles no layout. Se controles na banda impedirem o redimensionamento da banda, mova os controles na banda e depois reduza a altura.
**Constant band height**
Impede que a banda se estenda para acomodar dados longos ou se ajuste a linhas em branco que foram removidas.

# Run expression

Especifica expressões a serem avaliadas ao processar a banda de relatório.
 **On entry**
Especifica uma expressão a ser avaliada antes de processar a banda. Para construir uma expressão, clique no botão de reticências ( … ) para abrir o Expression Builder. Para obter mais informações, consulte Caixa de diálogo Expression Builder.
**On exit**
Especifica uma expressão a ser avaliada após processar a banda. Para construir uma expressão, clique no botão de reticências ( … ) para abrir o Expression Builder. Para obter mais informações, consulte Caixa de diálogo Expression Builder.

# Detail Band Properties

Especifica opções para a banda Detail ou conjunto de bandas Detail. Um conjunto de bandas Detail inclui suas bandas de cabeçalho e rodapé associadas, se foram especificadas.

> **Importante:** As opções listadas acima de Target alias no grupo a seguir não se aplicam a menos que você especifique pelo menos uma das condições de banda de detalhe novas no Visual FoxPro 9: o conjunto de bandas deve incluir um cabeçalho e rodapé, ou deve ter um alias de destino atribuído, ou deve haver mais de uma banda de detalhe no relatório. Se nenhuma dessas condições existir, o relatório é executado em modo de compatibilidade com versões anteriores e essas opções, que em versões anteriores se aplicavam apenas a bandas de grupo, não são avaliadas para a banda de detalhe do relatório.
 **Start on a new column**
Inicia uma nova coluna quando o conjunto de bandas Detail mudar. Selecionar esta caixa de seleção permite criar bandas Detail lado a lado. Disponível somente quando o layout de página contém mais de uma coluna. Observação Quebras de coluna ocorrem antes da banda Detail Header, se existir.
**Start on a new page**
Inicia uma nova página quando o conjunto de bandas Detail mudar. Observação Quebras de página ocorrem antes da banda Detail Header, se existir.
**Reset page number to 1 for each detail set**
Inicia uma nova página e reinicia a numeração de páginas sempre que o conjunto de bandas de detalhe mudar.
**Detail Header/Footer**
Especifica que bandas Detail Header e Detail Footer separadas existem para a banda de detalhe, formando um conjunto de bandas de detalhe.
**Reprint detail header on each page**
Especifica que o Detail Header segue o Page Header em todas as páginas da banda Detail quando a banda Detail se estende por mais de uma página.
**Start detail set on new page when less than**
Define a distância mínima da parte inferior da página que deve estar disponível para impedir que um conjunto de bandas de detalhe seja forçado a ser renderizado em uma nova página.
**Target alias**
Especifica uma expressão de alias de destino para a banda Detail. Para construir uma expressão, clique no botão de reticências ( … ) para abrir o Expression Builder. Para obter mais informações, consulte Caixa de diálogo Expression Builder. Observação Lembre-se de colocar um nome de tabela simples ou alias de cursor entre aspas ( "" ) para garantir que a expressão seja avaliada corretamente. Valores sem aspas serão interpretados como uma variável ou campo contendo o valor do alias. Consulte Como: especificar aliases de destino para bandas de detalhe e Trabalhando com tabelas relacionadas usando múltiplas bandas de detalhe em relatórios para obter mais informações.
