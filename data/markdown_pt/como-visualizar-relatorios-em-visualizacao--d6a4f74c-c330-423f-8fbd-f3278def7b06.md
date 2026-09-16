# Como: visualizar relatórios em visualização

Você pode visualizar um relatório em uma janela de visualização antes de enviá-lo a um destino de saída.

> **Observação:** As ações discutidas neste tópico têm resultados diferentes, dependendo da configuração de REPORTBEHAVIOR. Quando você usa o comando SET REPORTBEHAVIOR 90, o Visual FoxPro usa um objeto ReportListener para gerar seus resultados por meio de GDI+ em vez de GDI. Os resultados do processo de geração são enviados por uma interface de visualização diferente. Para obter mais informações, consulte SET REPORTBEHAVIOR Command e _REPORTPREVIEW System Variable.

### Para visualizar um relatório
- Abra o relatório ou etiqueta no designer apropriado.
- No menu View, clique em Preview. A janela de visualização e a Print Preview toolbar abrem para que você possa navegar pelo relatório.
- Para navegar na janela de visualização, você pode executar o seguinte usando a Print Preview toolbar: Para percorrer o relatório, clique em First Page, Previous Page, Go to Page, Next Page ou Last Page. Para alterar o tamanho da visualização, escolha um nível de zoom. Para imprimir o relatório, clique em Print. Para retornar ao modo de design, clique em Close Preview. Cuidado Ao fechar a janela de visualização, você pode ser solicitado a salvar suas alterações em um arquivo. Se receber este prompt, a seleção que você fizer não apenas fecha a janela de visualização, mas também o arquivo de layout de relatório. Para retornar ao modo de visualização, clique em Cancel. Para salvar suas alterações e fechar a janela de visualização e o arquivo de layout de relatório, clique em Save. Para deixar as alterações no layout sem salvar, clique em No.

### Para visualizar um relatório programaticamente
- Use o comando REPORT FORM ou LABEL FORM com a cláusula PREVIEW.

Para obter mais informações, consulte REPORT FORM Command e LABEL Command.

Por exemplo, o código a seguir exibe o relatório em uma janela de visualização modal:

```foxpro
REPORT FORM MyReport.FRX PREVIEW
```

 - Use o comando REPORT FORM ou LABEL FORM com a cláusula OBJECT TYPE 1 para solicitar explicitamente visualização assistida por objetos. Você também pode usar uma referência OBJECT no comando com uma referência a um objeto ReportListener e definir o valor da propriedade ListenerType do objeto como 1:

```foxpro
REPORT FORM MyReport.FRX OBJECT TYPE 1 &&preview
* - OR -
LOCAL loReportListener
loReportListener = CREATEOBJECT("ReportListener")
loReportListener.ListenerType = 1
REPORT FORM MyReport.FRX OBJECT loReportListener
```

Para obter mais informações, consulte ListenerType Property.
