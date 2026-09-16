# Propriedade ShowInTaskbar

Especifica se o objeto de formulário de nível superior aparece na barra de tarefas do Windows em tempo de execução. Esta configuração é somente leitura em tempo de execução.

```foxpro
Form.ShowInTaskbar = lExpr
```

#### Parâmetros
 **lExpr**
O padrão é true (.T.), habilitado. False (.F.) desabilita esta propriedade

# Observações

A configuração ShowInTaskbar é ignorada, a menos que o valor da propriedade ShowWindow Property = 2
