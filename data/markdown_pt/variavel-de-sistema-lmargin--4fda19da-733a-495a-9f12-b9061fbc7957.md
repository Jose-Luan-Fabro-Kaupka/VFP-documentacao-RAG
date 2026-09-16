# Variável de sistema _LMARGIN

Incluída para compatibilidade com versões anteriores. Use o Report Designer em vez disso.

Define a margem esquerda.

```foxpro
_LMARGIN = expN
```

# Observações

_LMARGIN é incluída para compatibilidade com versões anteriores. Use o Report Writer em vez disso.

_LMARGIN contém um valor numérico que determina a posição da margem esquerda para saída gerada com o comando ?. Valores válidos de _LMARGIN variam de 0 a 254.

Quando você envia saída para a impressora, o valor de _LMARGIN representa o número de espaços adicionais entre o deslocamento atual da página e o texto. O deslocamento da página é determinado por _PLOFFSET ou SET MARGIN.

_LMARGIN está ativa somente quando _WRAP é definido como .T..
