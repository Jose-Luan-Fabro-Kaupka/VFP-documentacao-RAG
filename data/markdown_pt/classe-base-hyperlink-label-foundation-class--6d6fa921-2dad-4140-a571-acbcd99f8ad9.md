# Classe base Hyperlink Label Foundation Class

Esta classe fornece a funcionalidade do objeto Hyperlink e inicia um navegador Web quando você clica em um label.

| Categoria | Internet |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Internet |
| Classe | _hyperlinklabel |
| Classe base | Label |
| Biblioteca de classes | _hyperlink.vcx |
| Classe pai | _label |
| Exemplo | ...\Samples\Solution\Ffc\hyperlnk.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do Component Gallery Item, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro abre um builder para que você possa especificar o label e a URL (em cTarget) a usar. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para obter mais informações sobre o uso de classes base.

| Propriedades, Eventos, Métodos | Descrição |
| --- | --- |
| cTarget property | Especifica a URL a usar. Padrão: "" |
| GoBack method | Executa um salto de hiperlink para trás na lista de histórico. Sintaxe: GoBack( ) Retorno: nenhum Argumentos: nenhum |
| GoForward method | Executa um salto de hiperlink para frente na lista de histórico. Sintaxe: GoForward( ) Retorno: nenhum Argumentos: nenhum |
| cFrame property | Interno à classe. |
| cHyperlinkClass property | Interno à classe. |
| cHyperlinkClassLibrary property | Interno à classe. |
| cLocation property | Interno à classe. |
| cTarget_assign method | Interno à classe. |
| Follow method | Interno à classe. |
| lFormsSynch property | Interno à classe. |
| lHyperlinkcreated property | Interno à classe. |
| lNewWindow property | Interno à classe. |
| lVisited property | Interno à classe. |
| oHyperlink property | Interno à classe. |
| oHyperlink_access method | Interno à classe. |
