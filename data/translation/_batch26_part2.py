# Temporary: large translation entries to merge into _write_batch26.py
PART2 = {
    "481b543d-7a57-4a98-91ed-96ec3bac29ca.md": """# Método OnPreviewClose

Ocorre quando o usuário fecha uma visualização de relatório ou opta por imprimir a partir de uma visualização de relatório.

```foxpro
oReportListener.OnPreviewClose([lPrint])
```

#### Parâmetros
 **lPrint**
Especifica se o usuário indicou desejo de imprimir as páginas no conjunto de páginas de saída atual após fechar a visualização de relatório.

# Valor de retorno

None.

# Observações

Aplica-se a: ReportListener Object.

A PreviewContainer API especifica que, quando o usuário fecha um formulário de visualização de relatório, o PreviewContainer deve chamar o método OnPreviewClose do ReportListener. Quando o usuário escolhe imprimir a partir da Visualização, Preview chama OnPreviewClose com um argumento True (`.T.`).

> **Observação:** O ReportListener invoca o método SetReport do PreviewContainer em OnPreviewClose com um argumento NULL ( .NULL. ). Neste momento, o ReportListener pode escolher definir sua referência PreviewContainer como NULL ( .NULL. ) ou mantê-la. No entanto, de acordo com as convenções da PreviewContainer API, é responsabilidade do PreviewContainer remover sua referência de retorno ao ReportListener neste momento. Para obter mais informações, consulte The Preview Container API e PreviewContainer Property .

Se o usuário optou por imprimir a partir da visualização, a execução de impressão começa após este método terminar. A execução de impressão usa páginas em cache preparadas para visualização neste ponto, de modo que a saída disponível corresponde exatamente ao que o usuário viu na visualização, incluindo quaisquer especificações RANGE ou de escopo incluídas no comando REPORT FORM que invocou a visualização.

Se o valor CommandClauses.Prompt do ReportListener é True (`.T.`) neste ponto, a caixa de diálogo de configuração da impressora aparece antes da execução de impressão. O usuário pode alterar as especificações com as quais o relatório imprime. Este valor pode ser True por um dos seguintes motivos:
 - Você usou a cláusula PROMPT no comando REPORT FORM original.
- O PreviewContainer ou ReportListener ajusta o valor CommandClauses.Prompt dinamicamente.

As páginas que imprimem nem sempre são o intervalo completo de páginas de saída disponíveis; podem ser algum subconjunto deste intervalo. Menos que o número total de páginas de saída pode imprimir por um dos seguintes motivos:
 - O usuário ajusta o intervalo de páginas na caixa de diálogo PROMPT.
- O PreviewContainer ou ReportListener ajusta os membros CommandClauses do ReportListener fornecidos para limitar a saída impressa a partir do método OnPreviewClose. Esses membros são PrintPageCurrent, PrintRangeFrom e PrintRangeTo. Para obter mais informações, consulte CommandClauses Property .

Se você usar NOPAGEEJECT para combinar vários relatórios em uma única execução de relatório, o valor de CommandClauses.Prompt é significativo apenas no momento em que o PreviewContainer invoca a execução de impressão. Se você não ajustou seu valor dinamicamente, o valor de CommandClauses.Prompt foi determinado por se o comando REPORT FORM final na execução de relatório incluiu a cláusula PROMPT.

> **Importante:** Como a caixa de diálogo de configuração da impressora aparece após o relatório ter sido renderizado, em resposta a CommandClauses.Prompt, e como o relatório foi renderizado com informações obtidas da impressora definida anteriormente, há algum potencial de incompatibilidade entre o relatório renderizado anteriormente e as instruções definidas pelo usuário na caixa de diálogo. Por exemplo, a impressora escolhida na caixa de diálogo pode ter um tamanho de página imprimível diferente da impressora original. Os resultados impressos neste cenário são determinados pela forma como o driver da impressora escolhida escolhe lidar com esta instrução de tamanho de página.

# Exemplo

Você pode alterar os vários membros dinâmicos de CommandClauses durante o método OnPreviewClose, para imprimir intervalos de páginas complexos. No esboço de código a seguir, um ReportListener derivado fornece uma caixa de diálogo personalizada para obter um intervalo de páginas complexo de um usuário e, em seguida, invoca o comportamento nativo várias vezes para imprimir os vários intervalos de páginas solicitados pelo usuário.

```foxpro
PROCEDURE OnPreviewClose(lPrint)
   LOCAL liRange
   IF lPrint
      NODEFAULT
      IF NOT EMPTY(THIS.CommandClauses.PrintPageCurrent
         *user chose "print current page" option from PreviewContainer.
         *Print only that page:
         THIS.CommandClauses.PrintRangeFrom = ;
           THIS.CommandClauses.PrintPageCurrent
         THIS.CommandClauses.PrintRangeTo = ;
           THIS.CommandClauses.PrintPageCurrent
         DODEFAULT(.T.)
      ELSE
         THIS.ShowCustomPageSetupDialog()
         THIS.CommandClauses.Prompt = .F.
         IF EMPTY(THIS.PageRangeArray[1])
            * no printing is requested
            DODEFAULT(.F.)
         ELSE
            * user chose at least one range;
            * go through the array set up by
            * the dialog and print the range(s)
            FOR liRange = 1 TO (ALEN(THIS.PageRangeArray,1))
               THIS.CommandClauses.PrintRangeFrom = ;
                 THIS.PageRangeArray[liRange,1]
               THIS.CommandClauses.PrintRangeTo = ;
                 THIS.PageRangeArray[liRange,2]
               DODEFAULT(.T.)
            ENDFOR
         ENDIF
      ENDIF
   ENDIF
ENDPROC
```

# Consulte também
- ReportListener Object
- OutputPageCount Property
- IncludePageInOutput Method
- Methods (Visual FoxPro)
- Language Reference (Visual FoxPro)
""",
    "485a56a2-27b6-41a6-9243-57440f9304dd.md": """# Controle OLE Container

Cria um controle OLE container.

```foxpro
OLEControl
```

# Observações

Um controle OLE container permite adicionar objetos OLE às suas aplicações. Objetos OLE incluem ActiveX Controls (arquivos .ocx) e objetos OLE inseríveis criados em outras aplicações, como Microsoft Word e Microsoft Excel. Diferentemente dos ActiveX Controls (arquivos .ocx), objetos OLE inseríveis não possuem seu próprio conjunto de eventos. Controles OLE container, diferentemente de controles OLE bound, não estão vinculados a um campo General em uma tabela Visual FoxPro.

Observe que o tipo de controle ActiveX colocado em um controle OLE container determina as propriedades, eventos e métodos disponíveis para o controle ActiveX

Para informações adicionais sobre objetos OLE no Visual FoxPro, consulte Sharing Information and Adding OLE.

# Exemplo

O exemplo a seguir adiciona um controle OLE Container a um formulário e usa as propriedades OleClass e DocumentFile para especificar Microsoft Excel como o servidor Automation e uma planilha Microsoft Excel como o arquivo a editar.

A propriedade DocumentFile especifica uma planilha chamada Book1.xls no diretório EXCEL na unidade C. Este exemplo não funcionará corretamente se o arquivo e o diretório especificados na propriedade DocumentFile não existirem; pode ser necessário modificar a propriedade DocumentFile para especificar um diretório e arquivo de planilha existentes.

* O método DoVerb é usado para ativar a planilha para edição.

```foxpro
frmMyForm = CREATEOBJECT('Form')  && Create a Form
frmMyForm.Closable = .F.  && Disable the window pop-up menu
frmMyForm.AddObject('cmdCommand1','cmdMyCmdBtn')  && Add Command button
frmMyForm.AddObject("oleObject","oleExcelObject")  && Add OLE object
frmMyForm.cmdCommand1.Visible=.T.  && Display the "Quit" Command button
frmMyForm.oleObject.Visible=.T.  && Display the OLE control
frmMyForm.oleObject.Height = 50  && OLE control height
frmMyForm.Show  && Display the Form
frmMyForm.oleObject.DoVerb(-1)  && -1 for Edit
READ EVENTS  && Start event processing
DEFINE CLASS oleExcelObject as OLEControl
   OleClass ="Excel.Sheet"  && Server name
   DocumentFile = "C:\\EXCEL\\BOOK1.XLS"  && This file must exist
ENDDEFINE
DEFINE CLASS cmdMyCmdBtn AS CommandButton  && Create Command button
   Caption = '\\<Quit'  && Caption on the Command button
   Cancel = .T.  && Default Cancel Command button (Esc)
   Left = 125  && Command button column
   Top = 210  && Command button row
   Height = 25  && Command button height
   PROCEDURE Click
      CLEAR EVENTS  && Stop event processing, close form
ENDDEFINE
```

# Consulte também
- OLE Container Control Properties, Methods, and Events
- ActiveX Controls Overview
- APPEND GENERAL Command
- CREATE FORM Command
- CREATE CLASS Command
""",
}
