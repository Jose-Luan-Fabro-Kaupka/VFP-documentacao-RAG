# Classe Foundation Item Locator

Esta classe fornece uma caixa de diálogo File Locator. Ela foi projetada para localizar um arquivo que seu aplicativo precisa, mas não consegue encontrar.

| Categoria | Misc Forms |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Dialogs |
| Classe | _locateitem |
| Classe base | Form |
| Biblioteca de classes | _dialogs.vcx |
| Classe pai | _dialog |
| Exemplo | ...\Samples\Solution\Ffc\dialogs.scx |

# Observações

Para usar, solte a classe em um projeto ou, no menu de atalho do Item da Galeria de Componentes, selecione Create Form ou Create Form. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe, criar uma subclasse ou criar um formulário. Quando você adiciona a classe a um formulário, o Visual FoxPro exibe uma caixa de diálogo Open para que você possa especificar o nome do formulário, depois cria e abre o formulário no Form Designer.

Na propriedade cDefaultFileName, especifique o arquivo que deseja recuperar. Se o arquivo não for localizado, o objeto oLocateItem abre uma caixa de diálogo GetFile para que você possa localizar o arquivo.

| Propriedades, Eventos, Métodos | Descrição |
| --- | --- |
| Propriedade cDefaultFileName | O nome do arquivo a localizar. Padrão: .NULL. |
| Propriedade cFilename | O nome de arquivo recuperado do botão Locate. Quando nenhum arquivo é encontrado, a caixa de diálogo GetFile aparece. Padrão: .NULL. |
| Objeto oLocateItem | Uma referência de objeto que contém o valor de retorno definido na propriedade cFileName. Padrão: .F. |
