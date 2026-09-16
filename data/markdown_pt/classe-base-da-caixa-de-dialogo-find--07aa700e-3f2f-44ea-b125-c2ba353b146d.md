# Classe base da caixa de diálogo Find

Essa classe fornece uma caixa de diálogo Find genérica com opções simples, como escolha de campo. Essa classe usa o objeto Find.

| Categoria | Consulta de dados |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Data Query |
| Classe | _finddialog |
| Classe base | Form |
| Biblioteca de classes | _table.vcx |
| Classe pai | _form |
| Exemplo | ...\Samples\Solution\Ffc\dataqry.scx |

# Observações

Para usar, solte a classe em um projeto ou, no menu de atalho do item Component Gallery, selecione Create Form ou Add to Project. Ao soltar a classe em um projeto, você pode escolher entre adicionar a classe, criar uma subclasse ou criar um formulário. Quando você solta a classe em um projeto ou escolhe Create a new form from the selected class no menu de atalho, o Visual FoxPro exibe uma caixa de diálogo Open para que você especifique o nome do formulário e, em seguida, cria e abre o formulário no Form Designer.

Consulte Diretrizes para usar classes base do Visual FoxPro para obter mais informações sobre o uso de classes base.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade cAlias | Especifica a fonte de dados na qual pesquisar. Padrão: "" |
| Propriedade cFindString | Especifica a cadeia de caracteres a pesquisar. Padrão: "" |
| Propriedade lAdvanced | Especifica se as opções avançadas serão exibidas na caixa de diálogo. Padrão: .F. |
| lFindAgain | Especifica se o arquivo será percorrido para localizar ocorrências sucessivas de cFindString. Padrão: .F. |
| Propriedade lMatchCase | Especifica a diferenciação entre maiúsculas e minúsculas da pesquisa. Padrão: .F. |
| Propriedade lSkipMemos | Especifica se os campos Memo serão eliminados da pesquisa. Padrão: .F. |
| Propriedade lWrapAround | Especifica se a pesquisa continuará desde o início quando o fim do arquivo for alcançado. Padrão: .F. |
| Método DOFind | Realiza uma pesquisa. Sintaxe: DoFind( ) Retorno: nenhum Argumentos: nenhum |
| Método SkipField | Remove o campo tcSkipField da pesquisa. Sintaxe: SkipField( ) Retorno: nenhum Argumentos: SkipField especifica o campo a ignorar durante a pesquisa. |
