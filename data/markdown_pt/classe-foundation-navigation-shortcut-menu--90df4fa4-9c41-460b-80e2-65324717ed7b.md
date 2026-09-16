# Classe Foundation Navigation Shortcut Menu

Este é um menu de atalho que pode ser solto em um formulário com itens para opções comuns de navegação de dados, classificação, filtragem e localização. Você chama esta classe do evento RightClick de um formulário.

| Categoria | Menus |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\User Controls |
| Classe | _navmenu |
| Classe base | Container |
| Biblioteca de classes | _table2.vcx |
| Classe pai | _container |
| Amostra | ...\Samples\Solution\Ffc\datasort.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho Item da Galeria de Componentes, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro solicita que você adicione automaticamente o código necessário para implementar o menu de atalho. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para mais informações sobre o uso de classes foundation.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| propriedade cClass | Especifica a classe da caixa de diálogo que contém o menu de atalho. Padrão: "" |
| propriedade cClasslib | Especifica a biblioteca de classes que contém a classe da caixa de diálogo que contém o menu de atalho. Padrão: "" |
| método DoMenu . | Executa uma rotina de menu. Sintaxe: Domenu( ) Retorno: nenhum Argumentos: nenhum |
| método RefreshForm | Atualiza o formulário ativo quando os dados são atualizados. Sintaxe: RefreshForm( ) Retorno: nenhum Argumentos: nenhum |
| método DeleteRecord | Exclui o registro atual. Sintaxe: DeleteRecord( ) Retorno: nenhum Argumentos: nenhum |
| método AddRecord | Adiciona um novo registro. Sintaxe: AddRecord( ) Retorno: nenhum Argumentos: nenhum |
| método DoFilter | Exibe uma caixa de diálogo de filtro. Sintaxe: DoFilter( ) Retorno: nenhum Argumentos: nenhum |
| método DoGoto | Exibe uma caixa de diálogo GoTo. Sintaxe: DoGoto( ) Retorno: nenhum Argumentos: nenhum |
| método DoSort | Exibe uma caixa de diálogo Sort. Sintaxe: DoSort( ) Retorno: nenhum Argumentos: nenhum |
| método DoDialog | Exibe uma caixa de diálogo. Sintaxe: DoDialog( ) Retorno: nenhum Argumentos: nenhum |
| método SetMenu | Especifica o conteúdo do menu por meio de código contendo expressões AddMenuBar ( ). Sintaxe: SetMenu( ) Retorno: nenhum Argumentos: nenhum |
| método DoFilter2 | Exibe uma caixa de diálogo Advanced Filter. Sintaxe: DoFilter2( ) Retorno: nenhum Argumentos: nenhum |
