# Filter Expression Dialog Box Foundation Class

Esta classe cria uma caixa de diálogo avançada de expressão de filtro.

| Category | Data Query |
| --- | --- |
| Default Catalog | Visual FoxPro Catalog\Foundation Classes\Data Query |
| Class | _filterexpr |
| Base Class | Form |
| Class Library | _table.vcx |
| Parent Class | _form |
| Sample | ...\Samples\Solution\Ffc\datasort.scx |

# Observações

Para usar, solte a classe em um projeto ou, no menu de atalho do item da Component Gallery, selecione Create Form ou Add to Project. Ao soltar a classe em um projeto, você pode escolher entre adicionar a classe, criar uma subclasse ou criar um formulário. Ao soltar a classe em um projeto ou escolher Create a new form from the selected class no menu de atalho, o Visual FoxPro exibe uma caixa de diálogo Open para que você especifique o nome do formulário. O Visual FoxPro então cria e abre o formulário no Form Designer.

_FilterExpr é uma caixa de diálogo modal que permite especificar uma expressão de filtro ou construir uma expressão de filtro usando uma de duas caixas de diálogo subsidiárias.

A propriedade lAdvanced alterna _FilterExpr entre dois modos, padrão e avançado. No modo padrão, o botão Build expression usa uma instância da classe _FilterDialog para construir uma expressão simples. No modo avançado, o botão usa o valor na variável de sistema _GETEXPR.

A propriedade cFilter contém o conteúdo atual da expressão de filtro que o usuário constrói. A caixa de edição vinculada à propriedade cFilter pode conter até 254 caracteres.

Se _FilterExpr não encontrar uma tabela sobre a qual atuar, retorna false (.F.) antes de sair do evento Init; caso contrário, restaura essas configurações em seu método Unload. Quando _FilterExpr é instanciado, se ALIAS( ) estiver vazio, ele procura uma tabela aberta na sessão de dados atual do formulário ou formset atualmente selecionado.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para mais informações sobre o uso de foundation classes.

| Properties, Events, Methods | Descriptionbox b |
| --- | --- |
| cFilter property | Contém a expressão de filtro processada no método SetupFilter. Padrão: (SPACE(254)) |
| lAdvanced property | Usado para alternar _FilterExpr entre dois modos, _FilterDialog false (.F) e GETEXPR true (.T.). Padrão: .F. |
| iOldSession property | A sessão de dados antiga. Padrão: 0 |
| iOldSelect property | A área de trabalho antiga. Padrão: 0 |
| SetFilter method | Define o valor de cFilter. Este método é útil principalmente quando _FilterDialog é chamado modalmente para trabalhar mais na expressão a ser construída. Sintaxe: SetFilter(tcValue) Retorno: cFilter Argumentos: tcValue especifica uma expressão para usar como filtro. cFilter é a expressão de filtro. |
| SetFilterOnTable method | Se a tabela atual permite navegação, este método aplica o filtro atual ao alias atual, emite um LOCATE e então invoca o método RefreshLastWindowAfterChange( ) para obter o filtro da próxima janela disponível em seu aplicativo. Sintaxe: SetFilterOnTable( ) Retorno: nenhum Argumentos: nenhum |
| cFilter_Access method | Interno à classe. Remove retornos de carro, avanços de linha e tabulações da expressão de filtro e substitui esses caracteres por espaços. |
