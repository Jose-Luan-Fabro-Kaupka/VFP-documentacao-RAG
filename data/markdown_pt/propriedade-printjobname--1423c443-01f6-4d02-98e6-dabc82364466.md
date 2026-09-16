# Propriedade PrintJobName

Mostra um valor especificado pelo usuário como o nome do documento que está sendo impresso na fila de impressão do Windows.

> **Observação:** A fila de impressão do Windows não é uma caixa de diálogo exibida dentro do Visual FoxPro. Ela é a janela que mostra os documentos aguardando impressão e o status de cada documento para uma impressora específica. Para acessar essa janela, clique duas vezes na impressora cujo status dos documentos deseja ver em Printers and Faxes.

```foxpro
ReportListener.PrintJobName [= cText]
```

# Valor de retorno

Tipo de dados Character, limitado a 255 caracteres.

O valor padrão é uma cadeia de caracteres vazia.

# Observações

Aplica-se a: objeto ReportListener.

Você pode usar esta propriedade para fornecer informações adicionais ao usuário em classes derivadas de ReportListener. Por exemplo, a classe base ReportListener User Feedback usa PrintJobName no título da janela de progresso, e a classe base ReportListener HTML usa PrintJobName no título do documento HTML. Se você não atribuir um valor a PrintJobName, ambas as classes usam por padrão o nome do arquivo de relatório ou rótulo, de forma semelhante ao valor padrão que o Visual FoxPro atribui na fila de impressão do Windows. Para obter mais informações, consulte Classes base ReportListener.

> **Observação:** Quando NOPAGEEJECT faz com que uma única execução de impressão seja usada para vários relatórios, o tamanho imprimível da página e outras características determinadas pela impressora são definidos pelo primeiro relatório da execução, pois é nesse momento que o spool de impressão é aberto. A propriedade PrintJobName também é aplicada nesse momento; portanto, apenas o primeiro valor de uma execução encadeada é significativo para um ReportListener com ListenerType 1 (modo de impressão).

# Exemplo

O exemplo a seguir ilustra a disponibilidade de várias propriedades PrintJobName durante uma única execução de vários relatórios encadeados com NOPAGEEJECT. Se você definir a propriedade ListenerType da classe derivada de ReportListener como `1` neste exemplo, o nome do documento em impressão na fila do Windows será My First Report durante toda a execução. No entanto, ao derivar classes de ReportListener e implementar outros valores de ListenerType, você pode usar cada valor de PrintJobName durante a execução encadeada.

```foxpro
LOCAL loListener
loListener = CREATEOBJECT("PJN")
loListener.PrintJobName = "My First Report"
REPORT FORM ? NOPAGEEJECT OBJECT loListener
loListener.PrintJobName = "My Second Report"
REPORT FORM ? OBJECT loListener
DEFINE CLASS PJN AS ReportListener
   PROCEDURE BeforeReport()
     MESSAGEBOX(THIS.PrintJobName + ;
       " (runs " + THIS.CommandClauses.File) + ")"
   ENDPROC
ENDDEFINE
```
