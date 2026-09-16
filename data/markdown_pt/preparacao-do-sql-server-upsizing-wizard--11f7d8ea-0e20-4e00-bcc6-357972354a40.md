# Preparação do SQL Server Upsizing Wizard

Antes de executar o SQL Server Upsizing Wizard, você deve preparar os lados cliente e servidor.

# Preparando o lado do SQL Server

Antes da migração, você deve garantir que possui as permissões necessárias no servidor, estimar o tamanho do banco de dados e verificar se o servidor tem espaço em disco suficiente. Também há preparações especiais para migrar para vários discos ou dispositivos.

### Verificando o espaço livre em disco

Verifique se há espaço em disco suficiente no servidor.

> **Cuidado:** Se o SQL Server Upsizing Wizard ficar sem espaço em disco no servidor, ele será interrompido, deixando um banco de dados parcial e quaisquer dispositivos que tenha criado no servidor. Você pode remover dispositivos, bancos de dados e tabelas com a ferramenta SQL Server Administration.

### Definindo permissões em bancos de dados do SQL Server

Para executar o SQL Server Upsizing Wizard, você deve ter determinadas permissões no servidor SQL para o qual fará a migração. As permissões necessárias dependem das tarefas que deseja realizar.
 - Para migrar para um banco de dados existente, você precisa das permissões CREATE TABLE e CREATE DEFAULT.
- Para criar um novo banco de dados, você precisa das permissões CREATE DATABASE e SELECT nas tabelas de sistema do banco de dados master.
- Para criar novos dispositivos, você deve ser administrador do sistema.

Para obter mais informações sobre a concessão de permissões de servidor, consulte a documentação do SQL Server.

### Estimando o tamanho do banco de dados e dos dispositivos do SQL Server

Ao criar um novo banco de dados, o SQL Server Upsizing Wizard solicita que você selecione dispositivos para o banco de dados e o log. Ele também solicita que você defina o tamanho do banco de dados e dos dispositivos.

### Estimando o tamanho do banco de dados do SQL Server

Quando o SQL Server cria um banco de dados, ele reserva uma quantidade fixa de espaço para esse banco de dados em um ou mais dispositivos. Nem todo esse espaço é necessariamente usado pelo banco de dados — o tamanho do banco de dados apenas limita quanto ele pode crescer antes de ficar sem espaço.

> **Observação:** Você pode aumentar o tamanho de um banco de dados do SQL Server após sua criação. Para obter mais informações, consulte o comando ALTER DATABASE na documentação do SQL Server.

Para estimar o espaço necessário para o banco de dados, calcule o tamanho total dos arquivos .dbf do Visual FoxPro das tabelas que deseja migrar, acrescido da taxa de crescimento do novo banco de dados do SQL Server. Em geral, cada megabyte de dados do Visual FoxPro requer pelo menos 1,3 a 1,5 MB no SQL Server.

Se houver bastante espaço em disco no servidor, multiplique por dois o tamanho das tabelas do Visual FoxPro. Isso garante que o SQL Server Upsizing Wizard tenha espaço suficiente para migrar o banco de dados e também deixa alguma margem para crescimento. Se você espera adicionar muitos dados ao banco de dados, aumente o multiplicador.

### Estimando o tamanho dos dispositivos do SQL Server

Todos os bancos de dados e logs do SQL Server são colocados em dispositivos. Um dispositivo é tanto um local lógico no qual bancos de dados e logs são colocados quanto um arquivo físico. Quando um dispositivo é criado, o SQL Server cria um arquivo, reservando assim uma quantidade definida de espaço em disco para uso próprio.

O SQL Server Upsizing Wizard exibe a quantidade de espaço livre disponível nos dispositivos existentes do SQL Server. Selecione um dispositivo que tenha pelo menos espaço livre suficiente para o tamanho estimado do banco de dados.

Se nenhum dispositivo existente tiver espaço livre suficiente, você poderá usar o SQL Server Upsizing Wizard para criar um novo dispositivo. Novos dispositivos devem ser pelo menos tão grandes quanto o tamanho estimado do banco de dados. Se possível, torne o dispositivo maior que o banco de dados para poder expandi-lo posteriormente ou colocar outros bancos de dados ou logs no mesmo dispositivo.

