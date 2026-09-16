# Propriedade DynamicFontOutline

Especifica se o texto associado a um objeto Column é contornado. Disponível em tempo de design e em tempo de execução.

```foxpro
Column.DynamicFontOutline[ = "lExpr"]
```

# Valor de retorno
 **" lExpr "**
Especifica uma expressão lógica que é avaliada como True (.T.) ou False (.F.). A expressão é reavaliada em tempo de execução cada vez que o controle Grid é atualizado. A tabela a seguir descreve as configurações para esses valores. lExpr avalia para Descrição True (.T.) O texto é contornado. False (.F.) O texto não é contornado. (Padrão)

# Observações

Aplica-se a: objeto Column

> **Observação:** O método AutoFit do Grid pode não redimensionar adequadamente para exibir todo o conteúdo de uma coluna se você usar esta propriedade.
