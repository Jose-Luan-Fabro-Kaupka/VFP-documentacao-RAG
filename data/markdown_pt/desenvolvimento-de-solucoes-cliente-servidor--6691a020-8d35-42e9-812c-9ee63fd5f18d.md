# Desenvolvimento de soluções cliente/servidor

Você pode usar o Visual FoxPro como front-end para desenvolver aplicativos cliente/servidor robustos. O Visual FoxPro combina o suporte de nível superior de views atualizáveis de dados do servidor com acesso direto à sintaxe nativa do servidor usando SQL pass-through. Isso fornece uma base sólida sobre a qual construir soluções cliente/servidor versáteis. Um dicionário de dados completo, views locais e remotas, suporte a nulos, transações, suporte a aplicativos internacionais e acesso a fontes de dados ODBC contribuem para os recursos que você precisa para desenvolvimento cliente/servidor.

# Aumentando o desempenho cliente/servidor

Você pode aumentar o desempenho do seu aplicativo cliente/servidor usando as propriedades e o driver ODBC fornecidos no Visual FoxPro.

# Controlando o desempenho com propriedades

Você pode aumentar o desempenho usando as seguintes propriedades de cursor e view remota:
 - CompareMemo
- FetchAsNeeded
- Prepared

Você pode exibir essas propriedades usando as funções DBGETPROP( ) Function e CURSORGETPROP( ) Function, ou definir as propriedades com as funções DBSETPROP( ) Function e CURSORSETPROP( ) Function.

Incluir ou excluir campos Memo na detecção de atualização Você pode usar a propriedade CompareMemo para controlar quando campos memo são usados para detectar conflitos de atualização. Esta propriedade de view e cursor determina se campos memo (tipos M ou G) são incluídos na cláusula WHERE de atualização. A configuração padrão, True (.T.), significa que campos memo são incluídos na cláusula WHERE. Se você definir esta propriedade como False (.F.), campos memo não participam da cláusula WHERE de atualização, independentemente das configurações de UpdateType.

A detecção de conflito otimista em campos Memo é desabilitada quando CompareMemo está definida como False (.F.). Para detecção de conflito em valores memo, CompareMemo deve estar definida como True (.T.).

Ajuste fino da busca de registros Use a propriedade FetchAsNeeded para especificar se todas as linhas são buscadas progressivamente ou apenas aquelas dentro do conjunto de linhas determinado pela propriedade FetchSize. Se você deseja buscar todas as linhas no conjunto de resultados usando o loop ocioso do Visual FoxPro, use a configuração padrão, False (.F.). Se você deseja buscar somente quando o usuário rolar além do conjunto de linhas determinado pela propriedade FetchSize, defina FetchAsNeeded como True (.T.) para buscar o próximo conjunto de linhas.

Acelerar operações de reconsulta em views parametrizadas Usando a propriedade Prepared, você pode definir se a consulta da view é preparada antes de ser executada. Se você definir esta propriedade como True (.T.), o Visual FoxPro envia uma solicitação ao driver ODBC para preparar ou compilar a consulta SQL que define a view. Se o driver ODBC da sua fonte de dados de back-end suportar o uso de instruções preparadas, reconsultas subsequentes na view aberta são executadas mais rapidamente.

# Definindo regras com o dicionário de dados

Os bancos de dados do Visual FoxPro (.dbc files) fornecem um dicionário de dados que permite adicionar regras, views, triggers, relacionamentos persistentes e conexões a cada tabela em um banco de dados.

Em um banco de dados você pode definir:
 - Regras em nível de campo ou registro que o Visual FoxPro impõe onde a tabela é usada em um aplicativo.
- Chaves de índice primário e candidato.
- Views locais e remotas.
- Triggers.
- Relacionamentos persistentes entre tabelas de banco de dados.
- Conexões a fontes de dados remotas.
- Procedimentos armazenados.
- Valores padrão em campos.
- Nomes longos de tabela e campo.

Além disso, você pode impor integridade referencial para cada relacionamento persistente usando o Referential Integrity Builder para definir regras para inserções, atualizações e exclusões.

O Visual FoxPro também suporta valores nulos em tabelas, melhorando muito a compatibilidade e conectividade com outras fontes de dados, como Microsoft Access, Visual Basic e servidores baseados em SQL. Para detalhes sobre valores nulos, pesquise por "null" e "null values".

Cada banco de dados do Visual FoxPro é completamente extensível pelo usuário, com acesso por meio de aprimoramentos de linguagem e designers visuais. Para obter mais informações sobre bancos de dados e dicionários de dados, consulte Developing Databases.

Visualizar dados locais, remotos e offline Você pode projetar e testar um aplicativo cliente/servidor no seu computador local usando dados de views remotas, locais ou heterogêneas de várias tabelas. Views locais usam tabelas no seu computador local em vez de tabelas em um servidor remoto, e views de várias tabelas usam dados relacionados de tabelas separadas. Você pode criar views parametrizadas para minimizar a quantidade de dados que você baixa do servidor, levar os dados em viagem ou atualizar dados remotos do seu aplicativo Visual FoxPro. Para obter mais informações sobre views, consulte Working with Views (Visual FoxPro).

Gerenciar acesso compartilhado com transações Você pode projetar seu aplicativo para fornecer acesso compartilhado a dados. O acesso compartilhado envolve compartilhar dados entre usuários e restringir o acesso quando necessário. Transações e buffering — pessimista ou otimista, em nível de registro ou tabela — significam menos programação para você. Processamento em lote integrado e controle detalhado sobre o tratamento de conflitos de atualização simplificam a atualização de dados em um ambiente multiusuário. Para detalhes sobre como projetar seu aplicativo para acesso compartilhado, consulte Programming for Shared Access.

Desenvolver aplicativos internacionais O Visual FoxPro fornece várias áreas de suporte para desenvolver aplicativos internacionais. Por exemplo, o Visual FoxPro suporta várias páginas de código. As páginas de código para grego e russo são suportadas em plataformas MS-DOS, Microsoft Windows e Macintosh. O Visual FoxPro também suporta conjuntos de caracteres de byte duplo para idiomas como japonês, coreano, chinês tradicional e chinês simplificado; no entanto, Unicode não é suportado. O Visual FoxPro suporta sequências de ordenação para idiomas como japonês, alemão, chinês tradicional e islandês. Para obter mais informações sobre aplicativos internacionais, consulte Developing International Applications.

Implementar um aplicativo cliente/servidor Além de usar views para desenvolvimento cliente/servidor, você pode enviar qualquer sintaxe nativa de servidor que desejar diretamente a um servidor com as funções SQL pass-through do Visual FoxPro. Essas funções permitem acesso e controle adicionais ao servidor além da capacidade das views. Para detalhes sobre SQL pass-through, consulte Enhancing Applications Using SQL Pass-Through Technology.

Depois de projetar seu aplicativo localmente, você pode fazer upsizing e implementá-lo contra uma fonte de dados de back-end. O upsizing aplica os benefícios da arquitetura cliente/servidor ao aplicativo local e permite criar um banco de dados de servidor remoto com a mesma estrutura de tabela e dados das tabelas Visual FoxPro originais. Quando você faz upsizing, escolhe quais tabelas vão para o servidor e quais permanecem localmente para acesso mais imediato. Para detalhes sobre upsizing, consulte Upsizing Visual FoxPro Databases.
