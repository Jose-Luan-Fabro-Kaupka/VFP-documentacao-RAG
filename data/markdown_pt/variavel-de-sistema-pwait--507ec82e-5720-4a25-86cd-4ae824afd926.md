# Variável de sistema _PWAIT

Incluída para compatibilidade com versões anteriores. Use o Report Designer em vez disso.

Define a pausa entre páginas de saída.

```foxpro
_PWAIT = expL
```

# Observações

Incluída para compatibilidade com versões anteriores — use o Report Writer em vez disso.

_PWAIT contém um valor lógico que determina se a impressora pausa ou não entre páginas de saída. _PWAIT permite imprimir em folhas individuais de papel, em oposição a formulários de alimentação contínua (fan-fold). Quando uma página é ejetada da impressora com EJECT ou quando _PLINENO excede _PLENGTH, o FoxPro suspende a saída para a impressora para que você possa inserir manualmente outra folha de papel.
