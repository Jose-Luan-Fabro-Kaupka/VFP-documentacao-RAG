# Tratamento de erros durante execuções de relatório

O Visual FoxPro 9.0 oferece melhorias significativas no processo de criação de saída, incluindo novas oportunidades para invocar código de aplicativo durante os procedimentos internos de manipulação de dados e renderização de saída do Report System nativo. Para fornecer adequadamente aos usuários a capacidade de desenvolver tais programas, o Visual FoxPro 9.0 também aprimora o relatório de erros e a depuração durante uma execução de relatório.

Este tópico aborda recursos de tratamento de erros com significado especial para relatórios e examina diferentes estratégias para lidar com conclusões anormais de execuções de relatório.

> **Observação:** Componentes de aplicativo como o Report Output Application e o Report Preview Application trabalham em conjunto com o Visual FoxPro Report System durante o processamento de saída. Eles funcionam como fábricas para fornecer referências de objeto apropriadas ao Report Engine. Embora esses componentes possam gerar erros e exigir depuração, eles não estão ativos durante a execução interna do relatório, que abrange eventos de processamento do evento BeforeReport ao evento AfterReport. Você pode depurar quaisquer problemas com esses componentes de maneira semelhante a qualquer outro aplicativo Visual FoxPro; eles não são abordados por este tópico. Para obter mais informações sobre a sequência de eventos em uma execução de relatório, consulte Understanding Visual FoxPro Object-Assisted Reporting.

> **Dica:** Você pode usar todas as ferramentas padrão de depuração do Visual FoxPro, como a Trace Window, ao examinar seu código de relatório. Você também encontrará a ReportListener Debug Foundation Class útil ao investigar sequências de eventos de relatório.

# Estratégias para tratamento de erros durante uma execução de relatório

Como a sequência de processamento de saída do Visual FoxPro pode incluir código de usuário extenso, você pode precisar encerrar uma execução de relatório antes de sua conclusão devido a um erro de código. Você também pode querer encerrar uma execução de relatório prematuramente porque um usuário final deseja interromper o relatório. Além disso, um manipulador de erros externo pode detectar um motivo para encerrar seu aplicativo enquanto uma execução de relatório está em andamento.

Em todas essas situações, você pode chamar o método CancelReport do ReportListener para garantir que o Visual FoxPro execute qualquer limpeza especial necessária, como fechar uma fila de impressão, para encerrar o relatório e seu aplicativo com segurança. Consulte o método CancelReport para obter mais informações.

A ReportListener User Feedback Foundation Class fornece um bom modelo para cancelar um relatório em resposta a uma solicitação do usuário final. Consulte o tópico do método DoMessage para o código no método CancelReport desta classe. Observe que o método emite NODEFAULT se o usuário final optar por retomar a execução do relatório em resposta a uma caixa de diálogo. Seu código pode seguir uma estratégia semelhante em resposta a erros recuperáveis. Para erros críticos, você pode preferir encerrar o relatório unilateralmente e encerrar o aplicativo após a limpeza do relatório.

Você pode verificar se o relatório terminou normalmente usando a função SYS(2024). Esta função retornará "Y" durante uma execução de relatório, até a conclusão do evento Unload, se o relatório não completou sua execução normalmente. Neste ponto, o processamento interno do Visual FoxPro Report System foi concluído. Se você determinar que o encerramento anormal da execução do relatório não ocorreu como resposta a uma solicitação do usuário final, você pode executar CANCEL ou QUIT com segurança ou solicitar tratamento semelhante de um objeto de aplicativo externo. Para obter mais informações, consulte Microsoft Visual FoxPro Technical Support.

### Exemplo 1: Cancelando um relatório

No exemplo a seguir, um erro ocorre no evento BeforeReport de um ReportListener, e seu evento Error responde chamando o método CancelReport da classe. O código do evento UnLoadReport relata o valor de SYS(2024) como "Y", como resultado da ação do evento Error.

> **Observação:** Se o erro ocorreu durante o evento LoadReport, SYS(2024) não retornaria "Y". Nenhum processamento interno ocorreu ainda, portanto não haveria nada para o Report Engine limpar.

