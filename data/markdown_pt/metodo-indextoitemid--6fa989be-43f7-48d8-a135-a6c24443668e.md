# Método IndexToItemID

Retorna um ItemID para um número Index fornecido.

```foxpro
Control.IndexToItemID(nIndex)
```

#### Parâmetros
 **nIndex**
Especifica um número que representa a posição em que um item é exibido em um controle.

# Valor de retorno

A tabela a seguir lista os valores de retorno do método IndexToItemID.

| Valor de retorno | Condição |
| --- | --- |
| nItemID | Retorna um ItemID para um número Index fornecido. |

# Observações

Aplica-se a: Controle ComboBox | Controle ListBox

Cada item adicionado a um ComboBox ou ListBox tem dois números de identificação atribuídos:
 - O nItemID, um número de identificação exclusivo.
- O nIndex, um inteiro correspondente à ordem em que os itens são exibidos pelo controle: O primeiro item na lista corresponde a nIndex = 1.

Inicialmente, conforme os itens são adicionados ao controle, esses dois números são idênticos. Mas conforme os itens são classificados, removidos e adicionados, esses números não são mais idênticos.

Use o método IndexToItemID para retornar o número nItemID de um item específico no controle quando você conhece seu número nIndex.
