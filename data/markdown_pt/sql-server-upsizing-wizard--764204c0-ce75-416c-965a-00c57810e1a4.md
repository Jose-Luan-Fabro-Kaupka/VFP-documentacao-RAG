# SQL Server Upsizing Wizard

O SQL Server Upsizing wizard cria um banco de dados SQL Server que duplica, tanto quanto possível, a funcionalidade do banco de dados Visual FoxPro.

> **Observação:** Para versões do SQL Server 6.5 e superiores, o wizard define o nível de compatibilidade como 6.5. Você pode precisar redefinir esse nível e fazer alterações adicionais após o upsizing.

Você pode criar um modelo de trabalho local da sua aplicação usando tabelas, views e bancos de dados Visual FoxPro para representar dados que eventualmente serão acessados em um servidor remoto. Quando estiver pronto para mover este protótipo para seu local de trabalho, você fará o upsizing. Você pode usar o SQL Server Upsizing wizard para:
 - Mover dados locais para um servidor remoto.
- Transformar tabelas base locais e views locais em tabelas base remotas e views remotas.
- Migrar uma aplicação local para uma aplicação cliente/servidor.

> **Observação:** O upsizing pode levar muito tempo, dependendo do tamanho dos seus dados, da quantidade de tráfego de rede e do número de demandas concorrentes sendo tratadas pelo seu servidor. Tabelas grandes podem exigir várias horas para upsizing.

Antes de executar o SQL Server Upsizing wizard, você deve preparar os lados cliente e servidor. Você deve ter certas permissões CREATE e SELECT no servidor e conexões nomeadas no cliente. Para obter mais informações, consulte SQL Server Upsizing Wizard Preparation.

Para acessar o SQL Server Upsizing wizard no menu Tools, escolha Wizards e clique em Upsizing.

# Etapa 1 - Selecionar banco de dados local

Na primeira etapa, você escolhe qual banco de dados local deseja fazer upsizing.
 **Database to upsize**
Lista os bancos de dados atualmente abertos. Selecione o banco de dados que deseja fazer upsizing. Se você não tiver um banco de dados aberto, escolha o botão Open para selecionar e abrir um banco de dados.

# Etapa 2 - Selecionar fonte de dados

Nesta etapa, você especifica opções para selecionar a fonte de dados ODBC SQL Server ou conexão nomeada que deseja usar.
 **ODBC data sources**
Escolha este botão de opção para exibir fontes de dados ODBC SQL Server. Quando selecionado, a lista adjacente é intitulada Available data sources.
**Connections**
Escolha este botão de opção para exibir conexões armazenadas no banco de dados aberto que se conectam a fontes de dados SQL Server. Quando selecionado, a lista adjacente é intitulada Existing connections.
**Available data sources**
Lista as fontes de dados ODBC que se conectam ao SQL Server. Esta lista é exibida quando o botão de opção ODBC data sources está selecionado.
**Existing connections**
Esta lista é exibida quando o botão de opção Connections está selecionado. Ela lista as conexões armazenadas no banco de dados aberto que se conectam a fontes de dados SQL Server.
**All**
Use esta caixa de seleção para exibir todas as fontes de dados que não são identificadas explicitamente com as palavras-chave "SQL Server" no título. As palavras "SQL Server" devem aparecer no nome da fonte de dados para o Visual FoxPro identificar a fonte de dados como uma fonte de dados SQL Server. Se sua fonte de dados usa um driver de terceiros para se conectar ao SQL Server, ela pode não ser identificada como uma fonte de dados SQL Server. A lista exibida depende de você ter o botão de opção ODBC data sources ou Connections selecionado.

Quando você clica em Next, o wizard conecta você ao SQL Server e exibe a caixa de diálogo SQL Server Login. Se você usou uma conexão nomeada com senha salva, o wizard faz seu logon no SQL Server selecionado sem solicitar informações de login ODBC.

### Usando uma conexão nomeada

Se você usa uma conexão nomeada para acessar sua fonte de dados, o SQL Server Upsizing wizard associa a conexão nomeada a quaisquer views remotas que cria durante o upsizing. Se a definição de conexão inclui uma senha, a opção Save Password With View (mais adiante na Etapa 8) é selecionada automaticamente para você e desabilitada; isso impede que a senha seja removida da definição de conexão.

