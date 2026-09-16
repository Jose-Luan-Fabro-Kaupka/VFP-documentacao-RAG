# Propriedade ListItemID

Especifica o número de ID exclusivo do item selecionado em um controle ComboBox ou ListBox. Não disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
Control.ListItemID[ = nItemID]
```

# Valor de retorno
 **nItemID**
As configurações e interpretações da propriedade ListItemID são: nItemID Descrição 0 Indica que nenhum item está selecionado. Observação Para controles ComboBox, o valor 0 significa que o usuário inseriu um valor que não está na lista. 1 ou qualquer número maior que 1 O ID do item selecionado. A propriedade ListItemID também é definida quando a propriedade SelectedID em um controle ListBox é definida.

# Observações

Aplica-se a: controle ComboBox | controle ListBox

Se o método RemoveListItem for usado para remover um item de uma lista, todos os itens restantes mantêm seus números de identificação exclusivos. Quando o método AddItem é usado para adicionar um item a uma lista e a propriedade Sorted está definida como False (.F.), nItemID recebe o menor número disponível. Quando o método AddListItem é usado para adicionar um item a uma lista e a propriedade Sorted está definida como False (.F.), você pode atribuir qualquer número a nItemID.
