# Variável de sistema _PAGENO

Contém o número da página atual.

```foxpro
_PAGENO = nCurrentPageNumber
```

#### Parâmetros
 **nCurrentPageNumber**
Especifica um valor numérico de 1 a 32.767 para o número da página atual. _PAGENO, _PBPAGE e _PEPAGE funcionam em conjunto. Se _PAGENO for definido (ou incrementado) de forma que caia fora do intervalo de _PBPAGE a _PEPAGE, nenhuma página é impressa.

# Observações

_PAGENO contém um valor numérico que determina o número da página atual. O padrão inicial é 1. _PAGENO permite imprimir números de página em saída contínua sem definir, inicializar e incrementar uma variável de memória para esse fim.
