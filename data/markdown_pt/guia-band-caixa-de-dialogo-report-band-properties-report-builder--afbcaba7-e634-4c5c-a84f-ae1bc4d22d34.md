# Guia Band, Caixa de diálogo Report Band Properties (Report Builder)

Permite definir opções para uma banda Detail no Report Designer ou Label Designer.

> **Observação:** Esta guia substitui a funcionalidade da caixa de diálogo nativa Report Band Properties do Visual FoxPro quando o Report Builder está ativo.
 - Como: configurar saída para bandas de relatório
- Como: especificar aliases de destino para bandas Detail

# Propriedades Detail

Especifica opções para a banda Detail ou conjunto de bandas Detail. Um conjunto de bandas Detail inclui suas bandas de cabeçalho e rodapé associadas, se tiverem sido especificadas.

> **Importante:** As opções listadas acima de Target alias expression no grupo a seguir não se aplicam a menos que você especifique pelo menos uma das condições de banda de detalhe novas no Visual FoxPro 9: o conjunto de bandas deve incluir um cabeçalho e um rodapé, ou deve ter um alias de destino atribuído, ou deve haver mais de uma banda de detalhe no relatório. Se nenhuma dessas condições existir, o relatório é executado no modo de compatibilidade com versões anteriores e essas opções, que em versões anteriores se aplicavam somente a bandas de grupo, não são avaliadas para a banda de detalhe do relatório.
 **Start on new column**
Inicia uma nova coluna quando o conjunto de bandas Detail mudar. Selecionar esta caixa de seleção permite criar bandas Detail lado a lado. Disponível somente quando o layout da página contém mais de uma coluna. Observação As quebras de coluna ocorrem antes da banda Detail Header, se existir alguma.
**Start on new page**
Inicia uma nova página quando o conjunto de bandas Detail mudar. Observação As quebras de página ocorrem antes da banda Detail Header, se existir alguma.
**Reset page number to 1 for each detail set**
Inicia uma nova página e reinicia a numeração de páginas sempre que o conjunto de bandas de detalhe mudar.
**Associated header and footer bands**
Especifica que existem bandas Detail Header e Detail Footer separadas para a banda de detalhe, formando um conjunto de bandas de detalhe.
**Reprint detail header on each page**
Especifica que o Detail Header segue o cabeçalho da página em todas as páginas da banda Detail quando a banda Detail abrange mais de uma página.
**Start detail set on new page when less than**
Define a distância mínima da parte inferior da página que deve estar disponível para impedir que um conjunto de bandas Detail seja forçado a ser renderizado em uma nova página.
**Target alias expression**
Especifica uma expressão de alias de destino para a banda Detail. Para construir uma expressão, clique no botão ellipsis (...) para abrir o Expression Builder. Para obter mais informações, consulte Expression Builder Dialog Box. Observação Lembre-se de colocar entre aspas ("") um nome de tabela simples ou alias de cursor para garantir que a expressão seja avaliada corretamente. Valores sem aspas serão interpretados como uma variável ou campo contendo o valor do alias. Consulte Como: especificar aliases de destino para bandas Detail e Working with Related Tables using Multiple Detail Bands in Reports para obter mais informações.
