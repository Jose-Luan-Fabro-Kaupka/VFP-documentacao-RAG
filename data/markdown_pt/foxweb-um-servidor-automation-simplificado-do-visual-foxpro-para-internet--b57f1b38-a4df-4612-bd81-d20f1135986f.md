# FoxWeb, um servidor Automation simplificado do Visual FoxPro para Internet

O FoxWeb é uma amostra simplificada de servidor Automation ISAPI projetada para colocar rapidamente um site Web em funcionamento. O FoxWeb fornece uma nova versão do Foxisapi.dll (também fornecido com o FoxIs do Visual FoxPro, uma amostra de servidor Internet do Visual FoxPro). O Foxisapi.dll agora pode gerenciar várias instâncias de servidores Automation do Visual FoxPro e fornece métodos adicionais de depuração para aplicativos Visual FoxPro projetados para a Internet.

# O servidor Automation FoxWeb

A amostra FoxWeb usa uma classe de servidor Visual FoxPro simples destinada a demonstrar o uso básico de um servidor executado sob FoxISAPI. Todo o código está armazenado em um arquivo chamado FoxWeb.prg. Este arquivo contém uma classe chamada Server, que é marcada como OLEPUBLIC para que seja registrada como componente COM de servidor Automation quando compilada. Esta classe é instanciada pelo FoxISAPI e contém vários métodos que podem ser invocados (como os métodos Hello e Delay) conforme mostrado abaixo. Esses métodos ilustram as estruturas exigidas pelo FoxISAPI para funcionar corretamente.

# Os arquivos de amostra FoxWeb

Os arquivos da nova amostra de servidor Automation FoxWeb do Visual FoxPro estão localizados no diretório Visual FoxPro ...\Samples\Servers\Foxisapi\FoxWeb.

# Configurando o servidor Automation FoxWeb

As seções a seguir descrevem como usar o Visual FoxPro para colocar rapidamente um site Web em funcionamento com o FoxWeb.

### Registrando o servidor Automation FoxWeb do Visual FoxPro

Os servidores Automation do Visual FoxPro que retornam HTML devem ser registrados. O registro é feito automaticamente se seu .exe ou .dll foi compilado com o Project Manager do Visual FoxPro ou com os comandos BUILD EXE, BUILD DLL ou BUILD MTDLL. Por exemplo, se você abrir o projeto FoxWeb fornecido com a amostra FoxWeb no Project Manager, pode escolher Build para criar um servidor Automation como um arquivo .dll in-process ou .exe out-of-process. Observe que o registro ocorre somente na máquina na qual o arquivo foi compilado.

Um servidor Automation do Visual FoxPro compilado como .exe out-of-process também pode ser registrado especificando o nome do servidor Automation e incluindo a opção /RegServer. Por exemplo, o seguinte comando registra o servidor Automation FoxWeb do Visual FoxPro:

```foxpro
FoxWeb.exe /RegServer
```

Um servidor Automation do Visual FoxPro compilado como .dll in-process também pode ser registrado com Regsvr32.exe. Por exemplo, o seguinte comando registra o servidor Automation FoxWeb do Visual FoxPro:

```foxpro
Regsvr32 FoxWeb.dll
```

> **Observação:** Se seu servidor Automation ISAPI do Visual FoxPro usa arquivos adicionais como .gif ou .jpg, certifique-se de colocar esses arquivos em diretórios que o Microsoft Internet Information Services (IIS) ou o Microsoft Personal Web Server possam acessar.

### Usando seu navegador Web para acessar um servidor Automation ISAPI do Visual FoxPro

Um servidor Automation ISAPI do Visual FoxPro é acessado do seu navegador Web fornecendo a URL (Universal Resource Locator) do servidor Automation. O navegador Web faz uma solicitação HTTP que é passada ao Microsoft IIS ou ao Microsoft Personal Web Server. O servidor Automation passa a solicitação ao Foxisapi.dll, que, por sua vez, passa a solicitação ao seu servidor Automation.

