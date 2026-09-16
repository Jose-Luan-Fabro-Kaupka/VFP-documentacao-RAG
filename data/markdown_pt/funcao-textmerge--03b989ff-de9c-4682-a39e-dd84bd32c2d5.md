# Função TEXTMERGE( )

Fornece a avaliação de uma expressão de caracteres.

```foxpro
TEXTMERGE(cExpression [, lRecursive [, cLeftDelim [, cRightDelim]]])
```

#### Parâmetros
 **cExpression**
Especifica a expressão de cadeia de caracteres a ser avaliada.
**lRecursive**
Especifica se todos os níveis de delimitadores em cExpression serão percorridos repetidamente, avaliando até que nenhum delimitador de mesclagem de texto permaneça.
**cLeftDelim**
Especifica o delimitador esquerdo a ser usado na pesquisa de mesclagem de texto. cLeftDelim é limitado a dois caracteres.
**cRightDelim**
Especifica o delimitador direito a ser usado na pesquisa de mesclagem de texto. cRightDelim é limitado a dois caracteres.

# Valor de retorno

Cadeia de caracteres. Representa o valor de cExpression, o texto mesclado.

# Observações

Os parâmetros cLeftDelim e cRightDelim substituem temporariamente quaisquer valores de SET TEXTMERGE DELIMITERS.

A função TEXTMERGE( ) responde às configurações atuais de SET TEXTMERGE SHOW | NOSHOW.

# Exemplo

O exemplo a seguir cria uma cadeia de texto e, em seguida, gera o TEXTMERGE dessa função.

```foxpro
SET TEXTMERGE OFF
TEXT to myvar noshow &&textm
   this is a test   <<datetime()>>
   <<program(-1)>>
   <<myvar>>
   textmerge(myvar) (this line is literal)
   <<doit(myvar)>>   (cause recursion
   END of orig text
endtext
?myvar
?"Now starting textmerge"
?textmerge(myvar)
PROCEDURE doit(myvar)
*  r=i   && cause an error
   if program(-1) > 3
     return "THEEND*********"
   endif
   return textmerge(myvar)
```
