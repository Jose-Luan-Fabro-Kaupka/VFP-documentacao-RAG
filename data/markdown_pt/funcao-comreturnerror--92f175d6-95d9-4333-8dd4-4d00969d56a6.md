# Função COMRETURNERROR( )

Preenche a estrutura de exceção COM com informações que clientes Automation podem usar para determinar a origem de erros de Automation.

```foxpro
COMRETURNERROR(cExceptionSource, cExceptionText)
```

#### Parâmetros
 **cExceptionSource**
Especifica o texto para a origem da exceção.
**cExceptionText**
Especifica o texto para a descrição da exceção.

# Observações

COMRETURNERROR( ) permite que servidores Automation do Visual FoxPro preencham a estrutura de exceção COM para que clientes Automation possam determinar a causa de um erro no servidor Automation.

Executar COMRETURNERROR( ) coloca o texto especificado na estrutura de exceção COM, aborta a execução do método atual e retorna o controle ao cliente. O servidor Automation permanece na memória e o cliente pode chamar mais métodos do servidor Automation.

Clientes do Visual FoxPro podem usar AERROR( ) para visualizar o texto colocado na estrutura de exceção COM.

> **Observação:** (Para usuários avançados) COMReturnErrorInfo preenche uma estrutura de informações de exceção COM. Isso é usado apenas para IDispatch (chamadas de late binding). Se você chamar o servidor via early binding e o cliente passar uma estrutura de exceção COM ao servidor, não há mecanismo de erro para retornar as informações de erro, a menos que o cliente faça um QueryInterface na interface ISupportsErrorInfo.
