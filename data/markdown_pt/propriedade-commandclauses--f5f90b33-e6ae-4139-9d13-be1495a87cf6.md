# Propriedade CommandClauses

Fornece uma lista das opções especificadas para um comando REPORT FORM ou LABEL.

```foxpro
ReportListener.CommandClauses
```

# Valor de retorno

Um objeto da classe Empty, durante ou após a execução de um comando REPORT FORM ou LABEL.

O valor padrão quando você cria pela primeira vez uma instância do objeto ReportListener é null (.NULL.)

# Observações

Aplica-se a: objeto ReportListener.

O Report Engine fornece um objeto CommandClauses ao ReportListener durante uma execução de relatório, para que o ReportListener possa tomar ação baseada em quaisquer opções que você especificou no comando. Este objeto é semelhante ao objeto CommandClauses que o Report Designer fornece ao Report Builder Application durante uma sessão de design. Consulte Understanding Report Builder Events para obter mais informações.

Nem todos os membros do objeto CommandClauses para ReportListeners correspondem exatamente a uma palavra-chave do comando REPORT FORM, e nem todos os membros estão disponíveis pelo mesmo período de tempo. Por exemplo, o membro RecordTotal é fornecido como uma conveniência aos ReportListeners pelo Engine quando o Engine avalia o escopo do REPORT FORM. Esta avaliação ocorre entre os eventos LoadReport e BeforeReport, portanto você não pode usar RecordTotal durante LoadReport.

> **Dica:** Você pode usar a Foundation Class ReportListener Debug para comparar os membros CommandClauses durante os eventos LoadReport e BeforeReport.

A tabela a seguir lista os membros CommandClauses e discute seus conteúdos e disponibilidade. Salvo indicação em contrário, o membro e o valor correto estão disponíveis de LoadReport até UnloadReport durante uma execução de relatório. Além disso, salvo indicação em contrário, nem o Report Engine nem a classe base ReportListener usam esses valores; eles são fornecidos para o uso de código em classes derivadas de ReportListener.

> **Observação:** Todas as referências a comandos REPORT FORM devem ser entendidas como referindo-se igualmente a comandos LABEL, salvo menção explícita.

