# Como: adicionar bandas a relatórios

Você pode adicionar bandas aos seus relatórios e etiquetas para especificar áreas adicionais e quando exibir determinados dados na página do relatório ou etiqueta. Você pode adicionar as seguintes bandas a relatórios e etiquetas:
 - Banda Title.
- Banda Summary.
- Bandas Detail.
- Banda Page Header, banda Page Footer ou ambas, para uma banda Summary.
- Bandas Detail Header e Detail Footer para uma banda Detail.

Para obter mais informações, consulte Report Bands.

### Para adicionar uma banda Title, Summary ou Detail
- Abra o relatório ou etiqueta para edição no designer apropriado.
- No menu Report, clique em Optional Bands . A caixa de diálogo Report Properties é aberta. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão, a caixa de diálogo Optional Bands é aberta em vez disso. Se _REPORTBUILDER estiver definida para um builder de terceiros, uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte _REPORTBUILDER System Variable e Optional Bands Dialog Box .
- Na caixa de diálogo Report Properties, clique na guia Optional Bands.
- Para selecionar as bandas que deseja adicionar, execute o seguinte: Para adicionar uma banda Title, na área Title, clique em Report has title band. Dica Para especificar que o conteúdo da banda Title seja exibido em uma página separada, clique em New page after title has printed. Para adicionar uma banda Summary, na área Summary, clique em Report has summary band . Dica Para especificar que o conteúdo da banda Summary seja exibido em uma página separada, clique em Summary prints as new page . Para adicionar uma banda Page Header ou Page Footer para a banda Summary, clique em Include page header with summary ou Include page footer with summary , ou ambos. Para adicionar bandas Detail, na área Detail bands, clique em Add para cada banda Detail que deseja adicionar. Cada banda Detail que você adiciona é numerada na ordem em que você as adiciona, da menor para a maior.
- Quando terminar, clique em OK .

Para obter mais informações, consulte Optional Bands Tab, Report Properties Dialog Box (Report Builder).

### Para adicionar bandas Detail Header e Detail Footer para uma banda Detail
- No designer apropriado, adicione uma banda Detail ao layout da página.
- No menu Report, clique em Edit Bands .
- Na caixa de diálogo Edit Bands, selecione a banda Detail desejada e clique em OK . A caixa de diálogo Detail Band Properties é aberta. Dica Você também pode clicar duas vezes no separador da banda Detail para abrir a caixa de diálogo de propriedades da banda Detail. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo Detail é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte _REPORTBUILDER System Variable .
- Na caixa de diálogo Detail Band Properties, clique na guia Band.
- Na área Detail properties, clique em Associated header and footer bands , e depois OK .

Para obter mais informações, consulte Band Tab, Report Band Properties Dialog Box (Report Builder).
