# Como: redimensionar controles de relatório

Você pode redimensionar qualquer controle de relatório, exceto controles Label. Você pode redimensionar cada controle de relatório manualmente ou alterar suas dimensões para corresponder ao tamanho de outro controle de relatório selecionado.

Para redimensionar arquivos de imagem e campos General em relatórios, primeiro defina-os para escalar. Para obter mais informações, consulte Redimensionando controles Picture/OLE vinculados mais adiante neste tópico.

Você também pode especificar que o controle de relatório expanda e contrai, ou estique, dependendo de seu conteúdo. Para obter mais informações, consulte Como: definir estiramento de controles de relatório.

> **Observação:** O tamanho de um controle Label depende do comprimento, estilo de fonte e tamanho de fonte do conteúdo no controle.

### Para redimensionar um controle de relatório manualmente
- Abra o relatório ou etiqueta no designer apropriado.
- No designer, selecione o controle. Alças de seleção aparecem nas bordas do controle.
- Arraste uma alça de seleção para aumentar ou diminuir o tamanho do controle. Dica Para dimensionamento mais preciso, você pode pressionar e manter a tecla SHIFT pressionada enquanto pressiona as teclas de seta para alterar o tamanho de um controle selecionado.

### Para especificar um tamanho para um controle de relatório
- Abra o relatório ou etiqueta no designer apropriado.
- No designer, clique duas vezes no controle de relatório que deseja redimensionar. A caixa de diálogo de propriedades do controle de relatório é aberta. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um construtor de terceiros, a caixa de diálogo do controle de relatório é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER .
- Na caixa de diálogo de propriedades do controle de relatório, clique na guia General se ela não estiver selecionada.
- Nas caixas Height e Width na área Size and position in layout, digite ou selecione a altura e a largura desejadas.
- Quando terminar, clique em OK .

Para obter mais informações, consulte Guia General, Caixa de diálogo Propriedades do controle de relatório (Report Builder).

### Para corresponder ao tamanho de outro controle de relatório
- Abra o relatório ou etiqueta no designer apropriado.
- No designer, selecione os controles de relatório desejados usando o método de seleção múltipla. Observação Se você agrupar controles de relatório usando o comando Group no menu Format, somente a opção de dimensionamento To Grid está disponível. Para obter mais informações, consulte Como: agrupar controles de relatório .
- No menu Format, selecione Size e escolha a opção apropriada no submenu: To Grid To Tallest To Shortest To Widest To Narrowest Os controles selecionados são redimensionados de acordo com a opção selecionada.

Por exemplo, selecionar To Tallest como opção de dimensionamento redimensiona todos os controles selecionados para o controle mais alto.

# Redimensionando controles Picture/OLE vinculados

Arquivos de imagem e campos General adicionados ao layout da página do relatório mantêm seu tamanho original por padrão. Quando adicionados ao layout, um arquivo de imagem ou o conteúdo do campo General pode não caber no quadro que contém a imagem ou o campo General. Se a imagem ou o campo General for maior que o quadro, somente uma parte da imagem ou do conteúdo do campo General aparece visível no canto superior esquerdo do quadro. A porção inferior direita restante se estende além do quadro e da visualização.

No entanto, você pode redimensionar arquivos de imagem e ajustar o conteúdo de campos General para caber em seus quadros.

### Para redimensionar um arquivo de imagem ou ajustar um campo General para caber em seu quadro
- Abra o relatório ou etiqueta no designer apropriado.
- No designer, clique duas vezes no controle Picture/OLE Bound que deseja redimensionar, ou clique com o botão direito nele e selecione Properties no menu de contexto. A caixa de diálogo Picture/OLE Bound Properties é aberta. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um construtor de terceiros, a caixa de diálogo Report Picture é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER e Caixa de diálogo Report Picture .
- Na caixa de diálogo Picture/OLE Bound Properties, clique na guia General se ela não estiver selecionada.
- Na guia General, escolha uma das seguintes opções na lista suspensa If source and frame are different sizes: Para preencher o quadro com a imagem ou o conteúdo do campo General, mas manter suas proporções relativas, clique em Scale contents, retain shape . Para preencher o quadro com a imagem ou o conteúdo do campo General e esticá-lo verticalmente ou horizontalmente conforme necessário, clique em Scale contents, fill the frame . Observação Escolher Scale contents, fill the frame pode distorcer as proporções da imagem ou do campo General.
- Quando terminar, clique em OK .

Para obter mais informações, consulte Guia General, Caixa de diálogo Propriedades do controle de relatório (Report Builder).
