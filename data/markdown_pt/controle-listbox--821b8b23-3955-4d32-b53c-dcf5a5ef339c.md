# Controle ListBox

Cria uma caixa de lista que exibe uma lista de itens dos quais você pode selecionar um ou mais. Uma caixa de lista é semelhante a uma caixa de combinação; no entanto, uma caixa de combinação exibe inicialmente um único item. Para mais informações sobre caixas de combinação, consulte ComboBox Control.

Para mais informações sobre como criar controles ListBox, consulte Form Designer e Using Controls.

```foxpro
ListBox
```

# Observações

A tabela a seguir lista propriedades comumente definidas em tempo de design.

| Property | Description |
| --- | --- |
| ColumnCount | Determines the number of columns in the list. |
| ControlSource | Specifies where to store the value that the user chooses from the list. |
| MoverBars | Specifies whether to display mover bars to the left of the items in the list so that a user can rearrange the item order. |
| Multiselect | Specifies whether the user can select more than one item in the list. |
| RowSource | Specifies the source of the values displayed in the list. |
| RowSourceType | Specifies the type of the source of the values displayed in the list. |

A tabela a seguir lista métodos comumente usados.

| Method | Description |
| --- | --- |
| AddItem | Adds an item to the list when RowSourceType is set to 0. |
| RemoveItem | Removes an item from the list when RowSourceType is set to 0. |
| Requery | Updates the list if the values in the source specified by RowSource have changed. |

A barra invertida ("\") é tratada como um caractere especial quando usada na expressão de um item. As seguintes regras se aplicam a este caractere:
 - Você pode desabilitar um item em uma caixa de lista ou caixa de combinação adicionando uma única barra invertida ao início da expressão.
- Qualquer múltiplo de duas barras invertidas usadas na expressão é exibido como uma única barra invertida. Por exemplo, uma ou duas barras invertidas usadas juntas serão exibidas como uma, e três ou quatro barras invertidas juntas serão exibidas como duas. O código de exemplo a seguir contém um item de caixa de lista contendo um caminho Universal Naming Convention (UNC). O código seria exibido na caixa de lista como \\MyServer\MyMachine\MyFolder. MyForm.List1.AddItem("\\\\MyServer\\MyMachine\\MyFolder")
- Se a expressão começar com várias barras invertidas, o item não é desabilitado. Se você quiser desabilitar um item que começa com várias barras invertidas, adicione uma barra invertida e um colchete de fechamento (]) ao início do item. Por exemplo, o seguinte desabilitaria o item de caminho UNC na caixa de lista: MyForm.List1.AddItem("\]\\\MyServer\\MyMachine\\MyFolder")
- Para incluir uma linha separadora, use uma barra invertida seguida de um hífen como o item a adicionar à caixa de lista. Por exemplo, o código a seguir adiciona uma linha separadora a uma caixa de lista: MyForm.List1.AddItem("\-")

Você também pode usar um controle ActiveX que adiciona características extras, como um CheckBox, aos controles ListView ou TreeView.

# Exemplo

O exemplo a seguir cria um controle ListBox. A fonte dos itens que aparecem na caixa de lista é uma matriz especificada com as propriedades RowSourceType e RowSource.

A propriedade MultiSelect da caixa de lista é definida como true (.T.), permitindo fazer várias seleções na lista. O item ou itens escolhidos são exibidos usando as propriedades ListCount, Selected e List (que determinam o número de itens na lista e os itens escolhidos).

```foxpro
CLEAR
DIMENSION gaMyListArray(10)
FOR gnCount = 1 to 10  && Fill the array with letters
   STORE REPLICATE(CHR(gnCount+64),6) TO gaMyListArray(gnCount)
NEXT
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
