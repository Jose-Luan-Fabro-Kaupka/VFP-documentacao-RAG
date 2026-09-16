# Propriedade FRXDataSession

Fornece o ID do datasession no qual o Report Engine coloca uma cópia privada do arquivo de relatório ou etiqueta (frx ou lbx) para uso do ReportListener durante uma execução de relatório.

```foxpro
ReportListener.FRXDataSession
```

# Valor de retorno

Tipo de dados Integer.

O valor padrão é -1 quando você cria a instância de ReportListener, indicando que o datasession especial não existe neste ponto.

# Observações

Aplica-se a: ReportListener Object.

Esta propriedade contém um valor válido (o ID de um datasession existente) de LoadReport até UnloadReport. No entanto, o Report Engine não abre a cópia somente leitura do arquivo de relatório ou etiqueta até depois do evento LoadReport e antes do evento BeforeReport. Isso dá a você a chance de manipular o arquivo de relatório ou etiqueta antes que o Report Engine leia as informações de layout do arquivo de relatório ou etiqueta e inicie a execução do relatório. Para obter mais informações sobre a ordem dos eventos durante o processamento em tempo de execução, consulte Understanding Visual FoxPro Object-Assisted Reporting.

> **Importante:** A cópia do arquivo de relatório ou etiqueta fornecida pelo Report Engine neste data session durante a execução é somente leitura. O ReportEngine e o ReportListener nativo não consultam o arquivo de relatório ou etiqueta durante a execução do relatório, depois de terem lido suas informações de layout durante os procedimentos de inicialização do relatório. Se o cursor fosse leitura/gravação e você fizesse alterações em seus dados, as alterações não seriam significativas para os componentes nativos de relatório do Visual FoxPro. A cópia do arquivo de relatório ou etiqueta é puramente para sua referência enquanto o relatório é executado. Você pode alterar certos aspectos de como o relatório renderiza vários objetos de layout, usando eventos do ReportListener. Para obter mais informações, consulte AdjustObjectSize Event e EvaluateContents Event.
