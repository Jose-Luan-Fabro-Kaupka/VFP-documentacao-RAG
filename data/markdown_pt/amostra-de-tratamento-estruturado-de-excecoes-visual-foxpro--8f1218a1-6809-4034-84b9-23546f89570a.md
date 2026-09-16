# Amostra de tratamento estruturado de exceções (Visual FoxPro)

Arquivo: ...\Samples\Solution\Toledo\TryCatch.scx

Você pode implementar tratamento estruturado de exceções usando a estrutura de tratamento de erros TRY...CATCH...FINALLY para executar um bloco específico de instruções se uma exceção especificada ocorrer quando seu programa é executado. Quando um erro, ou exceção, ocorre, um objeto Exception é criado.

Esta amostra demonstra como capturar exceções usando os blocos TRY e CATCH, limpar recursos usando o bloco FINALLY e lançar, ou escalar, exceções usando uma instrução THROW.

Para obter mais informações, consulte Structured Error Handling, TRY...CATCH...FINALLY Command e Exception Object Properties, Methods, and Events.

# Capturando exceções

Nesta amostra, você pode escolher um erro, ou exceção, que deseja causar no bloco TRY e visualizar as propriedades do objeto Exception gerado pela exceção.

### Para gerar uma exceção
- Na guia CATCHing Exceptions, selecione o erro desejado na lista suspensa e clique em Execute TRY block.

O bloco CATCH é executado e exibe as propriedades do objeto Exception.

O código a seguir mostra a estrutura de tratamento de erros nesta amostra específica. Normalmente, código que pode gerar uma exceção aparece no bloco TRY; no entanto, o comando ERROR é chamado especificamente para mostrar como o fluxo de controle é passado ao bloco CATCH somente quando uma exceção ocorre.

Você pode usar a propriedade UserValue do objeto Exception para armazenar qualquer informação adicional sobre o erro.

```foxpro
TRY
   ERROR nErrorCode
CATCH TO myException
   myException.UserValue = "I can handle this."
ENDTRY
```

# Limpando recursos

O bloco FINALLY geralmente limpa quaisquer recursos alocados pelo bloco TRY e é sempre o último código a ser executado antes que o controle saia da estrutura TRY...CATCH...FINALLY.

### Para observar como FINALLY executa após todo o outro código
- Na guia Using FINALLY, selecione uma opção ou digite um nome de tabela e caminho na caixa de combinação e clique em TRY.

O código a seguir demonstra como FINALLY executa após todo o outro código.

```foxpro
TRY
   lnPrevArea = SELECT()
   USE CUSTOMERS IN 0 EXCLUSIVE
* Handle when file does not exist.
CATCH TO myException WHEN myException.ErrorNo = 1
* Handle when file is in use.
CATCH TO myException WHEN myException.ErrorNo = 3
* Handle when file access is denied.
CATCH TO myException WHEN myException.ErrorNo = 1704
* Catch everything else.
CATCH TO myException
* Code in FINALLY block always executes.
FINALLY
IF USED('CUSTOMERS')
      USE IN CUSTOMERS
   ENDIF
   SELECT (lnPrevArea)
ENDTRY
```

# Lançando exceções

Para escalar uma exceção a um manipulador de erros de nível superior, use uma instrução THROW em um bloco CATCH.

Esta amostra usa blocos TRY aninhados. O bloco TRY interno pode tratar apenas o primeiro erro. Para erros subsequentes, o bloco TRY interno escala o objeto Exception para o bloco TRY externo. Quando uma exceção específica é lançada, especificamente `THROW oMyException` neste exemplo, a propriedade UserValue da exceção capturada no bloco externo contém a exceção lançada do bloco interno.

```foxpro
TRY
   * Run some code.
   TRY
      * Error occurs.
      ERROR 3
      CATCH TO InnerException WHEN InnerException.ErrorNo = 1
      InnerException.UserValue = "INNER TRY: I can handle this."
      CATCH TO InnerException
      InnerException.UserValue = "INNER TRY: I can't handle this."
      * Error cannot be handled so escalate to outer TRY block.
      THROW InnerException
   ENDTRY
CATCH TO OuterException
* In this case, when the exception is escalated, the caught exception's
* UserValue property contains the escalated exception from inner TRY.
? OuterException.UserValue.UserValue
ENDTRY
```

Você também pode lançar uma mensagem de cadeia de caracteres. Neste caso, a mensagem de cadeia de caracteres é armazenada na propriedade UserValue da exceção externa:

```foxpro
TRY
   * Run some code.
   TRY
      * Error occurs.
        ERROR 1
   CATCH
      THROW "INNER TRY: I can't handle this one."
   ENDTRY
CATCH TO OuterException
   ? OuterException.UserValue
ENDTRY
```
