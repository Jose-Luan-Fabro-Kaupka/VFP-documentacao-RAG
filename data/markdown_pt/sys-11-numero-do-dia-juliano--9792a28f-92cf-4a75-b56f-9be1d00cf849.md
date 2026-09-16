# SYS(11) - Número do dia juliano

Converte uma expressão de data ou cadeia de caracteres em formato de data em um número do dia juliano.

```foxpro
SYS(11, dExpression | tExpression | cExpression)
```

# Valor de retorno

Character

# Observações

SYS(11) retorna um número do dia juliano de uma expressão de data dExpression, uma expressão datetime tExpression ou uma expressão de caracteres cExpression em formato de data. O número do dia é retornado como uma cadeia de caracteres.

# Exemplo

```foxpro
? SYS(11, {^1998-06-06})
? SYS(11,'06/06/1998')
```