Por exemplo, a URL abaixo acessa o servidor Automation ISAPI chamado FoxWeb.Server:

```foxpro
HTTP://MyServer/Scripts/Foxisapi.dll/FoxWeb.server.Delay?30
```

A tabela a seguir descreve cada um dos elementos do exemplo de URL acima.

| Elemento da URL | Descrição |
| --- | --- |
| Myserver | A pasta virtual do IIS ou do Personal Web Server. |
| Scripts/Foxisapi.dll | A pasta Scripts do IIS ou do Microsoft Personal Web Server e o Foxisapi.dll. |
| FoxWeb.Server | O nome registrado (ProgID) do servidor Automation ISAPI do Visual FoxPro a chamar. Neste exemplo, FoxWeb é o nome do arquivo .exe ou .dll do servidor Automation do Visual FoxPro. Server é o nome da classe especificado na cláusula OLEPUBLIC do comando DEFINE CLASS que cria o servidor Automation. FoxWeb.Server também é o ProgID do servidor Automation conforme armazenado no Registro do Windows. Você pode usar o RegEdit para visualizar ou modificar o ProgID do servidor Automation. |
| Delay | O nome do método a executar no servidor Automation ISAPI do Visual FoxPro. |
| ?30 | Um parâmetro passado ao método. O ponto de interrogação é um delimitador que especifica que um parâmetro segue. Para este método, 30 especifica que a execução é atrasada por 30 segundos. O parâmetro é passado como uma cadeia de caracteres. |

### Passando parâmetros a métodos

O código a seguir é do método Delay em FoxWeb.prg e demonstra a estrutura para métodos executados nos servidores Automation ISAPI do Visual FoxPro.

```foxpro
PROCEDURE Delay
   LPARAMETERS cParm1, cIniFile, nPersistInstance
   *** Your code here ***
   RETURN AnHTMLString
ENDPROC
```

 **cParm1**
Uma cadeia de caracteres passada ao método. No método Delay, este parâmetro especifica o número de segundos que a execução é atrasada.
**cIniFile**
O nome do arquivo .ini (passado ao método pelo Foxisapi.dll) criado cada vez que um servidor Automation ISAPI do Visual FoxPro é acessado. Cada arquivo .ini é criado na pasta Scripts e tem um nome exclusivo que começa com "Fox." Você pode usar a função GetPrivateProfileString em FoxWeb.prg, por exemplo, para ler informações do arquivo .ini e retornar HTML personalizado baseado na configuração de um usuário.
**nPersistInstance**
Especifica se a instância do servidor Automation ISAPI do Visual FoxPro persiste após terminar de executar seu método. nPersistInstance é passado por referência ao método pelo Foxisapi.dll. Se nPersistInstance for definido como 0 no seu aplicativo Web, a instância do servidor Automation permanece ativa após a execução terminar. Se nPersistInstance for um valor diferente de 0, a instância do servidor Automation é liberada. Para desempenho ideal, nPersistInstance deve ser definido como 0; caso contrário, o servidor Automation deve ser iniciado novamente na próxima vez que for chamado.

### Usando Foxisapi.dll para agrupar servidores Automation

Como o Foxisapi.dll é free-threaded, ele agora pode agrupar vários servidores Automation ISAPI do Visual FoxPro para fornecer melhor escalabilidade aos seus aplicativos Web. Servidores Automation ISAPI agrupados permitem que um servidor Automation ISAPI livre atenda a uma solicitação quando outros servidores Automation ISAPI estão ocupados. Para aproveitar o agrupamento de servidores Automation ISAPI, as instâncias dos servidores Automation ISAPI devem ser tornadas persistentes definindo nPersistInstance como 0 no seu aplicativo Web.

