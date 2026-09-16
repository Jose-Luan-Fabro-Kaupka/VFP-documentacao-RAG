# Método AddColumn

Adiciona um objeto Column a um controle Grid.

```foxpro
Grid.AddColumn(nIndex)
```

#### Parâmetros
 **nIndex**
Especifica um número que representa a posição na grade onde a nova Column é adicionada.

# Observações

Aplica-se a: Controle Grid

Quando AddColumn( ) é chamado, as colunas existentes são movidas para a direita e suas propriedades ColumnOrder são incrementadas de acordo. A propriedade ColumnCount da grade também é aumentada.

A matriz da propriedade Controls da grade é ampliada em um elemento, e uma referência à nova coluna é colocada no novo elemento. A nova coluna recebe um nome exclusivo.

Por exemplo, para adicionar uma nova coluna e depois atribuir um novo nome a essa coluna, você pode fazer o seguinte.

```foxpro
THISFORM.Grid1.AddColumn(1)   && Insert column at left.
THISFORM.Grid1.Columns(THISFORM.Grid1.ColumnCount).Name = "NewColumn"
THISFORM.Grid1.NewColumn.ControlSource = "Customer.CustID"
```
