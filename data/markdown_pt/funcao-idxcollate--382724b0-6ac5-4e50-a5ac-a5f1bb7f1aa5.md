# Função IDXCOLLATE( )

Retorna a sequência de collating de um índice ou tag de índice.

```foxpro
IDXCOLLATE([cCDXFileName,] nIndexNumber [, nWorkArea | cTableAlias])
```

#### Parâmetros
 **cCDXFileName**
Especifica o nome do arquivo de índice composto. O arquivo de índice composto que você especifica pode ser o arquivo de índice composto estrutural aberto automaticamente com a tabela ou um arquivo de índice composto independente.
**nIndexNumber**
Especifica o índice ou tag de índice para o qual IDXCOLLATE( ) retorna a sequência de collating. IDXCOLLATE( ) retorna a sequência de collating para índices e tags de índice na seguinte ordem conforme nIndexNumber aumenta de 1 até o número total de arquivos de índice abertos e tags de índice: Sequências de collating para arquivos de índice .idx de entrada única (se algum estiver aberto) são retornadas primeiro. A ordem em que os arquivos de índice de entrada única são incluídos em USE ou SET INDEX determina como as sequências de collating são retornadas. Sequências de collation para tags no índice composto estrutural (se houver um) são retornadas em seguida. As sequências de collating são retornadas para as tags na ordem em que as tags são criadas no índice composto estrutural. Sequências de collating para tags em quaisquer índices compostos independentes abertos são retornadas por último. As sequências de collation são retornadas para as tags na ordem em que as tags são criadas nos índices compostos independentes. A cadeia de caracteres vazia é retornada se nIndexNumber for maior que o número total de arquivos .idx de entrada única abertos e tags de índice composto estrutural e independente.
**nWorkArea**
Especifica a área de trabalho da tabela para a qual IDXCOLLATE( ) retorna sequências de collating de arquivos de índice e tags de índice. IDXCOLLATE( ) retorna a cadeia de caracteres vazia se uma tabela não estiver aberta na área de trabalho que você especificar.
**cTableAlias**
Especifica o alias da tabela para a qual IDXCOLLATE( ) retorna sequências de collation de arquivos de índice e tags de índice. O Visual FoxPro gera uma mensagem de erro se você especificar um alias de tabela que não exista.

# Valor de retorno

Character

# Observações

IDXCOLLATE( ) pode ser usado para retornar a sequência de collating para cada tag em arquivos de índice composto de múltiplas entradas, permitindo que você exclua completamente um arquivo de índice e o reconstrua corretamente, usando uma série de comandos SET COLLATE e INDEX.

Observe que IDXCOLLATE( ) não é necessário para o funcionamento adequado de REINDEX, porque as informações de sequência de collation estão presentes nos índices e tags de índice existentes.

Para obter informações adicionais sobre o suporte internacional do Visual FoxPro, consulte Developing International Applications.

# Exemplo

O exemplo a seguir abre a tabela `Customer` no banco de dados `testdata`. FOR ... ENDFOR é usado para criar um loop no qual IDXCOLLATE( ) é usado para exibir a sequência de collation de cada tag de índice no índice estrutural `Customer`. O nome de cada tag de índice estrutural é exibido com sua sequência de collation.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE Customer     && Open Customer table.
CLEAR
FOR nCount = 1 TO TAGCOUNT()
   IF !EMPTY(TAG(nCount))  && Checks for tags in the index.
   ? TAG(nCount) + ' '  && Display tag name.
   ?? IDXCOLLATE(nCount)  && Display collation sequence.
   ELSE
      EXIT  && Exit the loop when no more tags are found.
   ENDIF
ENDFOR
```
