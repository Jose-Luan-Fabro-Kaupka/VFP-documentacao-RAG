# Como: configurar saída para bandas de relatório

Você pode configurar a saída para bandas de relatório das seguintes maneiras:
 - Controlar se as bandas de relatório mantêm uma altura constante ou se ajustam para dados extensos e linhas em branco suprimidas.
- Especificar que a saída das bandas Title e Summary seja exibida em páginas individuais.
- Especificar que a saída das bandas Detail comece com uma nova coluna ou página.
- Reiniciar o número da página para 1 para cada conjunto de detalhes.
- Repetir a saída do Detail Header em cada página.
- Especificar uma distância mínima da parte inferior da página que determina quando iniciar conjuntos de detalhes na próxima página.

### Para impedir que bandas de relatório ajustem seu tamanho para ajustar-se a dados extensos ou linhas em branco suprimidas
- Abra o relatório ou etiqueta no designer apropriado.
- No menu Relatório, clique em Edit Bands . A caixa de diálogo Edit Bands é aberta.
- Na caixa de diálogo Edit Bands, selecione a banda desejada e clique em OK . A caixa de diálogo de propriedades da banda de relatório é aberta. Dica Você também pode clicar duas vezes no separador da banda no Report Designer ou Label Designer para abrir a caixa de diálogo de propriedades da banda de relatório. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo da banda de relatório é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER e Caixa de diálogo Propriedades da banda de relatório .
- Na caixa de diálogo de propriedades da banda de relatório, clique na guia General se ela não estiver selecionada.
- Clique em Constant band height e então OK .

Para obter mais informações, consulte Guia General, Caixa de diálogo Propriedades da banda de relatório (Report Builder).

### Para exibir a saída da banda Title ou Summary em páginas individuais
- Abra o relatório ou etiqueta no designer apropriado.
- No menu Relatório, clique em Optional Bands . A caixa de diálogo Propriedades do relatório é aberta. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão, a caixa de diálogo Optional Bands é aberta em vez disso. Se _REPORTBUILDER estiver definida para um builder de terceiros, uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte Caixa de diálogo Optional Bands .
- Na caixa de diálogo Propriedades do relatório, clique na guia Optional Bands.
- Execute o seguinte: Para especificar que a saída da banda Title apareça em uma página separada, na área Title, clique em New page after title has printed . Para especificar que a saída da banda Summary apareça em uma página separada, na área Summary, clique em Summary prints as new page .
- Quando terminar, clique em OK .

Para obter mais informações, consulte Guia Optional Bands, Caixa de diálogo Propriedades do relatório (Report Builder).

### Para configurar saída para bandas Detail
- Abra o relatório ou etiqueta no designer apropriado.
- No menu Relatório, clique em Edit Bands .
- Na caixa de diálogo Edit Bands, clique na banda Detail desejada e então OK . A caixa de diálogo Propriedades da banda Detail é aberta. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo Detail é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER e Caixa de diálogo Propriedades da banda de relatório .
- Na caixa de diálogo Propriedades da banda Detail, clique na guia Band.
- Na área Detail properties, selecione as configurações de saída desejadas.
- Quando terminar, clique em OK .

Para obter mais informações, consulte Guia Band, Caixa de diálogo Propriedades da banda de relatório (Report Builder).
