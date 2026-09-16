# Função OBJTOCLIENT( )

Retorna uma posição ou dimensão de um controle ou objeto em relação ao seu formulário.

```foxpro
OBJTOCLIENT(ObjectName, nPosition)
```

#### Parâmetros
 **ObjectName**
Especifica o nome do controle ou objeto para o qual a posição no formulário é retornada.
**nPosition**
Especifica qual posição ou dimensão do formulário do controle ou objeto é retornada. A tabela a seguir lista os valores de nPosition e a posição ou dimensão correspondente retornada. nPosition Posição ou dimensão 1 Top 2 Left 3 Width 4 Height

# Valor de retorno

Numérico

# Observações

OBJTOCLIENT( ) retorna a posição ou dimensão de um controle ou objeto em relação à área de cliente do formulário no qual reside. Por exemplo, um controle ou objeto pode ser colocado em uma page em um page frame, e o page frame é colocado em um formulário. As propriedades Top, Left, Width e Height retornam a posição ou dimensão de um controle ou objeto em relação à page na qual é colocado. No entanto, você pode usar OBJTOCLIENT( ) para determinar a posição ou dimensão de um controle ou objeto em relação ao formulário no qual a page é colocada.

O valor retornado por OBJTOCLIENT( ) está em pixels.

# Exemplo

O exemplo a seguir usa OBJTOCLIENT( ) para exibir as posições e dimensões de duas check boxes em relação ao formulário no qual são colocadas. As propriedades Top, Left, Width e Height também são usadas para exibir as posições e dimensões das duas check boxes em relação ao page frame no qual são colocadas.

Um command button e um page frame são colocados em um formulário. A propriedade PageCount é usada para especificar o número de pages no page frame. A propriedade Tabs é definida como true (.T.) para especificar que o page frame tem guias para cada page. Check boxes são colocadas em cada page em posições diferentes.

Quando uma check box é clicada, o procedimento Click da check box é executado. Se a check box estiver marcada, as propriedades Top, Left, Width e Height são usadas para exibir as posições e dimensões da check box em relação ao page frame, e OBJTOCLIENT( ) é usada para exibir as posições e dimensões da check box em relação ao formulário. Se a check box estiver desmarcada, a janela principal do Microsoft Visual FoxPro é limpa.

