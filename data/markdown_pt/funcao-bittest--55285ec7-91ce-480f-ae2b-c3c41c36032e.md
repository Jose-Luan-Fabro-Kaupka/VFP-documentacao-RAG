# Função BITTEST( )

Determina se um bit específico em um valor Numeric, Varbinary ou Blob está definido como 1. Há uma versão numérica e uma versão binária da sintaxe.

> **Observação:** Se a expressão especificada não é um inteiro, ela é convertida para inteiro antes de executar a operação.

```foxpro
BITTEST(nNumericExpression1, nNumericExpression2)
```

```foxpro
BITTEST(BinaryExpression, nBitNumber)
```

#### Parâmetros
 **nNumericExpression1**
Especifica o valor Numeric a ser verificado para o bit especificado.
**nNumericExpression2**
Especifica a posição do bit em nExpression1 a ser verificada. nExpression2 pode variar de 0 a 31, com 0 como o bit mais à direita.
**BinaryExpression**
Especifica uma expressão Varbinary ou Blob a ser verificada para o bit especificado.
**nBitNumber**
Especifica um bit com base zero em qExpression . Se nBitNumber estiver fora do intervalo de qExpression , o Visual FoxPro gera um erro.

# Valor de retorno

Lógico. BITTEST( ) retorna True (.T.) se o bit especificado estiver definido como 1; caso contrário, retorna False (.F.).

# Exemplo

O exemplo a seguir usa BITTEST( ) para determinar se uma série de inteiros são pares. Se um inteiro é par, a função `IsEven` retorna True (.T.); caso contrário, retorna False (.F.).

```foxpro
CLEAR
? '2 even? '
?? IsEven(2)  && Even, .T. returned
? '3 even? '
?? IsEven(3)  && Not even, .F. returned
? '0 even? '
?? IsEven(0)  && Even, .T. returned
? '-13 even? '
?? IsEven(-13)  && Not even, .F. returned
Function IsEven
   PARAMETER nInteger
   RETURN NOT BITTEST(nInteger, 0)
```
