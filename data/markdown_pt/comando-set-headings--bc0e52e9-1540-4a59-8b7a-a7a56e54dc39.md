# Comando SET HEADINGS

Determina se os cabeçalhos de coluna são exibidos para os campos e se as informações do arquivo são incluídas quando TYPE é emitido para exibir o conteúdo de um arquivo.

```foxpro
SET HEADINGS ON | OFF
```

#### Parâmetros
 **ON**
(Padrão) Especifica que os nomes dos campos são exibidos. Se TYPE é emitido para exibir o conteúdo de um arquivo, o Visual FoxPro insere um avanço de página, o caminho e o nome do arquivo e a data no início da saída exibida.
**OFF**
Especifica que os nomes dos campos não são exibidos. Se TYPE é emitido para exibir o conteúdo de um arquivo, o Visual FoxPro não insere informações adicionais sobre o arquivo no início da saída exibida.

# Observações

SET HEADINGS especifica se um nome de campo aparece como cabeçalho de coluna acima de cada campo na saída de AVERAGE, CALCULATE, DISPLAY, LIST e SUM.
