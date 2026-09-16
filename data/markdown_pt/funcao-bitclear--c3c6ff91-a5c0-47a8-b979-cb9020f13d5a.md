# Função BITCLEAR( )

Limpa o bit especificado em um valor Numeric, Varbinary ou Blob definindo-o como 0 e retorna o valor resultante. Há uma versão numérica e uma versão binária da sintaxe.

> **Observação:** Se a expressão especificada não for um inteiro, ela é convertida em inteiro antes de executar a operação.

```foxpro
BITCLEAR(nNumericExpression1, nNumericExpression2)
```

```foxpro
BITCLEAR(BinaryExpression [, nStartBit [, nBitCount]])
```

#### Parâmetros
 **nNumericExpression1**
Especifica o valor Numeric no qual limpar o bit. Se a expressão não for um inteiro, ela é convertida em inteiro antes de definir o bit.
**nNumericExpression2**
Especifica a posição do bit em nExpression1 a limpar. nExpression2 pode variar de 0 a 31, com 0 localizado como o bit mais à direita.
**BinaryExpression**
Especifica uma expressão Varbinary ou Blob.
**[ nStartBit [, nBitCount ]]**
Especifica um número baseado em zero do primeiro bit para executar a operação como nStartBit e o número de bits para executar a operação como nBitCount . Se você não especificar nStartBit e nBitCount , a operação se aplica a todos os bits na expressão. Se você especificar somente nStartBit , a operação se aplica somente a nStartBit .

# Valor de retorno

Numeric, Varbinary ou Blob. BITCLEAR( ) retorna a expressão especificada sem o bit especificado.

# Exemplo

```foxpro
x = 7  && 0111 binary
y = 1  && 2nd bit position (0 = 1st bit position)
? BITCLEAR(x,y) && Returns 5, 0101 binary
```