### Usando uma fonte de dados

Se você usa um nome de fonte de dados em vez de um nome de conexão para fazer logon na fonte de dados, e escolhe que o wizard crie views remotas, o SQL Server Upsizing wizard cria uma conexão nomeada chamada "Upsize" (ou "Upsize2," "Upsize3," e assim por diante, se uma definição de conexão existir com o nome sugerido).

# Etapa 3 – Escolher tabelas

Nesta etapa, você pode selecionar as tabelas Visual FoxPro que deseja exportar para o SQL Server.
 **Available tables**
Lista todas as tabelas armazenadas no banco de dados que você escolheu para upsizing.
**Selected tables**
Lista as tabelas que você escolheu para upsizing no banco de dados no servidor. Você deve selecionar pelo menos uma tabela e pode escolher o botão >> para exportar todas as tabelas.

Quando você escolhe Next, o SQL Server Upsizing wizard lê a lista de tabelas que você selecionou para upsizing e tenta abrir essas tabelas para uso exclusivo no banco de dados que você escolheu para upsizing. Quaisquer tabelas que não possam ser abertas de forma exclusiva não estarão disponíveis para upsizing. As tabelas são abertas de forma exclusiva para impedir que outros usuários alterem os dados nas tabelas durante o processo de upsizing, o que ajuda a garantir a precisão dos dados exportados. Se alguma tabela já estiver aberta e compartilhada, o wizard fecha e depois reabre de forma exclusiva; isso pode fazer você perder quaisquer relações temporárias estabelecidas com os comandos SET RELATION ou SET SKIP.

### Escolhendo tabelas para exportar

É muito importante escolher as tabelas que você exporta com cuidado, pois essa escolha tem um impacto significativo no desempenho da sua aplicação. Exportar todas as tabelas pode resultar em consultas excessivas (e lentas) ao servidor. Um banco de dados cliente/servidor bem projetado geralmente consiste em uma mistura de tabelas locais e remotas.

Em geral, mantenha tabelas que mudam raramente ou com pouca frequência no seu banco de dados local, como uma tabela de nomes de estados e abreviações. Exporte tabelas que mudam frequentemente e são acessadas por muitos usuários, como uma tabela de pedidos.

O SQL Server Upsizing wizard exporta os nomes de campos, tipos de dados e dados da tabela. Para obter mais informações, consulte Planning Client/Server Applications e Optimizing Client/Server Performance.

# Etapa 4 - Mapear tipos de dados de campos

Nesta etapa, o Visual FoxPro exibe os mapeamentos de tipo de dados padrão usados para converter dados locais em dados remotos, conforme as tabelas são upsized para o servidor. Você pode escolher alterar esses mapeamentos padrão.

You cannot change the default mapping for a key field to a data type that prevents the field from being indexed. You can change the default mapping of a field that is part of an index key if you choose a data type that is indexable; however, you might want to change the data types for the other fields in the key to match. Visual FoxPro warns you if you change the default data type mapping for a field that is not a key field but is used in a Visual FoxPro index. If you make a mistake, click Default to reset the data types.
 **Table**
Selecione a tabela cujos campos você deseja mapear da lista de todas as tabelas que você escolheu para upsizing.
**Timestamp column**
Selecione esta caixa de seleção para adicionar uma coluna timestamp à versão do servidor da tabela. Se deseja aplicar isso a todas as tabelas, pode economizar tempo selecionando a caixa de seleção All Tables.
**Identity column**
Selecione esta caixa de seleção para adicionar uma coluna identity à versão do servidor da tabela. Se deseja aplicar isso a todas as tabelas, pode economizar tempo marcando a caixa de seleção All Tables.
**Default**
Escolha este botão para redefinir todas as configurações de campo da tabela para todos os campos na tabela selecionada de volta aos seus padrões. Este botão, em efeito, desfaz quaisquer alterações que você inseriu para uma tabela específica anteriormente na Etapa 4.
**Field Name**
Lista os campos contidos na tabela que você selecionou na caixa de listagem Table.
**FoxPro Type**
Lista o tipo de dados Visual FoxPro do campo.
**Server Type**
Lista o tipo de dados do servidor para o qual os dados Visual FoxPro neste campo serão mapeados quando a tabela for copiada para o servidor. Clique neste campo para exibir uma lista suspensa da qual você pode selecionar um tipo de dados de servidor diferente.
**Width**
Especifica a largura do campo.
**Precision**
Especifica a precisão decimal do campo, quando aplicável.

