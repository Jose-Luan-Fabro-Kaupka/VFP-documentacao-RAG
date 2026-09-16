# Função SIN( )

Retorna o seno de um ângulo.

```foxpro
SIN(nExpression)
```

#### Parâmetros
 **nExpression**
Especifica um ângulo cujo seno SIN( ) retorna. nExpression pode assumir qualquer valor e o valor retornado por SIN( ) varia entre –1 e 1. Observação nExpression é especificado em radianos. Use DTOR( ) para converter um ângulo de graus para radianos. O número de casas decimais exibidas por SIN( ) pode ser especificado com SET DECIMALS.

# Valor de retorno

Numeric

# Exemplo

```foxpro
CLEAR
? SIN(0)  && Displays 0.00
? SIN(PI()/2)  && Displays 1.00
? SIN(DTOR(90))  && Displays 1.00
```
