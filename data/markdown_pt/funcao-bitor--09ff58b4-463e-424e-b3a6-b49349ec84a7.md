# Função BITOR( )

Executa uma operação OR inclusiva bit a bit em dois ou mais valores dos tipos Numeric, Varbinary ou Blob e retorna o resultado. Há uma versão numérica e uma binária da sintaxe.

```foxpro
BITOR(nNumericExpression1, nNumericExpression2, ... , nNumericExpression26)
```

```foxpro
BITOR(BinaryExpression1, BinaryExpression2, ... , BinaryExpression26)
```

#### Parâmetros
 **nNumericExpression1 , nNumericExpression2, ... , nNumericExpression26**
Especifica valores Numeric nos quais executar a operação OR inclusiva bit a bit.
**BinaryExpression1 , BinaryExpression2, ... , BinaryExpression26**
Especifica valores Varbinary ou Blob nos quais executar a operação. Observação Você pode especificar no máximo 26 valores. Todos devem ter o mesmo tipo. Se as expressões não forem inteiros, serão convertidas em inteiros antes da operação.

# Valor de retorno

Numeric ou Varbinary. BITOR( ) retorna o resultado da operação OR inclusiva bit a bit nas expressões especificadas.

> **Observação:** Para valores Varbinary ou Blob, o valor de retorno é calculado como se todos os valores fossem preenchidos com 0h00 à direita até o comprimento do maior valor. Em seguida, a operação apropriada é executada entre eles.

# Observações

BITOR( ) compara cada bit de eExpressionN ao bit correspondente de eExpressionN+1. Se qualquer um dos bits for 1, o bit correspondente do resultado será definido como 1; caso contrário, será 0.

A tabela a seguir mostra o resultado de uma operação OR inclusiva nos bits correspondentes:

| Bit de eExpressionN | Bit de eExpressionN+1 | Bit resultante |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

# Exemplo

```foxpro
x = 5  && 0101 binary
y = 6  && 0110 binary
? BITOR(x,y) && Returns 7, 0111 binary
```