### Criando colunas Timestamp

Uma coluna timestamp do SQL Server contém um valor único, gerado pelo SQL Server, que é atualizado sempre que o registro do servidor é atualizado. Usar um campo timestamp em uma tabela remota atualizável pode aumentar o desempenho e a confiabilidade.

Se você atualiza campos usando os valores SQL WhereType do Visual FoxPro DB_KEYANDMODIFIED ou DB_KEYANDUPDATABLE, o Visual FoxPro deve verificar todos os campos modificados ou todos os campos atualizáveis para determinar se foram alterados por outro usuário. Como campos text ou image podem ter muitos megabytes de tamanho, comparar esses campos para alterações pode ser intensivo em rede e demorado, reduzindo o desempenho. A confiabilidade também pode ser afetada, porque converter o valor de um campo de ponto flutuante entre cliente e servidor pode fazer o valor parecer ter mudado quando não mudou.

Quando você adiciona um campo timestamp a uma tabela remota e atualiza usando o valor SQL WhereType DB_KEYANDTIMESTAMP, o Visual FoxPro usa apenas o valor no campo timestamp para determinar se um registro foi alterado antes de atualizá-lo. Como o Visual FoxPro pode comparar o valor no campo timestamp mais rapidamente do que pode avaliar os contextos de campos text ou image grandes, você pode aumentar o desempenho em dados remotos. No entanto, se você usa o valor SQL WhereType DB_KEYANDTIMESTAMP, qualquer alteração no registro remoto é reconhecida como um conflito de atualização, independentemente de o campo remoto alterado estar na lista de campos que você definiu como modificáveis na sua view remota.

Se você prefere atualizar campos usando os valores SQL WhereType do Visual FoxPro DB_KEYANDMODIFIED, pode melhorar o desempenho definindo a propriedade Compare Memo da view remota como false (.F.). Quando CompareMemo está definido como false, campos Memo são removidos da lista de campos da view remota comparados com os dados na linha do servidor remoto.

# Etapa 5 - Selecionar banco de dados de destino

Nesta etapa, você pode selecionar o banco de dados no servidor de fonte de dados para o qual deseja copiar tabelas.

Depois de conectar a um servidor e escolher uma fonte de dados, as tabelas que deseja fazer upsizing e o mapeamento de tipo de dados de campos, você pode usar um banco de dados existente ou criar um novo banco de dados como destino para seu banco de dados local upsized. Se você escolheu uma conexão nomeada anteriormente na Etapa 2, pode usar o banco de dados nomeado na conexão ou criar um novo banco de dados como destino.
 **Available databases on ' database name '**
Esta lista é exibida quando você seleciona o botão de opção Existing para adicionar tabelas Visual FoxPro a um banco de dados SQL Server existente. Selecione o banco de dados para o qual deseja copiar tabelas Visual FoxPro quando fizer upsizing.
**New database name**
Esta caixa de texto é exibida quando o botão de opção New está selecionado. Insira um nome para o novo banco de dados que deseja criar no servidor remoto para o qual está fazendo upsizing. O nome pode ter até 30 caracteres de comprimento e pode incluir letras, dígitos e os símbolos #, $ e _. Espaços não são permitidos.

Se você fizer upsizing para um banco de dados existente, o wizard pula para a Etapa 8.

Se você usa uma versão do Microsoft SQL Server posterior à 6.x, o wizard pula para a Etapa 8, quer você use um banco de dados existente ou crie um novo.

# Etapa 6 - Definir propriedades do banco de dados

Se você escolheu criar um novo banco de dados SQL Server anteriormente na Etapa 5, o wizard exibe esta etapa para ajudá-lo a selecionar o dispositivo e o tamanho do banco de dados. Você pode escolher criar seu novo banco de dados SQL Server em um dispositivo existente ou criar um novo dispositivo.

### Selecionando um dispositivo existente
 **Database device**
