# Função ACOS( )

Retorna o arco cosseno de uma expressão numérica especificada.

```foxpro
ACOS(nExpression)
```

#### Parâmetros
 **nExpression**
Especifica uma expressão numérica cujo arco cosseno ACOS( ) retorna. O valor de nExpression pode variar de –1 a +1. O valor retornado por ACOS( ) varia de 0 a pi (3,141592). O número de casas decimais retornadas por ACOS( ) é determinado por SET DECIMALS. Use RTOD( ) para converter radianos em graus.

# Valor de retorno

Numérico

# Observações

O arco cosseno é retornado em radianos.

# Exemplo

```foxpro
CLEAR
? RTOD(ACOS(0))  && Displays 90.00
STORE -1 to gnArcAngle
? RTOD(ACOS(gnArcAngle))  && Displays 180.00
? RTOD(ACOS(SQRT(2)/2))  && Displays 45.00
```
