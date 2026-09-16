# Variável de sistema _PADVANCE

Incluída para compatibilidade com versões anteriores. Use o Report Designer.

Define o método de avanço de página.

```foxpro
_PADVANCE = expC
```

#### Parâmetros
 expC deve avaliar como um dos seguintes:

FORMFEED Envia um caractere de avanço de formulário quando a página avança. FORMFEED é o padrão. Esta opção usa os controles internos de topo de formulário da impressora.

LINEFEEDS Envia um número calculado de avanços de linha quando a página avança. Esta opção posiciona a impressora no topo da próxima página calculando internamente quantos avanços de linha são necessários e enviando esse número de avanços de linha contínuos.

Ao calcular quantos avanços de linha enviar, o FoxPro usa a fórmula (_PLENGTH - _PLINENO) nas seguintes situações:

 Quando você emite EJECT PAGE sem um manipulador ON PAGE

 Quando você emite EJECT PAGE com um manipulador ON PAGE e a posição da linha é maior que o valor de linha ON PAGE

 Quando PRINTJOB ou ENDPRINTJOB fazem _PEJECT enviar uma ejeção de página para a impressora

O FoxPro usa a fórmula (_PLENGTH - MOD(PROW(), _PLENGTH)) quando você emite:

 EJECT

 SET DEVICE TO PRINTER e força uma ejeção com um @ ... SAY subsequente

Independentemente da configuração de _PADVANCE, você sempre pode enviar um caractere de avanço de formulário para a impressora emitindo CHR(12).

# Observações

Incluída para compatibilidade com versões anteriores — use o Report Writer.

_PADVANCE contém um valor de caractere que determina se o FoxPro avança para o topo de uma página usando um caractere de avanço de formulário ou usando avanços de linha.
