# Classe Foundation Sort Selector

Este conjunto de botões, quando colocado em um projeto ou formulário, executa uma ordenação ascendente ou descendente baseada no controle atual.

| Category | Data Query |
| --- | --- |
| Default Catalog | Visual FoxPro Catalog\Foundation Classes\Data Query |
| Class | _sortselect |
| Base Class | Container |
| Class Library | _table2.vcx |
| Parent Class | _container |
| Sample | ...\Samples\Solution\Ffc\datasort.scx |

# Observações

Para usar, arraste a classe para um projeto ou formulário ou, no menu de atalho do item do Component Gallery, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro coloca os botões no formulário. Você pode então especificar os valores de propriedade apropriados e fornecer quaisquer objetos de entrada e saída necessários. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

| Properties, Events, Methods | Description |
| --- | --- |
| DoSort method | Permite ordenar pelo campo atual ou especificar o campo pelo qual ordenar uma tabela. Sintaxe: DoSort([tcField] [,tcAlias] [,tcTag] [,tlDescending]) Retorno: nenhum Argumentos: tcField especifica o campo para ordenação. tcAlias especifica o alias da tabela a ser ordenada. tcTag especifica a tag de índice do campo, tcField. tlDescending especifica se a ordenação é descendente. |
