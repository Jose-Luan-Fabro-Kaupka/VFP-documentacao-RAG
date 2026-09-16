# Prioridade de Tratamento de Erros

O Visual FoxPro fornece vários tratadores de erros que você pode usar para detectar e tratar erros no código.

> **Cuidado:** O uso de declarações TRY...CATCH em um método cuja definição de classe não possui código de evento ou método Error pode impactar código existente e possivelmente quebrar a compatibilidade com versões anteriores. Portanto, declarações TRY...CATCH em métodos devem chamar apenas outros métodos de objeto que contenham código de evento ou método Error.

A tabela a seguir resume a prioridade dos tratadores de erros.

| Quando apenas o seguinte tratador de erros existe | Prioridade do tratador de erros |
| --- | --- |
| Nenhum ou nenhum tratador de erros existente pode tratar o erro | Mensagem de erro do sistema Visual FoxPro |
| Comando ON ERROR | ON ERROR tem precedência até que outro ON ERROR seja chamado ou o sistema de mensagens de erro do Visual FoxPro seja restaurado. Caso contrário, o Visual FoxPro exibe uma mensagem de erro do sistema. |
| Comando TRY...CATCH...FINALLY | TRY...CATCH...FINALLY tem precedência quando um erro ocorre no bloco TRY. Caso contrário, o Visual FoxPro exibe uma mensagem de erro do sistema. |
| Evento ou método Error | Error tem precedência quando um erro ocorre no código de método de um objeto. Caso contrário, o Visual FoxPro exibe uma mensagem de erro do sistema. |
| Comando TRY...CATCH...FINALLY Comando ON ERROR | TRY...CATCH...FINALLY tem precedência quando um erro ocorre em um bloco TRY. ON ERROR tem precedência quando: Um erro ocorre fora do bloco TRY. Um erro ocorre no bloco CATCH. Um erro ocorre no bloco FINALLY. Caso contrário, o Visual FoxPro exibe uma mensagem de erro do sistema. |
| Evento ou método Error Comando ON ERROR | Error tem precedência quando um erro ocorre no código de método de objeto. ON ERROR tem precedência quando: Um erro ocorre fora de uma definição de classe. Um erro ocorre dentro de uma definição de classe, mas fora do código de método. O erro é detectado no ponto de instanciação do objeto. Caso contrário, o Visual FoxPro exibe uma mensagem de erro do sistema. |
| Comando TRY...CATCH...FINALLY Evento ou método Error | TRY...CATCH...FINALLY tem precedência quando: Um erro ocorre em um bloco TRY fora de uma definição de classe. Um erro ocorre dentro do código de método de um objeto e está dentro de um bloco TRY. Um erro se origina em uma definição de classe fora do código de método, mas ocorre em um bloco TRY fora da definição de classe. Um erro ocorre em um bloco TRY dentro de código de procedimento externo ou método de objeto, e o método ou procedimento é chamado diretamente ou de outro método, independentemente de a chamada de método aparecer dentro ou fora de um bloco TRY. Error tem precedência quando: Um erro ocorre dentro do código de método, mas fora de um bloco TRY. Um erro ocorre no código de método de um objeto, e o método é chamado diretamente ou é chamado de outro método, independentemente de a chamada de método aparecer dentro ou fora de um bloco TRY. Observação Se a chamada de método estiver em um bloco TRY, e não existir código de evento ou método Error imediato para o objeto, o Visual FoxPro pesquisa código Error herdado da classe pai ou de outra classe na hierarquia de classes. Se nenhum código Error existir na hierarquia de classes, o Visual FoxPro procura um bloco CATCH correspondente ao bloco TRY do qual o método foi chamado. Caso contrário, o Visual FoxPro exibe uma mensagem de erro do sistema. |

# Resumo do Tratamento de Erros no Código de Método de Objeto

Para erros que ocorrem no código de método de um objeto, a ordem de prioridade para tratadores de erros é resumida da seguinte forma:
 - TRY...CATCH imediato, se existir, no mesmo método em que o erro ocorre. Isso também se aplica a procedimentos externos que um método chama.
- Evento Error, se existir, para o objeto.
- TRY...CATCH no próximo nível acima na cadeia de chamadas ou em um método de nível superior.
- Rotina ON ERROR, se existir.
- Mensagem de erro do sistema Visual FoxPro.

Para obter mais informações sobre prioridade de tratamento de erros em estruturas TRY...CATCH...FINALLY, consulte Prioridade de Tratamento de Erros em Estruturas TRY...CATCH...FINALLY. Para obter mais informações sobre prioridade de tratamento de erros em classes e objetos, consulte Prioridade de Tratamento de Erros em Classes e Objetos.

# Prioridade de Tratamento de Erros em Estruturas TRY...CATCH...FINALLY

A tabela a seguir resume a sequência de ações ao tratar erros ou comandos THROW no bloco TRY de uma estrutura TRY...CATCH...FINALLY.

