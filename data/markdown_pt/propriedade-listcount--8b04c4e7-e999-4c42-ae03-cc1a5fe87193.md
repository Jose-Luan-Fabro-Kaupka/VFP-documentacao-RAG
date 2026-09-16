# Propriedade ListCount

Contém o número de itens na parte de lista de um controle ComboBox ou ListBox. Não disponível em tempo de design; somente leitura em tempo de execução.

```foxpro
Control.ListCount
```

# Observações

Aplica-se a: ComboBox Control | ListBox Control

# Exemplo

O exemplo a seguir cria uma caixa de lista. A origem dos itens que aparecem na caixa de lista é um array; o array é especificado com as propriedades RowSourceType e RowSource.

ListCount é usado para percorrer todos os itens especificados pela propriedade List do ComboBox ou ListBox.

A propriedade MultiSelect da caixa de lista é definida como true (.T.), permitindo que você faça seleções múltiplas na caixa de lista. A propriedade ListCount é usada dentro de um loop FOR ... ENDFOR para exibir o item ou os itens que você escolhe na caixa de lista. As propriedades Selected e List são usadas para determinar os itens que você escolheu.

```foxpro
CLEAR
DIMENSION gaMyListArray(10)
FOR gnCount = 1 to 10  && Fill the array with letters
   STORE REPLICATE(CHR(gnCount+64),6) TO gaMyListArray(gnCount)
ENDFOR
frmMyForm = CREATEOBJECT('Form')  && Create a Form
frmMyForm.Closable = .f.  && Disable the Control menu box
frmMyForm.Move(150,10)  && Move the form
frmMyForm.AddObject('cmbCommand1','cmdMyCmdBtn')  && Add "Quit" Command button
frmMyForm.AddObject('lstListBox1','lstMyListBox')  && Add list box control
frmMyForm.lstListBox1.RowSourceType = 5  && Specifies an array
frmMyForm.lstListBox1.RowSource = 'gaMyListArray' && Array containing listbox items
frmMyForm.cmbCommand1.Visible =.T.  && "Quit" Command button visible
frmMyForm.lstListBox1.Visible =.T.  && "List Box visible
frmMyForm.SHOW  && Display the form
READ EVENTS  && Start event processing
DEFINE CLASS cmdMyCmdBtn AS CommandButton  && Create Command button
   Caption = '\<Quit'  && Caption on the Command button
   Cancel = .T.  && Default Cancel Command button (Esc)
   Left = 125  && Command button column
   Top = 210  && Command button row
   Height = 25  && Command button height
   PROCEDURE Click
      CLEAR EVENTS  && Stop event processing, close Form
      CLEAR  && Clear main Visual FoxPro window
ENDDEFINE
DEFINE CLASS lstMyListBox AS ListBox  && Create ListBox control
   Left = 10  && List Box column
   Top = 10  && List Box row
   MultiSelect = .T.  && Allow selecting more than 1 item
PROCEDURE Click
   ACTIVATE SCREEN
   CLEAR
   ? "Selected items:"
   ? "---------------"
   FOR nCnt = 1 TO ThisForm.lstListBox1.ListCount
      IF ThisForm.lstListBox1.Selected(nCnt)  && Is item selected?
         ? SPACE(5) + ThisForm.lstListBox1.List(nCnt) && Show item
      ENDIF
   ENDFOR
ENDDEFINE
```
