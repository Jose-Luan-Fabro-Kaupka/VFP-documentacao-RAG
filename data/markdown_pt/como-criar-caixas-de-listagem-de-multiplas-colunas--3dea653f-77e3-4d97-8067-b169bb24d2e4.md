# Como: criar caixas de listagem de múltiplas colunas

Embora o número padrão de colunas em uma caixa de listagem seja um, uma caixa de listagem no Visual FoxPro pode conter quantas colunas você quiser. Uma caixa de listagem de múltiplas colunas difere de uma grade porque você seleciona uma linha por vez em uma caixa de listagem de múltiplas colunas, enquanto pode selecionar células individuais em uma grade, e os dados na lista não podem ser editados diretamente.

### Para exibir várias colunas em uma caixa de listagem
- Defina a propriedade ColumnCount para o número de colunas desejadas.
- Defina a propriedade ColumnWidths . Por exemplo, se houver três colunas na caixa de listagem, o seguinte comando definirá as larguras das colunas como 10, 15 e 30, respectivamente: THISFORM.listbox.ColumnWidths = "10, 15, 30"
- Defina a propriedade RowSourceType como 6 - Fields .
- Defina a propriedade RowSource para os campos a serem exibidos nas colunas. Observação Para que as colunas se alinhem corretamente, você precisa definir a propriedade ColumnWidths ou alterar a propriedade FontName para uma fonte monoespaçada. A propriedade FirstElement de ListBoxes e ComboBoxes não é efetiva em listas de múltiplas colunas.

Quando o RowSourceType da lista está definido como 0 - None, você pode usar o método AddListItem para adicionar itens a uma caixa de listagem de múltiplas colunas. Por exemplo, o seguinte código adiciona texto a colunas específicas em uma caixa de listagem:

```foxpro
THISFORM.lst1.ColumnCount = 3
THISFORM.lst1.Columnwidths = "100,100,100"
THISFORM.lst1.AddListItem("row1 col1", 1,1)
THISFORM.lst1.AddListItem("row1 col2", 1,2)
THISFORM.lst1.AddListItem("row1 col3", 1,3)
THISFORM.lst1.AddListItem("row2 col2", 2,2)
```
