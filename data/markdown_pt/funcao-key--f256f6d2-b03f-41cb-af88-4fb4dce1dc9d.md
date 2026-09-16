# Função KEY( )

Retorna a expressão de chave de índice para uma tag de índice ou arquivo de índice.

```foxpro
KEY([CDXFileName,] nIndexNumber [, nWorkArea | cTableAlias])
```

#### Parâmetros
 **CDXFileName**
Especifica o nome de um arquivo de índice composto. KEY( ) retorna as expressões de chave de índice das tags de índice do arquivo .cdx. O arquivo de índice composto que você especificar pode ser o arquivo de índice composto estrutural aberto automaticamente com a tabela ou pode ser um arquivo de índice composto independente.
**nIndexNumber**
Especifica qual expressão de chave de índice retornar. USE e SET INDEX suportam uma lista de arquivos de índice que permite abrir vários índices para uma tabela. Qualquer combinação de arquivos de índice .idx de entrada única, arquivos de índice composto estrutural ou arquivos de índice composto independentes pode ser incluída na lista de arquivos de índice. A expressão numérica nIndexNumber especifica qual expressão de índice retornar dos arquivos de índice abertos. KEY( ) retorna expressões de índice de arquivos de índice abertos na seguinte ordem conforme nIndexNumber aumenta de 1 até o número total de arquivos .idx de entrada única abertos e tags de índice composto estrutural e independente: Expressões de índice de arquivos de índice .idx de entrada única (se algum estiver aberto) são retornadas primeiro. A ordem em que os arquivos de índice de entrada única são incluídos em USE ou SET INDEX determina como as expressões de índice são retornadas. Expressões de índice para cada tag no índice composto estrutural (se houver um) são retornadas em seguida. As expressões de índice são retornadas das tags na ordem em que as tags são criadas no índice composto estrutural. Expressões de índice para cada tag em quaisquer índices compostos independentes abertos são retornadas por último. As expressões de índice são retornadas das tags na ordem em que as tags são criadas nos índices compostos independentes. A cadeia de caracteres vazia é retornada se nIndexNumber for maior que o número total de arquivos .idx de entrada única abertos e tags de índice composto estrutural e independente.
**nWorkArea**
Especifica o número da área de trabalho da tabela cujas expressões de chave de índice você deseja que KEY( ) retorne. Se uma tabela não estiver aberta na área de trabalho que você especificar, KEY( ) retorna a cadeia de caracteres vazia.
**cTableAlias**
Especifica o alias da tabela cujas expressões de chave de índice você deseja que KEY( ) retorne. Se nenhuma tabela tiver o alias que você especificar, o Microsoft Visual FoxPro gera uma mensagem de erro. Se você omitir nWorkArea e cTableAlias, as expressões de chave de índice são retornadas para a tabela aberta na área de trabalho atual.

# Valor de retorno

Character

# Observações

Uma expressão de chave de índice é especificada quando uma tag de índice ou arquivo de índice é criado com INDEX. A expressão de chave de índice determina como uma tabela é exibida e acessada quando a tag de índice ou arquivo de índice é aberto como a tag ou arquivo de índice mestre controlador.

Para obter mais informações sobre a criação de tags de índice, arquivos de índice e expressões de chave de índice, consulte INDEX Command.

# Exemplo

O exemplo a seguir abre a tabela `customer` no banco de dados `testdata`. FOR ... ENDFOR é usado para criar um loop no qual KEY( ) é usado para exibir a expressão de índice de cada tag de índice no índice estrutural de `customer`. O nome de cada tag de índice estrutural é exibido com sua expressão de índice.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE Customer     && Open customer table
CLEAR
FOR nCount = 1 TO TAGCOUNT()
   IF !EMPTY(TAG(nCount))  && Checks for tags in the index
   ? TAG(nCount) + ' '  && Display tag name
   ?? KEY(nCount)  && Display index expression
   ELSE
      EXIT  && Exit the loop when no more tags are found
   ENDIF
ENDFOR
```
