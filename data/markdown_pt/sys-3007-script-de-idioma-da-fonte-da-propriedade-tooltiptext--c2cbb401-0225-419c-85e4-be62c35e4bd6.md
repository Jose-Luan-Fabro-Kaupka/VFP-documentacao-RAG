# SYS(3007) - Script de idioma da fonte da propriedade ToolTipText

Especifica um script de idioma de fonte para o texto que aparece como ToolTip de um controle.

```foxpro
SYS(3007 [, nFontCharSet])
```

#### Parâmetros
 **nFontCharSet**
Especifica um script de idioma de fonte para o texto que aparece como ToolTip de todos os controles. O texto do ToolTip é especificado com a propriedade ToolTipText . Consulte a função GETFONT( ) para obter uma lista dos valores de script de idioma de fonte disponíveis.

# Valor de retorno

Character. Se o parâmetro nFontCharSet for omitido, SYS(3007) retorna a configuração atual de script de idioma de fonte.
