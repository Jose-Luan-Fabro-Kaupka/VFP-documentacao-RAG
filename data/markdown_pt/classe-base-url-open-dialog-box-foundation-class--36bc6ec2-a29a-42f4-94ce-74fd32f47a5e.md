# Classe base URL Open Dialog Box Foundation Class

Esta caixa de diálogo, quando colocada em um formulário, fornece uma lista suspensa que armazena a lista de histórico de URLs.

| Category | Internet |
| --- | --- |
| Default Catalog | Visual FoxPro Catalog\Foundation Classes\Internet |
| Class | _openaddressdialog |
| Basse Class | Form |
| Class Library | _internet.vcx |
| Parent Class | _dialog |
| Sample | ...\Samples\Solution\Ffc\hyperlnk.scx |

# Observações

Para usar, solte a classe em um projeto ou, no menu de atalho Component Gallery Item, selecione Add to Project ou Create Form. Quando você adiciona a classe a um projeto, pode escolher entre adicionar a classe ou criar uma subclasse, ou criar um formulário. Quando você cria um formulário, o Visual FoxPro exibe uma caixa de diálogo Open para que você possa especificar o nome do formulário e, em seguida, cria e abre o formulário no Form Designer para que você possa especificar os valores apropriados de Target e lShellExecute.

| Properties, Events, Methods | Description |
| --- | --- |
| lShellExecute property | Runs the target URL. Default: .T. |
| Target property | Specifies the name of the target URL. Default: "" |
| cFileExt property | Internal to the class. |
