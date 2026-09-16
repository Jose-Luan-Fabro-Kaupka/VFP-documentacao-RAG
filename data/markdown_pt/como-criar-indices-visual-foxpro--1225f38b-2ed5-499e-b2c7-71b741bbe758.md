# Como: criar índices (Visual FoxPro)

Você pode criar um índice para uma tabela ao definir um campo para ela ou depois de criar a tabela. Ao criar um índice, você fornece uma expressão, que pode conter nomes de campos da tabela, para especificar como os registros devem ser organizados. Também pode especificar uma expressão de filtro para que o Visual FoxPro adicione ao índice somente os registros que atendam aos critérios do filtro.

> **Dica:** Índices são fáceis de criar, mas afetam o desempenho; portanto, use moderação ao criá-los. Não é necessário definir um índice para cada campo. Índices usados raramente podem reduzir o desempenho.

Você pode criar um índice usando o Table Designer do Visual FoxPro ou programaticamente. Para obter informações sobre o uso de comandos do Visual FoxPro para criar índices, consulte Criando índices programaticamente.

> **Observação:** Depois de criar um índice, você precisa selecioná-lo para usá-lo com a tabela. Para obter mais informações, consulte Como: definir índices de controle.

### Para criar um índice usando o Table Designer
- Abra o Table Designer para modificar a tabela.
- No Table Designer, escolha a guia Indexes.
- Na caixa Name, digite um nome para a marca de índice.
- Na lista Type, escolha o tipo de índice desejado.
- Na caixa Expression, digite o nome do campo que deseja usar para organizar os registros. -OU- Crie uma expressão de índice clicando no botão de reticências (...) à direita da caixa. Observação: ao especificar uma expressão de índice para índices binários, você deve especificar uma expressão lógica que não seja avaliada como valor nulo. Se a expressão de índice for alterada de forma a conter ou ser avaliada como um valor nulo, o Visual FoxPro gerará um erro.
- Escolha OK.

Para obter mais informações sobre tipos de índice, consulte Tipos de índice do Visual FoxPro.

Para considerações sobre expressões de índice, consulte Criação de índices com base em expressões e Considerações para criar expressões de índice.

Você pode adicionar um filtro ao índice para selecionar somente os registros que correspondam à expressão de filtro fornecida. Para obter mais informações, consulte Como: filtrar dados.

Ao criar um índice para uma tabela, o Visual FoxPro cria automaticamente um arquivo de índice composto estrutural (.cdx) para armazená-lo. Esse arquivo .cdx estrutural tem o mesmo nome da tabela e é aberto automaticamente quando a tabela é aberta. Para obter mais informações sobre arquivos de índice, consulte Arquivos de índice do Visual FoxPro.

> **Dica:** Por padrão, o Visual FoxPro exibe registros em ordem crescente. Você pode especificar a exibição em ordem decrescente ao criar o índice ou depois de criá-lo. Para obter mais informações, consulte Como: exibir registros em ordem decrescente.

Ao trabalhar com registros em tabelas, talvez seja necessário acessá-los em ordens diferentes. Por exemplo, você pode querer organizar uma tabela de clientes pelo nome do contato para encontrar rapidamente o nome desejado ou pelo código postal para gerar etiquetas de correspondência previamente ordenadas para uma postagem eficiente. Você pode criar e armazenar diferentes cenários de ordenação para tabelas criando vários índices para a mesma tabela.

# Criando índices programaticamente

Você pode criar índices em arquivos de índice composto estrutural (.cdx) usando a linguagem Visual FoxPro. Pode criar um índice ao criar uma tabela usando o comando SQL CREATE TABLE ou criar um índice para uma tabela existente usando o comando SQL ALTER TABLE ou o comando INDEX.

> **Observação:** Para criar um índice primário, use os comandos SQL CREATE TABLE ou ALTER TABLE. Não é possível usar o comando INDEX para criar índices primários.

### Para criar um índice em um arquivo .cdx estrutural ao criar uma tabela
- Use o comando SQL CREATE TABLE para especificar um nome e campos para a tabela.
- Para criar um índice primário, inclua a cláusula PRIMARY KEY no campo correspondente que deseja usar. -OU- Para criar um índice candidato, inclua a cláusula UNIQUE. Observação: incluir a cláusula UNIQUE não é o mesmo que especificar um índice exclusivo. -OU- Para todos os outros índices, inclua a cláusula FOREIGN KEY.

### Para criar um índice em um arquivo .cdx estrutural para uma tabela existente
- Use o comando SQL ALTER TABLE para especificar um nome e campos para a tabela.
- Para criar um índice primário, inclua a cláusula PRIMARY KEY ou ADD PRIMARY KEY no campo correspondente que deseja usar. -OU- Para criar um índice candidato, inclua a cláusula ADD UNIQUE. -OU- Para todos os outros índices, inclua a cláusula ADD FOREIGN KEY.

Por exemplo, usando a tabela Customer do banco de dados de exemplo TestData do Visual FoxPro, você pode usar qualquer um dos comandos a seguir para atribuir o campo Cust_ID como chave primária da tabela Customer:

```foxpro
ALTER TABLE Customer ADD PRIMARY KEY Cust_ID TAG Cust_ID
ALTER TABLE Customer ALTER COLUMN Cust_ID c(5) PRIMARY KEY
```

Para obter mais informações, consulte Comando CREATE TABLE - SQL, Comando ALTER TABLE - SQL e Comando INDEX.

Você também pode criar índices em arquivos .cdx estruturais copiando de um ou mais arquivos de índice independentes (.idx) com o comando COPY INDEXES e omitindo a cláusula TO.

### Para criar um índice em um arquivo .cdx estrutural a partir de um arquivo .idx
- Use o comando COPY INDEXES para especificar um ou mais nomes de arquivos .idx. Para incluir cada chave de índice de todos os arquivos .idx abertos, use a palavra-chave ALL.
- Omita a cláusula TO.

Para obter mais informações, consulte Comando COPY INDEXES.