> **Observação:** O tamanho do dispositivo não pode ser alterado. Certifique-se de criar dispositivos suficientemente grandes.

### Usando vários discos ou dispositivos do SQL Server

Na maioria dos casos, o SQL Server Upsizing Wizard fornece controle mais que suficiente sobre os dispositivos do SQL Server. Entretanto, se o servidor tiver vários discos ou se você quiser colocar um banco de dados ou log em vários dispositivos, talvez seja conveniente criar os dispositivos antes de executar o SQL Server Upsizing Wizard.

### Servidores com vários discos físicos

Se o servidor tiver mais de um disco rígido físico, talvez seja conveniente colocar o banco de dados em um disco e o log em outro. Em caso de falha de disco, haverá maior probabilidade de recuperar o banco de dados se o log e o banco de dados estiverem armazenados em discos físicos diferentes.

O SQL Server Upsizing Wizard permite criar novos dispositivos, mas somente em um disco físico — o mesmo disco do dispositivo do banco de dados Master.

Para colocar o banco de dados e o log em discos separados, verifique se há dispositivos suficientemente grandes em ambos os discos e crie novos dispositivos, se necessário. Em seguida, execute o SQL Server Upsizing Wizard.

### Colocando bancos de dados ou logs em vários dispositivos

O SQL Server permite que bancos de dados e logs se estendam por vários dispositivos. Entretanto, o SQL Server Upsizing Wizard permite especificar apenas um dispositivo para o banco de dados e um para o log.

Se quiser especificar vários dispositivos para um banco de dados ou log, torne esses dispositivos (e nenhum outro) os dispositivos padrão. Em seguida, execute o SQL Server Upsizing Wizard e escolha Default para o dispositivo do banco de dados ou do log.

> **Observação:** Se o tamanho do novo banco de dados ou log do SQL Server não exigir o uso de todos os dispositivos padrão, o SQL Server usará somente os dispositivos necessários para comportar o banco de dados ou o log.

# Preparando o cliente

Antes da migração, você deve ter acesso a um SQL Server por meio de uma fonte de dados ODBC ou conexão nomeada. Também deve ter um banco de dados do Visual FoxPro, do qual é recomendável fazer backup antes de executar o SQL Server Upsizing Wizard.

### Criando uma fonte de dados ODBC ou conexão nomeada

Ao criar um novo banco de dados remoto, você seleciona uma fonte de dados ODBC ou conexão nomeada no banco de dados do Visual FoxPro que acessa o SQL Server para o qual deseja migrar. Como não é possível prosseguir pelo Upsizing Wizard até selecionar uma conexão nomeada ou fonte de dados, você deve criar a conexão nomeada ou fonte de dados apropriada antes de iniciar o processo de migração.

Para obter informações sobre como criar uma conexão nomeada, consulte Como: definir conexões com fontes de dados remotas. Se quiser criar uma fonte de dados ODBC, execute o ODBC Administrator. Para obter informações sobre como configurar fontes de dados ODBC, consulte Como: configurar uma fonte de dados ODBC.

# Fazendo backup do banco de dados

É recomendável criar uma cópia de backup do banco de dados (arquivos .dbc, .dct e .dcx) antes da migração. Embora o SQL Server Upsizing Wizard não modifique arquivos .dbf, ele opera diretamente no .dbc, às vezes abrindo-o como uma tabela, e indiretamente, renomeando tabelas e exibições ao criar novas exibições remotas. Se você fizer backup do banco de dados, poderá revertê-lo ao estado original anterior à migração substituindo os arquivos .dbc, .dct e .dcx migrados pelas cópias de backup originais, o que desfaz a renomeação e a criação de novas exibições.

# Fechando tabelas

O SQL Server Upsizing Wizard tenta abrir exclusivamente todas as tabelas do banco de dados a ser migrado; se alguma tabela já estiver aberta e compartilhada, o assistente a fechará e reabrirá exclusivamente. Abrir tabelas exclusivamente antes da migração evita que outros usuários tentem modificar registros nas tabelas que estão sendo exportadas durante a exportação de dados. Se alguma tabela não puder ser aberta exclusivamente, o SQL Server Upsizing Wizard exibirá uma mensagem; essas tabelas não estarão disponíveis para migração.
