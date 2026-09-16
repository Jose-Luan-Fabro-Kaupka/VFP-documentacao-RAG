# Propriedade ShowTips

Determina se ToolTips são exibidas para os controles no objeto Form especificado ou no objeto toolbar especificado. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.ShowTips = lExpr
```

# Valor de retorno
 **lExpr**
Determina se ToolTips são exibidas para o controle especificado. As configurações da propriedade ShowTips são: Configuração Descrição True (.T.) (Padrão para o objeto toolbar) ToolTips são exibidas quando um usuário posiciona o mouse sobre um controle. False (.F.) (Padrão para o objeto Form) ToolTips não são exibidas quando um usuário posiciona o mouse sobre um controle.

# Observações

Aplica-se a: Form Object | _SCREEN System Variable | ToolBar Object

Você pode especificar o texto que aparece em cada ToolTip usando a propriedade ToolTipText.

A propriedade ShowTips de _SCREEN deve ser definida como True (.T.) para que Memo Tips sejam habilitadas em janelas Browse e controles Grid.
