# Propriedade CurrentControl

Especifica qual controle contido em um objeto Column é usado para exibir os valores da célula ativa. Disponível em tempo de design; de leitura/gravação em tempo de execução.

```foxpro
Column.CurrentControl[ = cName]
```

# Valor de retorno
 **cName**
Especifica o nome do controle que exibe e aceita dados para a célula ativa em um objeto Column.

# Observações

Aplica-se a: Objeto Column

O controle padrão é um TextBox com Text1 como propriedade Name. Use o método AddObject para adicionar outros controles.

Se a propriedade Sparse da Column estiver definida como true (.T.), somente a célula ativa na Column usa o objeto especificado na propriedade CurrentControl; as outras células exibem dados usando um TextBox. Se a propriedade Sparse estiver definida como false (.F.), todas as células na Column usam a propriedade CurrentControl para exibir dados.

> **Observação:** Você pode adicionar um número ilimitado de controles a um objeto Column usando o método AddObject. No entanto, você pode definir a propriedade CurrentControl para apenas um controle em qualquer momento.
