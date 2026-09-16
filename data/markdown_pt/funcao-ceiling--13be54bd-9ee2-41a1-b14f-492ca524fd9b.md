# Função CEILING( )

Retorna o próximo inteiro maior que ou igual à expressão numérica especificada.

```foxpro
CEILING(nExpression)
```

#### Parâmetros
 **nExpression**
Especifica o número cujo próximo inteiro maior CEILING( ) retorna.

# Valor de retorno

Numérico

# Observações

CEILING arredonda um número com parte fracionária para o próximo inteiro maior.

# Exemplo

```foxpro
STORE 10.1 TO num1
STORE -10.9 TO num2
? CEILING(num1)  && Displays 11
? CEILING(num2)  && Displays -10
? CEILING(10.0)  && Displays 10
? CEILING(-10.0) && Displays -10
```
