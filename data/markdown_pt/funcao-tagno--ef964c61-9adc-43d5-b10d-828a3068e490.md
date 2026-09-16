# Função TAGNO( )

Retorna a posição do índice para tags de arquivo de índice composto .cdx e arquivos de índice de entrada única .idx abertos.

```foxpro
TAGNO([IndexName [, CDXFileName [, nWorkArea | cTableAlias]]])
```

#### Parâmetros
 **IndexName**
Especifica o nome de uma tag de arquivo de índice composto .cdx ou de um arquivo de índice de entrada única .idx aberto para o qual TAGNO( ) retorna a posição do índice.
**CDXFileName**
Especifica o nome de um arquivo de índice composto .cdx que contém o nome da tag especificado com IndexName.
**nWorkArea**
Especifica a área de trabalho da tabela para a qual TAGNO( ) retorna a posição do índice para tags de arquivo de índice composto .cdx e arquivos de índice de entrada única .idx.
**cTableAlias**
Especifica o alias da tabela para a qual TAGNO( ) retorna a posição do índice para tags de arquivo de índice composto .cdx e arquivos de índice de entrada única .idx.

# Valor de retorno

Numérico

# Observações

TAGNO( ) retorna 0 se um índice mestre não estiver definido (a tabela está em ordem natural de número de registro) e os parâmetros opcionais forem omitidos.

Incluída para compatibilidade com dBASE.
