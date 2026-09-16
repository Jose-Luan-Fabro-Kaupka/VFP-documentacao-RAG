# Variáveis (Visual FoxPro)

Uma variável é um local de memória cujo valor pode mudar durante a operação de um programa. Uma variável pode conter um valor de qualquer tipo de dados. Você pode alterar o valor de uma variável a qualquer momento. Esta opção permite monitorar o status de qualquer coisa que muda durante a operação de uma aplicação.

Variáveis existem apenas enquanto uma aplicação está em execução ou na sessão do Visual FoxPro em que são criadas. Para especificar o escopo de uma variável, use as palavras-chave LOCAL Command, PRIVATE Command e PUBLIC Command.

# Criando variáveis

Para criar uma variável, armazene um valor em um elemento nomeado do Visual FoxPro usando o comando STORE Command ou o operador = Command (equal).

# Exemplo

Os exemplos a seguir são instruções de atribuição simples que são funcionalmente equivalentes.

```foxpro
STORE 7 TO nVar
nVar = 7
```

O exemplo a seguir usa uma variável, `nInc`, para manter o valor de um contador de loop. O Visual FoxPro atribui um novo valor à variável durante cada loop.

```foxpro
FOR nInc = 1 TO 10
   ? nInc
ENDFOR
```

O exemplo a seguir usa uma variável, cName, para manter o valor do campo `Firstname` da tabela `Customer`.

```foxpro
USE Customer
STORE Customer.Firstname TO cName
```