Exibe todos os dispositivos no SQL Server no qual você fez logon, incluindo dispositivos padrão. Selecione um dispositivo com espaço livre suficiente para seu banco de dados.
**Size**
Exibe o tamanho em megabytes do dispositivo de banco de dados selecionado na caixa de listagem Database Device adjacente.
**Free Space**
Exibe a quantidade de espaço livre restante no dispositivo de banco de dados selecionado na caixa de listagem Database Device.
**Database size**
Insira a quantidade de espaço, em megabytes, que deseja alocar para o novo banco de dados. O tamanho de um novo banco de dados deve ser de pelo menos dois megabytes, pois esse é o mínimo permitido pelo SQL Server.

#### Dispositivos padrão

Se um ou mais dispositivos foram definidos como dispositivos padrão no seu SQL Server, o SQL Server Upsizing wizard inclui uma entrada Default na lista de dispositivos disponíveis. A entrada Default pode representar mais de um dispositivo. Escolher o dispositivo padrão não garante que você terá espaço suficiente para fazer upsizing do seu banco de dados. O SQL Server Upsizing wizard verifica os dispositivos especificados como padrão para garantir que há espaço suficiente para o banco de dados.

> **Dica:** Para colocar seu banco de dados em vários dispositivos, torne esses dispositivos (e nenhum outro) dispositivos padrão. Quando executar o SQL Server Upsizing wizard, selecione Default para seu banco de dados.

Para obter mais informações sobre como definir o status padrão de dispositivos, consulte a documentação do SQL Server para uma descrição do procedimento de sistema sp_diskdefault.

### Criando um novo dispositivo

Se os dispositivos existentes estão muito cheios, você pode querer criar um novo dispositivo. Você deve ser administrador do sistema para criar novos dispositivos SQL Server.

 Para criar um novo dispositivo SQL Server
 - Selecione Create new device na lista de dispositivos. Se você é administrador do sistema, uma caixa de diálogo aparece. Caso contrário, uma mensagem de erro aparece.
- Digite um nome para o novo dispositivo. O nome do dispositivo deve ter 30 caracteres ou menos e consistir em letras, dígitos e os símbolos #, $ ou _. Espaços não são permitidos.
- Clique em OK. O novo nome do dispositivo é adicionado à caixa de listagem de dispositivos.
- Digite um tamanho de dispositivo. O tamanho do dispositivo deve ser de pelo menos dois megabytes. O tamanho combinado de novos dispositivos não pode exceder o espaço em disco disponível.

Se você é administrador do sistema, o SQL Server Upsizing wizard exibe a quantidade de espaço na unidade do servidor que armazena o banco de dados Master SQL Server.

> **Observação:** O tamanho de um dispositivo não pode ser alterado depois de definido. Certifique-se de criar dispositivos suficientemente grandes.

O novo dispositivo selecionado é criado depois que você escolhe o botão Finish. O SQL Server Upsizing wizard cria o novo dispositivo no mesmo diretório do dispositivo de banco de dados Master. Se você adicionar um novo dispositivo à lista, mas não selecionar o novo dispositivo como o dispositivo de banco de dados, o novo dispositivo não é criado.

O SQL Server Upsizing wizard pode gerar um relatório que inclui o nome lógico, nome físico e outras informações sobre novos dispositivos que você cria.

### Limitações de número de dispositivos

Todo dispositivo SQL Server recebe um número quando é criado. No entanto, o pool disponível de números de dispositivos é limitado. O valor padrão é 10, embora o número possa ser diferente no seu servidor. O SQL Server Upsizing wizard procura um número de dispositivo disponível. Se todos os números de dispositivos estiverem ocupados, você não poderá criar um novo dispositivo.

> **Observação:** Para aumentar o número de números de dispositivos SQL Server disponíveis, consulte a documentação do SQL Server para uma descrição do procedimento de sistema sp_configure.

# Etapa 7 - Especificar propriedades de log

Nesta etapa, você pode especificar o tamanho e o dispositivo para armazenar um log de transação. Um log de transação é criado para seu banco de dados pelo SQL Server e pode ser usado para reconstruir o banco de dados em caso de um problema grave do sistema.
 **Log Device**
