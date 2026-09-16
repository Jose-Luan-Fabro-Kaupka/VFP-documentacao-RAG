# Método DoVerb

Executa um verbo no objeto especificado.

```foxpro
Object.DoVerb[(Verb)]
```

#### Parâmetros
 **Verb**
O verbo a executar no objeto dentro do controle OLE container. Se não especificado, o verbo padrão é executado. O valor deste argumento pode ser um dos verbos padrão suportados por todos os objetos ou um índice do array da propriedade ObjectVerbs. Cada objeto pode suportar seu próprio conjunto de verbos. Os valores a seguir representam verbos padrão suportados por todos os objetos: Valor Ação 0 A ação padrão para o objeto. –1 Ativa o objeto para edição. Se o aplicativo que criou o objeto suporta ativação in-place, o objeto é ativado dentro do controle OLE container. –2 Abre o objeto em uma janela de aplicativo separada. Se o aplicativo que criou o objeto suporta ativação in-place, o objeto é ativado em sua própria janela. –3 Para objetos incorporados, oculta o aplicativo que criou o objeto. –4 Se o objeto suporta ativação in-place, ativa o objeto para ativação in-place e mostra quaisquer ferramentas de interface do usuário. Se o objeto não suporta ativação in-place, o objeto não é ativado e ocorre um erro. –5 Se o usuário move o foco para o controle OLE container, cria uma janela para o objeto e prepara o objeto para ser editado. Ocorre um erro se o objeto não suporta ativação com um único clique do mouse. –6 Usado quando o objeto é ativado para edição para descartar todo o registro de alterações que o aplicativo do objeto pode desfazer.

# Observações

Aplica-se a: Controle OLE Bound | Controle OLE Container

Se você definir a propriedade AutoActivate como 2 (DoubleClick), o controle OLE container ativa automaticamente o objeto atual quando o usuário clica duas vezes no controle.

> **Dica:** Embora você possa usar o nome do verbo (edit, open, play, e assim por diante) para especificar o verbo a usar com DoVerb , é muito mais rápido usar o índice (0, 1, 2, e assim por diante).

# Exemplo

O exemplo a seguir adiciona um controle OLE Container a um formulário e usa as propriedades OleClass e DocumentFile para especificar Microsoft Excel como Automation server e uma planilha do Microsoft Excel como o arquivo a editar.

A propriedade DocumentFile especifica uma planilha chamada Book1.xls no diretório EXCEL na unidade C. Este exemplo não funcionará corretamente se o arquivo e o diretório especificados na propriedade DocumentFile não existirem; pode ser necessário modificar a propriedade DocumentFile para especificar um diretório e arquivo de planilha existentes.

* O método DoVerb é usado para ativar a planilha para edição.

```foxpro
*frmMyForm = CREATEOBJECT('form')  && Create a form
*frmMyForm.Closable = .F.  && Disable the Control menu box
frmMyForm.AddObject('cmdCommand1','cmdMyCmdBtn')  && Add Command button
frmMyForm.AddObject("oleObject","oleExcelObject")  && Add OLE object
frmMyForm.cmdCommand1.Visible=.T.  && Display the "Quit" Command button
frmMyForm.oleObject.Visible=.T.  && Display the OLE control
frmMyForm.oleObject.Height = 50  && OLE control height
frmMyForm.Show  && Display the form
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
