# Exemplo: adicionar itens interativamente a uma caixa de listagem

Arquivo: ...\Samples\Solution\Controls\Lists\Ladd.scx

Este exemplo demonstra a adição e remoção de itens de caixa de listagem. Quando um usuário digita texto na caixa de texto e pressiona ENTER, o texto na caixa de texto é adicionado à lista e o cursor retorna à caixa de texto para que o usuário possa inserir outro valor.

Para permitir que um usuário adicione itens interativamente a uma lista, use o método AddItem. No exemplo, o seguinte código no evento KeyPress da caixa de texto adiciona o texto na caixa de texto à caixa de listagem e limpa a caixa de texto quando o usuário pressiona ENTER:

```foxpro
PARAMETERS nKeyCode, nShiftCtrlAlt
IF nKeyCode = 13     && Enter Key
   THISFORM.lstAdd.AddItem (This.Value)
   THIS.Value = ""
ENDIF
```

O seguinte código no evento DblClick da caixa de listagem remove o item que foi clicado duas vezes, enviando o valor para a caixa de texto:

```foxpro
THISFORM.txtAddText.Value = This.List(This.ListIndex)
THIS.RemoveItem (This.ListIndex)
```
