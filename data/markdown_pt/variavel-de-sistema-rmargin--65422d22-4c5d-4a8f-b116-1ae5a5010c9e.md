# Variável de sistema _RMARGIN

Incluída para compatibilidade com versões anteriores. Use o Report Designer.

Define a margem direita.

```foxpro
_RMARGIN = expN
```

# Observações

_RMARGIN está incluída para compatibilidade com versões anteriores. Use o Report Writer.

_RMARGIN contém um valor numérico que determina a posição da margem direita para saída gerada com o comando ?. O valor mínimo de _RMARGIN é o maior entre _LMARGIN + 1 ou _LMARGIN + _INDENT + 1. O valor máximo de _RMARGIN é 255. O padrão na inicialização é 80.

_RMARGIN está ativa somente quando _WRAP está definida como .T..
