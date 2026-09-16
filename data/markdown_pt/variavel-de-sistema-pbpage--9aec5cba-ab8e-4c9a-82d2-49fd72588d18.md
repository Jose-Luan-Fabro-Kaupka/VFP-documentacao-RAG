# Variável de sistema _PBPAGE

Incluída para compatibilidade com versões anteriores. Use o Report Designer em vez disso.

Retorna ou define a primeira página a imprimir.

```foxpro
_PBPAGE = expN
```

# Observações

_PBPAGE é incluída para compatibilidade com versões anteriores. Use o Report Writer em vez disso.

_PBPAGE contém um valor numérico que determina a primeira página a imprimir. Quando _PBPAGE é maior que _PAGENO, nenhuma página é impressa. Em vez disso, o FoxPro produz páginas internamente e incrementa _PAGENO e outras variáveis de sistema de memória. Quando _PAGENO atinge o valor de _PBPAGE, a impressão começa.

O valor de _PBPAGE pode variar de 1 a 32.767, inclusive. O padrão de inicialização é 1. O valor de _PBPAGE deve ser menor ou igual a _PEPAGE.