| Membro CommandClauses | Observações |
| --- | --- |
| .ASCII | Valor lógico, indica se a palavra-chave ASCII apareceu no comando REPORT FORM. ASCII não é suportado pela classe base ReportListener, e a palavra-chave é ignorada por padrão. No entanto, sua classe derivada pode optar por tomar ação baseada nesta palavra-chave. |
| .DE_NAME | Valor de dados Character, representa a cláusula NAME do comando REPORT FORM. Embora o valor de .DE_NAME esteja correto desde LoadReport, a referência DataEnvironment não está disponível até BeforeReport. Este valor está sempre presente, fornecendo o nome da referência de objeto ao DataEnvironment do relatório, quer você tenha especificado NAME no comando ou não. Como com DO FORM , o Visual FoxPro fornece uma variável pública padrão com o mesmo nome do arquivo de relatório ou etiqueta quando você não especifica NAME . |
| .ENVIRONMENT | Valor lógico, indica se a palavra-chave ENVIRONMENT apareceu no comando REPORT FORM. Esta palavra-chave não é frequentemente usada em execuções de relatório do Visual FoxPro; é permitida para compatibilidade com versões anteriores. Você pode usar a referência especificada em .DE_NAME para verificar a propriedade AutoOpenTables do DataEnvironment, em vez disso. |
| .FILE | Valor do tipo de dados Character, fornece o nome totalmente qualificado do arquivo de relatório ou etiqueta (frx ou lbx). |
| .HEADING | Tipo de dados Character, fornecendo o conteúdo do texto HEADING se você usar a cláusula HEADING < cText > no comando REPORT FORM. |
| .INSCREEN | Valor lógico, indica se o comando REPORT FORM incluiu a cláusula IN SCREEN. |
| .INWINDOW | Tipo de dados Character, fornece o nome da janela se você usou IN WINDOW < cText > no comando REPORT FORM. Este valor é uma cadeia de caracteres vazia se você não usar a cláusula IN WINDOW. |
| .ISDESIGNERLOADED | Valor lógico, indica se o comando REPORT FORM foi invocado durante uma sessão do Report Designer ou Label Designer. |
| .ISDESIGNERPROTECTED | Valor lógico, indica se o comando REPORT FORM foi invocado com a palavra-chave PROTECTED durante uma sessão do Report Designer ou Label Designer. |
| .ISREPORT | Valor lógico, indica se o comando foi REPORT FORM (.T. ) ou LABEL ( .F. ). |
| .NOCONSOLE | Valor lógico, indica se a palavra-chave NOCONSOLE apareceu no comando REPORT FORM. NOCONSOLE não é diretamente suportado pela classe base ReportListener, porque a saída assistida por objeto não é ecoada na janela de saída atual do Visual FoxPro. No entanto, sua classe derivada pode optar por tomar ação baseada nesta palavra-chave. Por exemplo, você poderia desenhar a saída em uma janela de saída ou fornecer uma versão de texto do conteúdo do relatório durante a execução do relatório, mas omitir esta ação quando o comando incluiu NOCONSOLE . |
| .NODIALOG | Valor lógico, indica se a palavra-chave NODIALOG apareceu no comando REPORT FORM. A classe base ReportListener suporta NODIALOG ajustando temporariamente o valor de sua propriedade QuietMode pela duração da execução do relatório. Consulte Propriedade QuietMode para obter mais informações. |
| .NOEJECT | Valor lógico, indica se a palavra-chave NOEJECT apareceu no comando REPORT FORM. |
| .NOPAGEEJECT | Valor lógico, indica se a palavra-chave NOPAGEEJECT apareceu no comando REPORT FORM. A classe base ReportListener fornece mais funcionalidade do que relatórios do Visual FoxPro não assistidos por objeto quando você usa NOPAGEEJECT . Esta propriedade fornece a capacidade de encadear relatórios quando você define a propriedade ListenerType do ReportListener com o valor 1 (visualização). Você pode usá-la para encadear relatórios em outros resultados de relatório que você cria. O tópico Classe básica ReportListener Base Foundation Class fornece um exemplo de duas execuções de relatório sendo adicionadas a um único documento de saída XML, usando a palavra-chave NOPAGEEJECT. |
| .NORESET | Valor lógico, indica se a palavra-chave NORESET apareceu no comando REPORT FORM. |
| .NOWAIT | Valor lógico, indica se a palavra-chave NOWAIT apareceu no comando REPORT FORM. A classe base ReportListener usa este valor para avaliar como chamar o método Show do Preview Container. Consulte The Preview Container API para obter mais informações. |
| .OFF | Valor lógico, indica se a palavra-chave OFF apareceu no comando REPORT FORM. Esta palavra-chave não foi documentada anteriormente para o comando REPORT FORM. Ela serve a mesma função que NOCONSOLE na classe base ReportListener. Suas classes derivadas podem optar por tratá-la da mesma forma que NOCONSOLE ou de forma diferente. |
| .OUTPUTTO | Valor inteiro, representando as várias possibilidades da cláusula TO, que pode ser TO PRINT ou TO [FILE] < Filename > . Se OUTPUTTO = 1 , a cláusula TO indica que a saída vai para a impressora. Se OUTPUTTO = 2 , a cláusula TO indica que a saída vai para um arquivo. No último caso, o membro CommandClauses.TOFILE fornece o nome do arquivo. Se não houve cláusula TO no comando REPORT FORM, este membro tem o valor 0 . Você pode ajustar os valores OUTPUTTO e TOFILE dinamicamente no evento LoadReport ou ao escolher imprimir da visualização, conforme descrito na entrada PROMPT abaixo. Suas alterações a esses valores são respeitadas quando o ReportListener inicia sua execução de impressão. |
| .PDSETUP | Valor lógico, indica se a palavra-chave PDSETUP apareceu no comando REPORT FORM. Como com outras cláusulas de compatibilidade com versões anteriores no comando REPORT FORM, suas classes derivadas são livres para usar este valor para qualquer finalidade. |
| .PLAIN | Valor lógico, indica se a palavra-chave PLAIN apareceu no comando REPORT FORM. |
| .PREVIEW | Valor lógico, indica se a palavra-chave PREVIEW apareceu no comando REPORT FORM. |
| .PRINTPAGECURRENT | Valor inteiro, padrão 0 , fornece uma maneira para um PreviewContainer dar informações a um ReportListener sobre qual página estava sendo exibida quando o PreviewContainer invocou o método OnPreviewClose do ReportListener. Quando o PreviewContainer usa o argumento .T. de OnPreviewClose para solicitar impressão após a visualização, e se .PRINTPAGECURRENT não é 0 , o ReportListener pode habilitar o recurso "Current Page" em qualquer caixa de diálogo que preceda a impressão, como a caixa de diálogo PROMPT nativa. Consulte Método OnPreviewClose para obter mais informações. |
| .PRINTRANGEFROM, .PRINTRANGETO | Valores inteiros, trabalham juntos para indicar um subconjunto do intervalo de páginas de saída ao imprimir após a visualização. .PRINTRANGEFROM tem padrão 1 e .PRINTRANGETO tem padrão -1 . O intervalo máximo de impressão é sempre 1 a ReportListener.OutputPageCount. Consulte Propriedade OutputPageCount para obter mais informações. |
| .PROMPT | Valor lógico, indica se a palavra-chave PROMPT apareceu no comando REPORT FORM. O ReportDesigner adiciona uma cláusula PROMPT quando você escolhe visualizar durante uma sessão de design. Observação Você pode ajustar o membro .PROMPT dinamicamente ao visualizar, por exemplo no evento OnPreviewClose( .T. ). O argumento .T. para OnPreviewClause indica que você deseja Imprimir quando a visualização termina. Você também pode alterar este valor no evento LoadReport. Sua alteração ao valor é respeitada quando o ReportListener inicia sua execução de impressão. Você pode encadear vários relatórios juntos, usando NOPAGEEJECT , e os vários relatórios podem não ter todos tido valores diferentes para CommandClauses.PROMPT. Neste cenário, o único valor significativo para PROMPT é o do último relatório no conjunto encadeado (o relatório sem NOPAGEEJECT ). |
| .RANGEFROM | Valor inteiro, indica o primeiro argumento da cláusula RANGE quando você usa esta cláusula no comando REPORT FORM. Se você não usar a cláusula RANGE no seu comando, este membro tem o valor 1 . O valor pode mudar entre o evento LoadReport e o evento BeforeReport, baseado em alterações feitas por um usuário a partir de uma caixa de diálogo PROMPT. RANGEFROM e RANGETO são avaliados pela classe base ReportListener quando você chama o Método IncludePageInOutput . |
| .RANGETO | Valor inteiro, indica o segundo argumento (opcional) da cláusula RANGE quando você usa esta cláusula no comando REPORT FORM. Se você não usar a cláusula RANGE no seu comando, ou se você não especificar seu segundo argumento, este membro tem o valor - 1 . O valor pode mudar entre o evento LoadReport e o evento BeforeReport, baseado em alterações feitas por um usuário a partir de uma caixa de diálogo PROMPT. RANGEFROM e RANGETO são avaliados pela classe base ReportListener quando você chama o Método IncludePageInOutput . |
| .RECORDTOTAL | Valor inteiro, indica o escopo completo de registros no alias atualmente selecionado que serão processados. O escopo é baseado nas cláusulas do comando REPORT FORM e quaisquer outras condições limitantes que você possa ter definido (como um comando SET FILTER). Este valor é 0 em LoadReport e contém o valor correto a partir de BeforeReport. É redefinido para 0 após UnloadReport. |
| .SAMPLE | Valor lógico, indica se a palavra-chave SAMPLE apareceu no comando LABEL. Esta palavra-chave não está disponível para o comando REPORT FORM. Portanto, este valor é sempre .F. a menos que você use o comando LABEL. |
| .STARTDATASESSION | Valor numérico, indica a sessão de dados na qual você emitiu o comando REPORT FORM ou LABEL. Para obter mais informações, consulte Understanding Visual FoxPro Object-Assisted Reporting . |
| .SUMMARY | Valor lógico, indica se a palavra-chave SUMMARY apareceu no comando REPORT FORM. Este valor é sempre .F. para um comando LABEL; é significativo apenas para comandos REPORT FORM. |
| .TOFILE | Tipo de dados Character, indica o nome do arquivo de saída de destino quando você usa a cláusula TO [FILE] < Filename > no comando REPORT FORM. Você pode ajustar este membro dinamicamente, conforme discutido acima em OUTPUTTO. |
| .TOFILEADDITIVE | Valor lógico, indica se a palavra-chave ADDITIVE apareceu no comando REPORT FORM como parte de TO [FILE] < Filename > ASCII . Esta palavra-chave se aplica apenas a ASCII e, como tal, é ignorada pela classe base ReportListener. |
| .WINDOW | Tipo de dados Character, fornece o nome da janela se você usou WINDOW < cText > no comando REPORT FORM. Este valor é uma cadeia de caracteres vazia se você não usar a cláusula WINDOW. |

# Exemplo

O exemplo a seguir é retirado da Foundation Class ReportListener User Feedback. A classe UpdateListener usa seu membro CommandClauses.FILE para determinar um título apropriado para sua janela de feedback, nos casos em que o usuário não especificou um valor para a propriedade PrintJobName.

```foxpro
IF EMPTY(THIS.PrintJobName)
   cName = PROPER(JUSTFNAME(THIS.CommandClauses.FILE))
ELSE
   cName = THIS.PrintJobName
ENDIF
THIS.ThermForm.Caption = ;
   cName + ": " + OUTPUTCLASS_CANCEL_INSTRUCTIONS_LOC
```
