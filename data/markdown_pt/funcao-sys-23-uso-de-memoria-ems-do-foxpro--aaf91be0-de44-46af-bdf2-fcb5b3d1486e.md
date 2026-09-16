# Função SYS(23) - Uso de memória EMS do FoxPro

Incluída para compatibilidade com versões anteriores.

Retorna a quantidade de memória EMS (em segmentos de 16K) que está sendo usada atualmente pelo FoxPro.

```foxpro
SYS(23)
```

# Valor de retorno

Valor de retorno - Character

# Observações

0 é retornado se nenhuma memória EMS estiver em uso.

SYS(23) sempre retorna 0 na versão Extended de 32 bits do FoxPro para MS-DOS, FoxPro para Windows e FoxPro para Macintosh.
