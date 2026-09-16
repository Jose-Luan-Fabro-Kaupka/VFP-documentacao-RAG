# Controle Line

Cria um controle que exibe uma linha horizontal, vertical ou diagonal.

```foxpro
Line
```

# Observações

Um controle Line é um controle gráfico que exibe uma linha horizontal, vertical ou diagonal que não pode ser alterada diretamente. No entanto, porque um controle Line tem um conjunto completo de propriedades, eventos e métodos que outros controles têm, o controle Line pode responder a eventos e pode ser alterado dinamicamente em tempo de execução.

Para informações adicionais sobre como criar linhas, consulte o tópico Form Designer e Using Controls.

# Exemplo

O exemplo a seguir demonstra como um controle Line pode ser adicionado a um formulário e como você pode usar a propriedade LineSlant para especificar a direção em que a linha inclina.

O método AddObject é usado para adicionar um controle Line a um formulário. Três botões de comando são adicionados ao formulário, permitindo alterar a direção em que a linha inclina ou fechar o formulário.

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
      CLEAR EVENTS  && Stop event processing, close Form
ENDDEFINE
```
