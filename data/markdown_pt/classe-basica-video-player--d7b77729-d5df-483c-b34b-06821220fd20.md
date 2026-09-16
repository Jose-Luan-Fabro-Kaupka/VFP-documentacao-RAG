# Classe básica Video Player

Esta classe carrega e reproduz um arquivo de vídeo e fornece acesso à Interface de Controle de Mídia (MCI).

| Categoria | Multimídia |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Multimedia |
| Classe | _videoplayer |
| Classe base | Container |
| Biblioteca de classes | multimedia.vcx |
| Classe pai | _container |
| Exemplo | ...\Samples\Solution\Forms\mci_play.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do item da Galeria de componentes, selecione Adicionar ao projeto ou Adicionar ao formulário. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse. Quando você escolhe uma opção no menu de atalho ou solta a classe em um formulário, o Visual FoxPro abre um construtor para que você possa especificar os valores apropriados de cFileName, lAutoOpen, lAutoPlay, lAutoRepeat e cControlSource.

Consulte Diretrizes para usar classes básicas do Visual FoxPro para obter mais informações sobre o uso de classes básicas.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade AutoOpen | Especifica se o arquivo de vídeo especificado deve ser aberto automaticamente quando a classe é criada. Padrão: .T. |
| Propriedade AutoPlay | Especifica se o arquivo de vídeo deve ser reproduzido automaticamente após a abertura. Padrão: .T. |
| Propriedade AutoRepeat | Se verdadeiro (.T.), especifica que o arquivo de vídeo será reproduzido continuamente. Padrão: .T. |
| Propriedade cFileName | Especifica o arquivo de vídeo associado ao Video Frame. Padrão: "" |
| Propriedade Controlsource | Especifica a origem dos dados à qual um objeto está vinculado. Padrão: "" |
| Propriedade MCIAlias | Especifica o alias para o arquivo de vídeo ao chamar comandos MCI. Se estiver vazio, o nome do arquivo é usado. Padrão: "" |
| Propriedade MCIError | Especifica o resultado do último comando MCI executado. Padrão: 0 |
| Propriedade MCIErrorString | Armazena a cadeia de erro do último comando MCI executado. Padrão: "" |
| Método CloseVideo | Fecha o arquivo de vídeo e libera todos os recursos. Sintaxe: CloseVideo( ) Retorno: nenhum Argumentos: nenhum |
| Método DoMCI | Executa um comando MCI. Sintaxe: DoMCI(cMCIcmd) Retorno: cRetString Argumentos: cMCIcmd especifica o comando a ser executado. |
| Método PauseVideo | Pausa um vídeo em reprodução. Sintaxe: PauseVideo( ) Retorno: nenhum Argumentos: nenhum |
| Método PlayVideo | Reproduz o vídeo atualmente carregado. Sintaxe: PlayVideo( ) Retorno: nenhum Argumentos: nenhum |
| Método SetPosition | Permite que o usuário defina a posição do arquivo de mídia. Sintaxe: SetPosition(cPosition) Retorno: nenhum Argumentos: cPosition especifica Start, End ou um número representando milissegundos no arquivo de mídia. |
| Método GetMCIError | Interno à classe. |
| Método OpenVideo | Interno à classe. |
| Método ShowMCIError | Interno à classe. |
