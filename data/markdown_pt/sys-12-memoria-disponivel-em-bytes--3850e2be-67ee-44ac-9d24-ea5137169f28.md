# SYS(12) - Memória disponível em bytes

Retorna a quantidade de memória abaixo de 640K disponível para executar um programa externo.

```foxpro
SYS(12)
```

# Valor de retorno

Character

# Observações

No Visual FoxPro, SYS(12) sempre retorna 655.360.

SYS(12) é semelhante a MEMORY( ), com duas exceções:
 - SYS(12) retorna a quantidade de memória disponível em bytes. MEMORY( ) retorna a memória disponível em kilobytes.
- SYS(12) retorna uma cadeia de caracteres. MEMORY( ) retorna um valor numérico.
