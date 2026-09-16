# Como: acessar dados do Visual FoxPro no Microsoft Office

Você pode acessar dados de bancos de dados e tabelas do Visual FoxPro em aplicações do Microsoft Office, como o Microsoft Excel ou o Microsoft Word, usando o Visual FoxPro OLE DB Provider.

> **Observação:** Você pode importar dados do Visual FoxPro usando o Visual FoxPro OLE DB Provider somente no Office XP.

### Para conectar a um banco de dados ou tabela do Visual FoxPro no Excel
- Abra uma planilha do Excel.
- No menu Data, aponte para Import External Data e clique em Import Data.
- Na caixa de diálogo Select Data Source, clique em New Source Data Connection.
- No Data Connection Wizard, selecione Other/Advanced.
- Na guia Provider, selecione Microsoft OLE DB Provider for Visual FoxPro.

A guia Connection na caixa de diálogo Data Link Properties é exibida.

### Para conectar a um banco de dados ou tabela do Visual FoxPro no Word
- Abra um documento do Word.
- No menu View, aponte para Toolbars e clique em Database.
- Na barra de ferramentas Database, clique no ícone Insert Database.
- Na caixa de diálogo Database, clique em Get Data.
- Na caixa de diálogo Select Data Source, clique em New Source Data Connection.
- No Data Connection Wizard, selecione Other/Advanced.
- Na guia Provider, selecione Microsoft OLE DB Provider for Visual FoxPro.

A guia Connection na caixa de diálogo Data Link Properties é exibida.

### Para adicionar uma pasta de banco de dados ou tabela do Visual FoxPro
- Na guia Connection e na caixa Select or enter a database name, digite o caminho e o nome do banco de dados ou da pasta de tabelas desejada. -ou- Para procurar um banco de dados ou pasta de tabelas do Visual FoxPro, clique no botão de reticências (...) à direita da caixa Select or enter a database name para abrir a caixa de diálogo Configure Connection.
- Especifique uma sequência de ordenação diferente, se desejado.
- Para testar a conexão, clique em Test Connection. Se a conexão for bem-sucedida, clique em OK.
