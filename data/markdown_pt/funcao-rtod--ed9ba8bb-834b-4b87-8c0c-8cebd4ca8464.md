# Função RTOD( )

Converte radianos para o equivalente em graus.

Você pode usar RTOD( ) ao trabalhar com as funções trigonométricas do Visual FoxPro COS( ), SIN( ) e TAN( ).

```foxpro
RTOD(nExpression)
```

#### Parâmetros
 **nExpression**
Especifica uma expressão numérica que representa um valor em radianos.

# Valor de retorno

Tipo de dados numérico. RTOD( ) retorna o número de graus convertidos a partir do número de radianos.

# Observações

Para converter graus em radianos, use a função DTOR( ).

# Exemplo

```foxpro
CLEAR
? RTOD(ACOS(0))  && Displays 90.00
STORE -1 to gnArcAngle
? RTOD(ACOS(gnArcAngle))  && Displays 180.00
? RTOD(ACOS(SQRT(2)/2)) && Displays 45.00
```
