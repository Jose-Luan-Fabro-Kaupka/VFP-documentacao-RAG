# Método CancelReport

Permite que o usuário ou um programa encerre anormalmente uma execução de relatório, de forma semelhante a pressionar Esc.

```foxpro
oReportListener.CancelReport()
```

#### Parâmetros

Nenhum.

# Valor de retorno

Nenhum.

# Observações

Aplica-se a: ReportListener Object.

Usando CancelReport, você pode encerrar um relatório antecipadamente. Quando você invoca este método, o ReportListener da classe base fornece o código de limpeza necessário, por exemplo fechando a fila de impressão, depois de verificar se um relatório está em execução antes de tentar suas tarefas de limpeza.

> **Importante:** Se você estiver depurando código de relatório ou tratando erros durante uma execução de relatório, deve invocar este método antes de emitir um comando CANCEL ou QUIT. Você também deve verificar se há uma execução de relatório ativa em procedimentos invocados por um manipulador ON SHUTDOWN. Você pode usar a função SYS(2040) para verificar se há um relatório ativo. Consulte SYS(2040) - Detect Report Status para obter mais informações.

Você pode adicionar ao código de limpeza interno do Visual FoxPro neste método. No entanto, você deve prever a possibilidade de este método ser chamado por fontes externas, como rotinas de tratamento de erros tentando encerrar um aplicativo de forma adequada. Por esse motivo, seu código neste método não deve falhar mesmo se um relatório não estiver em execução ativa, de forma semelhante ao comportamento nativo do ReportListener.

Por exemplo, se seu código define uma propriedade global indicando que um relatório falhou ao ser executado, ele deve garantir que o ReportListener estava realmente no processo de executar um relatório antes de definir o sinalizador.

Quando você invoca CancelReport, os eventos normais de relatório continuam até o final da página atual. Depois disso, o código de limpeza nativo é executado, seguido pelos eventos AfterReport e UnloadReport. Para obter mais informações sobre a sequência de eventos de relatório e o período durante o qual você pode cancelar um relatório com sucesso, consulte Understanding Visual FoxPro Object-Assisted Reporting.

Você pode verificar se uma chamada a CancelReport ocorreu, encerrando anormalmente o relatório, usando a função SYS(2024). Para obter mais informações, consulte SYS(2024) - Detect Report Cancellation.

> **Dica:** Você pode oferecer aos usuários a oportunidade de cancelar um relatório neste método, mas também oferecer a escolha de continuar a execução do relatório. Use NODEFAULT no método CancelReport para continuar a execução do relatório. O ReportListener User Feedback Foundation Class adota essa abordagem. Consulte o método DoMessage para o texto completo do código do método CancelReport desta classe. Consulte ReportListener User Feedback Foundation Class para obter mais informações.
