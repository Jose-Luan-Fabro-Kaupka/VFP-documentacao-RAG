# Como: permitir que usuários selecionem vários itens em um list box

O comportamento padrão de uma lista permite que um item por vez seja selecionado. No entanto, você pode tornar possível que um usuário selecione vários itens em uma lista.

### Para permitir vários itens selecionados em uma lista
- Defina a propriedade MultiSelect da lista como true (.T.).

Para processar os itens selecionados — copiá-los para uma matriz ou incorporá-los em outro lugar em seu aplicativo — percorra os itens da lista e processe aqueles para os quais a propriedade Selected é true (.T.). O código a seguir pode ser incluído no evento InteractiveChange de um list box para exibir os itens selecionados em um combo box, `cboSelected`, e o número de itens selecionados em uma caixa de texto, `txtNoSelected`:

```foxpro
nNumberSelected = 0  && a variable to track the number
THISFORM.cboSelected.Clear && clear the combo box
FOR nCnt = 1 TO THIS.ListCount
   IF THIS.Selected(nCnt)
      nNumberSelected = nNumberSelected + 1
      THISFORM.cboSelected.Additem (THIS.List(nCnt))
   ENDIF
ENDFOR
THISFORM.txtNoSelected.Value = nNumberSelected
```
