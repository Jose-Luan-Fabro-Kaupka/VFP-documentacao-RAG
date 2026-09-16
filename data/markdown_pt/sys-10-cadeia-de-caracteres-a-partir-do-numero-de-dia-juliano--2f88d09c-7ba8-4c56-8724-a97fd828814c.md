# SYS(10) - Cadeia de caracteres a partir do número de dia juliano

Converte um número de dia juliano em uma cadeia de caracteres.

```foxpro
SYS(10, nJulianDayNumber)
```

# Valor de retorno

Character

# Observações

SYS(10) retorna uma data do tipo Character a partir de um número de dia juliano nJulianDayNumber.

# Exemplo

```foxpro
? SYS(1)
? SYS(10,VAL(SYS(1)))
```