O número de servidores Automation ISAPI disponíveis para atender solicitações é determinado pelas configurações no arquivo de inicialização Foxisapi.ini. Para criar um pool de vários servidores Automation ISAPI, inclua uma entrada entre colchetes com o nome do servidor Automation ISAPI para o qual um pool é criado. Esta entrada é seguida por uma lista de servidores Automation ISAPI que compõem o pool, com um valor numérico que especifica o número máximo de instâncias de cada servidor Automation ISAPI que pode ser criado.

Por exemplo, colocar as seguintes linhas em Foxisap.ini cria um pool de sete servidores Automation ISAPI para solicitações de serviço a FoxWeb.myserver. O Foxisapi.dll cria até quatro instâncias do servidor Automation ISAPI FoxWeb.server e até três instâncias do servidor Automation ISAPI FoxWeb2.server para atender solicitações.

```foxpro
[FOXWEB.MYSERVER]
FOXWEB.SERVER=4
FOXWEB2.SERVER=3
```

A URL a seguir executa o método Delay em uma instância do FoxWeb.server ou do FoxWeb2.server servidores Automation ISAPI:

```foxpro
HTTP://MyServer/Scripts/Foxisapi.dll/FoxWeb.Myserver.Delay?30
```

O Foxisapi.ini pode especificar que os servidores Automation ISAPI sejam instanciados antecipadamente antes de uma solicitação de serviço ser recebida. Para fazer isso, adicione uma vírgula seguida de um asterisco (*) após o número de instâncias, conforme mostrado no exemplo a seguir.

```foxpro
[FOXWEB.MYSERVER]
FOXWEB.SERVER=4,*
FOXWEB2.SERVER=3,*
```

### Usando o Pool Manager em várias máquinas

O Foxisapi.dll fornece a capacidade de gerenciar servidores Automation ISAPI do Visual FoxPro em várias máquinas. Você pode usar Remote Automation ou DCOM (Distributed Component Object Model) para acessar os servidores Automation ISAPI. Observe que, para desempenho e escalabilidade ideais, as instâncias dos servidores Automation ISAPI devem ser tornadas persistentes definindo nPersistInstance como 0 no seu aplicativo Web.

O exemplo a seguir descreve um cenário em que dois servidores Automation ISAPI do Visual FoxPro, FoxWeb e FoxWeb2, são colocados em duas máquinas.

Machine_A é sua máquina local executando Windows 98, DCOM e Personal Web Server. Machine_B é sua máquina remota, acessível pela rede, executando Windows 2000 e DCOM.
 - Machine_A é sua máquina de desenvolvimento Visual FoxPro na qual você instalou as amostras de servidor Automation FoxISAPI do Visual FoxPro. Nesta máquina, abra o projeto FoxWeb no Project Manager do Visual FoxPro e escolha Build para criar um servidor Automation ISAPI como arquivo .exe out-of-process. Compilar o .exe registra automaticamente o servidor Automation ISAPI na máquina como FoxWeb.exe. Agora abra o projeto FoxWeb2 no Project Manager do Visual FoxPro e escolha Build para criar e registrar outro servidor Automation ISAPI como arquivo .exe.
- Para verificar se os servidores Automation ISAPI FoxWeb e FoxWeb2 estão registrados corretamente, você pode usar o RegEdit e pesquisar por FoxWeb e FoxWeb2. Observe que os ProgIDs dos servidores são FoxWeb.Server e FoxWeb2.Server, respectivamente. Server é o nome da classe especificado na cláusula OLEPUBLIC do comando DEFINE CLASS que cria o servidor Automation ISAPI. FoxWeb.prg é o aplicativo Internet Visual FoxPro incluído nos projetos FoxWeb e FoxWeb2. Os ProgIDs dos servidores Automation ISAPI apontam para Machine_A, a máquina local. As configurações do Registro para o servidor Automation ISAPI FoxWeb2 precisam ser alteradas para apontar para Machine_B, a máquina remota.
- Agora copie os arquivos FoxWeb2.exe, FoxWeb2.vbr e FoxWeb2.tlb de Machine_A, a máquina local, para Machine_B, a máquina remota.
- Use a opção /RegServer para registrar FoxWeb2.exe em Machine_B no prompt MS-DOS: C:\VFP\FOXWEB2.EXE /RegServer
- Por fim, pare e reinicie o Personal Web Server em Machine_A para garantir que ele reconheça as alterações no Registro.

