# Função REPLICATE( )

Retorna uma cadeia de caracteres que contém uma expressão de caracteres repetida o número de vezes especificado.

```foxpro
REPLICATE(cExpression, nTimes)
```

#### Parâmetros
 **cExpression**
Especifica a expressão de caracteres a ser repetida.
**nTimes**
Especifica o número de vezes que a expressão será repetida.

# Valor de retorno

Character

# Observações

No Visual FoxPro, o comprimento máximo da cadeia resultante é limitado pela memória disponível.

# Exemplo

```foxpro
CLEAR
? REPLICATE('HELLO ',4) && Displays HELLO HELLO HELLO HELLO
```
