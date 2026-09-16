# Classes Foundation ReportListener

O Sistema de Relatórios do Visual FoxPro 9 inclui diversos recursos novos voltados à extensibilidade, incluindo uma nova classe base ReportListener. Quando você usa classes baseadas em ReportListener, o Report Engine do Visual FoxPro executa seu comando REPORT FORM ou LABEL FORM em um novo modo de relatório assistido por objetos.

As classes na biblioteca de classes Foundation _REPORTLISTENER.vcx demonstram esses recursos. Elas fornecem acesso fácil às classes ReportListener derivadas fornecidas com o Report Output Application.

As classes baseadas em ReportListener nesta biblioteca de classes são idênticas às classes integradas ao Report Output Application. No entanto, elas não dependem de REPORTOUTPUT.APP. Quando você deseja usar essas classes em aplicações, pode incluir a biblioteca de classes _REPORTLISTENER.vcx da pasta Foundation Class (FFC) em seu projeto e ter a garantia de que possui todos os arquivos necessários.

> **Dica:** Algumas das classes nesta biblioteca usam classes auxiliares. Você encontrará essas classes auxiliares em uma biblioteca complementar, _FRXCURSOR.vcx, que também está incluída na pasta Foundation Class. Ao compilar _REPORTLISTENER.vcx em sua aplicação, o Project Manager observará a referência à biblioteca de classes _FRXCURSOR e incluirá os arquivos apropriados automaticamente.

# Nesta Seção

| Classe | Descrição |
| --- | --- |
| ReportListener Base Foundation Class | Esta classe, _ReportListener, serve como superclasse para as outras classes em _REPORTLISTENER.vcx. Ela fornece serviços centrais semelhantes às superclasses de outras classes base do Visual FoxPro disponíveis em _BASE.vcx. |
| ReportListener FXListener Foundation Class | A classe FXListener permite alterar as características de exibição dos controles de relatório durante a execução de um relatório. Ela usa duas coleções de membros: FXs (instruções de ajuste de conteúdo e formato) e GFXs (ajuste ou substituição da renderização GDIPlus-graphics). |
| ReportListener Utility and File-handling Foundation Class | A classe UtilityReportListener fornece opções de configuração em tempo de execução e manipulação de arquivos. |
| ReportListener User Feedback Foundation Class | A classe UpdateListener fornece feedback ao usuário durante execuções de relatório. O Report Output Application usa UpdateListener como sua classe ReportListener padrão designada para saída de Impressão e Visualização (valores ListenerType 0 e 1). |
| ReportListener XML Foundation Class | A classe XmlListener fornece saída XML de uma execução de relatório. O Report Output Application usa XmlListener como sua classe ReportListener padrão designada para saída XML (valor ListenerType 4). |
| ReportListener XML Display-Style Foundation Class | XmlDisplayListener ajusta as configurações XML de XmlListener de forma adequada para necessidades de saída de apresentação. Ela adiciona funcionalidade de publicação de arquivos de imagem. |
| ReportListener HTML Foundation Class | HtmlListener aplica especificações personalizadas para produção de HTML à saída XML de XmlDisplayListener. O Report Output Application usa HtmlListener como sua classe ReportListener padrão designada para saída HTML (valor ListenerType 5). |
| ReportListener Debug Foundation Class | A classe DebugListener fornece saída de depuração para ajudar desenvolvedores a entender o que acontece durante uma execução de relatório assistida por objetos. |

# Seções Relacionadas

Extending Report Functionality in Visual FoxPro

Understanding the Report Output Application

Using VFP Report Output XML
