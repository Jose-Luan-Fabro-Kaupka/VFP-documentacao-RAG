# Propriedade MoverBars

Especifica se barras de movimentação são exibidas em um controle ListBox. Disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
ListBox.MoverBars[ = lExpr]
```

# Valor de retorno
 **lExpr**
As configurações da propriedade MoverBars são: Setting Description True (.T.) Display mover bars. Users can interactively reorganize the contents of the control. False (.F.) Does not display mover bars. (Default)

# Observações

Aplica-se a: ListBox Control

Você pode selecionar e mover um item pressionando CTRL+UP ARROW, CTRL+DOWN ARROW, usando o mouse ou programaticamente chamando o método MoveItem. O evento OnMoveItem ocorre quando um item se move para cima ou para baixo em uma caixa de listagem.

A propriedade MoverBars está disponível somente se a propriedade RowSourceType estiver definida como 0 (None) ou 1 (Value).
