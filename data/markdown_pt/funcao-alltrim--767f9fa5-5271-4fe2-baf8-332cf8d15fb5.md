# Função ALLTRIM( )

Remove todos os espaços ou caracteres de análise iniciais e finais da expressão de caractere especificada, ou todos os bytes zero (0) iniciais e finais da expressão binária especificada.

```foxpro
ALLTRIM(Expression [, nFlags] [, cParseChar [, cParseChar2 [, ...]]])
```

#### Parâmetros
 **Expression**
Especifica uma expressão do tipo Character ou Varbinary da qual remover espaços ou bytes 0 iniciais e finais, respectivamente.
**nFlags**
Especifica se o corte é sensível a maiúsculas e minúsculas quando um ou mais caracteres de análise (cParseChar, cParseChar2, …) são incluídos. O corte é sensível a maiúsculas e minúsculas se nFlags é zero ou é omitido. O corte não é sensível a maiúsculas e minúsculas se nFlags é 1.
**cParseChar [, cParseChar2 [, ...]]**
Especifica uma ou mais cadeias de caracteres que são cortadas do início e do fim de cExpression. Se cParseChar não é incluído, então espaços ou bytes 0 iniciais e finais são removidos de Expression. Observação O número máximo de cadeias permitidas em cParseChar é 23.

# Valor de retorno

Character ou Varbinary. ALLTRIM( ) retorna a expressão especificada sem espaços, caracteres de análise ou bytes 0 iniciais ou finais, respectivamente.

# Observações

Você pode usar ALLTRIM( ) para garantir que espaços ou bytes 0 sejam removidos de dados inseridos por um usuário.

# Exemplo

O exemplo a seguir usa a função AFONT( ) para criar um array contendo os nomes de todas as fontes disponíveis. ALLTRIM( ) remove os espaços iniciais e finais dos nomes das fontes. O nome cortado de cada fonte é exibido junto com um exemplo da fonte. Se mais de 10 fontes estiverem instaladas, apenas as primeiras 10 são exibidas.

```foxpro
CLEAR
=AFONT(gaFontArray)  && Array containing font names
gnNumFonts= ALEN(gaFontArray)  && Number of fonts
IF gnNumFonts > 10
   gnNumFonts = 10  && Display first 10 fonts
ENDIF
FOR nCount = 1 TO gnNumFonts
   ? ALLTRIM(gaFontArray(nCount))  && Display font name
   ?? '  This is an example of ' ;
      + ALLTRIM(gaFontArray(nCount)) FONT gaFontArray(nCount), 8
ENDFOR
```
