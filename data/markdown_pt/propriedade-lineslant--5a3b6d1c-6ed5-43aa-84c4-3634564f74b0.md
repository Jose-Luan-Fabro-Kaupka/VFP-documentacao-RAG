# Propriedade LineSlant

Especifica a direção da inclinação de um controle Line ou cantos arredondados (curva de Bezier) para uma linha poligonal desenhada com um controle Line. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
Line.LineSlant [= cSlant]
```

# Valor de retorno
 **cSlant**
Especifica a direção da inclinação de um controle de linha ou cantos arredondados para linhas poligonais desenhadas com um controle de linha. A tabela a seguir lista os valores para cSlant. cSlant Descrição \ A linha inclina do canto superior esquerdo ao inferior direito. (Padrão) / A linha inclina do canto inferior esquerdo ao superior direito. S ou s A linha é desenhada como uma curva de Bezier quando uma matriz válida de coordenadas é definida para a propriedade PolyPoints. Para remover esta configuração, defina LineSlant como "\" ou "/". Observação A matriz PolyPoints deve especificar um total de (3 n + 1) coordenadas com n representando o número de curvas que você deseja desenhar como curva de Bezier. Se PolyPoints não contém coordenadas que formam um polígono válido, e a configuração "S" ou "s" é especificada, nenhuma linha é desenhada. Para obter mais informações, consulte Propriedade PolyPoints.

# Observações

Aplica-se a: Controle Line

# Exemplo de código

O exemplo a seguir cria um formulário com um controle Line e três botões de comando que demonstram os três valores para a propriedade LineSlant.

```foxpro
Public oForm
oForm = Createobject('Form')
With oForm
   .AddObject('linSample','Line')
   .AddObject('cmdSlantUp','cmdSlantUp')
   .AddObject('cmdSlantDown','cmdSlantDown')
   .AddObject('cmdBezier','cmdBezier')
   .linSample.Top = 10
   .linSample.Left = 25
   .linSample.Width = 300
   .linSample.Height = 200
   .SetAll('Visible', .T.)
* Creates an array of points that define the curve.
   Dimension aBezierPoints[4,2]
      aBezierPoints[1,1]= 0
      aBezierPoints[1,2]= 0
      aBezierPoints[2,1]= 100
      aBezierPoints[2,2]= 25
      aBezierPoints[3,1]= 0
      aBezierPoints[3,2]= 75
      aBezierPoints[4,1]= 100
      aBezierPoints[4,2]= 100
Endwith
oForm.Show(1)
* Defines a button that changes the slant of the line.
Define Class cmdSlantUp As CommandButton
   Caption = 'Slant \<Up (/)'
   Left = 25
   Top = 220
   Height = 25
   Procedure Click
      Thisform.linSample.Polypoints = ""
      Thisform.linSample.LineSlant = '/'  && Slant up
   Endproc
Enddefine
* Defines a button that changes the slant of the line.
Define Class cmdSlantDown As CommandButton
   Caption = 'Slant \<Down (\)'
   Left = 125
   Top = 220
   Height = 25
   Procedure Click
      Thisform.linSample.Polypoints = ""
      Thisform.linSample.LineSlant = '\'  && Slant down
   Endproc
Enddefine
* Defines a button that changes the line to a Bezier curve.
Define Class cmdBezier As CommandButton
   Caption = 'Be\<zier Curve (S) '
   Left = 225
   Top = 220
   Height = 25
   Procedure Click
      Thisform.linSample.Polypoints = "aBezierPoints" && Specifies points on the curve.
      Thisform.linSample.LineSlant = 'S' && Specifies to display a curve.
      Thisform.linSample.Visible = .T.
      Thisform.Visible = .T.
   Endproc
Enddefine
```
