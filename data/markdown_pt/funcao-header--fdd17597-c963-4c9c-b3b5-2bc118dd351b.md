# Função HEADER( )

Retorna o número de bytes no cabeçalho do arquivo de tabela atual ou especificado.

```foxpro
HEADER([nWorkArea | cTableAlias])
```

#### Parâmetros
 **nWorkArea | cTableAlias**
Retorna o tamanho do cabeçalho para uma tabela aberta em outra área de trabalho. nWorkArea especifica o número da área de trabalho e cTableAlias especifica o alias da tabela. Se você omitir a área de trabalho e o alias, HEADER( ) retorna o tamanho do cabeçalho da tabela aberta na área de trabalho atual. HEADER( ) retorna 0 se uma tabela não estiver aberta na área de trabalho especificada. Se uma tabela não tiver o alias especificado, o Visual FoxPro exibe uma mensagem de erro.

# Valor de retorno

Numeric

# Observações

Um cabeçalho de tabela contém informações sobre a tabela em si, como os nomes e tamanhos dos campos e a presença de um arquivo memo ou índice estrutural.
