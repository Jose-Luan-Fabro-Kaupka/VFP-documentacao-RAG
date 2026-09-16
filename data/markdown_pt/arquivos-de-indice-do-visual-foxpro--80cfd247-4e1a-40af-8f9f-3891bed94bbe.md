# Arquivos de índice do Visual FoxPro

Quando você cria um índice, fornece uma expressão, que pode conter nomes de campos de tabela, que especifica como os registros da tabela devem ser organizados. O Visual FoxPro cria uma chave de índice para cada registro na tabela baseada na expressão de índice e armazena as chaves de índice em um arquivo de índice. O arquivo de índice contém e mantém ponteiros para registros no arquivo de tabela (.dbf) e é organizado de acordo com os valores das chaves de índice. Um arquivo de índice é separado, mas associado a um arquivo .dbf.

O Visual FoxPro suporta os seguintes tipos de arquivos de índice: índice composto estrutural (.cdx), arquivos de índice composto não estrutural (.cdx) e arquivos de índice autônomo (.idx). Os arquivos .cdx estruturais e não estruturais podem conter vários índices, que possuem nomes, ou tags, que os identificam, enquanto o arquivo .idx autônomo contém apenas um único índice.

O diagrama a seguir mostra um arquivo .cdx com três nomes de índice, ou tags. Duas das tags de índice, emp_id e last_name, representam índices baseados em campos únicos. A tag de índice cntry_last organiza registros usando uma expressão de índice simples de dois campos.
 Um arquivo .cdx contendo várias tags que representam vários cenários de ordenação para registros

A tabela a seguir resume os tipos de arquivos de índice no Visual FoxPro, como são nomeados, o número de chaves de índice que podem conter e as limitações de caracteres para cada um.
 Tipos de arquivos de índice do Visual FoxPro
| Index file type | Description | Contains | Limits |
| --- | --- | --- | --- |
| Structural compound index (.cdx) files | Opens and closes with the table automatically. Uses same base name as the table file name. | Multiple index keys | 240-character limit on evaluated expression |
| Nonstructural compound index (.cdx) files | Must be opened explicitly. Uses a name different from the base table name and is defined by the user. | Multiple index keys | 240-character limit on evaluated expression |
| Standalone index (.idx) files | Must be opened explicitly. Uses a name different from the base table name and is defined by the user. | Single index key | 100-character limit on evaluated expression |

# Arquivos de índice composto estrutural

Quando você cria um índice para uma tabela, o Visual FoxPro cria automaticamente um arquivo .cdx estrutural para armazenar o índice. O termo "estrutural" refere-se ao fato de que o Visual FoxPro trata o arquivo .cdx estrutural como parte intrínseca da tabela, abre e fecha o arquivo .cdx estrutural automaticamente quando você abre e fecha a tabela, e mantém o arquivo .cdx estrutural automaticamente quando você adiciona, altera ou exclui registros da tabela. Se uma tabela do Visual FoxPro tem um arquivo de índice associado a ela, normalmente é um arquivo .cdx estrutural. Um arquivo .cdx estrutural sempre tem o mesmo nome base do arquivo de tabela (.dbf).

O arquivo .cdx estrutural pode conter vários índices no mesmo arquivo. É recomendável usar o arquivo .cdx estrutural para índices que você usa frequentemente e precisa manter regularmente, como aqueles usados para organizar registros para visualização diária, entrada de dados, Otimização de Consulta Rushmore ou relatórios impressos frequentemente.

> **Observação:** Para uma determinada tabela, o Visual FoxPro armazena índices primários e candidatos no arquivo .cdx estrutural associado ao arquivo de tabela (.dbf). Você não pode armazenar índices primários e candidatos em outros arquivos .cdx, como arquivos .cdx não estruturais, nem é possível usar arquivos de índice autônomo (.idx) para índices primários e candidatos, pois o arquivo de índice deve sempre abrir quando a tabela associada é aberta.

# Arquivos de índice composto não estrutural

Arquivos .cdx não estruturais armazenam vários índices que não são usados frequentemente. Você pode usar um arquivo .cdx não estrutural quando deseja criar vários índices para um propósito especial, mas não deseja que seu aplicativo mantenha esses índices de forma contínua. Um arquivo .cdx não estrutural sempre tem um nome diferente do arquivo de tabela (.dbf) e é definido pelo usuário.

Por exemplo, suponha que seu aplicativo contenha um conjunto especial de relatórios que analisa dados baseados em campos normalmente não indexados. Você pode criar um arquivo .cdx não estrutural contendo os índices apropriados, executar os relatórios e depois excluir o arquivo .cdx não estrutural.

> **Observação:** Diferentemente dos arquivos .cdx estruturais que abrem automaticamente quando a tabela associada é aberta, você deve abrir um arquivo .cdx não estrutural explicitamente usando o comando SET INDEX ou o comando USE com a cláusula INDEX. Para obter mais informações, consulte SET INDEX Command e USE Command .

# Arquivos de índice autônomo

Disponíveis principalmente para compatibilidade com versões anteriores, um arquivo .idx autônomo armazena uma única chave de índice que é temporária ou usada com menos frequência. Você pode usar arquivos autônomos (.idx) como índices temporários criando-os ou reindexando-os imediatamente antes de usá-los. Um arquivo .idx autônomo sempre tem um nome diferente do arquivo de tabela (.dbf) e é definido pelo usuário.

Por exemplo, suponha que você tenha um índice que usa apenas para relatórios de resumo trimestrais ou anuais. Em vez de incluir este índice no arquivo .cdx estrutural, onde é mantido sempre que você usa a tabela, você pode criar um arquivo .idx autônomo para armazenar este índice. Você pode criar quantos arquivos .idx desejar para uma determinada tabela.
