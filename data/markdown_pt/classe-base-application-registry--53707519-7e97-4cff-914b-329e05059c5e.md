# Classe base Application Registry

Esta classe fornece um conjunto de funções de registro que retornam informações específicas da aplicação, como versão e localização.

| Categoria | Utilitários do sistema |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Utilities |
| Classe | _filereg |
| Classe base | Custom |
| Biblioteca de classes | _registry.vcx |
| Classe pai | registry |
| Exemplo | ...\Samples\Solution\WinAPI\regfile.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do item da Component Gallery, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro coloca a classe no formulário. Você pode então especificar os valores apropriados e fornecer quaisquer objetos de entrada e saída necessários. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para obter mais informações sobre o uso de classes base.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| método GetAppPath | Verifica e retorna o caminho da aplicação associada a uma extensão específica. Sintaxe: GetAppPath(cExtension, cExtnKey, cAppKey, lServer) Retorno: GetApplication( cExtnKey , @cAppKey , lServer ) Argumentos: cExtension especifica a extensão da aplicação. cExtnKey especifica a chave de registro da aplicação. cAppKey especifica o caminho da aplicação. lServer especifica se a extensão é uma aplicação de servidor. |
| método GetLatestVersion | Retorna a versão mais recente para uma aplicação especificada. Sintaxe: Getlatestversion(cClass, cExtnKey, cAppKey, lServer) Retorno: cExtnKey , @cAppKey , lServer Argumentos: cClass especifica a chave de classe da aplicação. cExtension especifica a extensão da aplicação. cExtnKey especifica a chave de registro da aplicação. cAppKey especifica o caminho da aplicação. lServer especifica se esta é uma aplicação de servidor. |
| método GetApplication | Recupera a chave da aplicação. Sintaxe: Getapplication(cExtnKey, cAppKey, lServer) Retorno: @cAppKey Argumentos: cExtension especifica a extensão da aplicação. cExtnKey especifica a chave de registro da aplicação. cAppKey especifica o caminho da aplicação. lServer especifica se a extensão não é uma aplicação completa. |
