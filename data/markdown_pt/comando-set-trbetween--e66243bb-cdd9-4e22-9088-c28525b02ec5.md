# Comando SET TRBETWEEN

Habilita ou desabilita o rastreamento entre pontos de interrupção na Trace Window.

```foxpro
SET TRBETWEEN ON | OFF
```

#### Parâmetros
 **ON**
Especifica que cada linha de código do programa seja exibida e destacada na janela Trace conforme é executada. Emitir SET TRBETWEEN ON é idêntico a habilitar o comando Trace Between Breaks no menu Program da janela Trace.
**OFF**
(Padrão) Especifica que apenas a última linha em que a execução do programa foi pausada seja destacada na janela Trace. Emitir SET TRBETWEEN OFF é idêntico a desabilitar o comando Trace Between Breaks.

# Observações

A janela Trace exibe o código-fonte de um programa conforme o programa é executado. A linha do programa em execução é destacada. Quando a janela Trace está aberta, você pode definir pontos de interrupção que fazem a execução do programa parar.

A janela Trace também pode ser aberta emitindo ACTIVATE WINDOW TRACE, SET ECHO ON ou SET STEP ON.
