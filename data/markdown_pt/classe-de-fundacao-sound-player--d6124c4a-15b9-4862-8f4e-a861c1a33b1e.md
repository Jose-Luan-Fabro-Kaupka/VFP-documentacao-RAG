# Classe de fundação Sound Player

Esta classe carrega e reproduz um arquivo de som e fornece acesso à Media Control Interface (MCI).

| Categoria | Multimídia |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Multimedia |
| Classe | _soundplayer |
| Classe base | Container |
| Biblioteca de classes | _multimedia.vcx |
| Classe pai | _container |
| Exemplo | ...\Samples\Solution\Forms\mci_play.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do Component Gallery Item, selecione Add to Project ou Add to Form. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse. Quando você escolhe uma opção no menu de atalho ou solta a classe em um formulário, o Visual FoxPro abre um builder para que você possa especificar os valores apropriados de cFileName, lAutoOpen, lAutoPlay, lAutoRepeat e cControlSource.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para obter mais informações sobre o uso de classes de fundação.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade cControlSource | Especifica a fonte de dados à qual um objeto está vinculado. Padrão: "" |
| Propriedade cFileName | Especifica o nome do arquivo de som a reproduzir. Padrão: "" |
| Propriedade cMCIAlias | Especifica o alias do arquivo de vídeo ao chamar comandos MCI. Se vazio, o nome do arquivo é usado. Padrão: "" |
| Propriedade cMCIErrorString | Armazena a cadeia de erro do último comando MCI. Padrão: "" |
| Propriedade lAutoOpen | Especifica se o arquivo de vídeo especificado deve ser aberto automaticamente quando a classe é criada. Padrão: .T. |
| Propriedade lAutoPlay | Especifica se o arquivo de vídeo deve ser reproduzido automaticamente após a abertura. Padrão: .T. |
| Propriedade lAutoRepeat | Especifica se o vídeo é reproduzido continuamente. Padrão: .T. |
| Propriedade nMCIError | Especifica o resultado do último comando MCI executado. Padrão: 0 |
| Método CloseSound | Fecha o arquivo de som carregado e libera seus recursos. Sintaxe: CloseSound( ) Retorno: nenhum Argumentos: nenhum |
| Método OpenSound | Abre o arquivo de som. Sintaxe: OpenSound( ) Retorno: nenhum Argumentos: nenhum |
| Método PauseSound | Pausa o som em reprodução. Sintaxe: PauseSound( ) Retorno: nenhum Argumentos: nenhum |
| Método PlaySound | Reproduz o arquivo de som carregado. Sintaxe: PlaySound( ) Retorno: nenhum Argumentos: nenhum |
| Método SetPosition | Permite que o usuário defina a posição do arquivo de mídia. Sintaxe: SetPosition (cPosition) Retorno: nenhum Argumentos: cPosition especifica Start, End ou um número representando milissegundos no arquivo de mídia. |
| Método DoMCI | Interno à classe. |
| Método GetMCIError | Interno à classe. |
| Método ShowMCIError | Interno à classe. |
