# Classe base Botão de hiperlink

Esta classe fornece a funcionalidade do objeto Hyperlink e inicia um navegador Web quando você clica em um botão.

| Categoria | Internet |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Internet |
| Classe | _hyperlinkcommandbutton |
| Classe base | CommandButton |
| Biblioteca de classes | _hyperlink.vcx |
| Classe pai | _commandbutton |
| Exemplo | ...\Samples\Solution\Ffc\buttons.scx |

# Observações

Para usar, arraste a classe para um projeto ou formulário ou, no menu de atalho do item da Galeria de componentes, selecione Adicionar ao projeto ou Adicionar ao formulário. Quando você adiciona a classe a um formulário, o Visual FoxPro abre um construtor para que você possa especificar o nome do botão e a URL a usar. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Diretrizes para uso de classes base do Visual FoxPro para obter mais informações sobre o uso de classes base.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade cTarget | Especifica a URL a usar. Padrão: "" |
| Método GoBack | Executa um salto de hiperlink para trás na lista de histórico. Sintaxe: GoBack( ) Retorno: nenhum Argumentos: nenhum |
| Método GoForward | Executa um salto de hiperlink para frente na lista de histórico. Sintaxe: GoForward( ) Retorno: nenhum Argumentos: nenhum |
| Propriedade cFrame | Interno à classe. |
| Propriedade cHyperlinkclass | Interno à classe. |
| Propriedade cHyperlinkClassLibrary | Interno à classe. |
| Propriedade cLocation | Interno à classe. |
| Propriedade lFormSynch | Interno à classe. |
| Propriedade lHyperlinkCreated | Interno à classe. |
| Propriedade lNewWindow | Interno à classe. |
| Propriedade lVisited | Interno à classe. |
| Propriedade nVisitedForecolor | Interno à classe. |
| Propriedade oHyperlink | Interno à classe. |
| Método cTarget_assign | Interno à classe. |
| Método Follow | Interno à classe. |
| Método lVisited_assign( ) | Interno à classe. |
| Método nVisitedForecolor_assign( ) | Interno à classe. |
| Método oHyperlink_access( ) | Interno à classe. |
| Método ShowVisitedForecolor( ) | Interno à classe. |
