# Propriedade Selected

Especifica se um item está selecionado em um controle ComboBox ou ListBox. Não disponível em tempo de design e leitura/gravação em tempo de execução.

```foxpro
[Form.]Control.Selected(nIndex) [= lExpr ]
```

# Valor de retorno
 **nIndex**
Tipo de dados numérico. Selected especifica o índice de um item em um ComboBox ou ListBox .
**lExpr**
Tipo de dados lógico. A tabela a seguir lista as configurações para a propriedade Selected. Configuração Descrição True (.T.) O item está selecionado. False (.F.) O item não está selecionado. (Padrão)

# Observações

Aplica-se a: controle ComboBox | controle ListBox

Definir a propriedade Selected em um controle ListBox também define a propriedade ListItem e dispara o evento ProgrammaticChange.

A propriedade Selected é particularmente útil onde os usuários podem fazer seleções múltiplas. Você pode verificar rapidamente quais itens em uma lista estão selecionados. Você também pode usar esta propriedade para selecionar ou limpar itens em uma lista a partir de um programa. Para verificar se o terceiro item em uma caixa de lista está selecionado, use o seguinte código:

```foxpro
IF MyList.Selected(3)
  WAIT WINDOW "It's selected!"
ELSE
  WAIT WINDOW "It's not!"
ENDIF
```

# Exemplo

O exemplo a seguir cria uma caixa de lista. Uma matriz serve como origem dos itens que aparecem na caixa de lista, e o nome da matriz é especificado usando a propriedade RowSource. A propriedade RowSourceType é definida como 5 (matriz) para especificar que uma matriz é a origem dos itens na caixa de lista.

A propriedade MultiSelect da caixa de lista é definida como True (.T.), permitindo que você faça seleções múltiplas na caixa de lista. O item ou itens que você escolhe na caixa de lista são exibidos usando as propriedades ListCount, Selected e List para determinar o número de itens na caixa de lista e os itens que você escolheu.

```foxpro
CLEAR
DIMENSION gaMyListArray(10)
FOR gnCount = 1 to 10  && Fill the array with letters
   STORE REPLICATE(CHR(gnCount+64),6) TO gaMyListArray(gnCount)
NEXT
frmMyForm = CREATEOBJECT('Form')  && Create a form.
frmMyForm.Closable = .f.  && Disable window context menu.
frmMyForm.Move(150,10)  && Move the form.
frmMyForm.AddObject('cmbCommand1','cmdMyCmdBtn')  && Add "Quit" command button.
frmMyForm.AddObject('lstListBox1','lstMyListBox')  && Add ListBox control.
frmMyForm.lstListBox1.RowSourceType = 5  && Specifies an array.
frmMyForm.lstListBox1.RowSource = 'gaMyListArray' && Specifies array source containing list box items.
frmMyForm.cmbCommand1.Visible =.T.  && "Quit" command button visible.
frmMyForm.lstListBox1.Visible =.T.  && List box visible.
frmMyForm.SHOW  && Display form.
READ EVENTS  && Start event processing.
DEFINE CLASS cmdMyCmdBtn AS CommandButton  && Create command button.
   Caption = '\<Quit'  && Assign caption on the command button.
   Cancel = .T.  && Assign default Cancel command button (Esc).
   Left = 125  && Command button column.
   Top = 210  && Command button row.
   Height = 25  && Command button height.
   PROCEDURE Click
      CLEAR EVENTS  && Stop event processing and close form.
      CLEAR  && Clear main Visual FoxPro window.
ENDDEFINE
DEFINE CLASS lstMyListBox AS ListBox  && Create ListBox control.
   Left = 10  && List Box column
   Top = 10  && List Box row
   MultiSelect = .T.  && Allow selecting more than 1 item.
PROCEDURE Click
   ACTIVATE SCREEN
   CLEAR
   ? "Selected items:"
   ? "---------------"
   FOR nCnt = 1 TO ThisForm.lstListBox1.ListCount
      IF ThisForm.lstListBox1.Selected(nCnt)  && Is item selected?
         ? SPACE(5) + ThisForm.lstListBox1.List(nCnt) && Show item.
      ENDIF
   ENDFOR
ENDDEFINE
```
