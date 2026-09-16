# Comando SET TEXTMERGE DELIMITERS

Especifica o conjunto de caracteres delimitadores de mesclagem de texto a ser usado em vez do padrão.

```foxpro
SET TEXTMERGE DELIMITERS [TO cLeftDelimiter [, cRightDelimiter]]
```

#### Parâmetros
 **[TO cLeftDelimiter [, cRightDelimiter ]]**
Especifica os delimitadores a serem usados. Você pode especificar no máximo dois caracteres delimitadores. Os caracteres delimitadores padrão são os colchetes angulares duplos (<< e >>). Observação Se você especificar apenas um conjunto de caracteres delimitadores com cLeftDelimiter , os caracteres delimitadores esquerdo e direito são definidos como cLeftDelimiter . Se você especificar ambos os conjuntos de caracteres delimitadores com cLeftDelimiter e cRightDelimiter , o primeiro conjunto de caracteres delimitadores é definido como cLeftDelimiter e o segundo conjunto de caracteres delimitadores é definido como cRightDelimiter . Dica Para restaurar os caracteres delimitadores padrão, chame SET TEXTMERGE DELIMITERS sem argumentos.

# Observações

Você pode exibir os delimitadores atuais usados com o comando DISPLAY STATUS.

Para obter mais informações sobre caracteres delimitadores de mesclagem de texto, consulte Comando SET TEXTMERGE.
