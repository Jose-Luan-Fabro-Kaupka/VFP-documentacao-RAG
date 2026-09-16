# Variável de sistema _PLINENO

Incluída para compatibilidade com versões anteriores. Use o Report Designer em vez disso.

Retorna ou define o número da linha atual.

```foxpro
_PLINENO = expN
```

# Observações

_PLINENO é incluída para compatibilidade com versões anteriores. Use o Report Writer em vez disso.

_PLINENO contém um valor numérico que estabelece a posição da linha atual. Use _PLINENO para determinar a próxima linha para saída. À medida que o FoxPro envia saída para o dispositivo de impressão atual, ele incrementa _PLINENO para indicar a posição atual. expN pode ser um valor variando de 0 a (_PLENGTH - 1).

Diferentemente da função PROW(), que retorna a posição atual da cabeça de impressão e não é incrementada quando SET PRINTER está OFF, o FoxPro incrementa _PLINENO sempre que a saída vai para uma impressora, a tela ou um arquivo. SET PRINTER não tem efeito sobre _PLINENO.
