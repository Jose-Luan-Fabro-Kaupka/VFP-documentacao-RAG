# Exemplo de classificação de itens de caixa de lista

Arquivo: ...\Samples\Solution\Controls\Lists\Lsort.scx

Este exemplo demonstra como permitir que um usuário reorganize ou classifique os itens em uma lista. As propriedades principais a definir são:

```foxpro
   List.MoverBars = .T.
   List.Sorted = .T.
```

Defina a propriedade MoverBars como true (.T.) para permitir que um usuário reordene um item na lista arrastando o botão à esquerda do item para a nova posição.

Defina a propriedade Sorted como true (.T.) para exibir os itens da lista em ordem alfabética. Você ainda pode reorganizar os itens na lista depois que eles foram classificados. Defina a propriedade Sorted como .T. novamente para classificar a lista em ordem alfabética outra vez.

A propriedade Sorted se aplica somente se a propriedade RowSourceType da lista estiver definida como 0 (None) ou 1 (Value).
