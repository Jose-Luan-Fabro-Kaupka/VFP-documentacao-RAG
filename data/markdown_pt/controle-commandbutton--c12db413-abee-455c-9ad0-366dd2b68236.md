# Controle CommandButton

Cria um único botão de comando.

```foxpro
CommandButton
```

# Observações

Um botão de comando é normalmente usado para iniciar um evento que executa uma ação, como fechar um formulário, mover para um registro diferente, imprimir um relatório, e assim por diante. Use o controle CommandGroup para criar um conjunto de botões de comando que você pode manipular individualmente ou como um grupo.

Use a propriedade Caption para especificar o texto que aparece em um botão de comando. Use a propriedade Picture para especificar uma imagem para um botão de comando.

Você pode escolher um botão de comando clicando nele e, se a propriedade Default estiver definida como True (.T.), pressionando a tecla ENTER quando o botão de comando estiver selecionado. Se a propriedade Cancel do botão de comando estiver definida como True (.T.), você pode escolher o botão de comando pressionando a tecla ESC.

Para obter informações adicionais sobre botões de comando, consulte Form Designer e Usando controles.

# Exemplo

O exemplo a seguir demonstra como botões de comando podem ser adicionados a um formulário. A propriedade Caption é usada para especificar o texto nos botões de comando e o texto que indica a sequência de tecla de acesso de cada botão. A propriedade Cancel é usada para especificar um botão que é escolhido quando você pressiona ESC.

O método AddObject é usado para adicionar três botões de comando ao formulário, permitindo alterar a direção em que um controle Line inclina ou fechar o formulário.

```foxpro
frmMyForm = CREATEOBJECT('Form')  && Create a Form
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
DEFINE CLASS cmdMyCmndBtn1 AS CommandButton  && Create Command button
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
      CLEAR EVENTS  && Stop event processing, close Form
ENDDEFINE
```
