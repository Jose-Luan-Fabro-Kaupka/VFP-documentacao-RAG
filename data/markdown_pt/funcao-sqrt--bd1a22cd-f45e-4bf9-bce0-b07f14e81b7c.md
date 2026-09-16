# Função SQRT( )

Retorna a raiz quadrada da expressão numérica especificada.

```foxpro
SQRT(nExpression)
```

#### Parâmetros
 **nExpression**
Especifica a expressão numérica que SQRT( ) avalia. nExpression não pode ser negativo.

# Valor de retorno

Numérico

# Observações

O número de casas decimais no valor retornado por SQRT( ) é o maior entre a configuração atual de casas decimais e o número de casas decimais contidas em nExpression. A configuração atual de casas decimais é especificada com SET DECIMALS.

# Exemplo

```foxpro
CLEAR
? SQRT(4)  && Displays 2.00
? SQRT(2*SQRT(2))  && Displays 1.68
```