Você pode executar o comando Status no Foxisapi.dll para verificar o status de todos os servidores Automation ISAPI registrados no Foxisapi.ini. A URL a seguir executa o comando Status:

```foxpro
HTTP://Machine_A/Scripts/FoxISAPI.dll/Status
```

Você pode executar o comando Reset no Foxisapi.dll para redefinir todos os servidores Automation ISAPI registrados no Foxisapi.ini. O comando Reset libera todas as instâncias de servidores Automation ISAPI. A URL a seguir executa o comando Reset:

```foxpro
HTTP://Machine_A/Scripts/FoxISAPI.dll/Reset
```

Para testar a instalação, você pode abrir tantas instâncias do seu navegador Web quanto houver servidores Automation ISAPI no pool. Os navegadores Web podem estar em várias máquinas conectadas à sua rede. Você pode então chamar o método Delay na URL de cada navegador Web para que o Foxisapi.dll encaminhe solicitações de serviço aos outros servidores Automation ISAPI livres. Após o método Delay ser executado de cada navegador Web, você pode usar o método Status para verificar se todos os servidores Automation ISAPI no pool receberam solicitações de serviço.

### Usando FoxISAPI com servidores DLL

Se você usa FoxISAPI com servidores in-process multithreaded na versão anterior do Visual FoxPro, precisa desabilitar o suporte ao Pool Manager no FoxISAPI. Você pode fazer isso usando a configuração PoolMode no arquivo FoxIsapi.ini. A configuração PoolMode é global para todos os servidores, portanto recomendamos que você não deixe um único FoxIsapi.dll atender servidores EXE e DLL. Em vez disso, copie e renomeie os arquivos FoxIsapi.dll e FoxIsapi.ini para ter um conjunto para servidores EXE e outro para servidores DLL.

### Depurando seus servidores Automation ISAPI

O FoxIsapi.dll também permite depurar seus servidores Automation ISAPI na sua máquina local. Defina o número de instâncias do servidor Automation ISAPI que deseja depurar como 0, conforme mostrado no exemplo de arquivo FoxIsapi.ini a seguir:

```foxpro
[FOXWEB.MYSERVER]
FOXWEB.SERVER=0
```

O arquivo de programa Odebug.prg deve estar presente na pasta raiz do Visual FoxPro e os arquivos-fonte do servidor Automation ISAPI devem estar presentes. Certifique-se de que o servidor Automation ISAPI que deseja depurar esteja configurado como servidor Automation ISAPI persistente e que as informações de depuração estejam ativadas no projeto que contém os arquivos-fonte do servidor Automation ISAPI.

Quando o servidor Automation ISAPI é instanciado, o Foxisapi.dll inicia o Visual FoxPro para depuração, permitindo definir pontos de interrupção, rastrear o código e assim por diante.

# Comandos Foxisapi.dll

O Foxisapi.dll tem comandos que você pode chamar para determinar o status dos seus servidores Automation ISAPI e redefinir os servidores. A tabela a seguir lista os comandos Foxisapi.dll com uma descrição de cada um.

| Comando | Descrição |
| --- | --- |
| MultiMode | Executa o comando Reset e limita o número de instâncias de servidores Automation ISAPI aos valores especificados em Foxisapi.ini. |
| PoolMode | Habilita ou desabilita o suporte ao Pool Manager no FoxISAPI. Use este comando para desativar o Pool Manager para servidores DLL in-process. 0 – desabilita 1 - habilita (padrão) |
| Reset | Libera todas as instâncias dos servidores Automation ISAPI. |
| SingleMode | Executa o comando Reset e limita o número de instâncias de servidores Automation ISAPI a uma instância. Execute este comando para realizar manutenção; por exemplo, você pode abrir tabelas exclusivamente quando SingleMode estiver em vigor. |
| Status | Exibe o status atual dos servidores Automation ISAPI, as configurações do Foxisapi.ini e se SingleMode ou MultiMode está em vigor. |

