# Função CPCONVERT( )

Converte campos de caracteres ou memo, ou expressões de caracteres, para outra página de código.

```foxpro
CPCONVERT(nCurrentCodePage, nNewCodePage, cExpression)
```

#### Parâmetros
 **nCurrentCodePage**
Especifica a página de código da qual cExpression está sendo convertida.
**nNewCodePage**
Especifica a página de código para a qual cExpression é convertida.
**cExpression**
Especifica a expressão de caracteres que será convertida.

# Observações

Observe que CPCONVERT( ) não é necessária para o funcionamento normal do produto entre plataformas. Ela é usada estritamente para acessar os recursos de tradução subjacentes do Visual FoxPro.

Por exemplo, se a variável `gcCharExpr` contiver um caractere com determinada aparência no Macintosh (na página de código 10000), CPCONVERT( ) retornará um caractere com determinada aparência no Microsoft Windows (página de código 1252):

```foxpro
CPCONVERT(10000, 1252, gcCharExpr)
```

Para obter informações adicionais sobre páginas de código e o suporte internacional do Visual FoxPro, consulte Páginas de código compatíveis com o Visual FoxPro e Desenvolvimento de aplicativos internacionais.
