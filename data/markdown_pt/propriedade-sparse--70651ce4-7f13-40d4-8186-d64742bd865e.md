# Propriedade Sparse

Especifica se a propriedade CurrentControl afeta todas as células ou apenas a célula ativa em um objeto Column. Disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
Column.Sparse [= lExpr]
```

# Valor de retorno
 **lExpr**
As configurações da propriedade Sparse são as seguintes: Configuração Descrição True (.T.) (Padrão) Apenas a célula ativa da Column usa a configuração da propriedade CurrentControl para aceitar e exibir dados. As outras células usam o controle TextBox se o controle atual das células não for o objeto contêiner ou um botão de comando. As outras células permanecem vazias se o controle atual das células for o objeto contêiner ou um botão de comando. False (.F.) Todas as células no objeto Column usam a configuração da propriedade CurrentControl para exibir dados; a célula ativa aceita dados.

# Observações

Aplica-se a: Objeto Column
