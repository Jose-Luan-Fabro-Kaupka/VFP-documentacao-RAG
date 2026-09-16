# Propriedade OutputPageCount

Fornece o número de páginas que foram renderizadas e podem ser acessadas usando o método OutputPage.

```foxpro
ReportListener.OutputPageCount
```

# Valor de retorno

Tipo de dados Integer.

O valor padrão é 0. Esta propriedade é somente leitura.

# Observações

Aplica-se a: objeto ReportListener.

OutputPageCount fornece o número de páginas renderizadas durante a execução de um relatório. Se você usar a cláusula RANGE no comando LABEL ou REPORT FORM, esse número poderá ser menor que o número total de páginas no escopo do relatório.

As páginas em OutputPageCount são as únicas que você pode solicitar do ReportListener usando o método OutputPage.

> **Observação:** Exatamente como ou quando você pode solicitar essas páginas usando OutputPage depende de o mecanismo estar no modo de uma página por vez (valores de ListenerType orientados para impressão 0 e 2) ou no modo de todas as páginas de uma vez (valores de ListenerType orientados para visualização 1 e 3). Para obter mais informações, consulte Método OutputPage.

OutputPageCount não é redefinida entre relatórios, portanto você pode verificar seu valor entre as execuções. Quando um relatório é executado, OutputPageCount é definida como 0 antes de LoadReport, a menos que a execução anterior tenha usado a palavra-chave NOPAGEEJECT. Durante a passagem de cálculo, ela permanece com um valor constante, 0 ou o valor retido da última execução do relatório caso NOPAGEEJECT tenha sido usado, se o relatório estiver passando por várias passagens.

OutputPageCount não muda durante LoadReport ou BeforeReport. Ela é incrementada ao final de cada página incluída na saída. Portanto, a partir do evento AfterReport, OutputPageCount contém todas as páginas incluídas na saída até então, para o relatório atual e para quaisquer relatórios anteriores encadeados a ele usando NOPAGEEJECT.

> **Observação:** A classe base ReportListener determina se uma página é incluída na saída invocando internamente o método IncludePageInOutput. Em um relatório com várias passagens, ReportListener faz essa determinação somente na segunda passagem.

Para obter mais informações sobre como os componentes nativos do sistema de relatórios atribuem o valor de OutputPageCount e outros valores no início e no fim de uma execução de relatório, consulte Compreendendo os relatórios assistidos por objetos do Visual FoxPro.
