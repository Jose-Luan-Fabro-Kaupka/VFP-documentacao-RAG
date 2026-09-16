# Propriedade CallEvaluateContents

Indica se o ReportListener deve invocar EvaluateContents para todos os controles Field em um relatório.

```foxpro
ReportListener.CallEvaluateContents [= nSetting]
```

# Valor de retorno
 **nSetting**
Especifica uma configuração que indica o estado atual do controle. nSetting Description 0 (default) The EvaluateContents event code runs for all layout controls if there is code in the class hierarchy for this event. 1 The EvaluateContents event does not occur, even if there is code in the class hierarchy for this event. 2 The EvaluateContents event always occurs, whether or not there is code in the class hierarchy for this event. This value is primarily intended for users who expect to use BINDEVENT( ) rather than code in the method.

# Observações

Aplica-se a: ReportListener Object.

O Visual FoxPro chama EvaluateContents no início do processamento de banda, uma vez para cada controle Field. O código que você escreve para o evento EvaluateContents pode alterar o texto, a cor, a fonte e a exibição alpha do controle Field. Se a saída do seu relatório não exigir essa manipulação de texto em tempo de execução, você pode desativar o evento EvaulateContents para melhor desempenho.

# Exemplo

Se você tiver um relatório que altera a cor da caneta dos controles Field em tempo de execução no evento EvaluateContents do seu ReportListener, talvez queira desativar o evento se estiver imprimindo em uma impressora que não seja colorida. Este exemplo de código desativa o processamento do evento EvaluateContents com base no valor de uma caixa de seleção.

```foxpro
oReport = CREATEOBJECT("myReportlistener")
IF THISFORM.chkColorPrinter.Value = .F.
oReport.CallEvaluateContents = 1
ENDIF
REPORT FORM (myreportfile) OBJECT oReport PREVIEW
```
