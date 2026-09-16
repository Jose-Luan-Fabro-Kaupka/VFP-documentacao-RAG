# Método GetPageWidth

Retorna a largura da página em 960 pontos por polegada (dpi) durante a execução de um relatório.

```foxpro
iPageWidth = oReportListener.GetPageWidth()
```

#### Parâmetros

Nenhum.

# Valor de retorno

Tipo de dados Integer, a largura da página em pontos por polegada. Entre execuções de relatório, este método retorna `0`.

# Observações

Aplica-se a: Objeto ReportListener.

Este método e GetPageHeight permitem que um objeto de visualização ou qualquer outro “participante” do processo de saída consulte o objeto ReportListener para obter as dimensões da página, conforme determinadas pelas configurações da impressora vigentes na execução do relatório. O PreviewContainer do ReportListener usa esses métodos quando o objeto ReportListener chama seu método Show, para determinar como exibir o conteúdo do relatório atual.

Esses métodos fornecem valores utilizáveis em todos os pontos do processo de relatório após BeforeReport e antes de UnloadReport, a menos que você invoque continuação usando NOPAGEEJECT no comando REPORT FORM. Se usar NOPAGEEJECT, eles continuarão fornecendo resultados utilizáveis até que um REPORT FORM sem NOPAGEEJECT chegue ao evento UnloadReport. Em outros momentos, ambos retornam 0.

> **Observação:** O período em que GetPageHeight e GetPageWidth fornecem valores utilizáveis é determinado pelo momento em que ReportListener configura o layout da página e o trabalho de impressão. ReportListener não reavalia o layout e as dimensões entre comandos REPORT FORM quando você usa NOPAGEEJECT, pois essas execuções fazem parte de um único trabalho de impressão. Contudo, você pode criar classes derivadas de ReportListener capazes de tratar vários tamanhos de página durante uma execução continuada.

Para obter mais informações sobre a sequência de eventos no início e no fim de uma execução de relatório, consulte Entendendo relatórios do Visual FoxPro auxiliados por objetos.

Para ver código de exemplo ilustrativo e comentários sobre o uso apropriado, consulte Método GetPageHeight.
