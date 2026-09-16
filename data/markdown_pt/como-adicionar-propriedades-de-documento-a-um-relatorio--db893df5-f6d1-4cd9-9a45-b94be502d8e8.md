# Como: adicionar propriedades de documento a um relatório

As propriedades de documento de relatório permitem incluir informações adicionais no relatório. As propriedades de documento são incluídas como elementos e atributos na saída XML e HTML. Você pode usar métodos e eventos do objeto ReportListener para acessar essas propriedades. Além disso, você pode acessá-las durante o pós-processamento dos arquivos de saída.

Para obter informações sobre como criar relatórios que geram dados XML ou HTML, consulte ReportListener Foundation Classes.
 **Document Properties in XML Files**
O relatório XML inclui propriedades de documento, como elementos filho <property> do elemento <Run> do relatório. Por exemplo, se você definir o valor da propriedade Document.Title como "Inventory Report" e o valor da propriedade Document.Author como "Alfreds Futterkiste", seu arquivo de saída XML contém as seguintes tags. <Run> <property id="Document.Title">Inventory Report</property> <property id="Document.Author"> Alfreds Futterkiste </property> </Run>
**Document Properties in HTML Files**
O arquivo HTML inclui propriedades de documento, como valores de tags HTML nativas se houver uma tag HTML correspondente para a propriedade. Se não houver um elemento HTML correspondente para a propriedade, as tags <meta> na seção <head> do arquivo HTML incluem o valor da propriedade. Por exemplo, se você definir o valor da propriedade Document.Title como "Inventory Report" e o valor da propriedade Document.Author como "Alfreds Futterkiste", seu arquivo de saída HTML contém as seguintes tags. <head> <title> Inventory Report </title> <meta name="author" content="Alfreds Futterkiste"> </head>

### Para editar propriedades padrão de um relatório
- No menu Report, clique em Properties .
- Na caixa de diálogo Report Properties, clique na guia Document Properties.
- Na lista de propriedades de documento, clique na propriedade que deseja editar.
- Clique no botão Edit para abrir a caixa de diálogo Expression Builder Dialog Box .
- Digite a expressão que deseja avaliar em tempo de execução e clique em OK . Isso armazenará um valor na propriedade selecionada. A expressão pode ser qualquer expressão Visual FoxPro ou um comando Visual FoxPro (por exemplo, DATETIME() ). Para uma descrição das propriedades padrão, consulte Document Properties Tab, Report Properties Dialog Box (Report Builder) .

### Para adicionar propriedades personalizadas a um relatório
- No menu Report, clique em Properties .
- Na caixa de diálogo Report Properties, clique na guia Document Properties.
- Clique no botão Add para abrir a caixa de diálogo Add Property Dialog Box (Report Builder) . Add Property Dialog Box (Report Builder)
- Escolha um tipo de propriedade e digite o Name e Value da propriedade. O botão de reticências (...) ao lado da caixa Value abre a caixa de diálogo Expression Builde r. Para uma descrição dos tipos de propriedade, consulte Add Property Dialog Box (Report Builder) .

### Para excluir propriedades de relatório
- Selecione a propriedade que deseja excluir e clique em Clear .

> **Observação:** Clicar em Clear exclui a propriedade e o valor. Se você quiser limpar somente o valor, clique em Edit e exclua o valor no Expression Builder .
