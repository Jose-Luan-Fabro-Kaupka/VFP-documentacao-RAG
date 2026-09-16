# Amostra Mover itens entre caixas de listagem

Arquivo: ...\Samples\Solution\Controls\Lists\Lmover.scx

Esta amostra demonstra mover itens de uma caixa de listagem para outra. Um usuário pode clicar duas vezes em um item para movê-lo, selecionar um ou mais itens e arrastá-los, ou usar os botões de comando apropriados para mover os itens entre as listas.

As duas caixas de listagem e quatro botões de comando associados são salvos como uma classe: MoverLists em Samples.vcx. A classe base de MoverLists é CONTAINER. Para poder adicionar e remover itens das listas, o RowSourceType das listas deve ser definido como 0 – None. Se você deseja preencher a caixa de listagem com elementos de matriz ou valores de uma tabela, pode usar código como o seguinte:

```foxpro
*array
FOR i = 1 to ALEN(myarray)
   List.AddItem(myarray[i])
ENDFOR
*table
SCAN
   List.AddItem(table.field)
ENDSCAN
```

# Para mover itens clicando duas vezes

O código a seguir está associado ao evento DblClick da caixa de listagem esquerda (lstSource). Código semelhante está associado ao evento DblClick da caixa de listagem direita (lstSelected).

```foxpro
THIS.Parent.lstSelected.AddItem(THIS.List(THIS.ListIndex))
This.RemoveItem(THIS.ListIndex)
THIS.Parent.Refresh
```

"THIS" refere-se a lstSource. "THIS.Parent" refere-se à classe moverlists, o contêiner das listas.

# Para mover todos os itens de uma lista para outra

O código a seguir está associado ao evento Click de cmdAddAll:

```foxpro
  DO WHILE THIS.PARENT.lstSource.ListCount > 0
    THIS.PARENT.lstSelected.AddItem;
        (THIS.PARENT.lstSource.List(1))
   THIS.PARENT.lstSource.RemoveItem(1)
  ENDDO
  THIS.PARENT.Refresh
```

# Para mover itens selecionados de uma lista para outra

Se você remove um item de uma caixa de listagem, a propriedade ListCount da caixa de listagem é decrementada, assim como o ListIndex de todos os itens subsequentes na lista. Para mover vários itens selecionados, você precisa usar um loop DO WHILE. O código a seguir está associado ao evento Click de cmdAdd:

```foxpro
nCnt = 1
DO WHILE nCnt <= THIS.PARENT.lstSource.ListCount
   IF THIS.PARENT.lstSource.Selected(nCnt)
      THIS.PARENT.lstSelected.AddItem;
         (THIS.PARENT.lstSource.List(nCnt))
      THIS.PARENT.lstSource.RemoveItem(nCnt)
   ELSE
      nCnt = nCnt + 1
   ENDIF
ENDDO
THIS.PARENT.Refresh
```

# Para arrastar e soltar itens de uma lista para outra

Implementar arrastar e soltar entre as caixas de listagem envolve código associado aos eventos MouseDown, MouseMove, DragOver e DragDrop. Três propriedades definidas pelo usuário (DragThreshold, MouseX e MouseY) ampliam a usabilidade da classe.

O código MouseDown armazena as coordenadas X e Y do ponteiro do mouse em propriedades da classe.

```foxpro
*MouseDown
Parameters nButton, nShift, nXCoord, nYCoord
THIS.PARENT.MouseX = nXCoord
THIS.PARENT.MouseY = nYCoord
```

O código MouseMove garante que o botão esquerdo do mouse esteja pressionado antes de iniciar o procedimento de arrastar. Além disso, para evitar arrastar acidentalmente, este código verifica se o usuário moveu o mouse uma distância maior que um limite definido (8 pixels por padrão).

```foxpro
*MouseMove
Parameters nButton, nShift, nXCoord, nYCoord
IF nButton = 1 && Left Mouse
   IF ABS(nXCoord - THIS.PARENT.MouseX) > ;
      THIS.Parent.DragThreshold OR ;
         ABS(nYCoord - THIS.PARENT.MouseY) > ;
         THIS.Parent.DragThreshold
      THIS.Drag
   ENDIF
ENDIF
```

O código DragOver altera o DragIcon da origem quando o ponteiro do mouse entra e sai do "espaço aéreo" da caixa de listagem.

```foxpro
*DragOver
Parameters oSource, nXCoord, nYCoord, nState
DO CASE
   CASE nState = 0 && Enter
      oSource.DragIcon = THIS.Parent.CanDropIcon
   CASE nState = 1 && Leave
      oSource.DragIcon = THIS.Parent.NoDropIcon
ENDCASE
```

O código DragDrop garante que a origem do arrastar não seja a mesma que o destino do arrastar e chama o método associado ao evento Click do botão de comando cmdAdd (no caso de lstSelected) ou cmdRemove (no caso de lstSource).

```foxpro
*DragDrop
Parameters oSource, nXCoord, nYCoord
IF oSource.Name != THIS.Name
   THIS.PARENT.cmdAdd.Click
ENDIF
```
