# Função ATAN( )

Retorna em radianos o arco tangente de uma expressão numérica.

```foxpro
ATAN(nExpression)
```

#### Parâmetros
 **nExpression**
Especifica uma expressão numérica cujo arco tangente ATAN( ) retorna. nExpression pode ser qualquer valor. O valor retornado por ATAN( ) pode variar de –pi/2 a +pi/2 (–1,57079 a 1,57079). O número de casas decimais exibidas no valor retornado por ATAN( ) é determinado por SET DECIMALS.

# Valor de retorno

Numeric

# Observações

Use RTOD( ) para converter radianos em graus.

# Exemplo

```foxpro
CLEAR
? ATAN(0)  && Displays 0.00
STORE PI()/2 to gnAngle
? ATAN(gnAngle)  && Displays 1.00
? ATAN(PI()/2)  && Displays 1.00
? ATAN(DTOR(90))  && Displays 1.00
```
