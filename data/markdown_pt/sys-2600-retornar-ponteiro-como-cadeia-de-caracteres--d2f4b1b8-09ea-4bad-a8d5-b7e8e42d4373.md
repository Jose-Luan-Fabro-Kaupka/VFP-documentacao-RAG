# SYS(2600) - Retornar ponteiro como cadeia de caracteres

Interpreta um inteiro como ponteiro para a memória e retorna o conteúdo dessa memória como uma cadeia de caracteres, ou grava novos dados nesse local de memória.

```foxpro
SYS(2600, dwAddress, nLength [, cNewString])
```

#### Parâmetros
 **dwAddress**
Especifica o ponteiro para um endereço de memória. Esse valor é interpretado como um inteiro.
**nLength**
Especifica o número de bytes a serem lidos de dwAddress.
**cNewString**
Especifica um valor a ser retornado para dwAddress.

# Observações

Esta função é destinada apenas a programadores avançados.

# Exemplos

O código a seguir retorna a cadeia de caracteres cRes, que contém os nLen bytes começando em nAddress:

```foxpro
   cRes = SYS(2600, nAddress, nLen)
```

O código a seguir retorna a cadeia de caracteres cRes e também coloca nLen bytes de cSrc em nAddress:

```foxpro
   cRes = SYS(2600, nAddress, nLen, cSrc)
```
