# Exemplo Draw Lines and Shapes on a Form

Arquivo: ...\Samples\Solution\Forms\Graphics\Fdmain.scx

Este exemplo ilustra como usar métodos gráficos de formulário (PSet, Line e Circle) e propriedades (DrawMode, DrawStyle, DrawWidth) para permitir que um usuário desenhe figuras e formas em um formulário em cores diferentes e com larguras de caneta diferentes.

O exemplo inclui uma barra de ferramentas (definida em Fdproc.prg) e um formulário (baseado em frmFD em Fd.vcx). O usuário pode selecionar configurações na barra de ferramentas que afetam as propriedades gráficas do formulário. Quando o formulário está configurado para aceitar desenho do usuário, o MousePointer é definido como 2 (mira).

A funcionalidade de desenho está codificada nos métodos associados aos eventos MouseDown e MouseMove do formulário.

```foxpro
* MouseDown
PARAMETERS nButton, nShift, nXCoord, nYCoord
IF THIS.MousePointer = 2
   THIS.PSet(nXCoord, nYCoord)
ENDIF
* MouseMove
PARAMETERS nButton, nShift, nXCoord, nYCoord
IF THIS.MousePointer = 2
   THISFORM.LINE(nXCoord, nYCoord)
ENDIF
```
