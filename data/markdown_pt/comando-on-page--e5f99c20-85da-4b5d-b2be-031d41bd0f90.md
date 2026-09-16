# Comando ON PAGE

Especifica um comando que é executado quando a saída impressa atinge um número de linha especificado em um relatório ou quando você emite EJECT PAGE.

```foxpro
ON PAGE   [AT LINE nLineNumber [Command]]
```

#### Parâmetros
 **AT LINE nLineNumber [ Command ]**
Especifica o comando a ser executado no número de linha designado. O comando especificado é executado quando _PLINENO, a variável de sistema que mantém o número da linha atual em um relatório, se torna maior do que o número de linha especificado com nLineNumber . O comando especificado com ON PAGE também é executado quando você emite EJECT PAGE. Para obter mais informações, consulte EJECT PAGE Command .

# Observações

ON PAGE normalmente usa DO para executar um procedimento para tratar quebras de página, cabeçalhos e rodapés.

Executar ON PAGE sem a cláusula AT LINE limpa o comando ON PAGE.
