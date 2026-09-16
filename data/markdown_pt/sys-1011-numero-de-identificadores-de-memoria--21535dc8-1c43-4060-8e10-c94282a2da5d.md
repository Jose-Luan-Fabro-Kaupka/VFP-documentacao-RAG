# SYS(1011) - Número de identificadores de memória

Retorna o número de identificadores de memória em uso.

```foxpro
SYS(1011)
```

# Valor de retorno
Personagem

# Observações
Você pode usar SYS(1011) para verificar o uso da memória enquanto executa um teste repetidamente. Aumentar os valores apenas entre as duas primeiras execuções pode ser uma evidência de cache de memória. Aumentar valores além disso pode ser evidência de um problema.
