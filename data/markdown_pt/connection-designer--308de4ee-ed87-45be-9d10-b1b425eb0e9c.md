# Connection Designer

Permite criar e modificar conexões nomeadas. Para obter mais informações, consulte How to: Define Connections to Remote Data Sources.

O Connection Designer está disponível somente quando um banco de dados está aberto, porque as conexões são armazenadas como parte de um banco de dados.

# Specify Datasource
 **Data Source , Userid , Password**
Especifica que o Visual FoxPro exiba as três caixas a seguir: Data Source Permite escolher uma fonte de dados na lista de fontes de dados ODBC instaladas. Userid Permite inserir um nome de usuário ou ID se a fonte de dados exigir um. Password Permite inserir uma senha se a fonte de dados exigir uma. Database Permite escolher um banco de dados para o qual a fonte de dados selecionada se conectará.
**Connection String**
Especifica que o Visual FoxPro exiba a caixa de texto Connect String na qual você digita uma cadeia de conexão. Escolher o botão de diálogo exibe a caixa de diálogo Select Connection or Data Source, permitindo selecionar uma fonte de dados de arquivo ou de máquina existente.
**Verify Connection**
Permite verificar a conexão para a qual você acabou de inserir informações. Se a conexão foi bem-sucedida, uma caixa de diálogo aparece para indicar isso. Se a conexão não foi bem-sucedida, uma mensagem de erro aparece. Se nenhuma informação foi especificada para a conexão, a caixa de diálogo Select Database aparece, permitindo selecionar uma fonte de dados.
**New Data Source**
Exibe a caixa de diálogo Data Sources, que permite adicionar, excluir ou configurar fontes de dados.

# Display ODBC Login Prompts
 **When Login Info Is Not Specified**
Especifica que o Visual FoxPro solicite ao usuário a caixa de diálogo ODBC Data Source Login se o ID e a senha do usuário não estiverem armazenados na definição da conexão nomeada.
**Always**
Especifica que o Visual FoxPro sempre solicite ao usuário a caixa de diálogo ODBC Data Source Login. Isso permite que o usuário use um ID de login e senha diferentes dos armazenados na conexão nomeada.
**Never**
Especifica que o Visual FoxPro nunca solicite ao usuário. Esta opção garante maior segurança.

# Data Processing

Essas opções correspondem a propriedades de conexão que você também pode definir com a função DBSETPROP( ). Para obter mais informações sobre essas propriedades, consulte as propriedades de conexão na função DBGETPROP( ).
 **Asynchronous Execution**
Especifica uma conexão assíncrona. Esta opção corresponde à propriedade de conexão Asynchronous.
**Display Warnings**
Especifica a exibição de avisos não capturáveis. Esta opção corresponde à propriedade de conexão DispWarnings.
**Batch Processing**
Especifica que a conexão opere em modo de lote. Esta opção corresponde à propriedade de conexão BatchMode.
**Automatic Transactions**
Especifica que o processamento de transações é tratado automaticamente. Esta opção corresponde à propriedade de conexão Transactions.
**Packet Size**
Permite especificar o tamanho do pacote de rede (em bytes) para informações transmitidas para e a partir do site de dados remoto. Selecione uma opção na lista suspensa ou digite um valor.

# Timeout Intervals

Essas opções definem valores para propriedades de conexão que você também pode definir com a função DBSETPROP( ). Para obter mais informações sobre essas propriedades, consulte as propriedades de conexão na função DBGETPROP( ).
 **Connection (sec)**
Especifica o intervalo de timeout de conexão em segundos. Esta opção corresponde à propriedade de conexão ConnectTimeout.
**Query (sec)**
Especifica o intervalo de timeout de consulta em segundos. Esta opção corresponde à propriedade de conexão QueryTimeout.
**Idle (min)**
Especifica o intervalo de timeout de inatividade em minutos. Conexões ativas são desativadas após o intervalo de tempo especificado. Esta opção corresponde à propriedade de conexão IdleTimeout.
**Wait Time (ms)**
Especifica a quantidade de tempo em milissegundos que decorre antes que o Visual FoxPro determine se a instrução SQL terminou de ser executada. Esta opção corresponde à propriedade de conexão WaitTime.
