# Função SIGN( )

Retorna um valor numérico de 1, –1 ou 0 se a expressão numérica especificada for avaliada como um valor positivo, negativo ou 0.

```foxpro
SIGN(nExpression)
```

#### Parâmetros
 **nExpression**
Especifica a expressão numérica que SIGN( ) avalia. SIGN( ) retorna 1 se nExpression for avaliada como um número positivo, –1 se nExpression for avaliada como um número negativo e 0 se nExpression for avaliada como 0.

# Valor de retorno

Numérico

# Exemplo

```foxpro
STORE 10 TO gnNum1
STORE -10 TO gnNum2
STORE 0 TO gnZero
CLEAR
? SIGN(gnNum1)  && Displays 1
? SIGN(gnNum2)  && Displays -1
? SIGN(gnZero)  && Displays 0
```
