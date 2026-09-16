# Linguagem de manipulação de índices

Esses comandos e funções executam operações em arquivos de índice e retornam informações sobre eles.

| Use | Para |
| --- | --- |
| ATAGINFO( ) Function | Criar uma matriz que contém informações sobre arquivos de índice da tabela selecionada. |
| CANDIDATE( ) Function | Especificar se uma tag de índice é uma tag de índice candidata. |
| CDX( ) Function | Retornar o nome do arquivo de índice composto aberto que possui a posição de índice especificada. |
| CLOSE Commands | Fechar vários tipos de arquivo. |
| COPY INDEXES Command | Criar tags de índice composto a partir de arquivos de índice de entrada única .idx. |
| COPY TAG Command | Criar um arquivo de índice de entrada única (.idx) a partir de uma tag em um arquivo de índice composto. |
| DESCENDING( ) Function | Determinar se um índice foi criado com a palavra-chave DESCENDING. |
| DELETE TAG Command | Remover uma tag de um arquivo de índice composto. |
| FOR( ) Function | Retornar uma expressão de filtro de índice. |
| IDXCOLLATE( ) Function | Retornar a sequência de ordenação para um índice ou tag de índice. |
| INDEX Command | Criar um arquivo de índice. |
| INDEXSEEK( ) Function | Pesquisar uma tabela indexada sem mover o ponteiro de registro. |
| KEY( ) Function | Retornar a expressão de chave de índice para uma tag de índice ou arquivo de índice. |
| KEYMATCH( ) Function | Pesquisar uma tag de índice ou arquivo de índice por uma chave de índice. |
| MDX( ) Function | Retornar o nome do arquivo de índice composto aberto que possui o número de posição de índice especificado. |
| NDX( ) Function | Retornar o nome de um arquivo de índice (.IDX) aberto para a tabela atual ou especificada. |
| ORDER( ) Function | Retornar o nome do arquivo de índice ou tag controladora |
| PRIMARY( ) Function | Determinar se uma tag de índice é a tag de índice primária. |
| REINDEX Command | Reconstruir arquivos de índice abertos. |
| SET COLLATE Command | Especificar uma sequência de ordenação para campos de caractere em operações de indexação e classificação. |
| SET INDEX Command | Abrir um ou mais arquivos de índice para uso com a tabela atual. |
| SET KEY Command | Especificar acesso a um intervalo de registros baseado em suas chaves de índice. |
| SET ORDER Command | Designar um arquivo de índice ou tag controladora para uma tabela. |
| SET UNIQUE Command | Especificar se registros com valores de chave de índice duplicados são mantidos em um arquivo de índice. |
| SYS(14) - Index Expression | Retornar as expressões de índice dos índices. |
| SYS(21) - Controlling Index Number | Retornar a posição de índice da área de trabalho selecionada atual. |
| SYS(22) - Controlling Tag or Index Name | Retorna o nome da tag de índice composto .cdx controladora mestra ou do arquivo de índice .idx de uma tabela. |
| SYS(2021) - Filtered Index Expression | Retorna a expressão de filtro para um arquivo de índice de entrada única (.idx) aberto ou expressões de filtro para tags em arquivos de índice composto (.cdx). |
| SYS(2021) - Filtered Index Expression | Retornar uma expressão de filtro de um índice. |
| TAG( ) Function | Retornar um nome de tag de um arquivo de índice composto aberto ou o nome de um arquivo de índice de entrada única aberto. |
| TAGCOUNT( ) Function | Retornar o número de índices abertos. |
| TAGNO( ) Function | Retornar a posição de índice para um arquivo de índice. |
