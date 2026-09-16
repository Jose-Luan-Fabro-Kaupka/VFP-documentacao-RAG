# Evento Click

Ocorre quando você inclui código em um programa que dispara o evento, quando o usuário clica em um controle, altera o valor de certos controles ou clica em uma área em branco de um formulário.

```foxpro
PROCEDURE Object.Click
```

# Observações

Aplica-se a: CheckBox Control | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | Control Object (Visual FoxPro) | EditBox Control | Form Object | Grid Control | Header Object | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OptionButton Control | OptionGroup Control | Page Object | PageFrame Control | Shape Control | Spinner Control | TextBox Control (Visual FoxPro) | ToolBar Object

O evento Click ocorre quando o usuário:
 - Clica em uma caixa de seleção, botão de comando, caixa de combinação, caixa de listagem ou botão de opção com o botão esquerdo do mouse.
- Pressiona a tecla SPACEBAR quando um botão de comando, botão de opção ou caixa de seleção tem o foco.
- Pressiona ENTER quando um formulário tem um botão de comando com sua propriedade Default definida como True (.T.).
- Pressiona a tecla de acesso de um controle. Por exemplo, se o caption de um botão de comando é "\<Go", pressionar ALT+G dispara o evento Click.
- Clica em uma área em branco de um formulário. Eventos Click em um formulário não ocorrem quando o ponteiro está sobre a barra de título, o ícone do menu Window ou as bordas da janela.
- Clica na área de entrada de texto de um spinner.
- Clica em um controle desabilitado. O evento Click ocorre para o contêiner no qual o controle desabilitado está posicionado.

O evento Click também ocorre como resultado de código que você inclui e que emite o comando MOUSE.

> **Observação:** Redimensionar cabeçalhos de coluna de grade não dispara o evento Click para o cabeçalho da coluna. Isso afeta os separadores de coluna.

# Exemplo

O exemplo a seguir cria um controle OptionGroup e posiciona o controle em um formulário. O controle OptionGroup tem três botões, e dependendo do botão de opção em que você clicar, um círculo, elipse ou quadrado aparece. A propriedade ButtonCount é usada para especificar o número de botões no OptionGroup. As propriedades Buttons e Caption são usadas para especificar o texto exibido ao lado de cada botão de opção.

O controle Shape é usado para criar o círculo, elipse e quadrado. O evento Click do controle OptionGroup usa uma estrutura DO CASE ... ENDCASE e a propriedade Value para exibir a forma apropriada quando você clica em um botão de opção.

```foxpro
frmMyForm = CREATEOBJECT('Form')  && Create a Form
frmMyForm.Closable = .F.  && Disable the window pop-up menu
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
