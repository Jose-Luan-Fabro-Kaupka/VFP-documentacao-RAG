# Função COS( )

Retorna o cosseno de uma expressão numérica.

```foxpro
COS(nExpression)
```

#### Parâmetros
 **nExpression**
Especifica uma expressão numérica cujo cosseno COS( ) retorna. nExpression pode ser qualquer valor.

# Valor de retorno

Numeric

# Observações

COS( ) retorna o cosseno de nExpression em radianos. Use DTOR( ) para converter um ângulo de graus para radianos. O número de casas decimais que COS( ) retorna pode ser especificado com SET DECIMALS. O valor que COS( ) retorna varia entre –1 e 1.

# Exemplo

```foxpro
CLEAR
? COS(0)  && Displays 1.00
? COS(PI())  && Displays -1.00
? COS(DTOR(180))  && Displays -1.00
STORE PI() * 3 TO gnAngle
? COS(gnAngle)  && Displays -1.00
```
