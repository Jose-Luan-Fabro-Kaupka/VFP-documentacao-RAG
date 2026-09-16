# Função NVL( )

Retorna um valor não nulo de duas expressões.

```foxpro
NVL(eExpression1, eExpression2)
```

#### Parâmetros
 **eExpression1 , eExpression2**
NVL( ) retorna eExpression2 se eExpression1 avaliar como um valor nulo. NVL( ) retorna eExpression1 se eExpression1 não for um valor nulo. eExpression1 e eExpression2 podem ser de qualquer tipo de dados. NVL( ) retorna .NULL. se tanto eExpression1 quanto eExpression2 avaliarem como o valor nulo.

# Valor de retorno

Character, Date, DateTime, Numeric, Currency, Logical ou o valor nulo

# Observações

Use NVL( ) para remover valores nulos de cálculos ou operações em que valores nulos não são suportados ou não são relevantes.

# Exemplo

O exemplo a seguir cria uma variável de memória chamada `glMyNull` que contém o valor nulo. NVL( ) é usado para retornar um valor não nulo de `glMyNull` e outra expressão.

```foxpro
STORE .NULL. TO glMyNull  && A memory variable containing the null value
CLEAR
? NVL(.T., glMyNull)  && Displays .T.
? NVL(glMyNull, glMyNull)  && Displays .NULL.
```
