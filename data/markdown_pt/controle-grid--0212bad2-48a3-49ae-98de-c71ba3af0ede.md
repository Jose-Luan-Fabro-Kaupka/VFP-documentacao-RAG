# Controle Grid

Cria uma grade.

```foxpro
Grid
```

# Observações

Uma grade é um objeto contêiner que exibe dados em linhas e colunas, com aparência semelhante à janela Browse. Ela contém objetos Column, que podem conter um objeto Header e controles. Como a grade, suas colunas, cabeçalhos e controles têm conjuntos próprios de propriedades, você possui controle total sobre cada elemento. É possível criar uma grade interativamente usando o Grid Builder.

Para obter mais informações sobre criação de grades, consulte Uso de controles.

# Exemplo

O exemplo a seguir coloca um controle Grid em um formulário. A tabela `customer` é aberta e seu conteúdo é exibido na grade. A propriedade Caption define outro título de cabeçalho (Customer ID) para o campo CUST_ID. Um botão de comando fecha o formulário.

O método SetAll é usado com a propriedade DynamicBackColor para especificar as cores de fundo dos registros. Se o número do registro for par, DynamicBackColor será branco; caso contrário, será verde.

```foxpro
CLOSE ALL  && Close tables and databases
OPEN DATABASE (HOME(2) + 'data\testdata')
USE customer  IN 0  && Opens Customer table
frmMyForm = CREATEOBJECT('Form')  && Create a Form
frmMyForm.Closable = .F.  && Disable the window pop-up menu
frmMyForm.AddObject('cmdCommand1','cmdMyCmdBtn')  && Add Command button
frmMyForm.AddObject('grdGrid1','Grid')  && Add Grid control
frmMyForm.grdGrid1.Left = 25  && Adjust Grid position
frmMyForm.grdGrid1.SetAll("DynamicBackColor", ;
   "IIF(MOD(RECNO(), 2)=0, RGB(255,255,255) ;
   , RGB(0,255,0))", "Column")  && Alternate white and green records
frmMyForm.grdGrid1.Visible = .T.  && Grid control visible
frmMyForm.cmdCommand1.Visible =.T.  && "Quit" Command button visible
frmMyForm.grdGrid1.Column1.Header1.Caption = 'Customer ID'
frmMyForm.SHOW  && Display the form
READ EVENTS  && Start event processing
DEFINE CLASS cmdMyCmdBtn AS CommandButton  && Create Command button
   Caption = '\<Quit'  && Caption on the Command button
   Cancel = .T.  && Default Cancel Command button (Esc)
   Left = 125  && Command button column
   Top = 210  && Command button row
   Height = 25  && Command button height
   PROCEDURE Click
      CLEAR EVENTS  && Stop event processing, close form
      CLOSE ALL  && Close table and database
ENDDEFINE
```
