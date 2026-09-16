# Função FLOOR( )

Retorna o inteiro mais próximo que é menor ou igual à expressão numérica especificada.

```foxpro
FLOOR(nExpression)
```

#### Parâmetros
 **nExpression**
Especifica a expressão numérica para a qual FLOOR( ) retorna o inteiro mais próximo que é menor ou igual à expressão numérica.

# Valor de retorno

Numeric

# Exemplo

```foxpro
STORE  10.9 TO gnNumber1
STORE -10.1 TO gnNumber2
CLEAR
? FLOOR(gnNumber1)  && Displays 10
? FLOOR(gnNumber2)  && Displays -11
? FLOOR(10.0)  && Displays 10
? FLOOR(-10.0)  && Displays -10
```
