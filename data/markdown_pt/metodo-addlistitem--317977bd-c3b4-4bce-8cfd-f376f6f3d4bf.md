# Método AddListItem

Adiciona um novo item a um controle ComboBox ou ListBox, opcionalmente permitindo especificar o ID do item.

```foxpro
Control.AddListItem(cItem [, nItemID] [, nColumn])
```

#### Parâmetros
 **cItem**
Especifica o item a adicionar ao controle.
**nItemID**
Especifica um inteiro representando o ID exclusivo do item no controle. The maximum value you can specify for nItemID is 32,767. If you omit nItemID and the Sorted property is set to True (.T.), cItem is added in alphabetic sort order. If you omit nItemID and the Sorted property is set to False (.F.), cItem is added to the end of the list of the ComboBox or ListBox.
**nColumn**
Especifica a coluna do controle à qual adicionar o novo item. O padrão é 1.

# Observações

Aplica-se a: ComboBox Control | ListBox Control

Use o método AddItem ou AddListItem quando a propriedade RowSourceType estiver definida como 0 (None).

Cada item adicionado a um ComboBox ou ListBox tem dois números de identificação atribuídos:
 - nItemID , um inteiro correspondente ao ID exclusivo do item no controle: o primeiro item corresponde a nItemID = 1, a menos que outro nItemID seja especificado.
- nIndex , um inteiro correspondente à ordem em que os itens são exibidos pelo controle: o primeiro item no controle corresponde a nIndex = 1.

A barra invertida ("\") é tratada como caractere especial quando usada na expressão de um item. The following rules apply for this character:
 - Você pode desabilitar um item em uma list box ou combo box adicionando uma única barra invertida no início da expressão.
- Qualquer múltiplo de duas barras invertidas usado na expressão é exibido como uma única barra invertida. For example, one or two backslashes used together will display as one, three or four backslashes together will display as two. The following example code contains a list box item containing a Universal Naming Convention (UNC) path. The code displays in the list box as \\MyServer\MyMachine\MyFolder . MyForm.List1.AddItem("\\\\MyServer\\MyMachine\\MyFolder")
- Se a expressão começar com múltiplas barras invertidas, o item não é desabilitado. If you want to disable an item that begins with multiple backslashes, add a backslash and a close bracket (]) to the beginning of the item. For example, the following disables the UNC path item in the list box: MyForm.List1.AddItem("\]\\\MyServer\\MyMachine\\MyFolder")
- Para incluir uma linha separadora, use uma barra invertida seguida de hífen como o item a adicionar à list box. For example, the following code adds a separator line to a list box. MyForm.List1.AddItem("\-")

# Exemplo

Este exemplo demonstra o uso dos métodos AddItem e AddListItem para adicionar valores à matriz ListItem. Formas corretas e incorretas de preencher um combo box são mostradas para clareza.

