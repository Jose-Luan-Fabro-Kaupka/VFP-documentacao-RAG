# Comando ON ERROR

Especifica uma expressão válida ou um comando do Visual FoxPro a ser executado quando ocorre um erro no código em tempo de execução.

```foxpro
ON ERROR [Command]
```

#### Parâmetros
 **[ Command ]**
Especifica um comando ou expressão válida do Visual FoxPro a ser executada. Normalmente, ON ERROR usa o comando DO para especificar um procedimento ou programa de tratamento de erros. Para mais informações, consulte DO Command. Para restaurar o manipulador de erros do sistema do Visual FoxPro, use ON ERROR sem argumento.

# Observações

Se o procedimento de tratamento de erros incluir o comando RETRY, o programa executa a linha que causou o erro em vez de continuar na linha imediatamente seguinte. Para mais informações, consulte RETRY Command.

Você não pode aninhar comandos ON ERROR; chamar o comando ON ERROR em um procedimento especificado por um procedimento ON ERROR restaura o manipulador de erros do sistema do Visual FoxPro.

> **Dica:** Se ON ERROR especificar um procedimento, você pode passar o número do erro, a mensagem de erro, o número da linha do programa e o nome do programa ao procedimento incluindo as funções ERROR( ), MESSAGE( ), LINENO( ) e PROGRAM( ). Você pode usar essas informações para determinar e corrigir a causa do erro. Para mais informações, consulte ERROR( ) Function, LINENO( ) Function, MESSAGE( ) Function e PROGRAM( ) Function.

# Exemplo

O exemplo a seguir usa o comando ON ERROR com o comando DO para especificar um procedimento de tratamento de erros chamado errHandler. O comando DO também usa as funções ERROR( ), MESSAGE( ), PROGRAM( ) e LINENO( ) para passar informações adicionais de erro ao procedimento errHandler. O comando USE especifica uma tabela que não existe e gera um erro. O manipulador de erros errHandler é executado quando o erro ocorre e exibe as informações de erro passadas ao errHandler. ON ERROR sem argumentos restaura o manipulador de erros padrão do sistema do Visual FoxPro.

```foxpro
ON ERROR DO errHandler WITH ;
   ERROR(), MESSAGE(), MESSAGE(1), PROGRAM(), LINENO()
USE nodatabase
ON ERROR  && Restores system error handler.
PROCEDURE errHandler
   PARAMETER merror, mess, mess1, mprog, mlineno
   CLEAR
   ? 'Error number: ' + LTRIM(STR(merror))
   ? 'Error message: ' + mess
   ? 'Line of code with error: ' + mess1
   ? 'Line number of error: ' + LTRIM(STR(mlineno))
   ? 'Program with error: ' + mprog
ENDPROC
```
