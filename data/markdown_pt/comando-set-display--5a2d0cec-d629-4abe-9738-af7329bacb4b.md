# Comando SET DISPLAY

Incluído para compatibilidade com versões anteriores. Use as propriedades de fonte da variável de sistema _SCREEN em vez disso.

Permite alterar o modo de exibição atual em monitores que suportam diferentes modos.

```foxpro
SET DISPLAY TO CGA | COLOR | EGA25
	| EGA43 | MONO | VGA25 | VGA50
```

# Observações

No FoxPro para MS-DOS, SET DISPLAY permite alternar entre diferentes modos de exibição em monitores que suportam diferentes modos.

No FoxPro para Windows e FoxPro para Macintosh, SET DISPLAY altera o tamanho da fonte da janela principal do FoxPro. O tamanho da janela principal do FoxPro é aumentado, se necessário, para acomodar o número de linhas da opção que você especifica. Se a barra de status gráfica aparecer quando você emitir SET DISPLAY, ela será desativada.

A mensagem de erro "Display mode not available" aparece se uma opção não for suportada pelo seu hardware de vídeo.

A linha SET MESSAGE é redefinida para a última linha da janela principal do FoxPro sempre que SET DISPLAY é emitido.

CGA

 No FoxPro para MS-DOS, alterna o modo de exibição para CGA.

 No FoxPro para Windows e FoxPro para Macintosh, alterna o tamanho da fonte da janela principal do FoxPro para 9 pontos.

COLOR

 No FoxPro para MS-DOS, alterna o modo de exibição para colorido.

EGA25

 No FoxPro para MS-DOS, alterna o modo de exibição para EGA e 25 linhas.

 No FoxPro para Windows e FoxPro para Macintosh, alterna o tamanho da fonte da janela principal do FoxPro para 9 pontos e o tamanho da janela principal do FoxPro para 25 linhas.

EGA43

 No FoxPro para MS-DOS, alterna o modo de exibição para EGA e 43 linhas.

 No FoxPro para Windows, alterna o tamanho da fonte da janela principal do FoxPro para 7 pontos e o tamanho da janela principal do FoxPro para 50 linhas.

 No FoxPro para Macintosh, alterna o tamanho da fonte da janela principal do FoxPro para 8 pontos.

MONO

 No FoxPro para MS-DOS, alterna o modo de exibição para monocromático.

VGA25

 No FoxPro para MS-DOS, alterna o modo de exibição para VGA e 25 linhas.

 No FoxPro para Windows e FoxPro para Macintosh, alterna o tamanho da fonte da janela principal do FoxPro para 9 pontos e o tamanho da janela principal do FoxPro para 25 linhas.

VGA50

 No FoxPro para MS-DOS, alterna o modo de exibição para VGA e 50 linhas.

 No FoxPro para Windows, alterna o tamanho da fonte da janela principal do FoxPro para 7 pontos e o tamanho da janela principal do FoxPro para 50 linhas.

 No FoxPro para Macintosh, alterna o tamanho da fonte da janela principal do FoxPro para 8 pontos.
