# Variável de sistema _TABS

Incluída para compatibilidade com versões anteriores. Use o Report Designer em vez disso.

Especifica as configurações de tabulação.

```foxpro
_TABS = expC
```

# Observações

_TABS é incluída para compatibilidade com versões anteriores. Use o Report Writer em vez disso.

_TABS contém um valor de caractere que determina onde as paradas de tabulação aparecem na saída impressa. expC representa uma lista de tabulação que é uma série de números separados por vírgulas em ordem ascendente. Por padrão, _TABS contém a cadeia de caracteres nula, que define o espaçamento de _TABS em intervalos de 8 caracteres (8, 16, 24, 32, 40 e assim por diante).

Quando _WRAP está definido como .T., o FoxPro ignora quaisquer valores de _TABS maiores ou iguais a _RMARGIN. A instrução TABS que você inclui no arquivo de configuração é equivalente a _TABS, e especificar um valor TABS define automaticamente o valor em _TABS.