```foxpro
DEFINE CLASS errorListener as ReportListener
  PROCEDURE BeforeReport()
    REPORT FORM ?
  ENDPROC
  PROCEDURE Error(nError, cMethod, nLine)
     WAIT WINDOW MESSAGE()
     * MESSAGE() will report:
     * Report contains a nesting error.
     THIS.CancelReport()
  ENDPROC
  PROCEDURE UnloadReport()
     WAIT WINDOW SYS(2024)
     * SYS(2024) will report: "Y"
  ENDPROC
ENDDEFINE
```

### Exemplo 2: Encerrando um aplicativo como resultado de erro de relatório

No exemplo acima, a classe derivada de ReportListener trata o erro. Você pode preferir propagar o evento de erro para um manipulador de aplicativo externo para determinação da ação apropriada. Neste caso, o aplicativo externo precisa saber que uma execução de relatório estava em andamento quando o erro ocorreu, para que possa cancelar o relatório adequadamente antes de encerrar o aplicativo.

Para determinar que uma execução de relatório está em andamento em código externo, use a função SYS(2040). Para obter mais informações, consulte SYS(2040) - Detect Report Status.

O exemplo a seguir verifica o valor de retorno de SYS(2040) em um manipulador do comando ON ERROR.

```foxpro
PUBLIC oApp
oApp = CREATEOBJECT("MyApp")
ON ERROR oApp.ErrorHandler()
WAIT WINDOW "Some processing here..."
REPORT FORM ? OBJECT oApp.oE
WAIT WINDOW ;
  "Some more processing here, " + ;
  "will not occur because of error..."
DEFINE CLASS MyApp AS Custom
   oE = NULL
   PROCEDURE Init
      THIS.oE = CREATEOBJECT("errorListener")
   ENDPROC
   PROCEDURE ErrorHandler
     MESSAGEBOX("Error! " + MESSAGE())
     IF SYS(2040) # "0"
       THIS.oE.cancelReport()
     ENDIF
    IF _VFP.StartMode = 0
       CANCEL
    ELSE
       QUIT
    ENDIF
  ENDPROC
ENDDEFINE
DEFINE CLASS errorListener as ReportListener
  PROCEDURE BeforeBand()
    * parameters are missing
  ENDPROC
  PROCEDURE CancelReport()
    DODEFAULT()
    MESSAGEBOX("Cancelling Report!")
  ENDPROC
ENDDEFINE
```

### Exemplo 3: Cancelando um relatório durante o encerramento do aplicativo

Você pode usar uma estratégia semelhante em um manipulador ON SHUTDOWN se for possível que este manipulador seja chamado durante uma execução de relatório. O manipulador ON SHUTDOWN precisa de uma referência ao objeto ReportListener apropriado, assim como o objeto de aplicativo no exemplo acima. Para obter mais informações, consulte o comando ON SHUTDOWN.

> **Dica:** Timers não são disparados durante uma execução de relatório ou etiqueta. No entanto, é frequentemente possível que usuários finais decidam fechar seu aplicativo enquanto o Visual FoxPro está gerando saída. Portanto, não presuma que a necessidade de cancelar um relatório está sempre associada a um erro.

Você pode usar o exemplo simples a seguir para verificar essa capacidade.

```foxpro
PUBLIC rl
ON SHUTDOWN DO MyShutdown
rl = CREATEOBJECT("reportListener")
REPORT FORM ? OBJECT rl  && use a long report!
* use the close box on the main Visual FoxPro
* window while the report runs.
PROCEDURE MyShutDown
  IF SYS(2040) # "0"
     MESSAGEBOX("Now Cancelling Report!")
     rl.CancelReport()
  ENDIF
  ON SHUTDOWN
  IF _VFP.StartMode = 0
     CANCEL
  ELSE
     QUIT
  ENDIF
ENDPROC
```

### Exemplo 4: Usando o evento Error de um ReportListener

