# Classe básica de objeto Data Navigation

Este é um objeto de navegação não visual que pode ser usado por outros controles para navegar registros em uma fonte de dados, como uma tabela ou view.

| Category | Data Navigation |
| --- | --- |
| Default Catalog | Visual FoxPro Catalog\Foundation Classes\Data Navigation |
| Class | _tablenav |
| Base Class | Custom |
| Class Library | _table.vcx |
| Parent Class | _table |
| Sample | ...\Samples\Solution\Ffc\datanav.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do item do Component Gallery, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um projeto, pode escolher entre adicionar a classe ou criar uma subclasse. Quando você adiciona a classe a um formulário, o Visual FoxPro exibe o ícone da classe no formulário para que você possa adicionar objetos de navegação de dados e então referenciar os métodos de classe apropriados no formulário no Form Designer.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para obter mais informações sobre o uso de classes básicas.

| Properties, Events, Methods | Description |
| --- | --- |
| lCycle property | Controla o movimento quando o ponteiro de registro atinge o final ou o início do arquivo. Padrão: .F. |
| GoBottom method | Move o ponteiro de registro para o último registro. Syntax: GoBottom( ) Return: none Arguments: none |
| GoRecord method | Move o ponteiro de registro para um número de registro especificado. Syntax: GoRecord( ) Return: none Arguments: tiRecord |
| GoNext method | Move o ponteiro de registro para o próximo registro usando SKIP 1. Se esse movimento posicionar o ponteiro em EOF( ), o comportamento é determinado pela propriedade lCycle. Syntax: GoNext( ) Return: none Arguments: none |
| GoPrevious method | Move o ponteiro de registro para o registro anterior usando SKIP –1 se o ponteiro ainda não estiver em BOF( ). Se esse movimento posicionar o ponteiro em BOF( ), o comportamento é determinado pela propriedade lCycle. Syntax: GoNext( ) Return: none Arguments: none |
| GoTop method | Move o ponteiro de registro para o primeiro registro. Syntax: GoTop( ) Return: none Arguments: none |
