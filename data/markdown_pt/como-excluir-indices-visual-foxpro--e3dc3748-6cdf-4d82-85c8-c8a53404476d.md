# Como: excluir índices (Visual FoxPro)

Ao excluir índices, ou tags de índice, que você nunca usa, você pode melhorar o desempenho removendo a necessidade de o Visual FoxPro atualizar essas tags. Para excluir um índice, exclua a tag de índice no arquivo de índice composto (.cdx) ou exclua o arquivo de índice independente (.idx) inteiro.

Você pode excluir tags de índice em arquivos .cdx estruturais usando a IDE do Visual FoxPro ou a linguagem. Para excluir um arquivo .idx ou tags de índice de um arquivo .cdx não estrutural, use a linguagem do Visual FoxPro.

# Excluindo tags de índice de um arquivo .cdx estrutural

Você pode excluir uma tag de índice do arquivo .cdx estrutural usando o Table Designer, o comando DELETE TAG se você conhece o nome da tag, ou o comando SQL ALTER TABLE se você não conhece o nome da tag, mas sabe que a tag é um índice primário ou exclusivo.

### Para excluir uma tag de índice em um arquivo .cdx estrutural
- Abra o Table Designer para modificar sua tabela e escolha a guia Indexes.
- Selecione o índice e escolha Delete. Para obter mais informações, consulte Table Designer (Visual FoxPro).

-OU-
 - Use o comando DELETE TAG. Por exemplo, suponha que o arquivo .cdx estrutural da tabela Employee no banco de dados de exemplo do Visual FoxPro, TestData, contenha uma tag de índice chamada Title. O código a seguir exclui a tag de índice Title: USE Employee DELETE TAG Title Para excluir todas as tags no arquivo .cdx, inclua a cláusula ALL no comando DELETE TAG. Para obter mais informações, consulte DELETE TAG Command.

-OU-
 - Use a cláusula DROP PRIMARY KEY ou DROP UNIQUE TAG no comando SQL ALTER TABLE. Por exemplo, suponha que a tag de índice que você deseja excluir seja a chave primária da tabela Employee no banco de dados de exemplo, TestData, mas você não tinha o nome da chave de índice. Você pode usar a cláusula DROP PRIMARY KEY no comando SQL ALTER TABLE: USE employee ALTER TABLE DROP PRIMARY KEY Para obter mais informações, consulte ALTER TABLE - SQL Command.

# Excluindo tags de índice de um arquivo .cdx não estrutural

Você não pode visualizar as tags de índice em arquivos .cdx não estruturais no Table Designer. Portanto, você deve conhecer o nome da tag de índice e usar o comando DELETE TAG para excluir uma tag de índice de um arquivo .cdx não estrutural.

### Para excluir uma tag de índice em um arquivo .cdx não estrutural
- Use o comando DELETE TAG e a cláusula OF para especificar o nome da tag e o arquivo .cdx do qual deseja excluir a tag de índice. Por exemplo, suponha que você tenha um arquivo .cdx não estrutural chamado QRTLYRPT.CDX contendo uma tag chamada Title. A linha de código a seguir exclui a tag Title: DELETE TAG Title OF QRTLYRPT Para excluir todas as tags no arquivo .cdx, use a cláusula ALL no comando DELETE TAG. Para obter mais informações, consulte DELETE TAG Command.

# Excluindo arquivos .idx independentes

Um arquivo de índice independente (.idx) contém somente uma única expressão de chave de índice; portanto, você pode excluir o índice excluindo o arquivo .idx.

### Para excluir um arquivo .idx independente
- Use o comando DELETE FILE. Por exemplo, suponha que você tenha um arquivo .idx independente chamado OrdDate.idx. A linha de código a seguir exclui o arquivo .idx: DELETE FILE OrdDate.idx Para obter mais informações, consulte DELETE FILE Command.

Você também pode usar o sistema operacional do computador para excluir o arquivo.
