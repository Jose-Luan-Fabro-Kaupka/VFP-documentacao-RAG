# Função SUBSTRC( )

Retorna uma cadeia de caracteres da expressão de caracteres ou campo memo fornecida.

```foxpro
SUBSTRC(cExpression, nStartPosition [, nCharactersReturned])
```

#### Parâmetros
 **cExpression**
Especifica a expressão de caracteres ou campo memo da qual a cadeia de caracteres é retornada.
**nStartPosition**
Especifica a posição na expressão de caracteres ou campo memo cExpression a partir da qual a cadeia de caracteres é retornada. O primeiro caractere de cExpression é a posição 1. Se TALK estiver definido como ON e nStartPosition for maior que o número de caracteres em cExpression , o Visual FoxPro gera uma mensagem de erro. Se TALK estiver definido como OFF, a cadeia de caracteres vazia é retornada.
**nCharactersReturned**
Especifica o número de caracteres a retornar de cExpression . Se você omitir nCharactersReturned , os caracteres são retornados até o final da expressão de caracteres ser atingido.

# Valor de retorno

Caractere

# Observações

SUBSTRC( ) foi projetada para expressões que contêm caracteres de byte duplo. Se a expressão contém apenas caracteres de byte único, SUBSTRC( ) é equivalente a SUBSTR( ).

SUBSTRC( ) retorna uma cadeia de caracteres da expressão de caracteres ou campo memo fornecida. A expressão de caracteres ou campo memo pode conter qualquer combinação de caracteres de byte único e byte duplo.

SUBSTRC( ) não retornará um valor para um campo memo quando emitida na janela Debug. Para retornar um valor na janela Debug, coloque o nome do campo memo dentro de ALLTRIM( ) e coloque ALLTRIM( ) dentro de SUBSTRC( ).

Esta função é útil para manipular conjuntos de caracteres de byte duplo para idiomas como Hiragana e Katakana.
