# Função BITRSHIFT( )

Move bits em um valor numérico para a direita pelo número especificado de posições e retorna o valor resultante.

> **Observação:** Se as expressões especificadas não forem inteiros, elas são convertidas em inteiros antes de executar a operação.

```foxpro
BITRSHIFT(nExpression1, nExpression2)
```

#### Parâmetros
 **nExpression1**
Especifica o valor numérico no qual mover bits para a direita.
**nExpression2**
Especifica o número de posições de bit a mover para a direita.

# Valor de retorno

Numérico. BITRSHIFT( ) retorna a expressão especificada com bits movidos pelo número especificado de posições.

# Observações

BITRSHIFT( ) não suporta valores Varbinary.

# Exemplo

```foxpro
x = 5  && 0101 binary
y = 1  && Shift bits 1 position right
? BITRSHIFT(x,y) && Returns 2, 0010 binary
```
