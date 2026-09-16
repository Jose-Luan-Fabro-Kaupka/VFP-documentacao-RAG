# Como: exibir dados incorporados ou vinculados de tabelas

Em um formulário ou relatório, você pode exibir dados vinculados ou incorporados de campos General de uma tabela. Por exemplo, suponha que você tenha uma tabela de produtos em que cada registro inclua um campo General contendo um folheto (um documento do Word) sobre o produto. Em um formulário, seria possível exibir informações selecionadas dos registros, inclusive esse folheto.

### Para exibir dados de um campo General em um formulário
- No Designer de Formulários, adicione um controle OLE Bound ao formulário. O Visual FoxPro cria um objeto por meio do qual você poderá exibir os dados em tempo de execução.
- Especifique o campo General que contém os dados definindo a propriedade ControlSource do objeto. Por exemplo, se a tabela se chamar Inventory e o campo General se chamar Current, defina ControlSource como Inventory.Current.
- No formulário, adicione botões ou comandos de menu para navegar pelo campo General especificado em ControlSource.

### Para exibir dados de um campo General em um relatório
- Adicione um campo General ao relatório. Para obter detalhes, consulte Como: adicionar campos General a relatórios. Dica Ao criar um relatório, você pode vincular ou incorporar imagens ou ícones diretamente nele a partir de uma fonte externa usando o contêiner de imagem. Outras formas de dados, como documentos do Word ou planilhas do Microsoft Excel, só podem ser incluídas se tiverem sido previamente vinculadas ou incorporadas a um campo General em uma tabela do Visual FoxPro.
