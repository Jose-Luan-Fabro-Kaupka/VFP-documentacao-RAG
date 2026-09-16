# Assistente de Visualização Remota

Com este assistente, você pode criar visualizações usando dados remotos (ODBC). Você deve ter um banco de dados existente para armazenar sua visão, bem como uma fonte de dados existente ou conexão nomeada armazenada em um banco de dados. Se você não tem um banco de dados aberto, você é solicitado a selecionar um banco de dados existente ou criar um.

Antes de executar o assistente de Visualização Remota, você pode definir opções para visualização remota e padrões de conexão na guia Dados Remotos na caixa de diálogo Opções. Você pode criar conexões no designer Connection.

Para aceder ao assistente de Vista Remota
 - No menu Ferramentas, escolha Wizards e clique em Consultar .
- Na caixa de diálogo Seleção do Assistente, escolha Assistente de Visualização Remota .

# Passo 1 - Escolha a Fonte de Dados

Nesta etapa, você pode especificar, a partir de uma lista de fontes de dados disponíveis ODBC ou uma lista de conexões nomeadas, qual delas contém os dados de destino. Se a caixa estiver vazia, você deve definir suas fontes de dados e conexões no Microsoft Windows antes de executar o assistente. Você pode definir suas fontes de dados usando o painel de controle Fontes de Dados do painel de controle Ferramentas Administrativas. Se sua fonte de dados remota requer uma senha, você será solicitado para ele quando você clicar em Próximo.

Você também pode incluir tabelas de sistema para drivers ODBC que os suportam.

Depois de selecionar uma fonte de dados ODBC, você pode ver a caixa de diálogo Configurar conexão na qual você especifica se deve usar um banco de dados ou tabela livre, e a localização da tabela alvo.

# Passo 2 – Selecione campos

Nesta etapa, você especifica quais campos você deseja usar em sua visão remota.

Para selecionar os campos para sua visão
 - Use os controles Tabelas para localizar e selecionar a tabela que você deseja usar.
- Na caixa de campos disponíveis, selecione um ou mais campos que deseja usar na tabela selecionada e use os botões de seta para movê-los para a caixa de campos selecionados. Você pode usar campos de outras tabelas repetindo este processo. Você pode selecionar quantos campos você precisar e movê-los para a caixa de campos selecionados.

# Etapa 3 – Relacionar as Tabelas

Esta etapa mostra apenas se você selecionar campos de mais de uma tabela. Você pode especificar quais campos em cada tabela contêm as mesmas informações e pode governar a relação entre as tabelas, determinando assim os registros incluídos.

Selecione os campos desejados nas duas listas suspensas e, em seguida, escolha Adicionar. Se você usar várias tabelas em sua visão, então você deve relacionar as tabelas indicando quais campos contêm dados correspondentes em cada tabela.

Se um relacionamento não existe atualmente e o assistente não poderia sugerir campos para uma junção, você deve escolher os campos. Normalmente, as tabelas incluem campos para este fim e muitas vezes têm o mesmo nome.

# Passo 4 - Incluir Registros

Esta etapa mostra apenas se você selecionar campos de mais de uma tabela. Você pode especificar quais registros das tabelas selecionadas serão disponibilizados para o assistente Visão Remota.
** Apenas linhas correspondentes**
Retorna apenas registros de ambas as tabelas que correspondem à condição de comparação definida entre os dois campos na condição de junção. Isto é chamado de união interior.
** Todas as linhas desta tabela**
Devolve todas as linhas da tabela seleccionada. Isso torna possível para você criar uma junção externa esquerda ou direita. Para mais informações, consulte Como: Criar uma Vista Multitable .

# Passo 5 – Ordenar registros

Este passo permite que você especifique um ou mais campos para classificar os registros em sua visão remota.

Selecione até três campos ou índices para determinar a ordem em que os resultados da sua visualização serão ordenados. Se sua tabela já tiver um ou mais índices, você pode selecionar a tag index, que está listada abaixo dos campos, separada por uma linha, na janela de campos disponíveis. Selecione Ascendir para ordenar a view em ordem ascendente, ou Descendo para ordenar a view em ordem decrescente.

# Passo 6 - Registros de Filtros

Nesta etapa, você pode especificar uma condição de filtro, então apenas alguns dos registros que você escolheu para disponibilizar são usados na visão remota.

Para determinar a condição do filtro
 - Selecione um campo na lista suspensa do Campo.
- Especifique um operador, como igual ou contém, na caixa suspensa do Operador.
- Indique um valor na caixa de texto Valor. Por exemplo, se você quiser filtrar em uma cidade específica, como Helena, você pode escolher cidade na lista suspensa do Campo, escolher igual na lista suspensa do Operador e inserir Helena na caixa de texto Valor.

Você pode reduzir o número de registros criando expressões que filtram registros das tabelas ou visualizações selecionadas. Você pode criar duas expressões e conectá-las com E, que retorna apenas registros que cumprem ambos os critérios especificados, ou Ou, que retorna registros que atendem a ambos os critérios.

Você pode ver o resultado clicando no botão Preview.

# Passo 7 - Terminar

Nesta etapa, você pode escolher como lidar com a nova visão remota definida.
** Salvar visão remota**
Salva a visão remota recentemente definida e sai do assistente.
**Salvar visão remota e navegar**
Salva a nova visão remota e então a abre em uma janela Navegar, para que você possa rever os dados exibidos.
**Salve a visão remota e modifique-a no View Designer**
Salva a nova visão remota e, em seguida, modificá- la quando abrir no designer Ver.

# Veja Também
- Execução de ODBC Extensões para SQL
- ODBC Classe de Fundação de Registo
- Assistente do Tab Cross
- Assistente de Gráficos
- Assistente de Visualização Local
