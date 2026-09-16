# SYS(2024) - Detectar cancelamento de relatório

Esta função fornece informações sobre se um relatório foi concluído normalmente ou foi cancelado.

```foxpro
SYS(2024)
```

#### Parâmetros

Nenhum.

# Valor de retorno

Caractere. Retorna "Y" se o relatório atual foi interrompido antes de processar todo o escopo de dados. Retorna "N" se não houver relatório atual ou se o relatório atual não foi interrompido.

# Observações

Um relatório é considerado "interrompido" pelo Sistema de Relatórios do Visual FoxPro se uma das seguintes ações ocorrer:
 - O relatório está sendo executado no modo de relatório assistido por objetos, e um programa invoca o método CancelReport de um ReportListener antes que o relatório seja completamente processado. Para obter mais informações, consulte CancelReport Method.
- Um usuário pressiona ESC ou o botão Cancel no modo de relatório compatível com versões anteriores. Quando isso acontece, o valor SYS(2024) está disponível internamente para o mecanismo de relatório, embora possa não haver forma de os usuários acessarem o valor.
- Ocorre um erro de programa em código executado durante um relatório, seja em uma função definida pelo usuário ou em métodos de ReportListener, e o usuário opta por Cancel na caixa de diálogo de erro resultante.

Durante um relatório interrompido, SYS(2024) continua retornando "Y" até após a sequência completa de eventos do relatório. O valor de retorno desta função é redefinido para "N" após o evento UnloadReport terminar. Para obter mais informações, consulte UnloadReport Event.

# Exemplo

O código de exemplo a seguir é da classe utilityReportListener, responsável pelos procedimentos de manipulação de arquivos. Quando fecha um arquivo ao final da execução de um relatório, verifica que tipo de mensagem deve ser exibida ao usuário sobre o sucesso ou falha da execução do relatório. Se a execução do relatório não teve erros, a classe usa SYS(2024) para determinar se os resultados da execução do relatório estão completos antes de montar uma mensagem apropriada. Para obter mais informações sobre esta classe, consulte ReportListener Utility and File-handling Foundation Class.

```foxpro
* excerpted from
* utilityReportListener.closeTargetFile method
IF THIS.HadError
   THIS.DoMessage(OUTPUTCLASS_CREATEERRORS_LOC, ;
                  MB_ICONEXCLAMATION )
ELSE
   THIS.DoMessage( OUTPUTCLASS_SUCCESS_LOC + ;
                   IIF(SYS(2024)="Y", ;
                   CHR(13)+OUTPUTCLASS_REPORT_INCOMPLETE_LOC,""),;
                   MB_ICONINFORMATION)
ENDIF
```