Em dois dos três exemplos acima, a classe ReportListener não possui código de evento Error. Se você incluir tratamento de evento Error em uma classe ReportListener, como mostrado no primeiro exemplo, este código pode decidir tratar ou propagar qualquer erro que receba.

Se o evento Error trata um erro, ele pode usar CANCEL ou QUIT com segurança. Você pode usar esses comandos em outros eventos ou métodos do ReportListener também. Certifique-se de invocar o método CancelReport() do ReportListener antes de emitir a instrução CANCEL ou QUIT, no entanto.

No próximo exemplo, a classe ReportListener usa seu evento Error para tratar o erro e depois encerra o relatório imediatamente.

> **Dica:** O evento Error do ReportListener não tratará erros que ocorrem durante uma execução de relatório, mas fora do próprio código do ReportListener, como um erro em uma função definida pelo usuário (UDF) dentro do relatório ou um erro em uma expressão de relatório. Por esse motivo, ter código de evento Error no ReportListener não libera seu manipulador de erros externo da responsabilidade de estar ciente de erros de relatório. Uma combinação de abordagens é necessária para tratar todos os tipos de erros que podem ocorrer durante uma execução de relatório.

```foxpro
LOCAL oE
oE = CREATEOBJECT("errorListener")
WAIT WINDOW "Some processing here..."
REPORT FORM ? OBJECT oE
WAIT WINDOW ;
  "Some more processing here, " + ;
  "will not occur because of error..."

DEFINE CLASS errorListener as ReportListener
  PROCEDURE BeforeBand()
    * parameters are missing
  ENDPROC
  PROCEDURE Error(nError, cMethod, nLine)
   WAIT WINDOW "Error occured! " + CHR(13) + ;
               "SYS(2024) before CancelReport: " + SYS(2024)
   THIS.CancelReport()
   CANCEL
  ENDPROC
  PROCEDURE CancelReport()
    IF SYS(2040) # "0"
       MESSAGEBOX("Cancelling Report!")
       DODEFAULT()
       WAIT WINDOW "SYS(2024) is now: " + SYS(2024)
    ENDIF
  ENDPROC
ENDDEFINE
```

### Exemplo 5: Usando tratamento estruturado de erros com relatórios

Como estratégia final, você pode usar tratamento estruturado de erros com relatórios. Quando você executa o código de exemplo abaixo, no entanto, observe que seu código não chega à construção CATCH até depois que a execução do relatório terminou, da perspectiva do Report System. Embora você possa usar o método CancelReport, o código de usuário que você executa neste método deve ser projetado para executar com segurança, independentemente de um relatório estar realmente em andamento.

```foxpro
LOCAL oE
TRY
  oE = CREATEOBJECT("errorListener")
  WAIT WINDOW "Some processing here..."
  REPORT FORM ? OBJECT oE
  WAIT WINDOW ;
  "Some more processing here, " + ;
  "will not occur because of error..."
CATCH WHEN .T.
   WAIT WINDOW "An error occured! " + CHR(13) + ;
               "SYS(2024)=" + SYS(2024) + CHR(13) + ;
               "SYS(2040)=" + SYS(2040)
   * SYS(2024) will report "N"
   * SYS(2040) will report "0"
   oE.CancelReport()
ENDTRY

DEFINE CLASS errorListener as ReportListener
  PROCEDURE BeforeBand()
    * parameters are missing
  ENDPROC
  PROCEDURE CancelReport()
    IF SYS(2040) = "0"
       MESSAGEBOX("No report in progress, " + CHR(13) + ;
                  "but this method can still do user cleanup!")
       NODEFAULT
    ELSE
       MESSAGEBOX("Cancelling Report!")
       DODEFAULT()
    ENDIF
  ENDPROC
ENDDEFINE
```

# Erros durante uma execução de relatório que não ocorrem em linhas de código

No Visual FoxPro 9.0 e em todas as versões anteriores, é possível que erros ocorram durante execuções de relatório que não estão especificamente associados a uma linha rastreável de código de usuário. Esses erros incluem expressões de relatório ou variáveis de relatório que o Report Engine não pode resolver, bem como dificuldades ao inicializar o Data Environment do relatório.

