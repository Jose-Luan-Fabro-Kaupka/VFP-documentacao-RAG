# Variável de sistema _PSPACING

Incluída para compatibilidade com versões anteriores. Use o Report Designer em vez disso.

Define o espaçamento de linha da impressora.

```foxpro
_PSPACING = expN
```

# Observações

_PSPACING é incluída para compatibilidade com versões anteriores. Use o Report Writer em vez disso.

_PSPACING contém um valor numérico que determina se a saída é de espaçamento simples, duplo ou triplo. O padrão é espaçamento simples (1). expN deve ser um valor de 1 a 3.

Você pode definir _PSPACING na janela Command para alterar a saída de comandos como DISPLAY e LIST. _PSPACING também controla a altura de caixas definidas com DEFINE BOX. Uma caixa definida com altura 5 terá altura 15 se _PSPACING estiver definido como 3.
