# Classe Foundation Hyperlink Image

Esta classe fornece a funcionalidade do objeto Hyperlink e inicia um Web Browser quando você clica em uma imagem.

| Category | Internet |
| --- | --- |
| Default Catalog | Visual FoxPro Catalog\Foundation Classes\Internet |
| Class | _hyperlinkimage |
| Base Class | Image |
| Class Library | _hyperlink.vcx |
| Parent Class | _image |
| Sample | ...\Samples\Solution\Ffc\hyperlnk.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho Item do Component Gallery, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro abre um builder para que você possa especificar o nome da imagem e a URL a ser usada. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para obter mais informações sobre o uso de classes foundation.

| Properties, Events, Methods | Description |
| --- | --- |
| cTarget property | Specifies the URL to use. Default: "" |
| GoBack method | Executes a hyperlink jump backward within the history list. Syntax: GoBack( ) Return: none Arguments: none |
| GoForward method | Executes a hyperlink jump forward within the history list. Syntax: GoForward( ) Return: none Arguments: none |
| cFrame property | Internal to the class. |
| cHyperlinkClass property | Internal to the class. |
| cHyperlinkClassLibrary property | Internal to the class. |
| cLocation property | Internal to the class. |
| cTarget_assign method | Internal to the class. |
| Follow method | Internal to the class. |
| lFormsSynch property | Internal to the class. |
| lHyperlinkcreated property | Internal to the class. |
| lNewWindow property | Internal to the class. |
| lVisited property | Internal to the class. |
| oHyperlink property | Internal to the class. |
| oHyperlink_access method | Internal to the class. |
