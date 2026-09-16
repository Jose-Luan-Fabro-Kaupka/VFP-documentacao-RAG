# Tipos de índice do Visual FoxPro

O Visual FoxPro oferece diferentes tipos de índice para que você possa realizar tarefas adicionais com dados:
 - Controlar se valores duplicados são permitidos nos campos ou na expressão de índice especificada para gerar chaves de índice.
- Estabelecer integridade referencial em relacionamentos persistentes entre tabelas.
- Otimizar índices baseados em expressões lógicas.
- Selecionar e organizar um subconjunto de registros baseado na primeira ocorrência de um valor especificado.
- Otimizar operações de busca e consulta.

Você pode usar todos os tipos de índice do Visual FoxPro, exceto índices binários, para realizar operações de consulta, view, ordenação e SEEK em registros. Você pode usar todos os tipos de índice para otimizar condições de filtro e condições ON e WHERE em instruções SQL SELECT.

A tabela a seguir resume os tipos de índice disponíveis no Visual FoxPro.
 Tipos de índice do Visual FoxPro
| Tipo de índice | Descrição | Quantidade permitida |
| --- | --- | --- |
| Primary | Não permite valores duplicados nos campos ou na expressão especificada. | Um por tabela |
| Candidate | Não permite valores duplicados nos campos ou na expressão especificada. | Muitos por tabela |
| Regular | Permite valores duplicados nos campos ou na expressão especificada. | Muitos por tabela |
| Binary | Indexa registros baseados em uma expressão lógica válida e não nula. | Muitos por tabela |
| Unique | Seleciona um subconjunto de registros baseado na primeira ocorrência de um valor especificado. Incluído para compatibilidade com versões anteriores. | Muitos por tabela |

# Índices primários

O índice primário contém uma chave de índice para cada registro em uma tabela e é o índice padrão quando você não especifica outros índices como índice principal da tabela. O índice primário proíbe valores duplicados nos campos ou na expressão de índice especificada para gerar chaves de índice; portanto, cada chave de índice no índice primário é exclusiva. Você pode criar apenas um índice primário por tabela.

> **Observação:** Índices primários são parte integrante de uma tabela dentro de um banco de dados. Se você liberar uma tabela de um banco de dados, o índice primário é removido. Se você especificar um índice primário em qualquer campo que contenha dados duplicados, o Visual FoxPro gera um erro.

O índice primário também é usado principalmente na tabela primária ou "referenciada" para estabelecer integridade referencial em um relacionamento persistente entre tabelas.

# Índices candidatos

Semelhante a um índice primário, um índice candidato contém uma chave de índice para cada registro em uma tabela e proíbe valores duplicados nos campos ou na expressão de índice especificada para gerar chaves de índice. No entanto, você pode criar vários índices candidatos por tabela. O nome "candidate" na verdade se refere ao status do índice; ou seja, você pode criar índices candidatos como seleções alternativas para o índice primário.

> **Observação:** Se você especificar um índice candidato em qualquer campo que contenha dados duplicados, o Visual FoxPro gera um erro.

Índices candidatos podem ser usados como índice referenciado ou referenciador para estabelecer integridade referencial em um relacionamento persistente entre tabelas. Por exemplo, em um relacionamento persistente um-para-muitos ou um-para-um, você pode usar índices candidatos e primários para definir o lado "um" nesses relacionamentos.

# Índices regulares

Um índice regular contém uma chave de índice para cada registro na tabela, mas permite valores duplicados nos campos ou na expressão de índice especificada para gerar chaves de índice. Um índice regular é simplesmente um índice que não é exclusivo, primário ou candidato. Você pode criar mais de um índice regular para uma tabela.

Você não pode usar índices regulares para impor a exclusividade dos dados nesses registros. Você pode usar um índice regular como o lado "muitos" em um relacionamento persistente um-para-muitos.

# Índices binários

Um índice binário, ou bitmap, é usado para criar índices baseados em expressões lógicas, por exemplo, indexando registros excluídos, e é suportado para tabelas livres e de banco de dados. No entanto, índices binários não suportam o seguinte:
 - Usar expressões de índice que avaliam para null.
- Usar expressões de filtro da cláusula FOR.
- Alterar a ordem em que os registros são exibidos e processados, por exemplo, usando as palavras-chave ASCENDING, DESCENDING, UNIQUE ou CANDIDATE.
- Definir índices binários como índices de controle, por exemplo, usando o comando SET ORDER.
- Realizar operações de ordenação e busca.

Um índice binário pode ser significativamente menor que um índice não binário e pode melhorar a velocidade na manutenção de índices, por exemplo, ao usar índices baseados em registros excluídos. Para obter mais informações, consulte Índices baseados em registros excluídos. O Visual FoxPro frequentemente pode criar o bitmap de otimização Rushmore mais rapidamente para um índice binário se o número de registros retornados for superior a 3% do número total de registros. No entanto, o bitmap Rushmore pode ser criado mais lentamente se o número de registros retornados for inferior a 3% do número total de registros. O limite de 3% pode diminuir conforme o número de registros na tabela aumenta.

> **Observação:** Melhorias ou degradações de desempenho e tamanhos de índice binário podem variar com seus dados específicos e arquitetura de aplicativo. Os números usados no exemplo são baseados em testes usando dados de teste aleatórios.

Você pode criar índices binários usando o Table Designer ou o comando INDEX. Para obter mais informações, consulte Como: criar índices (Visual FoxPro) e Comando INDEX.

# Índices unique

Versões anteriores do Visual FoxPro incluíam índices unique. Índices unique na verdade não impedem que valores duplicados sejam inseridos na tabela. O nome "unique" na verdade descreve as entradas no arquivo de índice porque o arquivo não armazena uma chave de índice particular mais de uma vez e desconsidera ocorrências posteriores de chaves de índice duplicadas. Índices unique tornam possível especificar que apenas a chave de índice do primeiro registro correspondente à expressão de índice é adicionada ao índice. Após uma correspondência ocorrer, nenhuma outra chave de índice é adicionada ao índice. No entanto, a tabela ainda pode conter valores duplicados.

> **Dica:** Se desejar selecionar registros dessa maneira, é recomendável criar uma consulta ou view em vez disso. Para obter mais informações, consulte Trabalhando com consultas e Trabalhando com views.
