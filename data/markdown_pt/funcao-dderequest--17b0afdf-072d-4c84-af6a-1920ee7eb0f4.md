# Função DDERequest( )

Solicita dados de um aplicativo servidor em uma conversa de troca dinâmica de dados (DDE).

```foxpro
DDERequest(nChannelNumber, cItemName [, cDataFormat [, cUDFName]])
```

#### Parâmetros
 **nChannelNumber**
Especifica o número do canal do aplicativo servidor.
**cItemName**
Especifica o nome do item. O nome do item é específico do aplicativo e deve ser compreendido pelo aplicativo. Por exemplo, o Microsoft Excel usa notação de linha e coluna para referenciar células em uma planilha. O nome do item R1C1 designa a célula na primeira linha e primeira coluna da planilha.
**cDataFormat**
Especifica um formato para os dados solicitados. O formato padrão é CF_TEXT. Neste formato, os campos são delimitados com tabulações e os registros são delimitados com um retorno de carro e uma quebra de linha.
**cUDFName**
Permite uma transferência de dados assíncrona. Se você omitir cUDFName, o Visual FoxPro aguarda os dados do servidor pelo período especificado com DDESetOption( ). Se você especificar o nome de uma função definida pelo usuário com cUDFName, o Visual FoxPro continua a execução do programa imediatamente após a solicitação ser feita. Quando os dados estão disponíveis do aplicativo servidor, a função definida pelo usuário especificada com cUDFName é executada. A função definida pelo usuário recebe seis parâmetros nesta ordem: Parâmetro Conteúdo Número do Canal O número do canal do aplicativo servidor. Ação XACTCOMPLETE (transação bem-sucedida).XACTFAIL (transação com falha). Item O nome do item; por exemplo, R1C1 para uma célula de planilha do Microsoft Excel. Dados Os novos dados (REQUEST) ou dados passados (POKE ou EXECUTED). Formato O formato dos dados; por exemplo, CF_TEXT. Número da Transação O número da transação retornado por DDERequest( ). Use DDEAbortTrans( ) para cancelar uma transação não concluída. Se a transação falhar, você pode usar DDELastError( ) para determinar por que falhou. Quando você inclui cUDFName, DDERequest( ) retorna um número de transação maior ou igual a 0 se bem-sucedido, ou –1 se ocorrer um erro.

# Valor de retorno

Character

# Observações

Antes de solicitar dados usando DDERequest( ), você deve estabelecer um canal para o aplicativo servidor com DDEInitiate( ).

Se a solicitação de dados for bem-sucedida, DDERequest( ) retorna os dados como uma cadeia de caracteres. Se a solicitação falhar, DDERequest( ) retorna uma cadeia de caracteres vazia e DDELastError( ) retorna um valor diferente de zero. Se você incluir a função definida pelo usuário assíncrona cUDFName, DDERequest( ) retorna um número de transação se bem-sucedido, ou –1 se ocorrer um erro.

# Exemplo

O exemplo a seguir usa DDEInitiate( ) para estabelecer um canal DDE entre o Visual FoxPro e uma planilha do Microsoft Excel chamada Sheet1. 'Excel' é o nome do serviço, e 'Sheet1' é o nome do tópico. O número do canal é armazenado na variável de memória `mchannum` para uso em funções DDE subsequentes.

DDERequest( ) solicita o nome do item R1C1, os dados na primeira linha e coluna da planilha Sheet1.

```foxpro
mchannum = DDEInitiate('Excel', 'Sheet1')
IF mchannum != -1
   mrequest = DDERequest(mchannum, 'R1C1')
   IF !EMPTY(mrequest) AND DDELastError() = 0      && Successful
      WAIT WINDOW 'R1C1 contents: ' + mrequest
   ENDIF
   = DDETerminate(mchannum)            && Close the channel
ENDIF
```
