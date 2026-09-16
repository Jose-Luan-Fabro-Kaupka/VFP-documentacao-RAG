# Como: Resolver SQL Erros de Assistente de Atualização do Servidor

Se ocorrer algum erro enquanto o SQL Assistente de Upsizing do servidor está exportando dados, você é perguntado se deseja salvar informações de erro. Se você optar por salvar informações de erro, um relatório de erro é gerado.

A maioria dos erros de atualização ocorre porque não há espaço suficiente no banco de dados ou dispositivo de registro do seu servidor, ou porque seu banco de dados remoto não é grande o suficiente para aceitar os dados que você está exportando para o servidor. Certifique-se de que você seleciona dispositivos com amplo espaço livre e que você define o tamanho do seu banco de dados suficientemente alto. Alguns erros ocorrem devido a permissões de login inadequadas.

# Base de Dados ou Registo Completo

The SQL Server Upsizing wizard runs out of space and stops if the SQL database you selected or created is too small. To resolve this problem, you can increase the space for the database or the log. This solution can involve dropping (removing) the database or the log from the upsizing process.

## # Para aumentar o espaço para um novo banco de dados ou log
- Larga a base de dados.
- Se o SQL Assistente de Upsizing do servidor mudou os nomes de quaisquer tabelas locais, restaurar tabelas para seus nomes originais por: Copiar sua versão de backup do arquivo .dbc do seu banco de dados local para o seu sistema, sobrescrever o arquivo .dbc alterado. - Ou... Renomeando tabelas locais para seus nomes originais.
- Quando você executar o assistente novamente, especifique um banco de dados maior ou tamanho de log.

## # Para aumentar o espaço para um banco de dados existente
- Aumenta o tamanho da base de dados.
- Se o SQL Assistente de Upsizing do servidor mudou os nomes de qualquer tabela local, renomeando-os para seus nomes originais. Copiar sua versão de backup do arquivo .dbc do seu banco de dados local para o seu sistema, sobrescrever o arquivo .dbc alterado. - Ou... Renomeando tabelas locais para seus nomes originais.
- Passa o feiticeiro outra vez.

## # Para aumentar o espaço para um log existente
- Aumenta o tamanho do tronco. - Ou... Descartar o registo de transacções.
- Se o SQL Assistente de Upsizing do servidor mudou os nomes de quaisquer tabelas locais, renomeando-as com seus nomes originais. Copiar sua versão de backup do arquivo .dbc do seu banco de dados local para o seu sistema, sobrescrever o arquivo .dbc alterado. - Ou... Renomeando tabelas locais para seus nomes originais.
- Passa o feiticeiro outra vez.

Você deve sobrescrever tabelas da atualização parcial anterior para garantir que todas as relações de tabela são criadas.

For information on increasing the database or log size, see the ALTER DATABASE command in your SQL Server documentation. For information on dumping the transaction log, see the DUMP TRANSACTION command in your SQL Server documentation.

Dispositivo Completo

O dispositivo no qual está localizado um banco de dados ou log pode preencher. Você pode estender o banco de dados ou log para outro dispositivo usando o comando ALTER DATABASE ou SQL Administrador do servidor, ou você pode criar um dispositivo maior.

Para criar um dispositivo maior
- Larga o dispositivo.
- Reiniciar SQL Servidor.
- Criar um dispositivo maior. Cuidado Ao soltar um dispositivo, apaga todos os bancos de dados e registros no dispositivo, não apenas o banco de dados para o qual você está atualizando.

Você pode usar o procedimento do sistema sp dropdevice para soltar um dispositivo. Para mais informações, consulte seu SQL Documentação do servidor.

Nível de compatibilidade inadequado para aumentar

To upsize a database, Visual FoxPro sets the compatibility level of the target SQL database to 6.5 by calling the SP_DBCMPTLEVEL stored procedure on SQL Server. Make sure the SQL login you are using has the appropriate rights to perform this action.

## # Para ter certeza que o login SQL tem direitos apropriados
- Verifique se o login que você está usando tem as permissões como uma das seguintes: DBO Membro da função de servidor fixo do sysadmin DB_OWNER

Veja também
- SQL Server Upsizing Wizard
- Como SQL Assistente de Atualização do Servidor Funciona
- Wizards (Visual FoxPro)
- Upsizing Visual FoxPro Databases
