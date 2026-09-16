# Função KEYMATCH( )

Pesquisa uma tag de índice ou arquivo de índice por uma chave de índice.

```foxpro
KEYMATCH(eIndexKey [, nIndexNumber [, nWorkArea | cTableAlias]])
```

#### Parâmetros
 **eIndexKey**
Especifica a chave de índice que KEYMATCH( ) pesquisa. As chaves de índice em um arquivo de índice ou tag de índice são determinadas pela expressão de índice. Uma expressão de índice é especificada quando um arquivo de índice ou tag de índice é criado com INDEX. KEY( ) e SYS(14) podem ser usados para retornar as expressões de índice para arquivos de índice e tags de índice. Para mais informações sobre criação de arquivos de índice, expressões de índice e chaves de índice, consulte INDEX . Se você não incluir nenhum dos parâmetros opcionais, KEYMATCH( ) pesquisa o arquivo de índice mestre ou tag de índice mestre pela chave de índice que você especifica. Se um arquivo de índice mestre ou tag de índice mestre não estiver em vigor (por exemplo, você emitiu SET ORDER TO sem parâmetros para colocar a tabela em ordem física de registros), o Visual FoxPro gera uma mensagem de erro.
**nIndexNumber**
Especifica qual arquivo de índice ou tag de índice é pesquisado. nIndexNumber é tipicamente um inteiro que começa em 1 e é incrementado em 1 para pesquisar tags de índice adicionais. Se nIndexNumber for 1, o arquivo de índice .idx de entrada única mestre ou tag de índice mestre (se houver) é pesquisado. Conforme nIndexNumber aumenta, tags subsequentes no índice composto estrutural (se houver) são pesquisadas. As tags são pesquisadas na ordem em que foram criadas no índice composto estrutural. Conforme nIndexNumber continua a aumentar e todas as tags no índice composto estrutural foram pesquisadas, tags em quaisquer índices compostos independentes abertos são então pesquisadas. As tags são pesquisadas na ordem em que foram criadas nos índices compostos independentes. Uma mensagem de erro é gerada se nIndexNumber for maior que o número total de arquivos .idx de entrada única abertos e tags de índice composto estrutural e independente.
**nWorkArea | cTableAlias**
Pesquisa arquivos de índice ou tags abertos em outra área de trabalho. nWorkArea especifica o número da área de trabalho e cTableAlias especifica o alias da tabela. Se você omitir a área de trabalho e o alias, KEYMATCH( ) pesquisa arquivos de índice ou tags abertos para a tabela na área de trabalho atual. Se nenhuma tabela tiver o alias que você especifica, o Visual FoxPro gera uma mensagem de erro.

# Valor de retorno

Logical

# Observações

KEYMATCH( ) pesquisa uma tag de índice ou arquivo de índice por uma chave de índice específica e retorna true (.T.) se a chave de índice for encontrada; caso contrário, KEYMATCH( ) retorna false (.F.). KEYMATCH( ) pode ser usado para impedir chaves de índice duplicadas.

KEYMATCH( ) retorna o ponteiro de registro ao registro em que estava originalmente posicionado antes de KEYMATCH( ) ser emitido.