```foxpro
CLEAR
STORE _DBLCLICK TO gnDblClick  && Save double-click value
STORE 0.05 TO _DBLCLICK  && Make double-click unlikely
frmMyForm = CREATEOBJECT('Form')  && Create a form
frmMyForm.Closable = .f.  && Disable the window pop-up menu

frmMyForm.Move(150,10)  && Move the form
frmMyForm.AddObject('cmbCommand1','cmdMyCmdBtn')  && Add Command button
frmMyForm.AddObject('pgfPageFrame1','pgfMyPageFrame')  && Add PageFrame
frmMyForm.pgfPageFrame1.Page1.AddObject('chkCheckBox1','chkMyCheckBox1')
frmMyForm.pgfPageFrame1.Page2.AddObject('chkCheckBox2','chkMyCheckBox2')
frmMyForm.cmbCommand1.Visible =.T.  && "Quit" Command button visible
frmMyForm.pgfPageFrame1.Visible =.T.  && PageFrame visible
frmMyForm.pgfPageFrame1.Page1.chkCheckBox1.Visible =.T.
frmMyForm.pgfPageFrame1.Page2.chkCheckBox2.Visible =.T.
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
      STORE gnDblClick TO _DBLCLICK  && Restore double-click value
ENDDEFINE
DEFINE CLASS pgfMyPageFrame AS PageFrame  && Create PageFrame
   Left = 10  && PageFrame  column
   Top = 10  && PageFrame  row
   Height = 175  && PageFrame  height
   Width = 350  && PageFrame  height
   PageCount = 2  && 2 Pages on the PageFrame
   Tabs = .T.  && Tabs visible
ENDDEFINE
DEFINE CLASS chkMyCheckBox1 AS CheckBox  && Create first Check Box
   Top = 0
   Width = 200
   Caption = 'Display Position'
PROCEDURE Click
   DO CASE
      CASE ThisForm.pgfPageFrame1.Page1.chkCheckBox1.Value = 0
         ACTIVATE SCREEN
         CLEAR
      CASE ThisForm.pgfPageFrame1.Page1.chkCheckBox1.Value = 1
         ACTIVATE SCREEN
         CLEAR
         ? 'Positions relative'
         ? 'to PageFrame:'
         ?
         ? 'Top: '
         ?? ALLTRIM(STR;
            (ThisForm.pgfPageFrame1.Page1.chkCheckBox1.Top))
         ? 'Left: '
         ?? ALLTRIM(STR;
            (ThisForm.pgfPageFrame1.Page1.chkCheckBox1.Left))
         ? 'Width: '
         ?? ALLTRIM(STR;
            (ThisForm.pgfPageFrame1.Page1.chkCheckBox1.Width))
         ? 'Height: '
         ?? ALLTRIM(STR;
            (ThisForm.pgfPageFrame1.Page1.chkCheckBox1.Height))
         ?
         ? 'Positions relative'
         ? 'to Form:'
         ?
         ? 'Top: '
         ?? ALLTRIM(STR(OBJTOCLIENT;
            (ThisForm.pgfPageFrame1.Page1.chkCheckBox1,1)))
         ? 'Left: '
         ?? ALLTRIM(STR(OBJTOCLIENT;
            (ThisForm.pgfPageFrame1.Page1.chkCheckBox1,2)))
         ? 'Width: '
         ?? ALLTRIM(STR(OBJTOCLIENT;
            (ThisForm.pgfPageFrame1.Page1.chkCheckBox1,3)))
         ? 'Height: '
         ?? ALLTRIM(STR(OBJTOCLIENT(ThisForm.pgfPageFrame1.Page1.chkCheckBox1,4)))
   ENDCASE
ENDDEFINE
DEFINE CLASS chkMyCheckBox2 AS CheckBox  && Create second Check Box
   Top = 30
   Left = 175
   Width = 200
   Caption = 'Display Position'
PROCEDURE CLICK
   DO CASE
      CASE ThisForm.pgfPageFrame1.Page2.chkCheckBox2.Value = 0
         ACTIVATE SCREEN
         CLEAR
      CASE ThisForm.pgfPageFrame1.Page2.chkCheckBox2.Value = 1
         ACTIVATE SCREEN
         CLEAR
         ? 'Positions relative'
         ? 'to PageFrame:'
         ?
         ? 'Top: '
         ?? ALLTRIM(STR(ThisForm.pgfPageFrame1.Page2.chkCheckBox2.Top))
         ? 'Left: '
         ?? ALLTRIM(STR;
            (ThisForm.pgfPageFrame1.Page2.chkCheckBox2.Left))
         ? 'Width: '
         ?? ALLTRIM(STR;
            (ThisForm.pgfPageFrame1.Page2.chkCheckBox2.Width))
         ? 'Height: '
         ?? ALLTRIM(STR;
            (ThisForm.pgfPageFrame1.Page2.chkCheckBox2.Height))

         ?
         ? 'Positions relative'
         ? 'to Form:'
         ?
         ? 'Top: '
         ?? ALLTRIM(STR(OBJTOCLIENT;
            (ThisForm.pgfPageFrame1.Page2.chkCheckBox2,1)))
         ? 'Left: '
         ?? ALLTRIM(STR(OBJTOCLIENT;
            (ThisForm.pgfPageFrame1.Page2.chkCheckBox2,2)))
         ? 'Width: '
         ?? ALLTRIM(STR(OBJTOCLIENT;
            (ThisForm.pgfPageFrame1.Page2.chkCheckBox2,3)))
         ? 'Height: '
         ?? ALLTRIM(STR(OBJTOCLIENT;
            (ThisForm.pgfPageFrame1.Page2.chkCheckBox2,4)))
   ENDCASE
ENDDEFINE
```
