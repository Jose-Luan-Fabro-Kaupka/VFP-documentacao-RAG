# Classe base QBF

Esta classe fornece um conjunto de botões para consulta Query-By-Form.

| Categoria | Consulta de dados |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Data Query |
| Classe | _qbf |
| Classe base | Container |
| Biblioteca de classes | _dataquery.vcx |
| Classe pai | _container |
| Exemplo | ...\Samples\Solution\Forms\qbf.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do item da Galeria de componentes, selecione Adicionar ao projeto ou Adicionar ao formulário. Quando você adiciona a classe a um formulário, o Visual FoxPro coloca os botões de comando QBF no formulário. Você pode então especificar os valores de propriedade apropriados e fornecer quaisquer objetos de entrada e saída necessários. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade QBF_Table | Especifica a tabela na qual executar a consulta. Padrão: "" |
| Método ParseCondition( ) | Especifica um filtro baseado em uma consulta. Sintaxe: ParseCondition(cCondition, cControlSource) Retorno: lcRetCondition Argumentos: cControlSource especifica os dados vinculados ao controle. cCondition especifica a expressão de consulta. |