O Visual FoxPro 9.0 mantém compatibilidade com versões anteriores em seu tratamento de tais erros, conforme descrito nesta seção.

Quando um erro ocorre fora do código de usuário, o tratamento interno de erros do Visual FoxPro não oferece a você a oportunidade de suspender o relatório, porque não há linha de código na qual suspender.

Se você não tem um manipulador ON ERROR ou uma construção TRY… ENDTRY em vigor, o Visual FoxPro não invoca seu tratamento de erros até depois de executar sua limpeza interna e encerrar a execução do relatório.

Como demonstrado nos exemplos deste tópico, o valor da função MESSAGE() está disponível se ocorrer em código do ReportListener ou em outro código de usuário que você invoque durante uma execução de relatório. No entanto, se o erro não está associado a uma linha de código, MESSAGE() não é atribuído até depois que o Report Engine conclui sua limpeza.

Se um erro não está associado a uma linha de código, o valor de MESSAGE() não é atribuído de forma alguma, a menos que você tenha alguma forma de tratamento de erros em vigor no momento em que o comando REPORT FORM ou LABEL ocorre. Se você não tem um manipulador de erros e se usou o comando CLEAR ERROR antes da execução do relatório, MESSAGE() ainda está vazio após a execução do relatório. Se você não usou CLEAR ERROR, MESSAGE() mantém seu valor anterior.

# Comandos não suportados durante uma execução de relatório

Para tratar erros adequadamente, você deve começar planejando usar somente comandos que são seguros para usar durante uma execução de relatório.

Os comandos do Visual FoxPro na tabela abaixo não são suportados durante o processamento interno de saída, entre o evento BeforeReport e o evento AfterReport (inclusive).

Nem todos os erros nesta tabela gerarão um erro imediato, mas o uso desses comandos durante o processamento de saída leva a resultados imprevisíveis.

Esses comandos não são suportados, quer ocorram:
 - Diretamente no código de evento do ReportListener.
- Em código adicional invocado por um ReportListener, como código em uma biblioteca de procedimentos.
- Na janela de comando enquanto a execução está suspensa.
- Usando código invocado diretamente em expressões de relatório ou etiqueta, como funções definidas pelo usuário (UDFs).

Em alguns casos, conforme indicado na tabela, os comandos também não são suportados no evento LoadReport e no evento UnloadReport do ReportListener. Esses dois eventos de enquadramento fornecem ganchos de usuário em cada extremidade da execução de processamento interno.

Como caso final excepcional, enquanto o método OutputPage pode estar em execução após a conclusão da execução do relatório, se chamado por um objeto PreviewContainer, este método pode precisar de acesso a recursos incorporados no aplicativo, como arquivos de imagem, para executar sua tarefa. Por esse motivo, usar comandos como CLEAR ALL que podem descarregar o aplicativo chamador da memória não é suportado até que a visualização seja concluída. Quando o comando REPORT FORM ou LABEL inclui a palavra-chave NOWAIT, a visualização é concluída no momento em que a janela de visualização é fechada, a menos que o usuário escolha imprimir a partir da visualização. Se o usuário escolher imprimir, a visualização é concluída no momento em que o Visual FoxPro termina de enviar a saída do relatório para a impressora.

> **Observação:** Além dos comandos listados abaixo, todos os comandos que alteram sessões, áreas de trabalho, ponteiros de registro ou outros atributos dos dados sobre os quais os comandos REPORT FORM e LABEL atuam devem ser usados com cautela. Como em versões anteriores do Visual FoxPro, é responsabilidade do usuário restaurar o estado dos dados adequadamente ao usar esses comandos, com o entendimento de que outros ReportListeners e código de usuário adicional, bem como o Report Engine interno, podem ser afetados por suas alterações. Por exemplo, embora o comando BROWSE não apareça nesta tabela, ele tem potencial para alterar o ponteiro de registro, disparar código adicional anexado por meio de funções definidas pelo usuário (UDFs) e afetar relacionamentos de dados, portanto deve ser usado com cautela.

