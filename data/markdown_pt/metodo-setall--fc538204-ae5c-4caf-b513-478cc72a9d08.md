# Método SetAll

Atribui uma configuração de propriedade em todos os controles, ou em uma determinada classe de controles, em um objeto Container.

```foxpro
Container.SetAll(cProperty, Value [, cClass])
```

#### Parâmetros
 **cProperty**
Especifica a propriedade a ser definida.
**Value**
Especifica a nova configuração da propriedade. O tipo de dados de Value depende da propriedade sendo definida.
**cClass**
Especifica o nome da classe (a classe na qual o objeto é baseado, não a classe base do Visual FoxPro para o objeto).

# Observações

Aplica-se a: Objeto Column | Controle CommandGroup | Objeto Container | Objeto Form | Objeto FormSet | Controle Grid | Controle OptionGroup | Objeto Page | Controle PageFrame | Variável de sistema _SCREEN | Objeto ToolBar

Use o método SetAll para definir uma propriedade para todos os controles, ou para uma determinada classe de controles, em um Container. Por exemplo, para definir a propriedade BackColor em todos os objetos Column em um controle Grid como vermelho, emita o seguinte:

```foxpro
Form1.Grid1.SetAll("BackColor", RGB(255, 0, 0), "Column")
```

Você também pode definir as propriedades para objetos contidos por outros objetos dentro do contêiner. Para definir a propriedade ForeColor dos Headers contidos por cada objeto Column contido em um controle Grid como verde, emita o seguinte:

```foxpro
Form1.Grid1.SetAll("ForeColor", RGB(0, 255, 0), "Header")
```

# Exemplo

O exemplo a seguir usa o método SetAll com a propriedade DynamicBackColor para especificar as cores de fundo dos registros em um controle Grid. Se o número de um registro exibido no Grid é par, o DynamicBackColor do registro é branco; caso contrário, seu DynamicBackColor é verde.

Um controle Grid é colocado em um formulário, e a tabela `customer` é aberta e seu conteúdo exibido no grid. A propriedade Caption é usada para especificar uma legenda de cabeçalho diferente (Customer ID) para o campo CUST_ID. Um botão de comando é colocado no formulário para fechar o formulário.

```foxpro
CLOSE ALL  && Close tables and databases
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE customer  IN 0  && Opens Customer table
frmMyForm = CREATEOBJECT('Form')  && Create a form
frmMyForm.Closable = .f.  && Disable the window pop-up menu
frmMyForm.AddObject('cmdCommand1','cmdMyCmdBtn')  && Add Command button
frmMyForm.AddObject('grdGrid1','Grid')  && Add Grid control
frmMyForm.grdGrid1.Left = 25  && Adjust Grid position
frmMyForm.grdGrid1.SetAll("DynamicBackColor", "IIF(MOD(RECNO(), 2)=0, RGB(255,255,255), RGB(0,255,0))", "Column")  && Alternate white and green records
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
