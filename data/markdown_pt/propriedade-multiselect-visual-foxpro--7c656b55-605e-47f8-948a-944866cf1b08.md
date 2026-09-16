# Propriedade MultiSelect (Visual FoxPro)

Especifica se um usuário pode fazer seleções múltiplas em um controle ListBox e como as seleções múltiplas podem ser feitas. Disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
ListBox.MultiSelect[ = nChoice]
```

# Valor de retorno
 **nChoice**
As configurações da propriedade MultiSelect são: Configuração Descrição 0 (Padrão) Seleção múltipla não é permitida. 1 Seleção múltipla é permitida. Para selecionar vários itens em um controle ListBox, mantenha a tecla CTRL pressionada enquanto clica nos itens.

# Observações

Aplica-se a: Controle ListBox

Defina MultiSelect como true (.T.) para permitir que um usuário selecione vários itens em uma lista. Você pode usar a propriedade Selected para determinar quais itens estão selecionados.

# Exemplo

O exemplo a seguir cria um ListBox. A propriedade MultiSelect da caixa de lista é definida como true (.T.), permitindo que você faça seleções múltiplas na caixa de lista. A origem dos itens que aparecem na caixa de lista é uma matriz; a matriz é especificada com as propriedades RowSourceType e RowSource.

A propriedade ListCount é usada dentro de um loop FOR ... ENDFOR para exibir o item ou itens que você escolhe na caixa de lista. A propriedade Selected é usada para determinar os itens que você escolheu, e a propriedade List é usada para retornar os itens.

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
frmMyForm.AddObject('lstListBox1','lstMyListBox')  && Add ListBox control
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
