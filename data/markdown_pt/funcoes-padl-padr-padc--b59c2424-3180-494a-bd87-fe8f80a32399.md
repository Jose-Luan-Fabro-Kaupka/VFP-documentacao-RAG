# Funções PADL( ) | PADR( ) | PADC( )

Retorna uma cadeia de caracteres de uma expressão, preenchida com espaços ou caracteres até um comprimento especificado nos lados esquerdo ou direito, ou em ambos.

```foxpro
PADL(eExpression, nResultSize [, cPadCharacter])
```

```foxpro
PADR(eExpression, nResultSize [, cPadCharacter])
```

```foxpro
PADC(eExpression, nResultSize [, cPadCharacter])
```

#### Parâmetros
 **eExpression**
Especifica a expressão a ser preenchida. Esta expressão pode ser de qualquer tipo, exceto uma expressão lógica ou um campo general ou picture.
**nResultSize**
Especifica o número total de caracteres na expressão após o preenchimento.
**cPadCharacter**
Especifica o valor a usar para o preenchimento. Este valor é repetido conforme necessário para preencher a expressão até o número especificado de caracteres. Se você omitir cPadCharacter , espaços (caractere ASCII 32) são usados para o preenchimento.

# Valor de retorno

Character

# Observações

PADL( ) insere preenchimento à esquerda, PADR( ) insere preenchimento à direita e PADC( ) insere preenchimento em ambos os lados.

# Exemplo

```foxpro
STORE 'TITLE' TO gcString
CLEAR
? PADL(gcString, 40, '=')
? PADR(gcString, 40, '=')
? PADC(gcString, 40, '=')
```