Exibe uma lista de dispositivos de log no servidor remoto. Selecione o dispositivo que deseja usar para o log de transação. Idealmente, um banco de dados e seu log correspondente devem ser colocados em dispositivos que estão em discos físicos separados. Esses dispositivos devem ser criados antes de iniciar o SQL Server Upsizing wizard, pois o wizard cria todos os novos dispositivos no mesmo disco físico — o disco onde reside o dispositivo de banco de dados master. Se você tem apenas um disco físico, deve colocar o banco de dados e seu log em dispositivos separados, para poder usar o comando SQL server DUMP TRANSACTION.
**Size**
Exibe o tamanho em megabytes do dispositivo de banco de dados selecionado na caixa de listagem Log Device adjacente.
**Free Space**
Exibe a quantidade de espaço livre restante no dispositivo de log selecionado na caixa de listagem Log Device.
**Log Size**
Insira a quantidade de espaço, em megabytes, que deseja alocar para o log de transação. Para obter mais informações sobre como determinar o tamanho de log necessário, consulte Specifying Log Size mais adiante neste tópico.
**Database Size**
Exibe a quantidade de espaço alocada para o novo banco de dados na Etapa 6.

### Especificando tamanho de log

Como diretriz geral, você aloca de 10 a 20 por cento do tamanho do novo banco de dados SQL Server; esta diretriz depende de várias considerações discutidas na documentação do SQL Server.

Você pode inserir um valor de 0 para o tamanho do log, o que faz o wizard colocar o log (uma tabela chamada syslogs) no mesmo dispositivo do banco de dados. Quando o tamanho do log é definido como 0, o log consome a quantidade mínima de espaço no servidor, mas também enche muito rapidamente.

Quando você faz upsizing para um novo banco de dados, o SQL Server Upsizing wizard faz dump do log de transação sempre que ele enche. O dump faz uma cópia de backup de um banco de dados e seu log de transação em uma forma que pode ser lida com LOAD DATABASE. Para obter mais informações sobre o comando SQL Server DUMP TRANSACTION e sobre como estimar a quantidade de espaço a alocar para um log de transação, consulte a documentação do SQL Server.

> **Observação:** Você pode aumentar o tamanho de um log ou movê-lo para um novo dispositivo. Para obter mais informações, consulte a documentação do SQL Server para uma descrição do comando ALTER DATABASE e do procedimento de sistema sp_logdevice.

# Etapa 8 - Definir opções de upsizing

Nesta etapa, você pode controlar como o SQL Server Upsizing wizard exporta suas tabelas. Você também pode especificar as alterações que deseja que o SQL Server Upsizing wizard faça no banco de dados local. Você pode criar relatórios de upsizing, redirecionar views para usar dados remotos, criar novas views remotas em tabelas que são upsized e salvar senhas com views.

### Especificando atributos de tabela para upsizing

Por padrão, o SQL Server Upsizing wizard exporta a estrutura e os dados de uma tabela. Junto com nomes de campos e tipos de dados, você também pode exportar:
 - Índices
- Padrões
- Relações (restrições de integridade referencial)
- Regras de validação

O SQL Server Upsizing wizard pode exportar propriedades adicionais de tabela e criar colunas timestamp em certas tabelas SQL Server. O SQL Server Upsizing wizard também pode modificar seu banco de dados Visual FoxPro para que suas consultas, formulários e relatórios usem os dados nas suas novas tabelas SQL Server, em vez dos dados no banco de dados Visual FoxPro local.

Índices e padrões do Visual FoxPro tornam-se índices e padrões do SQL Server. Se você escolher exportar regras de validação, o SQL Server Upsizing wizard tenta exportar regras de validação em nível de campo e de linha para o SQL Server, onde se tornam stored procedures chamadas de triggers SQL Server. Relações de tabela exportadas também se tornam parte dos triggers.

> **Dica:** Se você exportar relações de tabela, certifique-se de exportar índices também ou pode experimentar desempenho medíocre.

### Atributos de tabela para upsizing
 **Indexes**
