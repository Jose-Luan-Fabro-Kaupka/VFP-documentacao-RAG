# Propriedade ItemTips

Especifica se dicas de item são exibidas para itens em uma caixa de combinação ou caixa de listagem. Disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
Control.ItemTips[= lExpression]
```

# Valor de retorno
 **lExpression**
As configurações da propriedade ItemTip são: Configuração Descrição True (.T.) Dicas de item são exibidas para itens em uma caixa de combinação ou caixa de listagem. False (.F.) (Padrão) Dicas de item não são exibidas para itens em uma caixa de combinação ou caixa de listagem.

# Observações

Aplica-se a: Controle ComboBox | Controle ListBox

Uma dica de item é uma pequena janela que exibe um item inteiro da caixa de combinação ou da caixa de listagem quando o ponteiro do mouse é posicionado sobre o item. Defina esta propriedade como true (.T.) sempre que os itens em um controle ComboBox ou ListBox sejam mais longos que a largura do controle.
