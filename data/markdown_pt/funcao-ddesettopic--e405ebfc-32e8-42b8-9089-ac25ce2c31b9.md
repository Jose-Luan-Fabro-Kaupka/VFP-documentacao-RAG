# Função DDESetTopic( )

Cria ou libera um nome de tópico de um nome de serviço em uma conversa de intercâmbio dinâmico de dados (DDE).

```foxpro
DDESetTopic(cServiceName, cTopicName [, cUDFName])
```

#### Parâmetros
 **cServiceName**
Especifica o nome do serviço. Nomes de serviço adicionais podem ser criados com DDESetService( ).
**cTopicName**
Especifica o nome do tópico a ser criado ou liberado. Se você incluir cUDFName, DDESetTopic( ) cria o nome do tópico cTopicName. Se você omitir cUDFName, o nome do tópico cTopicName é liberado. Se cTopicName for uma cadeia de caracteres vazia, a função definida pelo usuário especificada com cUDFName é executada para qualquer nome de tópico que não seja explicitamente declarado.
**cUDFName**
Especifica o nome da função definida pelo usuário executada quando um aplicativo cliente faz uma solicitação ao nome do tópico. Se você omitir cUDFName, o nome do tópico cTopicName é liberado do nome do serviço. Quando a função definida pelo usuário é executada, ela recebe os seguintes seis parâmetros na ordem indicada abaixo: Parâmetro Conteúdo Channel Number O número do canal do cliente. Action ADVISE, EXECUTE, INITIATE, POKE, REQUEST ou TERMINATE. Item O nome do item; por exemplo, R1C1 para uma célula de planilha do Microsoft Excel. Data Dados do cliente. Format O formato dos dados; por exemplo, CF_TEXT. Advise Status O tipo de link (0 = manual, 2 = notificação ou automático). Os valores dos parâmetros Item, Data e Advise Status dependem do parâmetro Action. A tabela a seguir lista os valores do parâmetro Action e os valores contidos nos parâmetros Item, Data e Advise Status. Um traço (–) indica que o valor do parâmetro é a cadeia de caracteres vazia. Valor Action Valor Item Valor Data Status Advise INITIATE – Nome do tópico – TERMINATE – – – POKE Nome do item Novos dados – REQUEST Nome do item – – EXECUTE – Novo comando – ADVISE Nome do item – Tipo de link Se a função definida pelo usuário tratar com sucesso a solicitação do cliente, a função definida pelo usuário deve retornar verdadeiro (.T.). Se a solicitação não puder ser tratada ou ocorrer um erro, a função definida pelo usuário deve retornar falso (.F.). Se falso for retornado quando o valor do parâmetro Action for INITIATE, a solicitação de nome de tópico do cliente é rejeitada. Se falso for retornado quando o valor for POKE, REQUEST ou EXECUTE, a solicitação é ignorada. Se falso for retornado quando o valor for ADVISE, a solicitação do cliente para um link de notificação ou automático é rejeitada.

# Valor de retorno

Logical

# Observações

Depois que um nome de tópico é criado, quaisquer solicitações de cliente ao nome do tópico fazem o Visual FoxPro executar a função definida pelo usuário especificada com cUDFName. A função definida pelo usuário recebe um conjunto de parâmetros cujos valores são determinados pela solicitação do cliente. O valor de retorno da função definida pelo usuário é passado ao cliente com DDEPoke( ). O valor de retorno é um valor lógico indicando se o nome do tópico pode fornecer o serviço solicitado pelo cliente.

DDESetTopic( ) retorna verdadeiro (.T.) se criar ou liberar com sucesso o nome do tópico. Retorna falso (.F.) se o nome do tópico não puder ser criado ou liberado. Use DDELastError( ) para determinar por que um nome de tópico não pode ser criado ou liberado.

# Exemplo

O exemplo a seguir cria um servidor de exemplo básico chamado `myserver` que suporta a execução de comandos do Visual FoxPro a partir de um aplicativo cliente. O aplicativo cliente faz solicitações a `myserver` através do tópico DO, e a substituição de macro é usada para executar o comando do cliente.

```foxpro
*** Set Visual FoxPro up as a DDE server ***
= DDESetService('myserver', 'DEFINE')
= DDESetService('myserver', 'EXECUTE', .T.)
= DDESetTopic('myserver', 'DO', 'DOTOPIC')
WAIT WINDOW 'Server portion service setup ... ' NOWAIT
*** Use Visual FoxPro as a DDE client ***
gnChannel = DDEInitiate('myserver','DO')
=DDEExecute(gnChannel, 'WAIT WINDOW "Command Executed ... "')
=DDETerminate(gnChannel)
PROCEDURE dotopic
PARAMETERS gnChannel, gcAction, gcItem, gData, gcFormat, gnAdvise
glResult = .F.
*** It's necessary to return .T. from an   ***
*** INITIATE action or no connection is made ***
IF gcAction = 'INITIATE'
   glResult = .T.
ENDIF
IF gcAction = 'EXECUTE'
   &gData
   glResult = .T.
ENDIF
IF gcAction = 'TERMINATE'
   WAIT WINDOW 'Goodbye ... ' NOWAIT
   glResult = .T.
ENDIF
RETURN glResult
```

Depois de executar este programa de exemplo, você configurou o serviço do Visual FoxPro, ao qual outros aplicativos podem acessar. Se você tem o Microsoft Excel, pode executar a macro do Excel a seguir:

```foxpro
gnMyChan = INITIATE("myserver","DO")
=EXECUTE(MyChan,"WAIT WINDOW 'Hi, this is EXCEL speaking'")
=RETURN()
```
