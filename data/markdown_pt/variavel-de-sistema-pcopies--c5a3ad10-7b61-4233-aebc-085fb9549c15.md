# Variável de sistema _PCOPIES

Incluída para compatibilidade com versões anteriores. Use o Report Designer em vez disso.

Retorna ou define o número de cópias a imprimir.

```foxpro
_PCOPIES = expN
```

# Observações

_PCOPIES está incluída para compatibilidade com versões anteriores. Use o Report Writer em vez disso.

_PCOPIES contém um valor numérico que determina quantas cópias da saída devem ser impressas. expN pode ser um valor de 1 a 32.767, inclusive. O padrão na inicialização é 1.

_PCOPIES tem efeito somente quando usada com PRINTJOB ... ENDPRINTJOB e, portanto, tem efeito somente em programas FoxPro. Coloque a instrução de atribuição _PCOPIES antes do PRINTJOB para definir o número de cópias a imprimir.
