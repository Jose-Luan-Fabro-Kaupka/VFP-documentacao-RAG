# Método GetPageHeight

Retorna a altura da página em 960 pontos por polegada (dpi) durante uma execução de relatório.

```foxpro
iPageHeight = oReportListener.GetPageHeight()
```

#### Parâmetros

Nenhum.

# Valor de retorno

Tipo de dados inteiro, a altura da página em 1/960 avos de polegada. Entre execuções de relatório, este método retorna `0`.

# Observações

Aplica-se a: ReportListener Object.

Este método e GetPageWidth permitem que um objeto de visualização ou qualquer outro "participante" no processo de saída consulte o objeto ReportListener sobre as dimensões da saída de página, conforme determinado pelas configurações da impressora em vigor para a execução do relatório. O PreviewContainer do ReportListener usa estes métodos quando o objeto ReportListener chama seu método Show, para determinar como exibir o conteúdo do relatório atual.

Estes métodos fornecem valores utilizáveis em todos os pontos do processo de relatório após BeforeReport e antes de UnloadReport, a menos que você invoque continuação usando NOPAGEEJECT no seu comando REPORT FORM. Se você usar NOPAGEEJECT, estes métodos continuam a fornecer resultados utilizáveis até que um REPORT FORM sem NOPAGEEJECT chegue ao seu evento UnloadReport. Em outros momentos, ambos os métodos retornam 0.

> **Observação:** O período durante o qual GetPageHeight e GetPageWidth fornecem valores utilizáveis é determinado quando o ReportListener configura o layout da página e o trabalho de impressão. O ReportListener não reavalia o layout da página e as dimensões da página entre comandos REPORT FORM quando você usa NOPAGEEJECT, pois estas execuções de relatório fazem parte de um único trabalho de impressão. No entanto, você pode criar classes derivadas de ReportListener que podem lidar com vários tamanhos de página durante uma execução de relatório continuada.

Para obter mais informações sobre a sequência de eventos no início e no fim de uma execução de relatório, consulte Understanding Visual FoxPro Object-Assisted Reporting.

# Exemplo

Você pode substituir este método para fornecer informações personalizadas de tamanho de página.

> **Importante:** Fornecer informações diferentes ao mecanismo de renderização do ReportListener não enviará instruções de tamanho de página para sua impressora. Quando uma impressora recebe as informações de cada página, e quando as informações que recebe não correspondem ao formato de página esperado, ela tem liberdade para determinar como lidará com os dados de saída. Por exemplo, pode esticar os dados de saída de uma página curta até caber no tamanho de papel esperado. No entanto, substituir este método com instruções diferentes pode fornecer funcionalidade significativa a outras formas de saída não dependentes de tamanhos de página físicos fixos, como HTML.

No exemplo a seguir, um objeto derivado da classe ReportListener substitui GetPageHeight de acordo com o valor de uma propriedade personalizada. O exemplo mostra uma visualização de duas execuções de relatório com alturas de página diferentes e usa o método DoMessage e a propriedade OutputPageCount do ReportListener para mostrar que as duas execuções de relatório para o mesmo relatório têm números diferentes de páginas.

```foxpro
LOCAL loReportListener, lcFRX
lcFRX = GETFILE("frx")
IF EMPTY(lcFRX)
   RETURN
ENDIF
loReportListener = CREATEOBJECT("halfSizePage")
REPORT FORM (lcFRX) OBJECT loReportListener
loReportListener.DoMessage("This report run was: " + ;
    TRANSF(loReportListener.OutputPageCount) + " pages long.")
loReportListener.wantHalfSizePage = .T.

REPORT FORM (lcFRX) OBJECT loReportListener
loReportListener.DoMessage("This report run was: " + ;
    TRANSF(loReportListener.OutputPageCount) + " pages long.")
DEFINE CLASS halfSizePage As ReportListener
   ListenerType = 1
   AllowModalMessages = .T.
   wantHalfSizePage = .F.

   PROCEDURE GetPageHeight()
     LOCAL liSize
     liSize = DODEFAULT()
   RETURN IIF(THIS.wantHalfSizePage, liSize/2, liSize)
ENDDEFINE
```
