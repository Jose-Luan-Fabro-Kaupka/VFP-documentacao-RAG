# Propriedades DynamicFontBold, DynamicFontItalic, DynamicFontStrikethru, DynamicFontUnderline

Especifica que o texto exibido em um objeto Column tem um ou mais dos seguintes estilos: Bold, Italic, Strikethru ou Underline. A expressão lógica é reavaliada cada vez que o controle Grid é atualizado. Disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
Column.DynamicFontBold [= "lExpr"]
Column.DynamicFontItalic [= "lExpr"]
Column.DynamicFontStrikeThru [= "lExpr"]
Column.DynamicFontUnderline [= "lExpr"]
```

# Valor de retorno
 **" lExpr "**
Especifica uma expressão lógica que avalia para True (.T.) ou False (.F.). A tabela a seguir descreve as configurações para esses valores. lExpr avalia para Descrição True (.T.) O estilo de fonte é bold, italic, strikethru ou underline. False (.F.) O estilo de fonte não é bold, italic, strikethru ou underline. (Padrão, exceto para DynamicFontBold)

# Observações

Aplica-se a: Column Object

Você pode usar essas propriedades para controlar a aparência do texto com base em valores de dados em tempo de execução. Por exemplo, você pode definir DynamicFontUnderline para indicar nomes de novos membros em uma organização.

> **Observação:** O método AutoFit do Grid pode não redimensionar adequadamente para exibir todo o conteúdo de uma coluna se você usar essas propriedades.
