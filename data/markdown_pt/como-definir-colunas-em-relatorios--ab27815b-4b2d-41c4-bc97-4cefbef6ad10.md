# Como: definir colunas em relatórios

Você pode definir várias colunas para o layout da página do relatório ou etiqueta. Várias colunas dividem um layout de página em seções verticais. O Report Designer e o Label Designer exibem uma coluna, permitindo que você coloque controles de relatório apenas em uma parte do layout da página. Em tempo de execução, o Report Engine repete o layout de coluna duas ou mais vezes para preencher a página.

> **Observação:** Se você aumentar o número de colunas no layout da página após organizar controles de relatório no layout, pode precisar mover ou redimensionar os controles para caber nos novos limites da coluna.

As colunas têm um par associado de bandas header e footer, que estão aninhadas dentro das bandas page header e page footer do relatório. As bandas column header aparecem acima de quaisquer bandas group header, e as bandas column footer aparecem abaixo de quaisquer bandas group footer, no layout do Report Designer. O comportamento dessas bandas e as opções que você pode definir para elas são semelhantes às disponíveis para bandas group header e footer. Para obter mais informações, consulte How to: Add Bands to Reports.

No entanto, a adição de várias colunas a um layout de relatório pode ter impacto no comportamento das bandas column, group e detail header e footer no relatório. Este impacto depende de como você define Column print order, conforme descrito nos procedimentos abaixo.

### Para definir colunas para um layout de página de relatório ou etiqueta
- Abra o relatório ou etiqueta no designer apropriado.
- No menu Report, clique em Properties . A caixa de diálogo Report Properties é aberta. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão, a caixa de diálogo Report Page Setup é aberta em vez disso. Se _REPORTBUILDER estiver definida para um builder de terceiros, uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte _REPORTBUILDER System Variable e Report Page Setup Dialog Box .
- Na caixa de diálogo Report Properties, clique na guia Page Setup.
- Na caixa Number, digite ou selecione o número de colunas que deseja que apareçam na página.
- Na caixa Width, digite ou selecione um valor para a largura da coluna.
- Na caixa Spacing, digite um valor para a quantidade de espaço que deseja entre cada coluna. Observação A caixa Spacing está disponível apenas ao especificar mais de uma coluna na caixa Number. Use o grupo de opções Column print order para determinar a ordem de impressão apropriada para os dados neste relatório ou etiqueta. Por padrão, o Report Designer seleciona o botão de opção Top to bottom. Nesta ordem de impressão, o Report Engine imprime registros consecutivamente em uma única coluna até atingir o final da altura disponível para a banda detail na página atual. Se você selecionar o botão de opção Left to right, o Report Engine imprime registros nas várias colunas, antes de continuar a imprimir um registro adicional na primeira coluna. Esta ordem de impressão é o padrão para o Label Designer e é frequentemente chamada de estilo de etiqueta . Observação No Visual FoxPro 9.0, definir a ordem de impressão no estilo de etiqueta tem algum impacto adicional em relatórios. Quando você usa esta opção para fazer as colunas fluir da esquerda para a direita, as bandas group e detail header e footer se estendem pela página, para que possam fornecer informações de cabeçalho verdadeiras para toda a linha. A banda detail começa uma linha abaixo de quaisquer bandas header que você projetar no layout. Em versões anteriores, Column print order não alterava o comportamento das bandas group header e footer, então o primeiro item detail era impresso adjacente ao group header mais interno na mesma linha.
- Clique em OK .

Para obter mais informações, consulte Page Layout Tab, Report Properties Dialog Box (Report Builder).
