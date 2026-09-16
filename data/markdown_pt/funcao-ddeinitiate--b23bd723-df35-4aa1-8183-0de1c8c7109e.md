# Função DDEInitiate( )

Estabelece um canal de troca dinâmica de dados (DDE) entre o Visual FoxPro e outro aplicativo baseado no Microsoft Windows.

```foxpro
DDEInitiate(cServiceName, cTopicName)
```

#### Parâmetros
 **cServiceName**
Especifica o nome do serviço do aplicativo servidor, que, na maioria dos casos, é o nome do arquivo executável sem sua extensão. O nome de serviço padrão para o Visual FoxPro é Visual FoxPro. Se você estiver estabelecendo um canal para o Microsoft Excel, cServiceName é Excel.
**cTopicName**
Especifica o nome do tópico. O tópico é específico do aplicativo e deve ser compreendido pelo aplicativo. Por exemplo, um tópico fornecido pela maioria dos servidores DDE é o tópico System. Consulte a documentação do aplicativo para os nomes de serviço e tópico suportados pelo aplicativo.

# Valor de retorno

Numérico

# Observações

DDEInitiate( ) estabelece um canal DDE entre o Visual FoxPro e um aplicativo servidor DDE. Depois que um canal é estabelecido, o Visual FoxPro pode solicitar dados do servidor referenciando o canal em funções DDE subsequentes. O Visual FoxPro atua como cliente, solicitando dados do aplicativo servidor através do canal.

Se o canal for estabelecido com sucesso, DDEInitiate( ) retorna o número do canal. Os números de canal são não negativos, e o número de canais que você pode estabelecer é limitado apenas pelos recursos do seu sistema.

DDEInitiate( ) retorna –1 se o canal não puder ser estabelecido. Se o aplicativo servidor não estiver aberto, o Visual FoxPro pergunta se você deseja abri-lo. Se você escolher Yes, o Visual FoxPro tenta abrir o aplicativo. (Você pode usar DDELastError( ) para determinar por que um canal não pode ser estabelecido.)

Para evitar ser perguntado se deseja abrir o aplicativo, defina a opção SAFETY de DDESetOption( ). Você também pode usar RUN com a opção /N para iniciar o aplicativo.

Um canal pode ser fechado com DDETerminate( ).

# Exemplo

O exemplo a seguir usa DDEInitiate( ) para estabelecer um canal DDE entre o Visual FoxPro e uma planilha do Microsoft Excel chamada Sheet1. 'Excel' é o nome do serviço e 'Sheet1' é o nome do tópico. O número do canal é armazenado na variável de memória `mchannum` para uso em funções DDE subsequentes.

```foxpro
mchannum = DDEInitiate('Excel', 'Sheet1')
IF mchannum != -1
   * Process client actions
   = DDETerminate(mchannum)  && Close the channel
ENDIF
```
