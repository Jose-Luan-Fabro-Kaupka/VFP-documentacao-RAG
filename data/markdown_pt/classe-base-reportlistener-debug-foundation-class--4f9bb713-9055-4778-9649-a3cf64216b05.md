# Classe base ReportListener Debug Foundation Class

A classe DebugListener fornece saída de depuração para ajudar os desenvolvedores a entender o que acontece durante uma execução de relatório assistida por objetos.

| Category | Reporting |
| --- | --- |
| Default Catalog | Visual FoxPro Catalog\Foundation Classes\Output\Report Listeners |
| Class | DebugListener |
| Base Class | ReportListener |
| Class Library | _REPORTLISTENER.vcx |
| Parent Class | UtilityReportListener ( ReportListener Utility and File-handling Foundation Class ) |

# Observações

DebugListener adiciona as seguintes propriedades e métodos públicos à sua classe pai, UtilityReportListener.

| Properties and methods | Description |
| --- | --- |
| doDebug Method | Fornece informações de depuração para um evento ou método ReportListener. Syntax: DoDebug(p0, pCount, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12 Return Values: none Parameters: p0 is a string representing the caller, used as an identifying label in each debug output line. pCount is the value of PCOUNT() in the calling method, passed so doDebug knows how many parameters are significant for this debug output line. p1 through p12 are the parameters received by the caller, passed to this method for debug output. Remarks : DebugLister calls this method from every method of the ReportListener class relevant to a report run. Each call is the same, as follows: THIS.DoDebug(PROGRAM(), PCOUNT(), p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12) A second debug output method, private to the class, provides debug information on the state of the CommandClauses object and ReportListener member properties in the LoadReport , BeforeReport, AfterReport, and UnloadReport events. |
| includeLoadandUnload Property | Indica se as informações de depuração devem incluir valores dos eventos LoadReport e UnloadReport. Padrão .T. Observações: Você pode definir este valor como .F. se escrever código LoadReport que pode retornar .F. para encerrar anormalmente a execução do relatório. Você também pode definir este valor como .F. se não precisar dos dados adicionais dos métodos LoadReport e UnloadReport. Para obter mais informações, consulte ReportListener Object . |
| verbose Property | Especifica se o DebugListener deve incluir informações estendidas sobre valores de parâmetros do tipo objeto, bem como informações de page, alias e recno() para cada evento ou método. Padrão .F. |
