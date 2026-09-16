# Função DTOR( )

Converte graus em radianos.

```foxpro
DTOR(nExpression)
```

#### Parâmetros
 **nExpression**
Especifica a expressão numérica cujo valor você deseja converter em radianos. Um ângulo expresso em formato grau:minuto:segundo deve ser convertido para seu equivalente decimal.

# Valor de retorno

Numérico

# Observações

DTOR( ) converte o valor de uma expressão numérica dada em graus para um valor equivalente em radianos. DTOR( ) é útil para trabalhar com as funções trigonométricas do Microsoft Visual FoxPro: ACOS( ), ASIN( ), COS( ), SIN( ), TAN( ).

Use RTOD( ) para converter radianos em graus.

# Exemplo

```foxpro
CLEAR
? DTOR(0)  && Displays 0.00
? DTOR(45) && Displays 0.79
? DTOR(90) && Displays 1.57
? DTOR(180)  && Displays 3.14
? COS(DTOR(90))  && Displays 0.00
```
