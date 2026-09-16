# Propriedade Closable

Especifica se o formulário pode ser fechado ao clicar duas vezes no ícone do menu pop-up da janela, escolher Close no menu pop-up da janela ou clicar no botão Close. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.Closable[ = lExpr]
```

# Valor de retorno
 **lExpr**
As configurações da propriedade Closable são: Configuração Descrição True (.T.) (Padrão) O item Close é adicionado ao menu pop-up da janela. False (.F.) O formulário não pode ser fechado ao clicar duas vezes no ícone do menu pop-up da janela, e o item Close é removido do menu pop-up da janela.

# Exemplo

Aplica-se a: Form Object | _SCREEN System Variable

O exemplo a seguir demonstra como a propriedade Closable é definida como False (.F.) para impedir que um formulário seja fechado usando o menu pop-up da janela ou o botão Close. Se a propriedade Closable do formulário estiver definida como True (.T.) e o formulário for fechado usando o menu pop-up da janela, CLEAR EVENTS deve ser emitido para interromper o processamento de eventos e sair do programa.

```foxpro
frmMyForm = CREATEOBJECT('Form')  && Create a Form
frmMyForm.Closable = .F.  && Disable the window pop-up menu
                          && and Close button
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
