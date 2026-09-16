# Função INDEXSEEK( )

Sem mover o ponteiro de registro, pesquisa uma tabela indexada pela primeira ocorrência de um registro cuja chave de índice corresponda a uma expressão especificada.

```foxpro
INDEXSEEK(eExpression [, lMovePointer [, nWorkArea | cTableAlias
   [, nIndexNumber | cIDXIndexFileName | cTagName]]])
```

#### Parâmetros
 **eExpression**
Especifica a expressão de chave de índice pela qual você deseja que INDEXSEEK( ) pesquise.
**lMovePointer**
Especifica se o ponteiro de registro é movido para o registro correspondente. Se lMovePointer for true (.T.) e existir um registro correspondente, o ponteiro de registro é movido para o registro correspondente. Se lMovePointer for true (.T.) e não existir um registro correspondente, o ponteiro de registro não é movido. Se lMovePointer for false (.F.) ou for omitido, o ponteiro de registro não é movido mesmo se existir um registro correspondente.
**nWorkArea**
Especifica o número da área de trabalho da tabela que é pesquisada pela chave de índice.
**cTableAlias**
Especifica o alias da tabela que é pesquisada. Se você omitir nWorkArea e cTableAlias , a tabela na área de trabalho atualmente selecionada é pesquisada.
**nIndexNumber**
Especifica o número do arquivo de índice ou tag que é usado para pesquisar a chave de índice. nIndexNumber refere-se aos arquivos de índice conforme listados em USE ou SET INDEX. Arquivos .IDX abertos são numerados primeiro na ordem em que aparecem em USE ou SET INDEX. Tags no arquivo .cdx estrutural (se existir) são então numeradas na ordem em que foram criadas. Finalmente, tags em quaisquer arquivos .cdx independentes abertos são numeradas na ordem em que foram criadas. Para obter mais informações sobre numeração de índices, consulte SET ORDER .
**cIDXIndexFileName**
Especifica um arquivo .idx que é usado para pesquisar a chave de índice.
**cTagName**
Especifica uma tag de um arquivo .cdx que é usada para pesquisar a chave de índice. O nome da tag pode ser de um arquivo .cdx estrutural ou de qualquer arquivo .cdx independente aberto. Observação O arquivo .idx tem precedência se existirem nomes duplicados de arquivo .idx e tag.

# Valor de retorno

Lógico

# Observações

INDEXSEEK( ) retorna true (.T.) se uma correspondência for encontrada; caso contrário, retorna false (.F.). Você pode usar INDEXSEEK( ) somente com uma tabela com uma ordem de índice definida, e pode pesquisar somente por uma chave de índice. A correspondência deve ser exata, a menos que SET EXACT esteja definido como OFF.

INDEXSEEK( ) fornece uma maneira rápida de pesquisar registros sem mover o ponteiro de registro. Como o ponteiro de registro não é movido, regras e gatilhos não são executados. Se INDEXSEEK( ) retornar true (.T.) indicando que um registro correspondente foi encontrado, você pode executar INDEXSEEK( ) novamente com o segundo parâmetro lMovePointer definido como true (.T.) para mover para o registro correspondente.

INDEXSEEK( ) retorna false (.F.) quando você está tentando encontrar um valor no registro criado mais recentemente (criado com INSERT INTO ou APPEND BLANK) até que o ponteiro de registro seja movido. Você pode executar um comando GO BOTTOM para fazer INDEXSEEK( ) encontrar o registro criado mais recentemente.
