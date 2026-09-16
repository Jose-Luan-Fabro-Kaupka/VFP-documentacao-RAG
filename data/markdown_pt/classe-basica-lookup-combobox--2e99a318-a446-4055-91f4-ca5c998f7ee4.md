# Classe básica Lookup Combobox

Esta classe realiza uma pesquisa de valores em um campo para preencher um combobox.

| Categoria | Consulta de dados |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Data Query |
| Classe | _cbolookup |
| Classe base | ComboBox |
| Biblioteca de classes | _dataquery.vcx |
| Classe pai | _combobox |
| Exemplo | ...\Samples\Solution\Ffc\datalook2.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do item do Component Gallery, selecione Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro abre um builder para que você possa especificar os valores apropriados de Lookup_table, Order_column, Display_column e Return_column. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade Display_column | Especifica o valor da coluna da Lookup_table a exibir na lista suspensa. Padrão: "" |
| Propriedade Lookup_table | Especifica a tabela na qual encontrar a coluna contendo os valores a exibir na lista suspensa. Padrão: "" |
| Propriedade Return_column | Especifica o valor da coluna (0, 1 ou 2) a retornar à propriedade Value do combo box. Padrão: "" |
| Propriedade Order_column | Especifica a coluna para ordenar os registros exibidos na lista suspensa (opcional). Padrão: "" |