| Comando(s) | Suportado nos eventos LoadReport e UnloadReport? | Observações |
| --- | --- | --- |
| CLEAR ALL RELEASE ALL CLOSE ALL | Não | Esta restrição visa principalmente preservar a referência do ReportListener e as tabelas de dados conforme esperado pelo Report Engine durante seu processamento do escopo do relatório. |
| RETRY RETURN TO MASTER RETURN TO <Procedure Name> | Não | |
| ?, ??, ??? \, \ @... SAY EJECT, EJECT PAGE PRINTJOB… ENDPRINTJOB LIST, DISPLAY, TYPE SET DEVICE,PRINTER | Sim | Esses comandos de saída são suportados durante a execução de saída se o dispositivo de destino para a execução de saída for diferente do dispositivo de destino para o comando de saída. Por exemplo, se seu comando REPORT FORM tem uma cláusula PREVIEW, você pode LIST MEMO TO <filename> durante a execução do relatório. |
| BEGIN TRANSACTION e comandos adicionais relacionados a transação | Sim | Comandos de transação são suportados se a transação for concluída dentro de um procedimento invocado ou de um evento do ReportListener. |
| MODIFY/CREATE CLASS, FORM, LABEL, REPORT […] | Sim | Todos os comandos que invocam Designers interativos do Visual FoxPro não são suportados, sejam modais ou invocados com a palavra-chave NOWAIT. Você pode invocar um editor de texto ( MODIFY FILE ou COMMAND ). |
| REPORT FORM LABEL | Não | Os comandos REPORT FORM e LABEL não podem ser aninhados. |

# Erros associados ao Visual FoxPro Report System

A tabela a seguir fornece uma lista de erros que podem ocorrer por motivos específicos ao processamento em tempo de execução de relatórios e etiquetas.

| Mensagem de erro e número | Causa ou cenário |
| --- | --- |
| "name" is not an object (Error 1924) | O Engine recebeu um comando REPORT FORM ou LABEL com uma cláusula OBJECT <ref> e <ref> não era um objeto. |
| Class definition "name" is not found (Error 1733) | O Engine recebeu uma referência NULL como resultado de uma cláusula OBJECT TYPE <N> em um comando REPORT FORM ou LABEL, indicando que o aplicativo especificado na variável de sistema _REPORTOUTPUT não pôde resolver este valor para uma referência de objeto ReportListener Object. |
| Data type is invalid for this property (Error 1732) | O Engine recebeu uma cláusula OBJECT TYPE <N> em um comando REPORT FORM ou LABEL, e o parâmetro <N> não era de tipo numérico. Este erro também pode ocorrer em conexão com o uso do método OutputPage, discutido abaixo. |
| Report contains a nesting error (Error 1645) | Um comando REPORT FORM ou LABEL foi invocado durante outra execução de relatório ou etiqueta. Observe que este erro ainda ocorre se o comando aninhado usa o modo de relatório compatível com versões anteriores, se um relatório diferente é solicitado ou se o comando aninhado inclui uma referência a um objeto ReportListener diferente. |
| Syntax error (Error 10) | O comando SET REPORTBEHAVIOR foi emitido com um parâmetro incorreto. |
| The current object does not inherit from class "name" (Error 1935) | O Engine recebeu uma referência de objeto que não herda da classe base ReportListener do Visual FoxPro. |
| Variable "variable" is not found (Error 12) | O Engine recebeu uma cláusula OBJECT TYPE <N> em um comando REPORT FORM ou LABEL, e o aplicativo especificado na variável de sistema _REPORTOUTPUT não pôde ser encontrado ou a variável estava vazia. |
| Must specify additional parameters (Error 94) Function argument value, type, or count is invalid (Error 11) Data type is invalid for this property (Error 1732) Error writing to file "file" (Error 1105) Output page "page" is not available (Error 2194) | Os erros neste grupo indicam que o método OutputPage do ReportListener foi invocado incorretamente. Para obter mais informações, consulte o método OutputPage. |
