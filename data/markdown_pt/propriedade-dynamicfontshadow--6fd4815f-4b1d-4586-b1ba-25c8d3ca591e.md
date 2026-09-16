# Propriedade DynamicFontShadow

Especifica se o texto associado a um objeto Column aparece com sombra. Disponível em tempo de design e em tempo de execução.

```foxpro
Column.DynamicFontShadow [= "lExpr"]
```

# Valor de retorno
 **" lExpr "**
Especifica uma expressão lógica que é avaliada como True (.T.) ou False (.F.). A expressão é reavaliada em tempo de execução sempre que o controle Grid é atualizado. A tabela a seguir descreve as configurações para esses valores. lExpr avalia para Descrição True (.T.) O texto tem sombra. False (.F.) O texto não tem sombra. (Padrão)

# Observações

Aplica-se a: Objeto Column

> **Observação:** O método AutoFit do Grid pode não redimensionar adequadamente para exibir todo o conteúdo de uma coluna se você usar esta propriedade.
