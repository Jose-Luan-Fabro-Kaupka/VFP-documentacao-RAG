# Controle ComboBox

Cria uma caixa de combinação que inicialmente exibe um único item. Contudo, quando você a seleciona, ela exibe uma lista de itens entre os quais é possível escolher. Uma caixa de combinação reúne os recursos de uma caixa de texto e uma caixa de listagem. Você pode inserir informações na parte de caixa de texto ou selecionar um item na parte de caixa de listagem do controle.

> **Dica:** A propriedade Style determina o tipo de lista contida no controle ComboBox. Para criar uma caixa de combinação suspensa, que exibe uma lista suspensa e uma caixa de edição, defina Style como 0. Para criar uma caixa de lista suspensa, que exibe somente a lista, defina Style como 2.

Para mostrar ou ocultar a lista de uma caixa de combinação, selecione o controle e pressione ALT+SETA PARA BAIXO.

Para obter informações sobre a criação de controles ComboBox, consulte Designer de Formulários e Uso de controles.

```foxpro
ComboBox
```

# Observações

A tabela a seguir lista as propriedades normalmente definidas em tempo de design.

| Propriedade | Descrição |
| --- | --- |
| Propriedade ColumnCount (Visual FoxPro) | Determina o número de colunas da lista. |
| Propriedade ControlSource | Especifica onde armazenar o valor escolhido pelo usuário na lista. |
| Propriedade MoverBars | Especifica se barras de movimentação são exibidas à esquerda dos itens para permitir que o usuário reorganize sua ordem. |
| Propriedade MultiSelect (Visual FoxPro) | Especifica se o usuário pode selecionar mais de um item na lista. |
| Propriedade RowSource | Especifica a origem dos valores exibidos na lista. |
| Propriedade RowSourceType | Especifica o tipo da origem dos valores exibidos na lista. |

A tabela a seguir lista os métodos normalmente usados.

| Método | Descrição |
| --- | --- |
| Método AddItem (Visual FoxPro) | Adiciona um item à lista quando RowSourceType está definido como 0. |
| Método RemoveItem | Remove um item da lista quando RowSourceType está definido como 0. |
| Método Requery | Atualiza a lista se os valores da origem especificada por RowSource tiverem sido alterados. |

A barra invertida ("\") é tratada como caractere especial quando usada na expressão de um item. Aplicam-se as seguintes regras:
 - Você pode desabilitar um item de uma caixa de listagem ou combinação adicionando uma única barra invertida ao início da expressão.
- Cada par de barras invertidas da expressão é exibido como uma única barra. Por exemplo, uma ou duas barras juntas são exibidas como uma, e três ou quatro são exibidas como duas. O código de exemplo a seguir contém um item com um caminho UNC. Ele é exibido como \\MyServer\MyMachine\MyFolder. MyForm.List1.AddItem("\\\\MyServer\\MyMachine\\MyFolder")
- Se a expressão começar com várias barras invertidas, o item não será desabilitado. Para desabilitar um item iniciado por várias barras, adicione uma barra e um colchete de fechamento (]) ao início. Por exemplo: MyForm.List1.AddItem("\]\\\MyServer\\MyMachine\\MyFolder")
- Para incluir uma linha separadora, use uma barra invertida seguida de hífen como item. Por exemplo: MyForm.List1.AddItem("\-")

Você também pode usar um controle ActiveX que acrescente características extras, como um controle Checkbox, aos controles ListView ou TreeView.
