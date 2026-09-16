# Propriedade Left (Visual FoxPro)

Especifica a distância entre a borda esquerda de um controle ou formulário e seu objeto contêiner. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.Left[ = nDist]
```

# Valor de retorno
 **nDist**
Especifica a distância entre a borda esquerda de um objeto ou formulário e a borda esquerda de seu objeto contêiner. O contêiner padrão para um formulário é a janela principal do Visual FoxPro.

# Observações

Aplica-se a: CheckBox Control | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | Control Object (Visual FoxPro) | Custom Object | EditBox Control | Form Object | Grid Control | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OLE Bound Control | OLE Container Control | OptionButton Control | OptionGroup Control | PageFrame Control | _SCREEN System Variable | Shape Control | Spinner Control | TextBox Control (Visual FoxPro) | Timer Control | ToolBar Object

A propriedade Left especifica a distância da posição zero do objeto em que o objeto está localizado. Por exemplo, se um formulário está contido na janela principal do Visual FoxPro, a posição zero está imediatamente à direita da borda esquerda da janela principal. Se uma barra de ferramentas está encaixada à esquerda da janela principal, a posição zero está imediatamente à direita da barra de ferramentas.

Use as propriedades Left, Top, Height e Width para operações baseadas nas dimensões externas de um objeto, como mover ou redimensionar. Use a propriedade ScaleMode para alterar a unidade de medida.

> **Observação:** A propriedade Left é somente leitura quando se aplica a um controle contido em um objeto Column.

# Exemplo

O exemplo a seguir demonstra como a propriedade Left é usada para posicionar controles em um formulário. O método AddObject é usado para adicionar um controle Line e três botões de comando a um formulário, e a propriedade Left especifica o posicionamento horizontal de cada controle no formulário.

```foxpro
frmMyForm = CREATEOBJECT('Form')  && Create a form
frmMyForm.Closable = .F.  && Disable the window pop-up menu

frmMyForm.AddObject('shpLine','Line')  && Add a Line control to the form
frmMyForm.AddObject('cmdCmndBtn1','cmdMyCmndBtn1')  && Up Cmnd button
frmMyForm.AddObject('cmdCmndBtn2','cmdMyCmndBtn2')  && Down Cmnd button
frmMyForm.AddObject('cmdCmndBtn3','cmdMyCmndBtn3')  && Quit Cmnd button
frmMyForm.shpLine.Visible = .T.  && Make Line control visible
frmMyForm.shpLine.Top = 20  && Specify Line control row
frmMyForm.shpLine.Left = 125  && Specify Line control column
frmMyForm.cmdCmndBtn1.Visible =.T.  && Up Command button visible
frmMyForm.cmdCmndBtn2.Visible =.T.  && Down" Command button visible
frmMyForm.cmdCmndBtn3.Visible =.T.  && Quit Command button visible
frmMyForm.SHOW  && Display the form
READ EVENTS  && Start event processing
DEFINE CLASS cmdMyCmndBtn1 AS COMMANDBUTTON  && Create Command button
   Caption = 'Slant \<Up'  && Caption on the Command button
   Left = 50  && Command button column
   Top = 100  && Command button row
   Height = 25  && Command button height

   PROCEDURE Click
      ThisForm.shpLine.Visible = .F.  && Hide the Line control
      ThisForm.shpLine.LineSlant ='/'  && Slant up
      ThisForm.shpLine.Visible = .T.  && Show the Line control
ENDDEFINE
DEFINE CLASS cmdMyCmndBtn2 AS CommandButton  && Create Command button
   Caption = 'Slant \<Down'  && Caption on the Command button
   Left = 200  && Command button column
   Top = 100  && Command button row
   Height = 25  && Command button height
   PROCEDURE Click
      ThisForm.shpLine.Visible = .F.  && Hide the Line control
      ThisForm.shpLine.LineSlant ='\'  && Slant down
      ThisForm.shpLine.Visible = .T.  && Show the Line control
ENDDEFINE
DEFINE CLASS cmdMyCmndBtn3 AS CommandButton  && Create Command button
   Caption = '\<Quit'  && Caption on the Command button
   Cancel = .T.  && Default Cancel Command button (Esc)
   Left = 125  && Command button column
   Top = 150  && Command button row
   Height = 25  && Command button height
   PROCEDURE Click
      CLEAR EVENTS  && Stop event processing, close form
ENDDEFINE
```
