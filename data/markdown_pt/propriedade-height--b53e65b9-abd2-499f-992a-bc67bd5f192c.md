# Propriedade Height

Especifica a altura de um objeto na tela. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.Height[ = nHeight]
```

# Valor de retorno
 **nHeight**
Especifica a altura do objeto medida na unidade de medida especificada pela propriedade ScaleMode do formulário.

# Observações

Aplica-se a: CheckBox Control | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | Control Object (Visual FoxPro) | Custom Object | EditBox Control | Form Object | Grid Control | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OLE Bound Control | OLE Container Control | OptionButton Control | OptionGroup Control | PageFrame Control | _SCREEN System Variable | Shape Control | Spinner Control | TextBox Control (Visual FoxPro) | Timer Control | ToolBar Object

Para formulários, a medida Height não inclui as bordas e a barra de título. Além disso, se a propriedade ScrollBars estiver definida para habilitar barras de rolagem, Height não inclui o espaço ocupado pela barra de rolagem quando ela aparece. No Visual FoxPro, a altura máxima de um formulário foi aumentada para aproximadamente 32.000 pixels.

Para controles, a altura é medida a partir do exterior da borda do controle.

O valor desta propriedade muda conforme o objeto é dimensionado pelo usuário ou por código.

Use as propriedades Height e Width para cálculos baseados na área total de um objeto.

> **Observação:** A propriedade Height é somente leitura quando se aplica a um controle contido em um objeto Column.

# Exemplo

O exemplo a seguir demonstra como a propriedade Height é usada para especificar a altura de três botões de comando em um formulário.

O método AddObject é usado para adicionar um controle Line e três botões de comando a um formulário. A propriedade Height especifica a altura vertical de cada botão de comando.

```foxpro
frmMyForm = CREATEOBJECT('form')  && Create a form
frmMyForm.Closable = .F.  && Disable the Control menu box
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
