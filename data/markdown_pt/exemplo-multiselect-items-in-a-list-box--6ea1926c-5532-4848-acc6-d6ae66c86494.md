# Exemplo Multiselect Items in a List Box

Arquivo: ...\Samples\Solution\Controls\Lists\Lmsel.scx

Este exemplo mostra como gerenciar vários itens selecionados em uma caixa de listagem. O formulário contém uma caixa de listagem com a propriedade MultiSelect definida como True (.T.). Uma caixa de combinação no formulário contém todos os itens selecionados na caixa de listagem.

Para processar os itens com seleção múltipla em uma caixa de listagem — para copiá-los para uma matriz ou incorporá-los em outro lugar em sua aplicação — percorra os itens da lista e processe aqueles para os quais a propriedade Selected está definida como verdadeiro (.T.). O código a seguir está incluído no evento Click da caixa de listagem para exibir os itens selecionados em uma caixa de combinação e o número de itens selecionados em uma caixa de texto:

```foxpro
nNoSelected = 0    && variable to track number of selected items
THISFORM.cboSelected.Clear    && clear the combo box
* main processing loop
FOR i = 1 TO THIS.ListCount
   IF THIS.Selected(i)
      nNoSelected = nNoSelected + 1
      THISFORM.cboSelected.Additem (THIS.List(i))
   ENDIF
ENDFOR
THISFORM.txtNoSelected.Value = nNoSelected
```

No código associado ao evento Init deste formulário, e em muitos lugares em toda esta aplicação de exemplo, os valores de cadeia de caracteres inicialmente adicionados à lista são primeiro definidos com uma diretiva `#DEFINE`. Cada uma das constantes definidas termina com "_LOC". As ferramentas internas de localização da Microsoft extraem essas definições para que as cadeias de caracteres possam ser traduzidas para qualquer idioma em que a aplicação esteja sendo localizada.
