# Função LOG( )

Retorna o logaritmo natural (base e) da expressão numérica especificada.

```foxpro
LOG(nExpression)
```

#### Parâmetros
 **nExpression**
Especifica a expressão numérica para a qual LOG( ) retorna o valor de x na equação e ^ x = nExpression . nExpression deve ser maior que 0.

# Valor de retorno

Numeric

# Observações

A base do logaritmo natural é a constante e. O número de casas decimais retornado no resultado é especificado com SET DECIMALS.

# Exemplo

```foxpro
CLEAR
? LOG(1)  && Displays 0.00
STORE EXP(2) TO gneSquare
? LOG(gneSquare)  && Displays 2.00
```
