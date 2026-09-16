# SYS(1) - Data juliana do sistema

Retorna a data atual do sistema como uma cadeia de caracteres com o número do dia juliano.

```foxpro
SYS(1)
```

# Valor de retorno

Character

# Observações

O valor retornado por SYS(1) é válido nas versões dos EUA do Visual FoxPro para qualquer data do sistema posterior a 14 de setembro de 1752 e anterior a 31 de dezembro de 9999.

# Exemplo

```foxpro
? SYS(1)
? SYS(10,VAL(SYS(1)))
```