Selecione para fazer upsizing de índices .cdx do Visual FoxPro.
**Defaults**
Selecione para fazer upsizing de valores padrão para campos de tabela.
**Relationships**
Selecione para fazer upsizing de relações armazenadas no banco de dados que você está fazendo upsizing.
**Validation rules**
Selecione para fazer upsizing de regras de validação de campo e tabela.
**Structure only, no data**
Selecione para fazer upsizing da estrutura de tabela vazia, sem copiar dados da tabela para a fonte de dados SQL Server.
**Use declarative referential integrity**
Habilitado ao fazer upsizing para um banco de dados SQL Server versão 6.x. Selecione para criar restrições SQL para impor integridade referencial.
**Null Mapping**
Selecione os campos que podem aceitar .NULL. Esta opção ajuda a garantir que comandos insert e update contra dados remotos tenham sucesso. Esta opção permite substituir as configurações de null existentes nos campos das tabelas Visual FoxPro sendo upsized. Se você escolher a opção General and Memo fields, todos os campos general e memo nas suas tabelas Visual FoxPro selecionadas serão upsized com esses campos definidos para permitir nulls. Há diferenças em como comandos SQL do Visual FoxPro como INSERT e UPDATE afetam dados locais e remotos dependendo das configurações de null para campos. Por exemplo, se você tem um comando INSERT que não inclui todos os campos em uma tabela, o Visual FoxPro insere espaços em branco nos campos não especificados para dados locais. Se o comando INSERT é emitido para uma view remota (dados SQL Server), nulls são inseridos nos campos não especificados no comando. O comando falhará se qualquer um desses campos não suportar nulls. É bastante fácil escrever um comando INSERT que inclui todos os campos e valores a serem inseridos. Observe, no entanto, que inserir conteúdo em um campo general é um pouco mais trabalhoso.

### Alterações a fazer localmente
 **Create upsizing report**
Cria uma série de relatórios documentando os resultados do processo de upsizing.
**Redirect views to remote data**
Altera a definição de views locais no banco de dados que você está fazendo upsizing para views remotas que usam as tabelas de servidor upsized como tabelas base. Suas consultas, formulários e relatórios então usam views nos dados na nova fonte de dados SQL Server em vez dos dados Visual FoxPro originais.
**Create remote views on tables**
Quando você faz upsizing de uma tabela local, precisa de uma view remota para acessar a tabela upsized no servidor remoto. O SQL Server Upsizing wizard pode criar novas views remotas conforme você faz upsizing. Conforme o wizard cria novas views remotas, renomeia todas as versões locais de tabelas adicionando o sufixo "_local" ao nome da tabela. Observação Criar views remotas em tabelas conforme você faz upsizing não é recomendado, porque essas views não otimizadas selecionam todos os dados na tabela em vez de selecionar apenas as informações que sua aplicação precisa. O método preferido é criar views parametrizadas. Você pode criar uma view parametrizada local, que então faz upsizing escolhendo Redirect views to remote data, ou criar uma nova view remota parametrizada na tabela depois de concluir o processo de upsizing. Para obter mais informações, consulte How to: Create Parameterized Views.
**Save password with views**
Por padrão, você deve inserir sua senha e ID de login ao abrir uma view remota em uma nova sessão com o Visual FoxPro. Selecione esta opção para armazenar sua senha localmente com a definição da view remota no seu banco de dados. Observação Esta caixa de seleção é marcada automaticamente para você e desabilitada se você usou uma conexão nomeada anteriormente na Etapa 2 para acessar sua fonte de dados e essa conexão nomeada inclui uma senha. Isso impede que a senha seja removida da definição de conexão.

### Criando relatórios de upsizing

Quando você seleciona Create Upsizing Report, o Visual FoxPro gera relatórios de upsizing que documentam as tabelas, views, campos, índices e restrições de integridade referencial que o SQL Server Upsizing wizard cria no SQL Server. O wizard coloca os relatórios em um novo projeto, usando os seguintes nomes de relatório:
 - RptErrors
- RptField
- RptIndex
- RptRels
- RptTable
- RptViews

Os relatórios de upsizing incluem informações sobre quaisquer dispositivos e bancos de dados criados, informações sobre quaisquer erros encontrados durante o processo de upsizing e uma explicação completa da forma como cada objeto Visual FoxPro é mapeado para um objeto SQL Server. Você pode visualizar ou imprimir esses relatórios após a conclusão do upsizing.

### Fazendo upsizing de todas as tabelas usadas por uma view local

Se você faz upsizing de todas as tabelas usadas por uma view local, a view local é renomeada adicionando o sufixo "_local" ao nome da view local existente. O SQL Server Upsizing wizard cria uma nova view baseada na instrução SQL da view local, substituindo os nomes de tabelas remotas pelos nomes de tabelas locais. O KeyField e outras propriedades de atualização da view são preservadas.

