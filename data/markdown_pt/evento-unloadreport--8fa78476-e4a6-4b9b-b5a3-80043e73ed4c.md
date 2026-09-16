# Evento UnloadReport

Ocorre ao final da execução de um relatório, depois que a saída foi finalizada no evento AfterReport.

```foxpro
PROCEDURE Object.UnloadReport
```

#### Parâmetros

Nenhum.

# Observações

Aplica-se a: Objeto ReportListener.

LoadReport e UnloadReport são os dois eventos de enquadramento da execução de relatório ou etiqueta; do ponto de vista do Sistema de Relatórios, a execução do relatório ainda não começou quando ele invoca LoadReport, e a execução do relatório já terminou quando invoca UnloadReport. Para mais informações e um exemplo de uso, consulte Evento LoadReport.