Cada um dos comandos Foxisapi.dll é chamado por uma URL especificada em Foxisapi.ini. A seguir está o conteúdo do arquivo Foxisapi.ini de amostra com as URLs padrão:

```foxpro
[FOXISAPI]
StatusURL = Status
ResetURL = Reset
SingleModeURL = SingleMode
MultiModeURL = MultiMode
```

A URL a seguir executa o comando Status:

```foxpro
HTTP://MyServer/Scripts/Foxisapi.dll/Status
```

No arquivo Foxisapi.ini de amostra a seguir, a URL do comando Status é alterada de Status para MyStatus:

```foxpro
[FOXISAPI]
StatusURL = MyStatus
ResetURL = Reset
SingleModeURL = MSingleMode
MultiModeURL = MultiMode
```

Após esta alteração em Foxisapi.ini, a URL a seguir executa o comando Status:

```foxpro
HTTP://MyServer/Scripts/FoxISAPI.dll/MyStatus
```

> **Observação:** Você deve redefinir o Foxisapi.dll com o comando Reset após fazer alterações no arquivo Foxisapi.ini para que as alterações entrem em vigor.

# Configurações adicionais do FoxISAPI.ini

O Foxisapi.dll lê Foxisapi.ini e configura suas definições conforme os itens contidos em Foxisapi.ini. A tabela a seguir descreve cada um dos itens adicionais que você pode colocar no arquivo Foxisapi.ini.

| Item | Descrição |
| --- | --- |
| AutoRefreshStatus | Especifica o número de segundos entre atualizações da página Status. O padrão é 0 segundos (a página Status não é atualizada) se este item for omitido ou se Foxisapi.ini não estiver presente. |
| BusyTimeout | Especifica o número de segundos que o Foxisapi.dll aguarda os servidores de aplicativo Visual FoxPro responderem antes de uma mensagem de tempo limite ser gerada. O padrão é 2 segundos se este item for omitido ou se Foxisapi.ini não estiver presente. |
| ReleaseTimeout | Especifica o número de segundos que o Foxisapi.dll aguarda um servidor de aplicativo Visual FoxPro ocupado responder antes do comando Reset ser executado. O padrão é 2 segundos se este item for omitido ou se Foxisapi.ini não estiver presente. |

O seguinte é retirado do arquivo Foxisapi.ini de amostra e demonstra os formatos dos itens adicionais que você pode colocar no arquivo:

```foxpro
[FOXISAPI]
BusyTimeout = 5
ReleaseTimeout = 15
```

> **Observação:** Você deve redefinir o Foxisapi.dll com o comando Reset após fazer alterações no arquivo Foxisapi.ini para que as alterações entrem em vigor.

# Dicas de configuração para o Microsoft Internet Information Services (IIS)

Duas entradas de registro do Microsoft IIS, PoolThreadLimit e ThreadTimeout, podem ser adicionadas ao seu registro para melhorar o desempenho com os servidores Automation FoxISAPI do Visual FoxPro. Essas entradas de registro determinam o número total de threads que o Internet Information Services pode criar e o tempo de existência das threads. Para mais informações sobre essas entradas de registro, consulte a documentação do Internet Information Services.

Um artigo da Microsoft Knowledge Base intitulado "How to Launch Automation servers from ISAPI Extensions" (número Q156223) está disponível em www.microsoft.com. Este artigo fornece informações sobre as permissões de segurança de acesso necessárias para iniciar servidores Automation como os servidores Automation ISAPI do Visual FoxPro.
