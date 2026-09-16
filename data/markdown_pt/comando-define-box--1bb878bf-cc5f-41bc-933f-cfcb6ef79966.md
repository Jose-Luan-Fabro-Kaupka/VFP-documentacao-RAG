# Comando DEFINE BOX

Incluído para compatibilidade com versões anteriores. Use o Report Designer em seu lugar.

Desenha uma caixa ao redor do texto impresso.

```foxpro
DEFINE BOX FROM column1
TO column2
	HEIGHT expN1
	[AT LINE expN2]
	[SINGLE | DOUBLE
	| border string]
```

# Observações

Incluído para compatibilidade com versões anteriores; use o Screen Builder em seu lugar.

Este comando desenha uma caixa ao redor do texto somente em relatórios impressos e somente se a variável de memória do sistema BOX estiver definida como verdadeiro (.T.). Use @ ...BOX ou @ ... TO para desenhar caixas na janela principal do FoxPro ou em uma janela definida pelo usuário.

Uma caixa só pode ser impressa se SET PRINTER estiver ON. Caixas só podem ser desenhadas ao redor da saída criada com o comando ? ou ??. Elas não podem ser desenhadas ao redor da saída criada com @ ... SAY.

Duas funções úteis com DEFINE BOX são PCOL() e PROW(). Elas retornam as posições atuais de coluna e linha de impressão.

FROM column1 TO column2

 O canto superior esquerdo da caixa aparece na coluna de impressão column1. O canto superior direito aparece na coluna column2.

HEIGHT expN1

 A altura da caixa é especificada por expN1 e é afetada pelo valor da variável de memória do sistema _PSPACING. Por exemplo, se expN1 for 5 e _PSPACING for 3, a altura será de 15 linhas.

AT LINE expN2

 A parte superior da caixa é desenhada a partir da linha de impressão atual, a menos que AT LINE expN2 seja incluído. expN2 é o número da linha em que a parte superior deve ser desenhada.

SINGLE | DOUBLE | border string

 A borda padrão é uma linha simples. Você pode especificar outro estilo com a cláusula SINGLE, DOUBLE ou border string. Inclua SINGLE para uma linha simples, DOUBLE para uma linha dupla ou defina sua própria borda com border string. A sintaxe da cadeia de borda é idêntica à de SET BORDER. Para obter mais informações, consulte SET BORDER.
