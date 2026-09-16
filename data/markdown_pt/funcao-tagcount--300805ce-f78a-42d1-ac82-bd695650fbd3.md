# Função TAGCOUNT( )

Retorna o número de tags de arquivos de índice compostos .cdx e arquivos de índice de entrada única .idx abertos.

```foxpro
TAGCOUNT([CDXFileName [, nWorkArea | cTableAlias]])
```

#### Parâmetros
 **CDXFileName**
Especifica o nome de um arquivo de índice composto para o qual TAGCOUNT( ) retorna o número de tags. Se CDXFileName não existir para a tabela atual, você deve especificar o nWorkarea ou cTableAlias em que ele existe. Se você omitir CDXFileName, TAGCOUNT( ) retorna o número de tags em todos os arquivos de índice compostos .cdx e arquivos de índice de entrada única .idx abertos na área de trabalho ou alias atualmente selecionada.
**nWorkarea**
Especifica a área de trabalho da tabela para a qual TAGCOUNT( ) retorna o número de tags do arquivo de índice composto .cdx.
**cTableAlias**
Especifica o alias da tabela para a qual TAGCOUNT( ) retorna o número de tags do arquivo de índice composto .cdx.

# Valor de retorno

Numeric

# Observações

Incluída para compatibilidade com dBASE.
