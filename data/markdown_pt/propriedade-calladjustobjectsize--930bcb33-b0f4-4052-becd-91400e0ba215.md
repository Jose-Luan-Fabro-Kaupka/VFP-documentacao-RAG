# Propriedade CallAdjustObjectSize

Indica se o ReportListener deve invocar AdjustObjectSize para todos os controles de layout apropriados.

```foxpro
ReportListener.CallAdjustObjectSize [= nSetting]
```

# Valor de retorno
 **nSetting**
Especifica uma configuração que indica o estado atual do controle. nSetting Description 0 (padrão) O código do evento AdjustObjectSize é executado para todos os controles de layout se houver código na hierarquia de classes para este evento. 1 O evento AdjustObjectSize não ocorre, mesmo se houver código na hierarquia de classes para este evento. 2 O evento AdjustObjectSize sempre ocorre, independentemente de haver código na hierarquia de classes para este evento. Este valor é destinado principalmente a usuários que esperam usar BINDEVENT( ) em vez de código no método.

# Observações

Aplica-se a: ReportListener Object.

O Visual FoxPro invoca AdjustObjectSize uma vez para cada elemento de layout do tipo Shape ou Picture, a menos que encontre uma destas condições:
 - Se não houver código na classe ReportListener derivada em tempo de execução
- Se o elemento estiver em uma banda não marcada como Stretchable (altura de banda fixa)

Se a saída do seu relatório não requer dimensionamento dinâmico de objetos, você pode desativá-lo para melhor desempenho.

# Exemplo

O exemplo de código a seguir usa CallAdjustObjectSize para otimizar a velocidade de relatórios se uma caixa de seleção em um formulário estiver marcada.

```foxpro
oReport = CREATEOBJECT("myReportlistener")
IF THISFORM.chkNoAdjustSize.Value = .T.
oReport.CallAdjustObjectSize = 1
ENDIF
REPORT FORM (myreportfile) OBJECT oReport PREVIEW
```