### Fazendo upsizing de algumas das tabelas usadas por uma view local

Se você faz upsizing de apenas algumas das tabelas usadas por uma view local, o SQL Server Upsizing wizard não renomeia as views locais. Em vez disso, renomeia as tabelas Visual FoxPro que você exporta com o sufixo "_local." Por exemplo, se você exportar uma tabela chamada "Employees," a tabela é renomeada "Employees_local" no seu banco de dados. O wizard então cria uma view remota para cada uma das tabelas que você exportou. Cada view seleciona todos os campos e todos os registros da tabela remota.

> **Observação:** O Visual FoxPro trata dados locais e remotos de maneiras diferentes. O design de acesso a dados de uma aplicação usando dados locais pode se tornar muito ineficiente quando aplicado como está a dados remotos.

### Caixa de diálogo Advanced
 **Make Primary Key a Clustered Index**
Por padrão, tabelas que têm uma chave primária automaticamente recebem um índice clustered criado no SQL Server pelo Upsizing wizard. Isso ocorre porque é um padrão do SQL Server se a cláusula [CLUSTERED | NONCLUSTERED] não for especificada na instrução ALTER TABLE, que o wizard usa. Sendo que chaves primárias frequentemente já estão em ordem sequencial, um índice clustered pode não ser necessário. Esta opção permite controlar se um índice clustered é criado.
**Drop Local Tables**
Se você escolher criar views remotas para suas tabelas, o wizard criará um novo conjunto de views remotas usando os nomes de suas tabelas correspondentes (e renomeará as tabelas originais). É possível que você não precise mais usar as tabelas locais. Esta opção permite remover as tabelas locais do banco de dados.
**Default Remote View Name**
Se você escolher criar views remotas, pode querer controlar a nomenclatura dessas tabelas. Por padrão, o nome usado é o da tabela original (e a tabela original é renomeada). As seguintes opções permitem controlar a nomenclatura de views remotas. Prefix Especifica uma cadeia de caracteres para adicionar antes de cada um dos nomes de view remota recém-criados. Suffix Especifica uma cadeia de caracteres para adicionar ao final de cada um dos nomes de view remota recém-criados. None (Same as local table name.) Por padrão, usa o nome da tabela e renomeia a tabela original.

# Etapa 9 - Concluir

Nesta etapa, você pode escolher:
 - Fazer upsizing sem gerar código SQL.
- Apenas gerar código SQL para upsizing.
- Fazer upsizing e gerar código SQL.
 **Upsize**
Selecione para começar a criar bancos de dados e tabelas, conforme aplicável, no servidor remoto.
**Save generated SQL**
Selecione para que o upsizing wizard gere o script SQL necessário para fazer upsizing do seu banco de dados e depois pare sem começar a criar bancos de dados e tabelas no seu servidor remoto. Você pode usar esta opção para fornecer um script SQL de upsizing que então personaliza para atender às necessidades da sua aplicação. Depois de modificar e salvar o script SQL, você executa o script para concluir o processo de upsizing. Este processo em duas etapas fornece enorme flexibilidade, permitindo usar o Visual FoxPro para gerar a grande maioria do código que você precisará, mas fornecendo um método para ajustar finamente a instalação upsized.
**Upsize and save generate SQL**
Selecione para fazer upsizing do seu banco de dados e salvar o script SQL gerado pelo wizard.

A primeira e a terceira opções de upsizing estão disponíveis apenas se você tiver permissão CREATE TABLE no servidor. Se você escolher qualquer uma das opções que salvam código SQL gerado, todo o código SQL gerado pelo SQL Server Upsizing wizard é armazenado no seu disco rígido.

> **Observação:** O upsizing pode levar muito tempo, dependendo do tamanho dos seus dados, da quantidade de tráfego de rede e do número de demandas concorrentes sendo tratadas pelo seu servidor. Tabelas grandes podem exigir várias horas para exportar.

Para fazer upsizing do seu banco de dados, selecione a opção de upsizing desejada e escolha Finish.

O SQL Server Upsizing wizard cria dispositivos e bancos de dados se necessário e começa a exportar objetos Visual FoxPro para o SQL Server.
