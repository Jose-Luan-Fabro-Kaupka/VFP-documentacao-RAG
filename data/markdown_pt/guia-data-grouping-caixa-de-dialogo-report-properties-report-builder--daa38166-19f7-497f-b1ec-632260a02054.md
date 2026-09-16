# Guia Data Grouping, caixa de diálogo Report Properties (Report Builder)

Permite especificar regiões aninhadas do layout que são renderizadas somente quando uma expressão altera seu valor.

Esta guia é pré-selecionada quando você escolhe Data Grouping no menu Report ou no menu de contexto do layout de relatório.

Esta guia também aparece na caixa de diálogo Properties das bandas Detail.

> **Observação:** Esta guia substitui a funcionalidade da caixa de diálogo nativa Visual FoxPro Data Grouping Dialog Box quando o Report Builder está ativo.
 - How to: Add Data Groups to Reports
- How to: Edit Data Groups in Reports
- How to: Configure Output for Data Groups
- How to: Delete Data Groups in Reports
 **Group nesting order**
Lista as expressões que determinam quebras entre grupos de dados. O botão de movimentação permite alterar a ordem de aninhamento das expressões de grupo.
**Add**
Adiciona uma nova expressão de grupo de dados à lista Group nesting order.
**Remove**
Exclui a expressão de grupo de dados selecionada da lista Group nesting order.
**Group on**
Exibe a expressão de grupo de dados selecionada na lista Group nesting order. Expressões vazias não são válidas. Você pode digitar ou construir uma expressão clicando no botão de reticências (…). Para obter mais informações, consulte Expression Builder Dialog Box .

# Group starts on

Especifica onde as informações das bandas agrupadas serão renderizadas quando o valor da expressão de grupo mudar.
 **New line**
Especifica que o grupo começará imediatamente na próxima linha da saída.
**New column**
Especifica que a alteração da expressão de grupo forçará as informações a serem renderizadas como uma nova coluna. Disponível somente quando o layout de página contém mais de uma coluna.
**New page**
Especifica que a alteração da expressão de grupo forçará as informações a serem renderizadas como uma nova página.
**New page number 1**
Inicia uma nova página e reinicia a numeração de páginas sempre que o valor da expressão de grupo de dados mudar.

# Reprint group header on each page

Especifica que o cabeçalho de grupo segue o cabeçalho de página em todas as páginas do grupo de dados quando o grupo de dados abrange mais de uma página.

# Start group on new page when less than

Especifica a distância mínima da parte inferior da página que determina quando iniciar o cabeçalho de grupo na próxima página.

> **Dica:** Use esta opção para evitar um cabeçalho de grupo "órfão" e dados potencialmente inadequados no final de uma página sem informações de detalhe correspondentes. Um cabeçalho de grupo órfão pode exibir dados de um registro não mostrado em outro lugar na página, já que o rodapé de página exibirá informações apropriadas ao grupo anterior.
