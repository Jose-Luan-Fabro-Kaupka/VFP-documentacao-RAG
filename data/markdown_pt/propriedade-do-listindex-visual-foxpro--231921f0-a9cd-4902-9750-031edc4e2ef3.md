# Propriedade do ListIndex (Visual FoxPro)

Especifica o número de índice do item selecionado em um controle ComboBox ou ListBox. Não disponível no momento do projeto; leia/escrever em tempo de execução.

```foxpro
Control.ListIndex[ = nIndex]
```

# Valor de Retorno
**nIndex**
As configurações para a propriedade ListIndex são: Configuração Descrição 0 (Por omissão) Indica que nenhum item selecionado. Para uma caixa de combinação, isto significa que o usuário inseriu um valor não na lista. 1 ... ListCount O índice do item selecionado.

Observações

Aplica-se a: Controle de ComboBox

O seguinte mostra o texto do item seleccionado.

```foxpro
? List(MyList.ListIndex)
```

Você pode retornar o mesmo valor usando a propriedade Valor do controle.

A configuração da propriedade MultiSelect de uma ListBox para .T. permite selecionar mais de um item. Neste caso, o ListIndex conterá o índice do item que atualmente possui a borda de seleção.

Veja também
- Método AddItem (Visual FoxPro)
- Método AddListItem
- Método IndexToItemID
- Método ItemIDToIndex
- Lista de propriedades
