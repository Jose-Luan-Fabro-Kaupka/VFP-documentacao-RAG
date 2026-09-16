# Propriedade ListItem

Um array de cadeias de caracteres usado para acessar os itens em um controle ComboBox ou ListBox por ID de item. Não disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
Control.ListItem(nRow [, nCol])[ = cChar]
```

# Valor de retorno
 **nRow**
Especifica a linha da qual recuperar o item. Você pode usar a propriedade Control .listitemID.
**nCol**
Especifica, opcionalmente, a coluna da qual derivar o valor. Se você especificar somente listitemID , a coluna 1 fornece o valor.
**nChar**
Representa um valor, opcionalmente, a ser atribuído ao Control .listitem especificado.

# Observações

Aplica-se a: ComboBox Control | ListBox Control

Use a propriedade List para recuperar itens na ordem em que são exibidos; use a propriedade ListItem para recuperar itens de acordo com seu ID de item.

> **Observação:** Para adicionar itens a uma caixa de combinação ou caixa de lista, use o método AddItem ou AddListItem. Para remover itens, use o método RemovetItem ou o método RemoveListItem. Para manter os itens em ordem alfabética, defina a propriedade Sorted do controle como True (.T.) antes de adicionar itens à lista.

A propriedade ListItem também é definida quando a propriedade Selected em um controle Listbox é definida.
