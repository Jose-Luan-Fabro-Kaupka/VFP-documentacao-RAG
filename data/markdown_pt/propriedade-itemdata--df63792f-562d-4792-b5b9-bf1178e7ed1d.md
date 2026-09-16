# Propriedade ItemData

Usa um índice para referenciar um array unidimensional que contém o mesmo número de itens que a configuração da propriedade List de um controle ComboBox ou ListBox. Não disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
Control.ItemData(nIndex)[ = nData]
```

# Valor de retorno
 **nIndex**
Especifica o índice do item a armazenar ou recuperar. O nIndex corresponde à ordem de exibição dos itens na lista.
**nData**
O número a armazenar ou recuperar da lista ItemData.

# Observações

Aplica-se a: controle ComboBox | controle ListBox

Use a propriedade ItemData para associar um número específico a cada item em uma caixa de combinação ou caixa de listagem. Você pode então usar esses números no código para identificar os itens na lista. Por exemplo, você pode usar um número de identificação para identificar cada nome de funcionário em uma caixa de listagem. Ao preencher a caixa de listagem, preencha também os elementos correspondentes no array ItemData com os números dos funcionários.

> **Observação:** Quando você insere um item em uma lista com o método AddItem, um item é automaticamente alocado no array ItemData também. No entanto, o valor não é inicializado; ele mantém o valor que estava nessa posição antes de você adicionar o item à lista. Ao usar a propriedade ItemData, certifique-se de definir o valor de cada elemento ao adicionar novos itens a uma lista.
