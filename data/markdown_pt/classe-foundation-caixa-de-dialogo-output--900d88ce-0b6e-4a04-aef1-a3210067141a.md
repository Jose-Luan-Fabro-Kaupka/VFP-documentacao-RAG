# Classe Foundation Caixa de diálogo Output

Esta classe usa o objeto Report para exibir uma caixa de diálogo que solicita ao usuário uma opção de saída de relatório.

| Categoria | Relatórios |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Output |
| Classe | _outputdialog |
| Classe base | Form |
| Biblioteca de classes | _reports.vcx |
| Classe pai | _form |
| Amostra | ...\Samples\Solution\Ffc\output.scx |

# Observações

Para usar, solte a classe em um projeto ou, no menu de atalho Item da Galeria de Componentes, selecione Create Form. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe, criar uma subclasse ou criar um formulário. Se você escolher Create a new form, o Visual FoxPro abre um construtor para que você possa especificar o nome do formulário, depois cria e abre o formulário no Form Designer.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para mais informações sobre o uso de classes foundation.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| propriedade cAlias | Especifica o nome da fonte de dados para saída. Padrão: "" |
| propriedade cDestination | Especifica a lista de destinos disponíveis que mudam dinamicamente dependendo se cReport , cAlias , ou ambos, contêm valores. Padrão: "" |
| propriedade cDisplayFontName | Especifica o nome de uma exibição na tela da saída; por exemplo, quando você emite BROWSE ou quando a classe _Showtext é instanciada para exibição de texto. Padrão: .F. |
| propriedade cFieldList | Especifica uma lista separada por vírgulas de campos ou expressões. Afeta apenas fontes de dados diretas (BROWSEs e LISTs). Padrão: "" |
| propriedade cHTMLClass | Especifica uma classe HTML opcional e biblioteca de classes passada para _GENHTML. Padrão: "" |
| propriedade cHTMLStyleID | Especifica um estilo HTML opcional passado para _GENHTML. Padrão: .F. |
| propriedade cReport | Especifica o nome do relatório ou etiqueta para saída. Padrão: "" |
| propriedade cScope | Especifica uma expressão de escopo válida para saída. Padrão: .F. |
| propriedade lAddSourceNameToDropdown | Especifica se alguns destinos são exibidos na matriz aDestinations. Padrão: .F. |
| propriedade lPreventScopeChanges | Especifica se você pode alterar o escopo de saída. Padrão: .F. |
| propriedade lPreventSourceChanges | Especifica se alterações de origem para cAlias ou cReport são impedidas. Padrão: .F. |
| método cAlias_access | Interno à classe. |
| método cAlias_assign | Interno à classe. |
| método cDestination_access | Interno à classe. |
| método cDestination_assign | Interno à classe. |
| método cDisplayFontName_access | Interno à classe. |
| método cDisplayFontName_assign | Interno à classe. |
| método cFieldList_access | Interno à classe. |
| método cFieldList_assign | Interno à classe. |
| método CheckOKButton | Interno à classe. |
| cHTMLClass_access | Interno à classe. |
| cHTMLClass_assign | Interno à classe. |
| cHTMLStyleID_access | Interno à classe. |
| cHTMLStyleID_assign | Interno à classe. |
| método cReport_access | Interno à classe. |
| método cReport_assign | Interno à classe. |
| método cScope_access | Interno à classe. |
| método cScope_assign | Interno à classe. |
| método lAddSourceNameToDropdown_access | Interno à classe. |
| método lAddSourceNameToDropdown_assign | Interno à classe. |
| método lPreventScopeChanges_assign | Interno à classe. |
| método lPreventSourceChanges_access | Interno à classe. |
| método lPreventSourceChanges_assign | Interno à classe. |
| método RespondToPermissionForScopeChanges | Interno à classe. |
| método RespondToPermissionForSourceChanges | Interno à classe. |
