# Função MDX( )

Retorna o nome do arquivo de índice composto .cdx aberto que tem o número de posição de índice especificado.

```foxpro
MDX(nIndexNumber [, nWorkArea | cTableAlias])
```

#### Parâmetros
 **nIndexNumber**
Especifica qual nome de arquivo de índice composto retornar. Se a tabela tem um arquivo de índice composto estrutural e nIndexNumber é 1, o nome do arquivo de índice composto estrutural (que é sempre o mesmo que o nome da tabela) é retornado. Se nIndexNumber é 2, o nome do primeiro arquivo de índice composto especificado com USE ou SET INDEX é retornado. Se nIndexNumber é 3, o nome do segundo arquivo de índice composto é retornado, e assim por diante. Se nIndexNumber é maior que o número de arquivos de índice composto abertos, uma cadeia de caracteres vazia é retornada. Se a tabela não tem um arquivo de índice composto estrutural e nIndexNumber é 1, o nome do primeiro arquivo de índice composto especificado com USE ou SET INDEX é retornado. Se nIndexNumber é 2, o nome do segundo arquivo de índice composto é retornado, e assim por diante. Se nIndexNumber é maior que o número de arquivos de índice composto abertos, uma cadeia de caracteres vazia é retornada.
**nWorkArea**
Especifica o número da área de trabalho para arquivos de índice composto abertos em áreas de trabalho diferentes da atual. Se você omitir este argumento opcional, os nomes dos arquivos de índice composto são retornados para a área de trabalho atual.
**cTableAlias**
Especifica o alias da tabela para arquivos de índice composto abertos em áreas de trabalho diferentes da atual. Se você omitir este argumento opcional, os nomes dos arquivos de índice composto são retornados para a área de trabalho atual.

# Valor de retorno

Character

# Observações

MDX( ) é idêntico a CDX( ).

Arquivos de índice podem ser abertos para uma tabela com a cláusula INDEX do comando USE ou com SET INDEX. Um arquivo de índice composto estrutural é aberto automaticamente com sua tabela. MDX( ) ignora quaisquer arquivos de índice .idx especificados com USE ou com SET INDEX.

Use TAG( ) para retornar nomes de tags de um arquivo de índice composto; use NDX( ) para retornar o nome de um arquivo de índice .idx aberto.

No Visual FoxPro para Windows, quando SET FULLPATH está ON, MDX( ) retorna o caminho para o arquivo .cdx com o nome do arquivo .cdx. Quando SET FULLPATH está OFF, MDX( ) retorna a unidade em que o arquivo .cdx reside com o nome do arquivo .cdx.
