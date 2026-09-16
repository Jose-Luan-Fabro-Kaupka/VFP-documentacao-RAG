# Comando SET DEVICE

Direciona a saída de @ ... SAY para a tela, uma impressora ou um arquivo.

```foxpro
SET DEVICE TO SCREEN | TO PRINTER [PROMPT] | TO FILE FileName
```

#### Parâmetros
 **TO SCREEN**
Direciona a saída de @ ... SAY para a janela principal do Visual FoxPro ou para a janela definida pelo usuário ativa.
**TO PRINTER [PROMPT]**
Direciona a saída de @ ... SAY para a impressora. Uma ejeção de página é emitida quando as coordenadas em @ ... SAY especificam um local na página superior ao local especificado pelas coordenadas no @ ... SAY anterior. Você pode incluir a cláusula opcional PROMPT para exibir uma caixa de diálogo antes do início da impressão. Nessa caixa de diálogo, o usuário pode ajustar as configurações da impressora, incluindo o número de cópias a imprimir e os números de página. O driver de impressora instalado determina quais configurações de impressora o usuário pode ajustar. Coloque PROMPT imediatamente após TO PRINTER.
**TO FILE FileName**
Especifica um arquivo para o qual @ ... SAY envia saída.

# Observações

A saída de @ ... SAY pode ser enviada para a janela principal do Visual FoxPro, a janela definida pelo usuário ativa, a impressora ou um arquivo.
