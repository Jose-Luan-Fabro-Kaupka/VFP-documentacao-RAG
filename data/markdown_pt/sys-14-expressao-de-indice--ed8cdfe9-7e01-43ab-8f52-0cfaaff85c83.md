# SYS(14) - Expressão de índice

Retorna a expressão de índice de um arquivo de índice .idx de entrada única aberto ou expressões de índice para tags em arquivos de índice compostos .cdx.

```foxpro
SYS(14, nIndexNumber [, nWorkArea | cTableAlias])
```

#### Parâmetros
 **nIndexNumber**
Especifica qual expressão de índice retornar dos arquivos de índice ou tags abertos. SYS(14) retorna expressões de índice de arquivos de índice abertos e tags na seguinte ordem conforme nIndexNumber aumenta de 1 até o número total de arquivos de entrada única abertos e tags de índice compostos estruturais e independentes: Expressões de índice de arquivos de índice de entrada única (se algum estiver aberto) são retornadas primeiro. A ordem em que os arquivos de índice de entrada única são incluídos em USE ou SET INDEX determina a ordem em que as expressões de índice são retornadas. Expressões de índice para cada tag no índice composto estrutural (se houver um) são retornadas em seguida. As expressões de índice são retornadas das tags na ordem em que as tags foram criadas no índice estrutural. Expressões de índice para cada tag em quaisquer índices compostos independentes abertos são retornadas por último. As expressões de índice são retornadas das tags na ordem em que as tags foram criadas nos índices compostos independentes. A cadeia de caracteres vazia é retornada se nIndexNumber for maior que o número total de arquivos de entrada única abertos e tags de índice compostos estruturais e independentes.
 **nWorkArea | cTableAlias**
Especifica um número de área de trabalho ou alias de área de trabalho. Se você omitir nWorkArea e cTableAlias , expressões de índice são retornadas de arquivos de índice abertos na área de trabalho atual. Se uma tabela não tiver o alias que você especificar, o Visual FoxPro gera uma mensagem de erro.

# Valor de retorno

Character

# Observações

Uma expressão de índice é especificada quando um arquivo de índice ou tag é criado com INDEX. A expressão de índice determina como uma tabela é exibida e acessada quando um arquivo de índice ou tag é usado para ordenar a tabela.

Para obter mais informações sobre expressões de índice e criação de arquivos de índice e tags, consulte Comando INDEX. SYS(14) é semelhante à função KEY( ).

USE e SET INDEX suportam uma lista de nomes de arquivos de índice que permite abrir arquivos de índice para uma tabela. Qualquer combinação de arquivos de índice de entrada única, nomes de arquivos de índice compostos estruturais ou independentes pode ser incluída na lista de arquivos de índice.
