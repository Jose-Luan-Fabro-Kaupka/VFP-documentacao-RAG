# Propriedade PolyPoints

Especifica uma matriz de coordenadas para criar formas de polígono usando o controle Shape e linhas de polígono usando o controle Line. Leitura/gravação em tempo de design e em tempo de execução.

Para controles Shape, PolyPoints cria uma forma de polígono. Para controles Line, PolyPoints cria uma linha de polígono ou forma.

```foxpro
Control.PolyPoints [= cArrayName]
```

# Valor de retorno
 **cArrayName**
Especifica o nome de uma matriz contendo pares de coordenadas para desenhar uma forma ou linha de polígono. As coordenadas usam o formato (X, Y). A matriz deve estar no escopo para que o objeto exiba corretamente o polígono ou polilinha Dica A matriz pode ter qualquer dimensão; no entanto, ter duas colunas facilita a programação. Armazene o ponto de coordenada X na primeira coluna e o ponto de coordenada Y na segunda coluna. A matriz deve ser preenchida inteiramente com valores numéricos; caso contrário, elementos finais contendo False (.F.) impedirão que a linha ou forma seja desenhada. Observação PolyPoints requer pelo menos dois pares de coordenadas para desenhar uma linha, três pares de coordenadas para desenhar uma linha de polígono, três pares de coordenadas para desenhar uma forma de polígono com o controle Shape e quatro pares de coordenadas para desenhar uma linha de polígono fechada ou forma com o controle Line. Para criar uma forma de polígono com o controle Line, o quinto par de coordenadas na matriz deve ter as mesmas coordenadas do primeiro par para desenhar o último segmento de linha e completar a forma de polígono. Ao definir a propriedade LineSlant para desenhar curvas Bezier, você deve especificar um total de (3n + 1) coordenadas com n representando o número de curvas que deseja desenhar. Para obter mais informações, consulte Propriedade LineSlant .

# Observações

Aplica-se a: Controle Line | Controle Shape

O Visual FoxPro desenha polígonos na ordem em que as coordenadas aparecem na matriz, o que afeta as regiões de preenchimento associadas aos polígonos. Você pode desenhar formas dentro do polígono sem tocar a borda do polígono especificando pontos dentro da borda. Para obter mais informações sobre regiões e estilos de preenchimento, consulte Propriedade FillStyle e Propriedade FillColor (Visual FoxPro).

As coordenadas especificadas na matriz são porcentagens relativas às dimensões do controle Shape (ou Line), de modo que o polígono será redimensionado conforme a forma é redimensionada.

Atualizar a matriz atualiza o controle Shape ou Line automaticamente na próxima vez que ele é desenhado.

Se a matriz contém um número ímpar de elementos, o último elemento é ignorado.

Se PolyPoints está definido, o Visual FoxPro ignora a propriedade Style quando está definida como 3 (Themed), a propriedade Curvature e as configurações da propriedade SpecialEffect tridimensional.

O Visual FoxPro redesenha a forma automaticamente quando a configuração Rotation, que gira a forma, é alterada. Para obter mais informações, consulte Propriedade Rotation (Visual FoxPro).

A matriz deve estar no escopo para o objeto exibir o polígono ou polilinha. Se você deseja exibir o polígono em tempo de design, a propriedade PolyPoints deve apontar para uma matriz pública no escopo. Para obter mais informações sobre escopo, consulte Acesso a Variáveis.

# Exemplo

O exemplo a seguir exibe um formulário com uma linha de polígono desenhada usando o controle Line baseada em uma matriz de coordenadas especificada pela propriedade PolyPoints.

```foxpro
DIMENSION poly[5,2]
poly[1,1]= 0
poly[1,2]= 50
poly[2,1]= 50
poly[2,2]= 100
poly[3,1]= 100
poly[3,2]= 50
poly[4,1]= 50
poly[4,2]= 0
poly[5,1]=0
poly[5,2]=50
frmMyForm = CREATEOBJECT('Form')
frmMyForm.AddObject('shpLine','Line')
frmMyForm.AddObject('cmdCmndBtn1','cmdMyCmndBtn1')
frmMyForm.shpLine.Top = 20
frmMyForm.shpLine.Left = 125
frmMyForm.shpLine.PolyPoints = "poly"
frmMyForm.shpLine.Visible = .T.
frmMyForm.cmdCmndBtn1.Visible =.T.
frmMyForm.Show
READ EVENTS
DEFINE CLASS cmdMyCmndBtn1 AS CommandButton
   Caption = '\<Quit'
   Cancel = .T.
   Left = 125
   Top = 150
   Height = 25
   PROCEDURE Click
      CLEAR EVENTS
ENDDEFINE
```
