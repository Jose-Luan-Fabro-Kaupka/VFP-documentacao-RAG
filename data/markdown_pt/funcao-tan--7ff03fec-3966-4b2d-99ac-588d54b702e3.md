# Função TAN( )

Esta função trigonométrica retorna a tangente de um ângulo.

```foxpro
TAN(nExpression)
```

#### Parâmetros
 **nExpression**
Especifica o ângulo em radianos para o qual TAN( ) retorna a tangente. Para converter um ângulo de graus para radianos, use DTOR( ). O número de casas decimais retornado por TAN( ) pode ser especificado com SET DECIMALS.

# Valor de retorno

Numeric

# Exemplo

```foxpro
CLEAR
? TAN(0)  && Displays 0.00
? TAN(PI()/4)  && Displays 1.00
? TAN(PI()*3/4)  && Displays -1.00
```
