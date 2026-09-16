# Propriedade List

Uma matriz de cadeias de caracteres usada para acessar os itens em um controle ComboBox ou ListBox. Não disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
Control.List(nRow [, nCol]])[ = cChar]
```

# Valor de retorno
 **nRow**
Especifica a linha do item a ser recuperado usando a ordem de exibição. Por exemplo, nRow = 3 especifica a terceira linha mostrada na lista.
**nCol**
Especifica a coluna do item a ser recuperado usando a ordem de exibição. Por exemplo, nCol = 2 especifica a segunda coluna mostrada na lista. Se nCol não é especificado, a propriedade List recupera a primeira coluna por padrão. Especifique nCol apenas para controles ComboBox e ListBox que têm mais de uma coluna.
**cChar**
Especifica um valor a adicionar a uma caixa de combinação ou caixa de listagem.

# Observações

A propriedade List funciona em conjunto com a propriedade ListCount; enumerar uma lista de 1 a ListCount retorna todos os itens da lista.

Você não pode usar funções de matriz com a propriedade List. No entanto, se você definir a propriedade RowSourceType como 5 (Array) e definir a propriedade RowSource para a matriz de valores a serem contidos na lista, você pode usar funções de matriz na matriz especificada na propriedade RowSource.

> **Observação:** Quando RowSourceType é definido como 0 ou 1, adicione itens a uma caixa de combinação ou caixa de listagem usando o método AddItem. Para remover itens, use o método RemoveItem. Para manter os itens em ordem alfabética, defina a propriedade Sorted do controle como true (.T.) antes de adicionar itens à lista.

# Exemplo

Aplica-se a: ComboBox Control | ListBox Control

No exemplo a seguir, ListCount é usado para percorrer todos os itens especificados pela propriedade List da caixa de combinação ou caixa de listagem.

O exemplo a seguir cria uma caixa de listagem. A fonte dos itens que aparecem na caixa de listagem é uma matriz; a matriz é especificada com as propriedades RowSourceType e RowSource.

A propriedade MultiSelect da caixa de listagem é definida como true (.T.), permitindo fazer várias seleções na caixa de listagem. A propriedade ListCount é usada dentro de um loop FOR ... ENDFOR para exibir o item ou itens que você escolhe na caixa de listagem. A propriedade Selected é usada para determinar os itens que você escolheu, e a propriedade List é usada para retornar os itens.

```foxpro
CLEAR
DIMENSION gaMyListArray(10)
FOR gnCount = 1 to 10  && Fill the array with letters
   STORE REPLICATE(CHR(gnCount+64),6) TO gaMyListArray(gnCount)
ENDFOR
frmMyForm = CREATEOBJECT('Form')  && Create a Form
frmMyForm.Closable = .F.  && Disable the Control menu box
frmMyForm.Move(150,10)  && Move the form
* Add "Quit" command button and list box control
frmMyForm.AddObject('cmbCommand1','cmdMyCmdBtn')
frmMyForm.AddObject('lstListBox1','lstMyListBox')
* && Specifies an array containing listbox items
frmMyForm.lstListBox1.RowSourceType = 5
frmMyForm.lstListBox1.RowSource = 'gaMyListArray'
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
