# Função DDEAbortTrans( )

Encerra uma transação de troca dinâmica de dados (DDE) assíncrona.

```foxpro
DDEAbortTrans(nTransactionNumber)
```

#### Parâmetros
 **nTransactionNumber**
Especifica o número da transação retornado por DDEExecute( ), DDEPoke( ) ou DDERequest( ) quando a transação é enviada ao aplicativo servidor.

# Valor de retorno

Lógico

# Observações

Uma transação assíncrona permite que a execução do programa Visual FoxPro continue sem esperar que o aplicativo servidor responda a uma solicitação de dados.

DDEExecute( ), DDEPoke( ) e DDERequest( ) aguardam o período especificado por DDESetOption( ) para que um aplicativo servidor responda, a menos que você especifique uma função definida pelo usuário para executar quando o aplicativo servidor responder. Especificar uma função definida pelo usuário para executar nessas funções cria uma transação assíncrona.

Se DDEAbortTrans( ) for chamado antes que o servidor processe a solicitação, a função definida pelo usuário não será chamada para a transação.

DDEAbortTrans( ) retorna true (.T.) se a transação assíncrona for encerrada com sucesso e retorna false (.F.) se a transação assíncrona não puder ser encerrada. Use DDELastError( ) para determinar por que a transação não pôde ser encerrada.