| Quando os seguintes tratadores de erros existem e um erro ocorre no primeiro bloco de código listado | Sequência de ações |
| --- | --- |
| Nenhum | Exibir mensagem de erro do sistema Visual FoxPro apropriada. |
| Bloco de código CATCH | Bloco de código CATCH trata o erro. |
| Bloco de código CATCH Bloco de código FINALLY | Bloco de código CATCH trata o erro. Bloco de código FINALLY é executado. |
| Bloco de código CATCH interno Bloco de código FINALLY interno Estrutura TRY externa | Bloco de código CATCH interno trata o erro. Bloco de código FINALLY interno é executado. Bloco de código FINALLY externo é executado. Se nenhum bloco de código CATCH interno existir, bloco de código FINALLY interno é executado, bloco de código CATCH externo trata o erro, e bloco de código FINALLY externo é executado. |
| Bloco de código CATCH Bloco de código FINALLY Comando ON ERROR | Bloco de código CATCH trata o erro. Bloco de código FINALLY é executado. Comando ON ERROR é executado. Se nenhum bloco de código CATCH existir, bloco de código FINALLY é executado, e ON ERROR trata o erro. |
| Bloco de código CATCH Bloco de código FINALLY Bloco de código Error | Bloco de código CATCH trata o erro. Bloco de código FINALLY é executado. Evento Error é executado. Se nenhum bloco de código CATCH existir, bloco de código FINALLY é executado, e o evento Error trata o erro. |

Para obter informações sobre como estruturas TRY...CATCH...FINALLY tratam erros, consulte Tratamento Estruturado de Erros.

# Prioridade de Tratamento de Erros em Classes e Objetos

Quando um erro ocorre no código de método de um objeto, e o método é chamado diretamente ou do bloco TRY de uma estrutura TRY...CATCH...FINALLY, o Visual FoxPro segue o procedimento de tratamento de erros para esse objeto específico. Este protocolo torna possível manter o encapsulamento e o controle de seus componentes. Normalmente, o evento Error do objeto, se existir, tem precedência sobre outros tratadores de erros, a menos que o código de método do objeto contenha sua própria estrutura TRY...CATCH...FINALLY.

Para obter mais informações sobre tratamento de erros para classes e objetos, consulte Tratamento de Erros de Classe e Objeto.

### Exemplos de Prioridade de Tratamento de Erros para Código de Método de Objeto

No exemplo a seguir, em que a classe contém um evento Error, o código instancia um objeto de uma classe personalizada chamada MyObjectClass, que define dois métodos que contêm blocos TRY...CATCH, um método que contém um erro e um evento Error. O objeto então chama dois dos métodos definidos.

O bloco TRY em Method1 contém uma chamada ao método personalizado RaiseError, que gera um erro. No entanto, o bloco CATCH em Method1 não trata este erro; em vez disso, o código no evento Error da classe trata este erro e exibe a mensagem especificada. Se o evento Error não existisse, o bloco CATCH em Method1 exibiria a mensagem especificada.

Em contraste, quando um erro ocorre antes do bloco TRY em Method2, o evento Error trata este erro exibindo a mensagem especificada. Quando um segundo erro ocorre no bloco TRY em Method2, o bloco CATCH trata o segundo erro e exibe a mensagem especificada.

```foxpro
CLEAR
oMyObject = CREATEOBJECT("MyClass")
oMyObject.Method1()
?
oMyObject.Method2()
DEFINE CLASS MyClass AS Custom
   PROCEDURE Method1
      ? "Method1"
      TRY
         ? "Calling RaiseError method in TRY block for Method1."
         This.RaiseError()
      CATCH
         ? "Entered CATCH block for Method1. Caught error."
      ENDTRY
   ENDPROC
   PROCEDURE Method2
      ? "Method2"
      ? "Generating an error before TRY block in Method2."
      ERROR 1
      TRY
         ? "Generating an error in TRY block for Method2."
         ERROR 1
      CATCH
         ? "Entered CATCH block for Method2. Caught error."
      ENDTRY
   ENDPROC
   PROCEDURE RaiseError
      ? "Entered RaiseError method. Generating an error."
      ERROR 1
   ENDPROC
   PROCEDURE Error(t1,t2,t3)
      ? "Error event for MyObjectClass occurred."
   ENDPROC
ENDDEFINE
```

No exemplo a seguir, em que a classe não contém um evento Error, o código instancia um objeto de uma classe personalizada chamada MyClass, que define dois métodos: o primeiro contém um bloco TRY...CATCH enquanto o segundo não.

O bloco TRY em myMethod1 contém uma chamada a myMethod2, que gera um erro. O bloco CATCH em Method1 trata este erro e exibe informações para o erro do Visual FoxPro gerado.

No entanto, se o exemplo chamasse myMethod2 diretamente, por exemplo, seguindo `oMyObject.myMethod1()` com `oMyObject.myMethod2()`, então a declaração `ON ERROR` `DO errorHandler` precisaria especificar uma rotina funcional chamada errorHandler para tratar o erro em myMethod2. Após tratar o erro, a rotina ON ERROR retorna a execução ao programa para que a declaração seguinte à que contém o erro possa ser executada.

```foxpro
CLEAR
ON ERROR DO errorHandler && Create a functional error handler to test.
oMyObject=CREATEOBJECT("myClass")
oMyObject.myMethod1()
* oMyObject.myMethod2()  && Remove comment character to test this line.
DEFINE CLASS myClass AS Custom
   PROCEDURE myMethod1
      ? "myMethod1"
      TRY
         ? "Calling myMethod2 in TRY block for myMethod1."
         THIS.myMethod2()
      CATCH TO omyError
         ? "Entered CATCH block for myMethod1. Caught: ", ;
            omyError.ErrorNo, " ", omyError.Message
      ENDTRY
   ENDPROC
   PROCEDURE myMethod2
      ?
      ? "myMethod2"
      ? "Generating an error in myMethod2."
      x=y         && Variable y does not exist. CATCH handles this error.
      ? "This line displays if CATCH does not handle the preceding error."
   ENDPROC
ENDDEFINE
```
