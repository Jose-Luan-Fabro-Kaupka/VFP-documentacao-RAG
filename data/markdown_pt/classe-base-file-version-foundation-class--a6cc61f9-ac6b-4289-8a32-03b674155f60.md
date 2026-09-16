# Classe base File Version Foundation Class

Recupera informações do recurso de versão de um arquivo e as armazena em uma matriz.

| Categoria | File Utilities |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Utilities |
| Classe | _fileversion |
| Classe base | Custom |
| Biblioteca de classes | _utility.vcx |
| Classe pai | _custom |
| Amostra | ...\Samples\Solution\WinAPI\getver.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do Component Gallery Item, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro coloca a classe no formulário. Você pode então especificar os valores apropriados e fornecer os objetos de entrada e saída necessários. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

| Properties, Events, Methods | Descrição |
| --- | --- |
| propriedade cFileName | O nome do arquivo de destino. Padrão: "" |
| propriedade aVersion[12,0] | Matriz contendo as informações de versão do arquivo. Padrão: .F. |
| método GetVersion | Recupera informações de versão para cFileName. Sintaxe: GetVersion( ) Retorno: none Argumentos: none |
| método DisplayVersion | Exibe as informações de versão para cFileName. Sintaxe: DisplayVersion( ) Retorno: none Argumentos: none |
