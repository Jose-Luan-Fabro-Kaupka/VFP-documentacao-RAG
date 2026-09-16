# Como: criar índices usados com menos frequência

Se você deseja criar um índice que usa com pouca frequência, por exemplo, para uma finalidade especial, pode armazená-lo em arquivos de índice composto não estruturais (.cdx), que podem conter vários índices. Incluído para compatibilidade com versões anteriores, você também pode armazenar um único índice temporário ou usado com menos frequência em um arquivo de índice autônomo (.idx). Para obter mais informações sobre arquivos de índice para armazenar índices usados com pouca frequência, consulte Visual FoxPro Index Files.

Você pode criar índices em arquivos .cdx não estruturais e arquivos .idx autônomos usando a linguagem Visual FoxPro.

# Índices em arquivos de índice composto não estruturais

Para uma tabela existente, você pode criar um índice em um arquivo .cdx não estrutural usando o comando INDEX com as cláusulas TAG e OF ou copiando de um ou mais arquivos de índice autônomos (.idx) usando o comando COPY INDEXES.

### Para criar um índice em um arquivo de índice .cdx não estrutural
- Use o comando INDEX para especificar uma expressão de índice.
- Inclua a cláusula TAG para especificar o nome, ou tag, do índice.
- Inclua a cláusula OF para especificar o nome do arquivo .cdx não estrutural.

Por exemplo, o código a seguir abre a tabela Employee no banco de dados de exemplo TestData do Visual FoxPro e cria um índice com base no campo Title. O comando INDEX inclui a cláusula TAG para especificar um nome, ou tag, para o índice e a cláusula OF para armazenar o índice em um arquivo .cdx não estrutural chamado QRTLYRPT com a extensão de arquivo .cdx:

```foxpro
OPEN DATABASE (HOME(2) + 'Data\TestData')
USE Employee
INDEX ON Title TAG Title OF QRTLYRPT
```

Para obter mais informações, consulte OPEN DATABASE Command, USE Command e INDEX Command.

### Para criar um índice em um arquivo .cdx não estrutural a partir de um arquivo .idx
- Use o comando COPY INDEXES para especificar um ou mais nomes de arquivos .idx. Para incluir cada chave de índice de todos os arquivos .idx abertos, use a palavra-chave ALL.
- Inclua a cláusula TO para especificar o nome do arquivo .cdx não estrutural.

Para obter mais informações, consulte COPY INDEXES Command.

# Índices em arquivos de índice autônomos

Para uma tabela existente, você pode criar um índice de chave única em um arquivo .idx autônomo usando o comando INDEX com a cláusula TO ou copiando um índice de um arquivo de índice composto (.cdx) usando o comando COPY TAG.

> **Dica:** Para criar um arquivo de índice pequeno e de acesso rápido, inclua a cláusula COMPACT. No entanto, para criar um arquivo .idx compatível com os formatos de índice do FoxBASE+® e do FoxPro® versão 1.0, omita a cláusula COMPACT.

> **Observação:** Por padrão, arquivos .cdx são sempre compactos.

### Para criar um índice de chave única
- Use o comando INDEX para especificar a expressão de índice.
- Inclua a cláusula TO para especificar o nome do arquivo .idx.
- Inclua a cláusula COMPACT.

Por exemplo, o código a seguir abre a tabela Orders no banco de dados de exemplo TestData do Visual FoxPro e cria um índice com base no campo Order_Date. A cláusula TO especifica OrdDate como o nome do arquivo .idx. O comando SET ORDER define a ordem da tabela para o arquivo OrdDate, e o comando BROWSE abre uma janela browse que exibe os registros organizados pelo campo Order_Date:

```foxpro
OPEN DATABASE (HOME(2) + 'Data\TestData')
USE Orders
INDEX ON Order_Date TO OrdDate COMPACT
SET ORDER TO OrdDate
BROWSE
```

Para obter mais informações, consulte OPEN DATABASE Command, USE Command, INDEX Command, SET ORDER Command e Browse Window.

Você também pode criar um índice autônomo a partir de um índice em um arquivo .cdx usando o comando COPY TAG.

### Para criar um índice de chave única a partir de um arquivo .cdx
- Use o comando COPY TAG para especificar o nome do índice no arquivo .cdx.
- Se necessário, inclua a cláusula FROM para especificar o nome do arquivo .cdx.
- Inclua a cláusula TO para especificar o nome do arquivo .idx.
- Inclua a cláusula COMPACT.

Por exemplo, suponha que um dos índices em um arquivo .cdx estrutural seja usado apenas para relatórios trimestrais ou anuais. Você pode transferir esse índice do arquivo .cdx para um arquivo .idx. O código a seguir abre a tabela Employee no banco de dados de exemplo TestData do Visual FoxPro e cria um índice de chave única com base no índice chamado Birth_Date no arquivo .cdx estrutural associado à tabela Employee. O índice de chave única é armazenado em um arquivo .idx chamado BirthDate.

```foxpro
OPEN DATABASE (HOME(2) + 'Data\TestData')
USE Employee
COPY TAG Birth_Date TO BirthDate COMPACT
```

> **Observação:** Quando uma tabela está aberta, qualquer arquivo .cdx estrutural associado também está aberto.

> **Dica:** Depois de criar o arquivo .idx a partir do arquivo .cdx, você deve excluir a tag do arquivo .cdx. Para obter mais informações sobre a exclusão de índices, consulte How to: Delete Indexes (Visual FoxPro) .

Para obter mais informações, consulte OPEN DATABASE Command, USE Command e COPY TAG Command.
