# Propriedades BackColor, ForeColor

Especificam a cor de fundo ou de primeiro plano usada para exibir texto e elementos gráficos em um objeto. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
Object.BackColor[ = nColor]
Object.ForeColor[ = nColor]
```

# Valor de retorno
 **nColor**
Especifica um único valor de cor. Se nColor for um valor negativo, o Visual FoxPro usará o inteiro e ignorará quaisquer problemas de estouro. Por exemplo, -1 equivale a 0xFFFFFFFF. A tabela a seguir lista valores de cor típicos. Cor Valores RGB nColor Branco 255, 255, 255 16777215 Preto 0, 0, 0 0 Cinza 192, 192, 192 12632256 Cinza escuro 128, 128, 128 8421504 Vermelho 255, 0, 0 255 Vermelho escuro 128, 0, 0 128 Amarelo 255, 255, 0 65535 Amarelo escuro 128, 128, 0 32896 Verde 0, 255, 0 65280 Verde escuro 0, 128, 0 32768 Ciano 0, 255, 255 16776960 Ciano escuro 0, 128, 128 8421376 Azul 0, 0, 255 16711680 Azul escuro 0, 0, 128 8388608 Magenta 255, 0, 255 16711935 Magenta escuro 128, 0, 128 8388736

# Observações

Aplica-se a: controle CheckBox | objeto Column | controle ComboBox | controle CommandButton | controle CommandGroup | objeto Container | objeto Control (Visual FoxPro) | controle EditBox | objeto Form | controle Grid | objeto Header | controle Label (Visual FoxPro) | controle OptionButton | controle OptionGroup | objeto Page | variável de sistema _SCREEN | controle Shape | controle Spinner | controle TextBox (Visual FoxPro) | objeto ToolBar

O Visual FoxPro usa um esquema de cores vermelho-verde-azul (RGB). Cada componente vermelho, verde e azul é representado por um número entre 0 e 255. Use a função RGB( ) para converter as três cores componentes em um único nColor composto.

> **Observação:** A propriedade ForeColor não se aplica aos controles CommandGroup, OptionGroup ou Shape.

As configurações de cor, ou temas, do sistema operacional definem as configurações padrão de cor das propriedades BackColor e ForeColor.

Se a propriedade Themes for True (.T.), definir o valor da propriedade BackColor produzirá uma sobreposição com 35% de transparência sobre o botão com tema. Isso produz um efeito de colorização.

A propriedade BackColor de Page é desconsiderada se Themes de Page for True (.T.). Entretanto, como uma página é apenas uma representação visual no Class Designer, a cor de fundo é exibida.

# Exemplo

O exemplo a seguir demonstra como o controle Shape pode ser usado para exibir um círculo, uma elipse ou um quadrado em um formulário e como a propriedade BackColor pode especificar a cor de cada forma.

Um formulário é criado, e um conjunto de botões de opção e um botão de comando são colocados nele. Quando você escolhe um dos botões de opção, a forma correspondente é exibida no formulário. A propriedade BackColor especifica a cor de cada forma. As propriedades Height, Width e Curvature de cada forma determinam o tipo de forma criada.

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
