# Função GETWORDCOUNT( )

Conta as palavras em uma cadeia de caracteres.

```foxpro
GetWordCount(cString[, cDelimiters])
```

#### Parâmetros
 **cString**
Especifica a cadeia de caracteres cujas palavras serão contadas.
**cDelimiters**
Opcional. Especifica um ou mais caracteres opcionais usados para separar palavras em cString. Os delimitadores padrão são espaço, tabulação, retorno de carro e quebra de linha. Observe que GetWordCount( ) usa cada um dos caracteres em cDelimiters como delimitadores individuais, e não a cadeia inteira como um único delimitador.

# Valor de retorno

Numeric

# Observações

GetWordCount( ) assume por padrão que as palavras são delimitadas por espaços ou tabulações. Se você especificar outro caractere como delimitador, esta função ignora espaços e tabulações e usa apenas o caractere especificado.

Se você usar "AAA aaa, BBB bbb, CCC ccc." como a cadeia de caracteres de destino para GetWordCount( ), você pode obter todos os resultados a seguir.

```foxpro
cString = "AAA aaa, BBB bbb, CCC ccc."
? GetWordCount(cString)               && 6 - character groups, delimited by " "
? GetWordCount(cString, ",")               && 3 - character groups, delimited by ","
? GetWordCount(cString, ".")               && 1 - character group, delimited by "."
```
