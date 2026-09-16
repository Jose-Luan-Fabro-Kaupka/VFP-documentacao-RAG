# Função BITAND( )

Executa uma operação AND bit a bit em dois ou mais valores do tipo Numeric, Varbinary ou Blob e retorna o resultado. Há uma versão numérica e uma versão binária da sintaxe.

```foxpro
BITAND(nNumericExpression1, nNumericExpression2, ... , nNumericExpression26)
```

```foxpro
BITAND(BinaryExpression1, BinaryExpression2, ... , BinaryExpression26)
```

#### Parâmetros
 **nNumericExpression1 , nNumericExpression2, ... , nNumericExpression26**
Especifica valores Numeric para executar a operação AND bit a bit.
**BinaryExpression1 , BinaryExpression2, ... , BinaryExpression26**
Especifica valores Varbinary ou Blob para executar a operação AND bit a bit. Observação Você pode especificar no máximo 26 valores. Os valores especificados devem ter o mesmo tipo. Se as expressões especificadas não são inteiros, elas são convertidas em inteiros antes de executar a operação.

# Valor de retorno

Numeric ou Varbinary. BITAND( ) retorna o resultado da operação AND bit a bit executada nas expressões especificadas.

> **Observação:** Para valores Varbinary ou Blob, o valor de retorno é calculado como se todos os valores fossem preenchidos com 0h00 à direita do valor até o comprimento do valor mais longo. A operação apropriada é então executada entre esses valores.

# Observações

BITAND( ) compara cada bit em eExpressionN com o bit correspondente em eExpressionN+1. Se os bits em eExpressionN e eExpressionN+1 são ambos 1, o bit de resultado correspondente é definido como 1; caso contrário, o bit de resultado correspondente é definido como 0.

A tabela a seguir mostra o resultado de uma operação AND bit a bit em bits eExpressionN e eExpressionN+1 correspondentes:

| bit eExpressionN | bit eExpressionN+1 | Bit resultante |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 1 | 1 |
| 1 | 0 | 0 |

# Exemplo

```foxpro
x = 3  && 0011 binary
y = 6  && 0110 binary
? BITAND(x,y) && Returns 2, 0010 binary
```
