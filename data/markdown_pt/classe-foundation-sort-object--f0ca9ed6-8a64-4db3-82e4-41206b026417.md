# Classe Foundation Sort Object

Esta classe, quando colocada em um formulário, permite classificar uma fonte de dados.

| Category | Data Query |
| --- | --- |
| Default Catalog | Visual FoxPro Catalog\Foundation Classes\Data Query |
| Class | _tablesort |
| Base Class | Custom |
| Class Library | _table.vcx |
| Parent Class | _table |
| Sample | ...\Samples\Solution\Ffc\datasort.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho Item do Component Gallery, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro coloca o ícone da classe no formulário. Você pode então especificar os valores de propriedade apropriados e fornecer quaisquer objetos de entrada e saída necessários. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para obter mais informações sobre o uso de classes foundation.

| Properties, Events, Methods | Description |
| --- | --- |
| lDescending property | Specifies whether the sort order is ascending or descending. Default: .F. |
| DoSort method | Makes it possible for you to sort on the current field or to specify the field on which to order a table or alias. Syntax: DoSort([tcField] [,tcAlias] [,tcTag] [,tlDescending]) Return: none Arguments: tcField specifies the field to sort on. tcAlias specifies the alias of the table to sort. tcTag specifies the index tag of the field, tcField . tlDescending specifies whether the sort is a descending sort. |
| GetSortTag method | Looks for an appropriate tag name by looking at key expressions in the table relevant to the field name. Syntax: Getsorttag(tcField, tcAlias) Return: lcTag Arguments: tcField specifies the field to sort on. tcAlias specifies the alias of the table to sort. |
| RemoveSort method | Removes the current index tag. Syntax: RemoveSort(tcAlias) Return: none Arguments: tcAlias specifies the alias of the table from which to remove the tag. |
