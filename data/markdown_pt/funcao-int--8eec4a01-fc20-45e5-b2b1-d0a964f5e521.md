# Função INT( )

Avalia uma expressão numérica e retorna a parte inteira da expressão.

```foxpro
INT(nExpression)
```

#### Parâmetros
 **nExpression**
Especifica a expressão numérica para a qual INT( ) retorna a parte inteira.

# Valor de retorno

Numeric

# Exemplo

```foxpro
CLEAR
? INT(12.5)  && Displays 12
? INT(6.25 * 2)  && Displays 12
? INT(-12.5)  && Displays -12
STORE -12.5 TO gnNumber
? INT(gnNumber)  && Displays -12
```
