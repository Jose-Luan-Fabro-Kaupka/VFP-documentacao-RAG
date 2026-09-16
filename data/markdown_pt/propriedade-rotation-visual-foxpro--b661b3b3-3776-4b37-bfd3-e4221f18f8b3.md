# Propriedade Rotation (Visual FoxPro)

Especifica um número de graus para girar um controle no sentido anti-horário. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
Control.Rotation [= nValue]
```

# Valor de retorno
 **nValue**
Especifica de 0 a 360 graus de rotação para um controle. A configuração padrão é 0.

# Observações

Aplica-se a: Label Control (Visual FoxPro) | Line Control | Shape Control

A clareza do texto pode variar dependendo da fonte e do tamanho da fonte especificados. Por exemplo, tamanhos de fonte pequenos aparecem melhor definidos em 0, 90 ou 180 graus.

Para controles Label, a seguinte funcionalidade se aplica ao definir Rotation:
 - Rotation funciona somente com fontes TrueType. Certas configurações de fonte, como FontStrikethru, podem não ser exibidas adequadamente em certos ângulos.
- Rotation não é suportado quando a propriedade Style está definida como 3 (Themed) porque o texto da etiqueta é desenhado pelo tema. Para mais informações, consulte a propriedade Style .
- Ao alinhar texto na etiqueta, a propriedade Alignment é respeitada somente quando Rotation está definida como 0. Caso contrário, a etiqueta é centralizada e depois girada. Para mais informações, consulte a propriedade Alignment .
- A propriedade WordWrap é suportada somente quando Rotation está definida como 0. Em outras palavras, se Rotation estiver definida com um valor diferente de 0, não ocorre quebra de palavras mesmo se WordWrap estiver definida como True (.T.). Para mais informações, consulte a propriedade WordWrap .
- A propriedade AutoSize não redimensiona o controle com base na configuração Rotation. O texto é sempre centralizado na etiqueta. Portanto, é recomendável garantir que a etiqueta seja grande o suficiente para acomodar qualquer posição de rotação. Para mais informações, consulte a propriedade AutoSize .
- Teclas de atalho (\<) especificadas na propriedade Caption não são exibidas, embora permaneçam funcionais, quando as etiquetas são giradas. Para mais informações, consulte a propriedade Caption (Visual FoxPro) .

Para controles Shape e Line, a seguinte funcionalidade se aplica ao definir Rotation:
 - Rotation se aplica ao desenhar formas de polígono e linhas criadas pela propriedade PolyPoints. Para mais informações, consulte a propriedade PolyPoints .
- O controle gira em torno de seu eixo central.

# Exemplo

O exemplo a seguir cria um formulário e adiciona uma etiqueta e dois botões de comando baseados em classes personalizadas. A propriedade Rotation é definida cada vez que você clica no botão de comando Rotate, que gira a etiqueta.

As linhas de código a seguir usam a função CREATEOBJECT( ) para criar um formulário e o método AddObject para adicionar um controle Label e dois botões de comando personalizados ao formulário. A propriedade Visible é então definida como True (.T.) para a etiqueta e os botões de comando para que sejam exibidos no formulário. O método Show exibe o formulário e o comando READ EVENTS inicia o processamento de eventos. O comando DEFINE CLASS define uma classe Label personalizada e classes CommandButton e contém configurações para as propriedades apropriadas.

```foxpro
frmMyForm = CREATEOBJECT('Form')
frmMyForm.AddObject('lblLabel1','lblMyLabel')
frmMyForm.AddObject('cmdCmndBtn1','cmdMyCmndBtn1')
frmMyForm.AddObject('cmdCmndBtn2','cmdMyCmndBtn2')
frmMyForm.lblLabel1.Visible = .T.
frmMyForm.cmdCmndBtn1.Visible =.T.
frmMyForm.cmdCmndBtn2.Visible =.T.
frmMyForm.Show
READ EVENTS
DEFINE CLASS lblMyLabel AS Label
   Caption = "MyLabel"
   Left = 150
   Top = 50
   Height = 50
   Width = 50
ENDDEFINE
```

A definição de classe para o seguinte botão de comando incrementa a propriedade Rotation no evento Click cada vez que o botão é clicado. Quando a propriedade Rotation é aumentada, a etiqueta gira pelo número especificado de graus. Quando o número de graus totaliza 360, a propriedade Rotation é redefinida para 0 para que a etiqueta apareça na posição inicial.

```foxpro
DEFINE CLASS cmdMyCmndBtn1 AS CommandButton
   Caption = '\<Rotate'
   Left = 125
   Top = 150
   Height = 25
   PROCEDURE Click
      ThisForm.lblLabel1.Visible = .F.
      ThisForm.lblLabel1.Rotation = ThisForm.lblLabel1.Rotation + 45
      IF ThisForm.lblLabel1.Rotation = 360
         ThisForm.lblLabel1.Rotation = 0
      ENDIF
      ThisForm.lblLabel1.Visible = .T.
ENDDEFINE
```

A definição de classe para o seguinte botão de comando inclui o comando CLEAR EVENTS no evento Click do botão de comando para interromper o processamento de eventos e fechar o formulário.

```foxpro
DEFINE CLASS cmdMyCmndBtn2 AS CommandButton
   Caption = '\<Quit'
   Cancel = .T.
   Left = 125
   Top = 200
   Height = 25
   PROCEDURE Click
      CLEAR EVENTS
ENDDEFINE
```
