# Propriedade DynamicCurrentControl

Especifica qual controle em um objeto Column é usado para exibir os valores da célula ativa. Disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
Column.DynamicCurrentControl [= cExpression]
```

# Valor de retorno
 **cExpression**
Especifica uma expressão de caracteres que avalia para o nome do controle que exibe e aceita dados para a célula ativa na coluna especificada em tempo de execução. O nome do controle é reavaliado cada vez que o controle Grid é atualizado. Observação O controle padrão é um controle TextBox com Text1 como propriedade Name. Para adicionar outros controles, use o método AddObject.

# Observações

Aplica-se a: Objeto Column

> **Observação:** O método AutoFit do Grid pode não redimensionar adequadamente para exibir todo o conteúdo de uma coluna se você usar esta propriedade.

Se a propriedade Sparse da coluna estiver definida como True (.T.), apenas a célula ativa na coluna usa o objeto especificado na configuração da propriedade DynamicCurrentControl para exibir dados; as outras células exibem dados usando uma caixa de texto. Se a propriedade Sparse estiver definida como False (.F.), todas as células na coluna usam o objeto especificado na configuração da propriedade DynamicCurrentControl para exibir dados.
