# Controle OptionGroup

Cria um grupo de botões de opção.

```foxpro
OptionGroup
```

# Observações

Grupos de botões de opção são contêineres que contêm botões de opção. Um grupo de botões de opção permite fazer uma escolha em um conjunto de botões. Escolher um botão de opção torna essa escolha atual e libera a escolha anterior. Um marcador ao lado do botão de opção indica a escolha atual. Por exemplo, botões de opção podem ser usados para direcionar a saída a um arquivo, uma impressora ou uma janela.

Para obter mais informações sobre a criação de grupos de botões de opção, consulte Usando controles.

# Exemplo

O exemplo a seguir cria um controle OptionGroup e o posiciona em um formulário. O controle OptionGroup tem três botões e, dependendo do botão de opção clicado, exibe um círculo, uma elipse ou um quadrado. As propriedades Buttons e Caption são usadas para especificar o texto exibido ao lado de cada botão de opção.

O controle Shape é usado para criar o círculo, a elipse e o quadrado. O evento Click do controle OptionGroup usa uma estrutura DO CASE ... ENDCASE e a propriedade Value para exibir a forma apropriada quando você clica em um botão de opção.

```foxpro
frmMyForm = CREATEOBJECT('Form')  && Create a Form
frmMyForm.Closable = .F.  && Disable the Control menu box
frmMyForm.AddObject('cmdCommand1','cmdMyCmndBtn')  && Add Command button
frmMyForm.AddObject('opgOptionGroup1','opgMyOptGrp') && Add Option Group
frmMyForm.AddObject('shpCircle1','shpMyCircle')  && Add Circle Shape
frmMyForm.AddObject('shpEllipse1','shpMyEllipse')  && Add Ellipse Shape
frmMyForm.AddObject('shpSquare','shpMySquare')  && Add Box Shape
frmMyForm.cmdCommand1.Visible =.T.  && "Quit" Command button visible
frmMyForm.opgOptionGroup1.Buttons(1).Caption = "\<Circle"
frmMyForm.opgOptionGroup1.Buttons(2).Caption = "\<Ellipse"
frmMyForm.opgOptionGroup1.Buttons(3).Caption = "\<Square"
frmMyForm.opgOptionGroup1.SetAll("Width", 100) && Set Option group width
frmMyForm.opgOptionGroup1.Visible = .T.  && Option Group visible
frmMyForm.opgOptionGroup1.Click  && Show the circle
frmMyForm.SHOW  && Display the form
READ EVENTS  && Start event processing
DEFINE CLASS opgMyOptGrp AS OptionGroup  && Create an Option Group
   ButtonCount = 3  && Three Option buttons
   Top = 10
   Left = 10
   Height = 75
   Width = 100
   PROCEDURE Click
      ThisForm.shpCircle1.Visible = .F.  && Hide the circle
      ThisForm.shpEllipse1.Visible = .F.  && Hide the ellipse
      ThisForm.shpSquare.Visible = .F.  && Hide the square

      DO CASE
         CASE ThisForm.opgOptionGroup1.Value = 1
            ThisForm.shpCircle1.Visible = .T. && Show the circle
         CASE ThisForm.opgOptionGroup1.Value = 2
            ThisForm.shpEllipse1.Visible = .T.  && Show the ellipse
         CASE ThisForm.opgOptionGroup1.Value = 3
            ThisForm.shpSquare.Visible = .T.  && Show the square
      ENDCASE
ENDDEFINE
DEFINE CLASS cmdMyCmndBtn AS CommandButton  && Create Command button
   Caption = '\<Quit'  && Caption on the Command button
   Cancel = .T.  && Default Cancel Command button (Esc)
   Left = 125  && Command button column
   Top = 210  && Command button row
   Height = 25  && Command button height
   PROCEDURE Click
      CLEAR EVENTS  && Stop event processing, close Form
ENDDEFINE
DEFINE CLASS shpMyCircle AS SHAPE  && Create a circle
   Top = 10
   Left = 200
   Width = 100
   Height = 100
   Curvature = 99
   BackColor = RGB(255,0,0)  && Red
ENDDEFINE
DEFINE CLASS shpMyEllipse AS SHAPE  && Create an ellipse
   Top = 35
   Left = 200
   Width = 100
   Height = 50
   Curvature = 99
   BackColor = RGB(0,128,0)  && Green
ENDDEFINE
DEFINE CLASS shpMySquare AS SHAPE  && Create a square
   Top = 10
   Left = 200
   Width = 100
   Height = 100
   Curvature = 0
   BackColor = RGB(0,0,255)  && Blue
ENDDEFINE
```
