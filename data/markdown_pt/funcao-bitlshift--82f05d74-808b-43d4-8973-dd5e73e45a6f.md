# Função BITLSHIFT( )

Move bits em um valor numérico para a esquerda pelo número especificado de posições e retorna o valor resultante.

> **Observação:** Se as expressões especificadas não são inteiros, elas são convertidas para inteiros antes de executar a operação.

```foxpro
BITLSHIFT(nExpression1, nExpression2)
```

#### Parâmetros
 **nExpression1**
Especifica o valor numérico no qual mover bits para a esquerda.
**nExpression2**
Especifica o número de posições de bit a mover para a esquerda.

# Valor de retorno

Numérico. BITLSHIFT( ) retorna a expressão especificada com bits movidos pelo número especificado de posições.

# Observações

BITLSHIFT( ) não suporta valores Varbinary.

# Exemplo

```foxpro
x = 5  && 0101 binary
y = 1  && Shift bits 1 position left
? BITLSHIFT(x,y) && Returns 10, 1010 binary
```
