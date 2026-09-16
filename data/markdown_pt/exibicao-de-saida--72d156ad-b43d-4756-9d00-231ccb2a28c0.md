# Exibição de saída

O comando DEBUGOUT permite gravar valores na janela Debug Output em um arquivo de log de texto. Alternativamente, você pode usar o comando SET DEBUGOUT ou a guia Debug da caixa de diálogo Options.

Se você não estiver gravando comandos DEBUGOUT em um arquivo de texto, a janela Debug Output Window deve estar aberta para que os valores DEBUGOUT sejam gravados. A linha de código a seguir imprime na janela Debug Output no momento em que a linha de código é executada:

```foxpro
DEBUGOUT DATETIME()
```

Além disso, você pode habilitar o rastreamento de eventos e escolher que o nome e os parâmetros de cada evento que ocorre sejam exibidos na janela Debug Output.
