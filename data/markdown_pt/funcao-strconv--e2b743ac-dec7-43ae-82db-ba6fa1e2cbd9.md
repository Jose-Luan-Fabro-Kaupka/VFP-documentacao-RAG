# Função STRCONV( )

Converte expressões de caracteres entre representações de byte único, byte duplo, UNICODE e específicas de localidade.

```foxpro
STRCONV(cExpression, nConversionSetting [, nRegionalIdentifier [, nRegionalIDType]])
```

#### Parâmetros
 **cExpression**
Especifica a expressão de caracteres que STRCONV( ) converte.
**nConversionSetting**
Especifica o tipo de conversão. A tabela a seguir lista os valores de nConversionSetting e o tipo de conversão realizada. nConversionSetting Conversão 1 Converte caracteres de byte único em cExpression para caracteres de byte duplo. Suportado somente para Locale ID (especificado com os parâmetros nRegionalIdentifier ou nRegionalIDType). 2 Converte caracteres de byte duplo em cExpression para caracteres de byte único. Suportado somente para Locale ID (especificado com os parâmetros nRegionalIdentifier ou nRegionalIDType). 3 Converte caracteres Katakana de byte duplo em cExpression para caracteres Hiragana de byte duplo. Suportado somente para Locale ID (especificado com os parâmetros nRegionalIdentifier ou nRegionalIDType). 4 Converte caracteres Hiragana de byte duplo em cExpression para caracteres Katakana de byte duplo. Suportado somente para Locale ID (especificado com os parâmetros nRegionalIdentifier ou nRegionalIDType). 5 Converte caracteres de byte duplo para UNICODE (caracteres wide). 6 Converte UNICODE (caracteres wide) para caracteres de byte duplo. 7 Converte cExpression para minúsculas específicas de localidade. Suportado somente para Locale ID (especificado com os parâmetros nRegionalIdentifier ou nRegionalIDType). 8 Converte cExpression para maiúsculas específicas de localidade. Suportado somente para Locale ID (especificado com os parâmetros nRegionalIdentifier ou nRegionalIDType). 9 Converte caracteres de byte duplo em cExpression para UTF-8 10 Converte caracteres Unicode em cExpression para UTF-8 11 Converte caracteres UTF-8 em cExpression para caracteres de byte duplo. 12 Converte caracteres UTF-8 em cExpression para caracteres UNICODE. 13 Converte caracteres de byte único em cExpression para binário base64 codificado. 14 Converte dados codificados em base64 em cExpression para dados originais não codificados. 15 Converte caracteres de byte único em cExpression para hexBinary codificado. 16 Converte caracteres de byte único em cExpression para hexBinary decodificado.
**nRegionalIdentifier**
Especifica o Locale ID, página de código ou valor FontCharSet a ser usado para a conversão. Se nRegionalIDType for omitido, o Locale ID é usado para a conversão. Se nRegionalIdentifier for omitido, o Locale ID do sistema é usado por padrão. Se nRegionalIdentifier for inválido ou não suportado na máquina, o erro "Invalid locale ID" é gerado. nRegionalIdentifier Idioma 1029 Tcheco 1031 Alemão 1033 Inglês (Padrão) 1034 Espanhol 1036 Francês 1040 Italiano 1045 Polonês 1046 Português (Brasil) 2070 Português (Portugal)
**nRegionalIDType**
Especifica se um Locale ID, página de código ou FontCharSet é usado para a conversão. O parâmetro nRegionalIdentifier, descrito acima, é usado para especificar o Locale ID, página de código ou FontCharSet real usado para a conversão. nRegionalIDType Descrição 0 (Padrão) Especifica que o parâmetro nRegionalIdentifier é um valor Locale ID. 1 Especifica que nRegionalIdentifier é um valor de página de código. 2 Especifica que nRegionalIdentifier é um valor FontCharSet.

# Valor de retorno

Tipo de dados Character. STRCONV( ) retorna a expressão de caracteres convertida.

# Observações

O Visual FoxPro desconsidera caracteres inválidos ou comprimento incorreto em cadeias de caracteres codificadas em base 64 e hexBinary.

Esta função é útil para manipular conjuntos de caracteres de byte duplo para idiomas como Hiragana e Katakana.
