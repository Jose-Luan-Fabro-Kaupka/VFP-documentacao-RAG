# Exemplo Display Child Records from a Relationship

Arquivo: ...\Samples\Solution\Controls\Grid\1_many.scx

Este exemplo demonstra a coordenação de um formulário um-para-muitos com dois grids exibindo os lados "muitos" dos relacionamentos. Muito pouco código é necessário neste exemplo. Definir algumas propriedades é tudo o que é necessário.

# Configurações de propriedade

Caixas de texto para o lado "um" do relacionamento:

```foxpro
ControlSource = Customer.cust_id
ControlSource = Customer.company
```

Grid para o primeiro lado "muitos" do relacionamento:

```foxpro
ChildOrder = cust_id
LinkMaster = customer
RecordSource = orders
RecordSourceType = 1 - Alias
RelationalExpr = customer.cust_id
ColumnCount = 4
   Column1.ControlSource = "orders.order_no"
   Column1.Header1.Caption = "Order"
   Column2.ControlSource = "orders.order_date"
   Column2.Header1.Caption = "Date"
   Column3.ControlSource = "orders.to_name"
   Column3.Header1.Caption = "Ship To"
   Column4.ControlSource = "orders.order_amt"
   Column4.Sparse = .F.
   Column4.Header1.Caption = "Total"
   Column4.Text1.InputMask = "$$999,999.99"
```

Grid para o 2º lado "muitos" do relacionamento:

```foxpro
ChildOrder = order_id
LinkMaster = Orders
RecordSource = Orditems
RecordSourceType = 1 - Alias
RelationalExpr =Orders.order_id
ColumnCount = 4
   Column1.ControlSource = "orditems.line_no"
   Column1.Header1.Caption = "Item"
   Column2.ControlSource = "products.prod_name"
   Column2.Header1.Caption = "Product"
   Column3.ControlSource = "orditems.quantity"
   Column3.Header1.Caption = "Qty."
   Column4.ControlSource = "orditems.unit_price"
   Column4.Sparse = .F.
   Column4.Header1.Caption = "Price"
   Column4.Text1.InputMask = "$$9,999.99"
```

Além das caixas de texto e dos grids, o formulário contém um objeto baseado na classe VCR em Buttons.vcx. A propriedade SkipTable desta classe é definida como a tabela na qual você deseja que o ponteiro de registro seja movido quando o usuário escolhe um botão de navegação de tabela. Como o usuário pode facilmente mover manualmente pelos registros nos grids (Orders e Orditems), SkipTable é definida como Customer.
