# Procedimentos e funções definidos pelo usuário

Definir rotinas e operações usadas com frequência como procedures e functions separadas pode reduzir o tamanho e a complexidade do programa, tornando o código mais fácil de ler e manter. Por exemplo, você precisa fazer alterações apenas uma vez na procedure ou function em vez de várias vezes ao longo do programa. Procedures e functions permitem manter código usado com frequência em um único local para que você possa chamá-lo de diferentes partes do aplicativo.

Convencionalmente, uma procedure contém código que executa uma operação, enquanto uma function contém código que executa operações e retorna um valor específico. A maioria, senão todas, as funções nativas do Visual FoxPro retornam valores. No Visual FoxPro, tanto procedures quanto functions podem retornar valores. Ao criar procedures e functions, você pode escolher se seguirá a convenção de retornar um valor apenas de functions.

Por exemplo, as linhas de código a seguir ilustram a forma básica de uma procedure e uma function:

```foxpro
PROCEDURE myProcedure
   * Insert procedure code.
ENDPROC
FUNCTION myFunction
 * Insert function code.
  RETURN myFuncReturnValue
ENDFUNC
```

Em suas formas básicas, procedures e functions podem não parecer úteis ou diferentes umas das outras. No entanto, procedures e functions também podem aceitar e processar dados que o programa chamador passa a elas por meio de parâmetros, que você pode incluir como parte das definições e chamadas de procedure e function. Dados passados a procedures e functions são às vezes chamados de "arguments". Procedures e functions também diferem na forma como os programas passam dados a elas por padrão. Para obter mais informações, consulte Parameters in Procedures and Functions.

Functions que você cria no Visual FoxPro são às vezes chamadas de user-defined functions (UDFs). Você pode incluir procedures ou functions com outro código executável normal em um arquivo de programa (.prg) ou isoladamente em um arquivo .prg separado.

> **Observação:** Se você incluir procedures e functions com outro código, elas devem existir no final do arquivo .prg, após todo o outro código normal. Você não pode incluir código executável normal de programa após procedures e functions em um arquivo .prg. Apenas outras procedures, functions e definições de classe definidas pelo usuário podem seguir a primeira instrução PROCEDURE ou FUNCTION no arquivo.
