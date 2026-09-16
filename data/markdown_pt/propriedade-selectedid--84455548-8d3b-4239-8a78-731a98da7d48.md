# Propriedade SelectedID

Especifica se um item está selecionado em um combo box ou list box. Não disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
Control.SelectedID(nItemID)[= lExpr]
```

# Valor de retorno
 **nItemID**
Especifica o ID do item de um item em um combo box ou ListBox.
**lExpr**
As configurações para a propriedade SelectedID são: Configuração Descrição True (.T.) O item está selecionado. False (.F.) (Padrão) O item não está selecionado.

# Observações

Aplica-se a: ComboBox Control | ListBox Control

Definir a propriedade SelectedID em um controle Listbox também define a propriedade ListItemID e dispara o evento ProgrammaticChange.

A propriedade SelectedID é particularmente útil quando os usuários podem fazer múltiplas seleções. Você pode verificar rapidamente quais itens em uma lista estão selecionados. Você também pode usar esta propriedade para selecionar ou desmarcar itens em uma lista usando código. Para verificar se o terceiro item em um ListBox está selecionado, execute o seguinte:

```foxpro
IF MyList.SelectedID(3)
    WAIT WINDOW "It's selected!"
ELSE
    WAIT WINDOW "It's not!"
ENDIF
```
