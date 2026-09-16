# Evento LoadReport

Ocorre antes da execução de um relatório e antes que a saída seja inicializada no evento BeforeReport. Fornece acesso às cláusulas do comando de relatório.

```foxpro
PROCEDURE Object.LoadReport
```

#### Parâmetros

Nenhum.

# Observações

Aplica-se a: objeto ReportListener.

LoadReport e UnloadReport são os dois eventos que delimitam a execução do relatório ou da etiqueta. Do ponto de vista do Sistema de Relatórios, a execução ainda não começou quando LoadReport é chamado e já terminou quando UnloadReport é chamado.

Consequentemente, esses eventos permitem realizar determinadas atividades de preparação e limpeza. Por exemplo, em LoadReport, você pode alterar o conteúdo da tabela de definição do relatório ou etiqueta (frx ou lbx), pois o Mecanismo de Relatórios e ReportListener ainda não leram a tabela. O trabalho de impressão ainda não começou, a menos que esse comando REPORT FORM continue um trabalho iniciado por um REPORT FORM anterior que usou NOPAGEEJECT; portanto, você pode alterar a configuração atual da impressora.

> **Observação:** Para obter informações sobre a ordem dos eventos na execução de um relatório, consulte Compreendendo relatórios assistidos por objeto do Visual FoxPro.

Se o código do evento LoadReport retornar False (`.F.`), o relatório não será executado. O spool de impressão não será aberto, a visualização não será instanciada, outros eventos Listener não serão chamados e assim por diante. Esse comportamento é semelhante ao evento Load de formulários e conjuntos de formulários: se Load retornar `.F.`, o formulário não será instanciado.

As cláusulas usadas para chamar REPORT FORM ou LABEL FORM ficam disponíveis em LoadReport; contudo, alguns valores ainda não foram calculados. Para obter mais informações, consulte a propriedade CommandClauses.

# Exemplo

Na definição de classe a seguir, o arquivo de definição de relatório (frx) especificado em REPORT FORM é "trocado" por um arquivo temporário durante LoadReport. Ele retorna à posição original durante UnloadReport.

```foxpro
DEFINE CLASS rlswap AS ReportListener
   ListenerType = 1  && to see the results, use a preview
   realFRX = ""
   useFRX = ""
   tempFRX = FORCEPATH(SYS(2015),SYS(2023))
   PROCEDURE LoadReport
      THIS.realFRX = THIS.CommandClauses.FILE
      THIS.useFRX = GETFILE("frx")
      IF EMPTY(THIS.useFRX)
         RETURN .F.
      ENDIF
      SET DATASESSION TO THIS.FRXDataSession
      SET SAFETY OFF  && it's scoped to session anyway
      THIS.ClearFRX(THIS.tempFRX)
      RENAME  (FORCEEXT(THIS.realFRX,"frx")) TO ;
               FORCEEXT(THIS.tempFRX,"frx")
      RENAME  (FORCEEXT(THIS.realFRX,"frt")) TO ;
               FORCEEXT(THIS.tempFRX,"frt")
      COPY FILE  (FORCEEXT(THIS.useFRX,"frx")) TO ;
               FORCEEXT(THIS.realFRX,"frx")
      COPY FILE  (FORCEEXT(THIS.useFRX,"frt")) TO ;
               FORCEEXT(THIS.realFRX,"frt")
   ENDPROC
   PROTECTED PROCEDURE clearFRX(tFRX)
      IF FILE(FORCEEXT(tFRX,"frx"))
         ERASE FORCEEXT(tFRX,"frx")) NORECYCLE
      ENDIF
      IF FILE(FORCEEXT(tFRX,"frt"))
         ERASE FORCEEXT(tFRX,"frt")) NORECYCLE
      ENDIF
   ENDPROC
   PROCEDURE UnloadReport
      SET DATASESSION TO THIS.FRXDataSession
      USE IN FRX
      THIS.clearFRX(THIS.realFRX)
      RENAME  (FORCEEXT(THIS.tempFRX,"frx")) TO ;
               FORCEEXT(THIS.realFRX,"frx")
      RENAME  (FORCEEXT(THIS.tempFRX,"frt")) TO ;
               FORCEEXT(THIS.realFRX,"frt")
   ENDPROC
ENDDEFINE
```
