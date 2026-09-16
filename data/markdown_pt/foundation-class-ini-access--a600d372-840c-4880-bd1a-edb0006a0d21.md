# Foundation Class INI Access

Esta classe fornece um conjunto de funções de registro que acessam configurações de arquivo no estilo INI antigo.

| Categoria | System Utilities |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Utilities |
| Classe | oldinireg |
| Classe base | Custom |
| Biblioteca de classes | Registry.vcx |
| Classe pai | registry |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do Component Gallery Item, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro posiciona a classe no formulário. Você pode então especificar os valores de propriedade apropriados e fornecer quaisquer objetos de entrada e saída necessários. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Método GetINIEntry | Recupera informações de uma entrada INI. Sintaxe: GetINIEntry(cValue, cSection, cEntry, cINIFile) Argumentos: cValue especifica o valor a ser aplicado a cEntry . cSection especifica a seção do arquivo .ini na qual cEntry ocorre. cEntry especifica o item a receber cValue . cINIFile especifica o nome do arquivo .ini. |
| Método GetINISection | Recupera informações de uma seção INI. Sintaxe: GetINISection(@aSections, cSection, cINIFile) Argumentos: aSections especifica uma matriz de cSections incluídas no arquivo .ini. cSection especifica a seção do arquivo cINIfile a ser recuperada. cINIFile especifica o nome do arquivo .ini. |
| Método LoadINIFuncs | Carrega funções necessárias para ler arquivos .ini. Sintaxe: LoadINIFuncs( ) Retorno: nenhum Argumentos: nenhum |
| Método WriteINIEntry | Grava uma entrada INI específica. Sintaxe: WriteINIEntry(cValue, cSection, cEntry, cINIFile) Argumentos: cValue especifica o novo valor. cSection especifica a seção do arquivo cINIfile a ser recuperada. cINIFile especifica o nome do arquivo .ini. |
