# Variável de sistema _WRAP

Incluída para compatibilidade com versões anteriores. Use o Report Designer.

Define a quebra automática de palavras.

```foxpro
_WRAP = expL
```

# Observações

_WRAP está incluída para compatibilidade com versões anteriores. Use o Report Writer.

_WRAP contém um valor lógico que determina se a saída quebra linhas automaticamente. O padrão é .F..

Quando _WRAP é .T., a saída do comando ? que ultrapassaria a margem direita (_RMARGIN) quebra automaticamente para a margem esquerda (_LMARGIN). _WRAP deve ser .T. para que _ALIGNMENT, _INDENT, _LMARGIN e _RMARGIN afetem a saída.
