# Como: adicionar campos General a relatórios

Você pode adicionar conteúdo em campos General ao layout de página do relatório ou etiqueta. Por exemplo, você pode adicionar um documento do Microsoft Excel armazenado em um campo General a um relatório de vendas. Você pode adicionar campos General a relatórios usando o controle Picture/OLE Bound.

> **Dica:** Armazenar imagens em campos General permite exibir uma imagem diferente dependendo do registro ou de um grupo de registros. Quando você adiciona a imagem ao layout, especifique o nome do campo General que contém a imagem em vez do nome do arquivo. Para obter mais informações, consulte General Field Type e Como: adicionar imagens a relatórios.

### Para adicionar um campo General ao layout de página
- Abra o relatório ou etiqueta no designer apropriado.
- No menu Report, aponte para Insert Control e clique em Picture/OLE Bound. A caixa de diálogo Picture/OLE Bound Properties é aberta. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo Report Picture é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER e Caixa de diálogo Report Picture.
- Na caixa de diálogo Picture/OLE Bound Properties, clique na guia General se ela não estiver selecionada.
- Na área Control source na guia General, clique em General field name. Na caixa Control source, digite o nome do campo General. Dica Para procurar e selecionar um campo, clique no botão ellipsis ( … ) para abrir a caixa de diálogo Expression Builder. A caixa de diálogo Expression Builder exibe os campos disponíveis quando o ambiente de dados do relatório contém uma tabela ou exibição.
- Quando terminar na caixa de diálogo Picture/OLE Bound Properties, clique em OK. O controle de relatório Picture/OLE Bound aparece na banda Page Header por padrão. Depois de adicionar o controle, você pode movê-lo arrastando-o para a posição desejada. Dica Você pode adicionar controles Picture/OLE Bound na posição desejada selecionando-os na barra de ferramentas Report Controls e desenhando-os. Se o campo General na tabela contiver dados diferentes de um arquivo de imagem, como um documento do Microsoft Excel ou Microsoft Word, um ícone representando esses dados aparece no relatório ou etiqueta quando você gera a saída. Quando você adiciona campos General, seu conteúdo mantém o tamanho original por padrão. Para obter mais informações, consulte Como: redimensionar controles de relatório.

Para obter mais informações, consulte Guia General, Caixa de diálogo Report Control Properties (Report Builder).
