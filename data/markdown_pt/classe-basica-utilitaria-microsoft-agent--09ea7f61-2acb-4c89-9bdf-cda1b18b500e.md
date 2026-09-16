# Classe básica utilitária Microsoft Agent

Esta classe fornece acesso às rotinas da API do Microsoft Agent para que você possa integrar à aplicação agentes semelhantes aos Assistentes do Office, como o periquito Peedy.

| Categoria | Utilitários do sistema |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Utilities |
| Classe | _agent |
| Classe base | Custom |
| Biblioteca de classes | _agent.vcx |
| Classe pai | _custom |
| Exemplo | ...\Samples\Solution\Ffc\Agent.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do item da Galeria de Componentes, selecione Add to Project ou Add to Form. Ao adicioná-la a um formulário, o Visual FoxPro coloca seu ícone no formulário. Você pode especificar os valores apropriados das propriedades e fornecer os objetos de entrada e saída necessários. Ao soltá-la em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Diretrizes para usar classes básicas do Visual FoxPro para obter mais informações.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade ActiveAgent | Fornece um ponteiro para o objeto de personagem Agent ativo. Padrão: .F. |
| Propriedade AgentControl | Fornece um ponteiro para o objeto Agent. Padrão: .F. |
| Propriedade ErrorOccurred | Definida como True (.T.) quando ocorre um erro em LOAD. Padrão: .F. |
| Propriedade ErrorState | Sempre definida como LOAD. |
| Método GestureAt | Faz o agente ativo gesticular em um ponto. Sintaxe: GestureAt(tnX, tnY, tnCoords, toObj) Retorno: .F. se não houver ActiveAgent. Argumentos: tnX especifica a coordenada x; tnY, a coordenada y; tnCoords, se as coordenadas são locais ou globais; toObj, a referência para conversão LocalToWorld. |
| Método Hide | Oculta o agente ativo. Sintaxe: Hide( ) Retorno: .F. se não houver ActiveAgent. Argumentos: nenhum |
| Método Interrupt | Interrompe uma animação. Sintaxe: Interrupt(toRequest) Retorno: .F. se não houver ActiveAgent. Argumentos: toRequest especifica o objeto de solicitação. |
| Método Load | Carrega um personagem Agent do local especificado, que pode ser arquivo ou URL. Sintaxe: Load(tcAgentName, tcAgentLocation) Retorno: .F. se ocorrer um erro. Argumentos: tcAgentName especifica o nome; tcAgentLocation, o arquivo do agente. |
| Método LocalToWorld | Converte coordenadas locais em globais. Sintaxe: LocalToWorld(tnAxis, tnPos, toObj) Retorno: valor convertido de tnPos. Argumentos: tnAxis especifica o eixo; tnPos, a coordenada; toObj, o objeto em relação ao qual a conversão é feita. |
| Método MoveBy | Move o agente ativo pelos valores passados nas direções x ou y. Sintaxe: MoveBy(tnX, tnY, tnCoords, toObj) Retorno: .F. se não houver ActiveAgent. Argumentos: tnX e tnY especificam coordenadas; tnCoords, se são locais ou globais; toObj, a referência para LocalToWorld. |
| Método MoveTo | Move o agente padrão ou passado para o local especificado. Sintaxe: MoveTo(tnX, tnY, tnCoords, toObj) Retorno: .F. se não houver ActiveAgent. Argumentos: tnX e tnY especificam coordenadas; tnCoords, se são locais ou globais; toObj, a referência para LocalToWorld. |
| Método Play | Faz o agente ativo reproduzir uma animação. Sintaxe: Play(tcAnimation) Retorno: .F. se não houver ActiveAgent ou uma referência Request Object. Argumentos: tcAnimation especifica a animação. |
| Método SetActiveAgent | Define como ativo o agente com o nome passado. Sintaxe: SetActiveAgent(tcAgentName) Retorno: .T. se ActiveAgent for definido. Argumentos: tcAgentName especifica o nome. |
| Método Show | Exibe o agente ativo. Sintaxe: Show(tnX, tnY, tnCoords, toObj) Retorno: .F. se não houver ActiveAgent. Argumentos: tnX e tnY especificam coordenadas; tnCoords, se são locais ou globais; toObj, a referência para LocalToWorld. |
| Método Speak | Faz o agente ativo falar a frase passada. Sintaxe: Speak(tcText) Retorno: .F. se não houver ActiveAgent ou uma referência Request Object. Argumentos: tcText especifica o texto. |
| Método Stop | Interrompe uma animação em repetição. Sintaxe: Stop( ) Retorno: .F. se não houver ActiveAgent. Argumentos: nenhum |
| Método Wait | Aguarda a conclusão de uma solicitação. Sintaxe: Wait(toRequest) Retorno: .F. se não houver ActiveAgent. Argumentos: toRequest especifica o objeto solicitante. |
