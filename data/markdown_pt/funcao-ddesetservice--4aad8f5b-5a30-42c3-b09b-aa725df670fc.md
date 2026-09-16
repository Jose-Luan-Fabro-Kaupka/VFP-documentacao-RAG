# Função DDESetService( )

Cria, libera ou modifica nomes e configurações de serviço DDE.

```foxpro
DDESetService(cServiceName, cOption [, cDataFormat | lExpression])
```

#### Parâmetros
 **cServiceName**
Especifica o nome do serviço a criar, liberar, modificar ou sobre o qual retornar informações.
**cOption**
Especifica criar, liberar ou modificar um nome de serviço ou retornar informações sobre um nome de serviço. A tabela a seguir lista as opções que você pode especificar com cOption , os valores padrão das opções e uma descrição de cada opção. Opção Valor padrão Descrição DEFINE – Cria um novo nome de serviço. RELEASE – Libera um nome de serviço existente. ADVISE .F. Habilita ou desabilita a notificação do cliente sobre alterações em nomes de item. EXECUTE .F. Habilita ou desabilita a execução de comandos. POKE .F. Habilita ou desabilita pokes do cliente para o serviço. REQUEST .T. Habilita ou desabilita solicitações ao nome do serviço. FORMATS CF_TEXT Especifica formatos de dados suportados.
**DEFINE**
Cria um novo nome de serviço. Por exemplo, o comando a seguir cria o nome de serviço myservice : glNewService = DDESetService('myservice', 'DEFINE')
**RELEASE**
Libera um nome de serviço existente para liberar recursos do sistema. Quando um nome de serviço é liberado, todos os nomes de tópico do serviço também são liberados. O comando a seguir libera o nome de serviço criado no exemplo anterior: glRelease = DDESetService('myservice', 'RELEASE') Para liberar o serviço padrão do Visual FoxPro, emita este comando: glRelFox = DDESetService('FoxPro', 'RELEASE')
**ADVISE**
Especifica se um cliente é notificado quando os dados mudam em um nome de item ou especifica retornar o status de advise atual para um nome de serviço. Consulte DDEAdvise( ) para obter informações adicionais sobre como avisar clientes. Para habilitar a notificação do cliente, especifique true (.T.) para lExpression . Especificar false (.F.) para lExpression desabilita a notificação do cliente. Para retornar o status de notificação do cliente atual para o nome do serviço, omita lExpression . DDESetService( ) retorna true se a notificação do cliente estiver habilitada para o nome do serviço; retorna false se a notificação do cliente estiver desabilitada.
**EXECUTE**
Permite habilitar ou desabilitar solicitações de execução de comandos a um nome de serviço ou determinar o status de execução atual para um nome de serviço. Para habilitar solicitações do cliente para executar um comando, especifique true (.T.) para lExpression . Especificar false (.F.) para lExpression desabilita solicitações do cliente para executar um comando. .F. é o valor padrão. Para retornar o status de execução de comandos atual para o nome do serviço, omita lExpression . DDESetService( ) retorna true se solicitações de execução de comandos do cliente estiverem habilitadas para o nome do serviço; caso contrário, retorna false. Os comandos a seguir habilitam a execução de comandos e desabilitam solicitações de dados de aplicativos cliente para o nome de serviço myservice . O status de execução de comandos atual para myservice é então exibido: glExecute = DDESetService('myservice', 'EXECUTE', .T.) glRequest = DDESetService('myservice', 'REQUEST', .F.) ? DDESetService('myservice', 'EXECUTE')
**POKE**
Permite habilitar ou desabilitar solicitações de poke ao nome do serviço. Você também pode determinar o status de poke atual para um nome de serviço. Consulte DDEPoke( ) para obter informações adicionais sobre como enviar dados por poke a um servidor ou cliente. Para habilitar solicitações de poke do cliente, especifique true (.T.) para lExpression . Especificar false (.F.) para lExpression desabilita solicitações de poke do cliente. .F. é o valor padrão. Para retornar o status de poke atual para o nome do serviço, omita lExpression . DDESetService( ) retorna true se solicitações de poke estiverem habilitadas para um nome de serviço; retorna false se solicitações de poke estiverem desabilitadas.
**REQUEST**
Use REQUEST para habilitar ou desabilitar solicitações do cliente a um nome de serviço ou retornar o status de solicitação atual para o nome do serviço. Para habilitar solicitações do cliente ao nome do serviço, especifique true (.T.) para lExpression . Especificar false (.F.) desabilita solicitações do cliente ao nome do serviço. True (.T.) é o valor padrão. Para retornar o status de solicitação atual para um nome de serviço, omita lExpression . DDESetService( ) retorna true se solicitações do cliente estiverem habilitadas para o nome do serviço; retorna false se solicitações do cliente estiverem desabilitadas. Os comandos a seguir desabilitam solicitações de aplicativos cliente ao nome de serviço myservice e exibem o status de solicitação atual para myservice : glRequest = DDESetService('myservice', 'REQUEST', .F.) ? DDESetService('myservice', 'REQUEST')
**FORMATS [ cDataFormat ]**
Especifica os formatos de dados suportados pelo nome do serviço. Solicitações do servidor para formatos não especificados com cDataFormat são rejeitadas. Ao especificar formatos de dados, inclua uma lista dos formatos suportados separados por vírgulas. Por exemplo: =DDESetService('myservice', 'FORMATS', 'CF_TEXT, CF_SYLK') Se você omitir cDataFormat , apenas o formato CF_TEXT é suportado.
**lExpression**
Especifica o estado das opções REQUEST, EXECUTE, POKE ou ADVISE. Especifique true (.T.) para lExpression para habilitar a opção ou false (.F.) para desabilitá-la.

# Valor de retorno

Lógico

# Observações

O Visual FoxPro pode atuar como um servidor de troca dinâmica de dados (DDE) para enviar dados a aplicativos cliente baseados em Microsoft Windows. DDESetService( ) é usado para criar, liberar ou modificar nomes e configurações de serviço no Visual FoxPro. Cada nome de serviço pode ter um conjunto de nomes de tópico criados com DDESetTopic( ). Aplicativos cliente solicitam dados de nomes de tópico DDE.

DDESetService( ) retorna true (.T.) se o nome do serviço for criado, liberado ou modificado com sucesso. Se o nome do serviço não puder ser criado, liberado ou modificado, DDESetService( ) retorna false (.F.).

DDESetService( ) também pode ser usado para retornar informações sobre um nome de serviço. O Visual FoxPro tem o nome de serviço padrão FoxPro. O nome de serviço do Visual FoxPro tem um nome de tópico chamado System. A tabela a seguir lista todos os nomes de item suportados pelo tópico System.

| Nome do item | Item |
| --- | --- |
| Topics | Uma lista de nomes de tópico disponíveis |
| Formats | Uma lista de formatos suportados |
| Status | Busy ou Ready |
| SysItems | Uma lista de nomes de item |

Você pode usar DDESetTopic( ) para modificar o nome de serviço FoxPro ou liberá-lo. Para obter informações sobre manipulação de nomes de serviço do Visual FoxPro, consulte as opções da Função DDESetTopic( ).
