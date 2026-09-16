# Função ABS( )

Retorna o valor absoluto da expressão numérica especificada.

```foxpro
ABS(nExpression)
```

#### Parâmetros
 **nExpression**
Especifica a expressão numérica cujo valor absoluto ABS( ) retorna.

# Valor de retorno

Numérico

# Exemplo

```foxpro
? ABS(-45)       && Displays 45
? ABS(10-30)     && Displays 20
? ABS(30-10)     && Displays 20
STORE 40 TO gnNumber1
STORE 2 TO gnNumber2
? ABS(gnNumber2-gnNumber1)     && Displays 38
```
