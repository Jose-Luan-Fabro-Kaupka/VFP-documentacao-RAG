# Exemplo: permitir que os usuários arrastem e soltem controles

Arquivo: ...\Samples\Solution\Forms\Ddrop.scx

Este exemplo explica como implementar operações de arrastar e soltar. Uma página do formulário ilustra o arraste manual de controles chamando o método Drag. Chamar explicitamente o método Drag permite processar outro código no evento Click do controle. A outra página ilustra o uso da configuração Automatic de DragMode, para que a operação seja iniciada automaticamente quando o usuário pressiona o botão do mouse sobre os controles.

# Reposicionando o botão de comando

No evento MouseMove de cmdDrop, se o botão esquerdo do mouse estiver pressionado, determine a distância do ponteiro em relação às partes superior e esquerda do botão de comando e inicie a operação de arrastar.

```foxpro
LPARAMETERS nButton, nShift, nXCoord, nYCoord
IF nButton = 1 && Left button
   THISFORM.XOffset = nXCoord – THIS.Left
   THISFORM.YOffset = nYCoord - THIS.Top
   THIS.Drag
ENDIF
```

No evento DragDrop da página em que o botão de comando está, reposicione-o.

```foxpro
oSource.Left = nXCoord - THISFORM.XOffset
oSource.Top = nYCoord - THISFORM.Yoffset
```

# Alterando a cor da forma

A propriedade DragMode dos quadrados coloridos na página Change Colors do formulário está definida como 1 – Automatic. Assim que o usuário pressiona o botão do mouse sobre os quadrados, a operação de arrastar começa. Qualquer código adicionado ao evento Click dos quadrados nunca seria executado.

O código no evento DragDrop do círculo altera sua propriedade BackColor para corresponder à da origem da operação de arrastar.

```foxpro
LPARAMETERS oSource, nXCoord, nYCoord
THIS.BackColor = oSource.BackColor
```
