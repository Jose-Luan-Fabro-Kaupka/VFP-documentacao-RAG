# Comando DELETE TAG

Remove uma tag ou tags de um arquivo de índice composto (.cdx). Existem duas versões da sintaxe.

```foxpro
DELETE TAG TagName1 [OF CDXFileName1] [, TagName2 [OF CDXFileName2]]...
```

```foxpro
DELETE TAG ALL [OF CDXFileName]
```

#### Parâmetros
 **TagName1 [OF CDXFileName1 ] [, TagName2 [OF CDXFileName2 ]] ...**
Especifica uma tag a ser removida de um arquivo de índice composto. Você pode excluir várias tags com um DELETE TAG incluindo uma lista de nomes de tags separados por vírgulas. Se duas ou mais tags com o mesmo nome existem nos arquivos de índice abertos, você pode remover uma tag de um arquivo de índice específico incluindo OF CDXFileName .
**ALL [OF CDXFileName ]**
Remove todas as tags de um arquivo de índice composto. Se a tabela atual tem um arquivo de índice composto estrutural, todas as tags são removidas do arquivo de índice, o arquivo de índice é excluído do disco e o sinalizador no cabeçalho da tabela indicando a presença de um arquivo de índice composto estrutural associado é removido. Use ALL com OF CDXFileName para remover todas as tags de um arquivo de índice composto aberto que não seja o arquivo de índice composto estrutural.

# Observações

Arquivos de índice composto, criados com INDEX, contêm tags correspondentes a entradas de índice. DELETE TAG é usado para remover uma tag ou tags de arquivos de índice composto abertos. Você pode excluir apenas tags de arquivos de índice composto abertos na área de trabalho atual. Se você remover todas as tags de um arquivo de índice composto, o arquivo é excluído do disco.

O Visual FoxPro procura primeiro uma tag no arquivo de índice composto estrutural (se houver um aberto). Se a tag não estiver no arquivo de índice composto estrutural, o Visual FoxPro então procura a tag nos outros arquivos de índice composto abertos.

O Visual FoxPro emite um aviso se você tentar excluir uma tag de índice primário ou candidato e SET SAFETY estiver ON.
