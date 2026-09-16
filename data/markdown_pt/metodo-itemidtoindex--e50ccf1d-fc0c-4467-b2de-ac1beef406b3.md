# Método ItemIDToIndex

Retorna o valor de nIndex, a posição de um item na lista de um controle.

```foxpro
 [nIndex =]Control.ItemIDToIndex(nItemID)
```

#### Parâmetros
 **nItemID**
O número de identificação exclusivo associado a esse item.

# Observações

Aplica-se a: ComboBox Control | ListBox Control

Cada item adicionado a uma combo box ou list box tem dois números atribuídos a ele:
 - O nItemID, um número de identificação exclusivo.
- O nIndex, um inteiro correspondente à ordem em que os itens são exibidos pelo controle. O primeiro item na lista corresponde a nIndex = 1.

Inicialmente, conforme os itens são adicionados ao controle, esses dois números são idênticos. Mas conforme os itens são classificados, removidos e adicionados, esses números não são mais idênticos.

Use o método ItemIDToIndex para recuperar o número nIndex de um item específico na lista do controle quando você conhece seu número nItemID.
