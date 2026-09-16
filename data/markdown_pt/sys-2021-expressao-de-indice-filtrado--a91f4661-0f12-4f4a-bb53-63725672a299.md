# SYS(2021) - Expressão de índice filtrado

Retorna a expressão de filtro de um arquivo de índice de entrada única (.idx) aberto ou expressões de filtro para tags em arquivos de índice composto (.cdx).

```foxpro
SYS(2021, nIndexNumber [, nWorkArea | cTableAlias])
```

#### Parâmetros
 **nIndexNumber**
A expressão numérica nIndexNumber especifica qual expressão de filtro retornar dos arquivos de índice abertos. SYS(2021) retorna expressões de filtro dos arquivos de índice abertos na seguinte ordem conforme nIndexNumber aumenta de 1 até o número total de arquivos .idx de entrada única abertos e tags de índice composto estrutural e independente: Expressões de filtro de arquivos .idx de entrada única (se houver algum aberto) são retornadas primeiro. A ordem em que os arquivos .idx de entrada única são incluídos em USE ou SET INDEX determina a ordem em que as expressões de filtro são retornadas. Expressões de filtro para cada tag no arquivo .cdx estrutural (se houver um) são retornadas em seguida. As expressões de filtro são retornadas das tags na ordem em que as tags foram criadas no índice estrutural. Expressões de filtro para cada tag em quaisquer arquivos .cdx independentes abertos são retornadas por último. As expressões de filtro são retornadas das tags na ordem em que as tags foram criadas nos índices compostos independentes. A cadeia de caracteres vazia é retornada se nIndexNumber for maior que o número total de arquivos .idx de entrada única abertos e tags de arquivos .Cdx estruturais e independentes.
**nWorkArea**
Especifica o número da área de trabalho para uma tabela aberta em outra área de trabalho.
**cTableAlias**
Especifica um alias de tabela para uma tabela aberta em outra área de trabalho. Se uma tabela não tiver o alias que você especificar, o Visual FoxPro exibe uma mensagem de erro.

# Valor de retorno

Character

# Observações

Você pode criar índices filtrados no Visual FoxPro. Se você incluir a cláusula FOR opcional em INDEX, o arquivo de índice atua como um filtro na tabela. Somente registros que correspondem à expressão de filtro lExpression na cláusula FOR estão disponíveis para exibição e acesso. Chaves de índice são criadas no arquivo de índice somente para os registros que correspondem à expressão de filtro.

A cadeia de caracteres vazia é retornada se um índice ou tag de índice foi criado sem uma cláusula FOR.

USE e SET INDEX suportam uma lista de nomes de arquivos de índice que torna possível abrir arquivos de índice para uma tabela. Qualquer combinação de nomes de arquivos .idx de entrada única, nomes de arquivos .cdx estruturais e nomes de arquivos .cdx independentes pode ser incluída na lista de nomes de arquivos de índice.

SYS(2021) retorna expressões de filtro de arquivos de índice abertos na área de trabalho atual, a menos que você inclua uma área de trabalho ou alias específico.