```foxpro
PUBLIC ofrmListExamples
ofrmListExamples=NEWOBJECT("frmListExamples")
ofrmListExamples.Show
RETURN
DEFINE CLASS frmListExamples AS form
 DataSession = 2
 Top = 0
 Left = 0
 Height = 262
 Width = 325
 Caption = "List and ListItem Array Example"
 Name = "frmListExamples"
 ADD OBJECT shape1 AS shape WITH ;
  Top = 43, ;
  Left = 32, ;
  Height = 76, ;
  Width = 261, ;
  SpecialEffect = 0, ;
  Name = "Shape1"
 ADD OBJECT cbolistbad AS combobox WITH ;
  ColumnCount = 3, ;
  ColumnWidths = "100,100,50", ;
  Height = 22, ;
  Left = 111, ;
  Sorted = .T., ;
  Style = 2, ;
  TabIndex = 1, ;
  Top = 53, ;
  Width = 147, ;
  Name = "cboListBad"
 ADD OBJECT cbolistitem AS combobox WITH ;
  ColumnCount = 3, ;
  ColumnWidths = "100,100,50", ;
  Left = 34, ;
  Sorted = .T., ;
  Style = 2, ;
  TabIndex = 3, ;
  Top = 154, ;
  Name = "cboListItem"
 ADD OBJECT label1 AS label WITH ;
  FontBold = .T., ;
  Caption = "Using the List Array:", ;
  Height = 17, ;
  Left = 34, ;
  Top = 24, ;
  Width = 176, ;
  TabIndex = 7, ;
  Name = "Label1"
 ADD OBJECT label2 AS label WITH ;
  FontBold = .T., ;
  Caption = "Using the ListItem Array:", ;
  Height = 17, ;
  Left = 34, ;
  Top = 135, ;
  Width = 173, ;
  TabIndex = 8, ;
  Name = "Label2"
 ADD OBJECT cbolistgood AS combobox WITH ;
  ColumnCount = 3, ;
  ColumnWidths = "100,100,50", ;
  Height = 22, ;
  Left = 111, ;
  Sorted = .T., ;
  style = 2, ;
  TabIndex = 2, ;
  Top = 86, ;
  Width = 147, ;
  Name = "cboListGood"
 ADD OBJECT label3 AS label WITH ;
  Alignment = 1, ;
  Caption = "Wrong!", ;
  Height = 17, ;
  Left = 51, ;
  Top = 56, ;
  Width = 47, ;
  TabIndex = 9, ;
  Name = "Label3"
 ADD OBJECT label4 AS label WITH ;
  Alignment = 1, ;
  Caption = "Right!", ;
  Height = 17, ;
  Left = 58, ;
  Top = 89, ;
  Width = 40, ;
  TabIndex = 10, ;
  Name = "Label4"
 PROCEDURE cbolistbad.Init
  WITH This
   .AddItem( 'Cleveland' )
   .AddItem( 'Ohio', .NewIndex, 2 )
   .AddItem( '44122', .NewIndex, 3 )
   .AddItem( 'Caversham' )
   .AddItem( 'England', .NewIndex, 2 )
   .AddItem( 'RG4 8BX', .NewIndex, 3 )
   .AddItem( 'Buffalo' )
   .AddItem( 'New York', .NewIndex, 2 )
   .AddItem( '14228', .NewIndex, 3 )
   .AddItem( 'Milwaukee' )
   .AddItem( 'Wisconsin', .NewIndex, 2 )
   .AddItem( '43225', .NewIndex, 3 )
   .AddItem( 'International Falls')
   .AddItem( 'Minnesota', .NewIndex, 2 )
   .AddItem( '42666', .NewIndex, 3 )
  ENDWITH
 ENDPROC
 PROCEDURE cbolistitem.Init
  WITH This
   .AddListitem( 'Cleveland' )
   .AddListItem( 'Ohio', .NewItemID, 2 )
   .AddListItem( '44122', .NewItemID, 3 )
   .AddListItem( 'Caversham' )
   .AddListItem( 'England', .NewItemID, 2 )
   .AddListItem( 'RG4 8BX', .NewItemID, 3 )
   .AddListItem( 'Buffalo' )
   .AddListItem( 'New York', .NewItemID, 2 )
   .AddListItem( '14228', .NewItemID, 3 )
   .AddListItem( 'Milwaukee' )
   .AddListItem( 'Wisconsin', .NewItemID, 2 )
   .AddListItem( '43225', .NewItemID, 3 )
   .AddListItem( 'International Falls')
   .AddListItem( 'Minnesota', .NewItemID, 2 )
   .AddListItem( '42666', .NewItemID, 3 )
  ENDWITH
 ENDPROC
 PROCEDURE cbolistgood.Init
  WITH This
   .AddItem( 'Cleveland' )
   .List[.NewIndex, 2] = 'Ohio'
   .List[.NewIndex, 3] = '44122'
   .AddItem( 'Caversham' )
   .List[.NewIndex, 2] = 'England'
   .List[.NewIndex, 3] = 'RG4 8BX'
   .AddItem( 'Buffalo' )
   .List[.NewIndex, 2] = 'New York'
   .List[.NewIndex, 3] = '14228'
   .AddItem( 'Milwaukee' )
   .List[.NewIndex, 2] = 'Wisconsin'
   .List[.NewIndex, 3] = '43225'
   .AddItem( 'International Falls' )
   .List[.NewIndex, 2] = 'Minnesota'
   .List[.NewIndex, 3] = '42666'
  ENDWITH
 ENDPROC
ENDDEFINE
```
