# Propriedade ItemIDData

Usa um número de identificação exclusivo para fazer referência a um array unidimensional que contém o mesmo número de itens que a configuração da propriedade List de um controle ComboBox ou ListBox. Não disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
Control.ItemIDData(nItemID)[ = nData]
```

# Valor de retorno
 **nItemID**
Especifica o ID do item, um número de identificação exclusivo.
**nData**
O número a ser armazenado ou recuperado da lista ItemIDData.

# Observações

Aplica-se a: controle ComboBox | controle ListBox

Use a propriedade ItemIDData para associar um número específico a cada item de uma caixa de combinação ou caixa de listagem. Em seguida, você pode usar esses números no código para identificar os itens. Por exemplo, pode usar um número de identificação para identificar cada nome de funcionário em uma caixa de listagem. Ao preencher a caixa de listagem, preencha também os elementos correspondentes no array ItemIDData com os números dos funcionários.

> **Observação:** Ao inserir um item em uma lista com o método AddItem, um item também é alocado automaticamente no array ItemIDData. Entretanto, o valor não é inicializado; ele mantém o valor que estava nessa posição antes de o item ser adicionado à lista. Ao usar a propriedade ItemIDData, certifique-se de definir o valor de cada elemento ao adicionar novos itens a uma lista. Esse é o mesmo array acessado pela propriedade ItemData.
