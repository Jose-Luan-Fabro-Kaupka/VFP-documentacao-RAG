# Variável de sistema _PRETEXT

Especifica uma expressão de caractere para prefixar linhas de mesclagem de texto.

```foxpro
_PRETEXT = cExpression
```

# Observações

Usada com SET TEXTMERGE, você pode mesclar texto dentro de um programa. Você pode enviar linhas de texto, o conteúdo de variáveis e os resultados de expressões e funções para a tela, uma janela, uma impressora, um arquivo de texto ou um arquivo de baixo nível.

Se você armazenar uma expressão de caractere em _PRETEXT, a expressão de caractere é adicionada ao início da linha de texto de saída. Para facilitar a indentação do programa, você pode armazenar uma tabulação ou tabulações em _PRETEXT.
