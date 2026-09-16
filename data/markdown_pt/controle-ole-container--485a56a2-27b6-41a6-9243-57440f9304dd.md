# Controle OLE Container

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
   DocumentFile = "C:\EXCEL\BOOK1.XLS"  && This file must exist
ENDDEFINE
DEFINE CLASS cmdMyCmdBtn AS CommandButton  && Create Command button
   Caption = '\<Quit'  && Caption on the Command button
   Cancel = .T.  && Default Cancel Command button (Esc)
   Left = 125  && Command button column
   Top = 210  && Command button row
   Height = 25  && Command button height
   PROCEDURE Click
      CLEAR EVENTS  && Stop event processing, close form
ENDDEFINE
```
