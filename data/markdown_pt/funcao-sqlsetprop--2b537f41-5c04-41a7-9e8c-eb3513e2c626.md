# Função SQLSETPROP( )

Especifica configurações para uma conexão ativa. Você pode usar SQLSETPROP( ) para especificar configurações no nível da conexão. Para especificar configurações padrão do Visual FoxPro no nível do ambiente, inclua 0 como identificador de instrução.

```foxpro
SQLSETPROP(nStatementHandle, cSetting [, eExpression])
```

#### Parâmetros
 **nStatementHandle**
Especifica o identificador de instrução para a fonte de dados retornado por SQLCONNECT( ).
**cSetting**
Especifica a configuração. A tabela a seguir lista os valores de cSetting. Configuração Descrição Asynchronous Especifica se os conjuntos de resultados são retornados de forma síncrona (False (.F.), o padrão) ou assíncrona (True (.T.)). Leitura/gravação. BatchMode Especifica se SQLEXEC( ) retorna conjuntos de resultados todos de uma vez (True (.T.), o padrão) ou individualmente com SQLMORERESULTS( ) (False (.F.)). Leitura/gravação. ConnectBusy Contém True (.T.) se uma conexão compartilhada estiver ocupada; caso contrário, contém False (.F.). Somente leitura. ConnectString A cadeia de conexão de login. Somente leitura. ConnectTimeOut Especifica o tempo de espera (em segundos) antes de retornar um erro de tempo limite de conexão. Se você especificar 0, a espera é indefinida e um erro de tempo limite nunca é retornado. ConnectTimeOut pode ser de 0 a 600. O padrão é 15. Leitura/gravação. DataSource O nome da fonte de dados conforme definido no arquivo ODBC.INI. Leitura/gravação. DisconnectRollback Especifica se uma transação pendente é confirmada ou revertida quando SQLDISCONNECT( ) é chamado para o último identificador de conexão. O padrão é false (.F.), indicando que uma transação pendente é confirmada quando SQLDISCONNECT( ) é chamado para o último identificador de conexão. Especifique true (.T.) para reverter uma transação pendente quando SQLDISCONNECT( ) é chamado para o último identificador de conexão. Conexões com processamento automático de transações não são afetadas por esta configuração. Leitura/gravação. DispLogin Contém um valor numérico que determina quando a caixa de diálogo Login ODBC é exibida. DispLogin pode assumir os seguintes valores: 1 ou DB_PROMPTCOMPLETE (de FOXPRO.H). 1 é o padrão. 2 ou DB_PROMPTALWAYS (de FOXPRO.H). 3 ou DB_PROMPTNEVER (de FOXPRO.H). Se 1 ou DB_PROMPTCOMPLETE for especificado, o Visual FoxPro exibe a caixa de diálogo Login ODBC somente se alguma informação obrigatória estiver ausente. Se 2 ou DB_PROMPTALWAYS for especificado, a caixa de diálogo Login ODBC é sempre exibida, permitindo alterar configurações antes de conectar. Se 3 ou DB_PROMPTNEVER for especificado, a caixa de diálogo Login ODBC não é exibida e o Visual FoxPro gera um erro se as informações de login obrigatórias não estiverem disponíveis. Leitura/gravação. DispWarnings Especifica se mensagens de erro são exibidas (True (.T.)) ou não são exibidas (False (.F.), o padrão). Leitura/gravação. IdleTimeout O intervalo de tempo limite de inatividade em minutos. Conexões ativas são desativadas após o intervalo de tempo especificado. O valor padrão é 0 (aguardar indefinidamente). Leitura/gravação. ODBChdbc O identificador interno de conexão ODBC, que pode ser usado por arquivos de biblioteca externa (arquivos FLL) para chamar ODBC. Somente leitura. ODBChstmt O identificador interno de instrução ODBC, que pode ser usado por arquivos de biblioteca externa (arquivos FLL) para chamar ODBC. Somente leitura. PacketSize O tamanho do pacote de rede usado pela conexão. Ajustar este valor pode melhorar o desempenho. O valor padrão é 4096 bytes (4K). Leitura/gravação. Password A senha de conexão. Somente leitura. QueryTimeOut Especifica o tempo de espera (em segundos) antes de retornar um erro geral de tempo limite. Se você especificar 0 (o padrão), a espera é indefinida e um erro de tempo limite nunca é retornado. QueryTimeOut pode ser de 0 a 600. Leitura/gravação. Shared Especifica se a conexão subjacente é uma conexão compartilhada (True (.T.)) ou não (False (.F.)). Somente leitura. Transactions Contém um valor numérico que determina como a conexão gerencia transações na tabela remota. Transactions pode assumir os seguintes valores: 1 ou DB_TRANSAUTO (de FOXPRO.H). 1 é o padrão. O processamento de transações para a tabela remota é tratado automaticamente. 2 ou DB_TRANSMANUAL (de FOXPRO.H). O processamento de transações é tratado manualmente por meio de SQLCOMMIT( ) e SQLROLLBACK( ) . Leitura/gravação. UserId A identificação do usuário. Somente leitura. WaitTime A quantidade de tempo em milissegundos que decorre antes do Visual FoxPro verificar se a instrução SQL terminou de ser executada. O padrão é 100 milissegundos. Leitura/gravação.
**eExpression**
Especifica o valor da configuração designada com cSetting . Se você omitir eExpression , o valor padrão é restaurado para a configuração.

# Valor de retorno

Tipo de dados numérico. SQLSETPROP( ) retorna 1 se for bem-sucedido. Caso contrário, retorna – 1 se ocorrer um erro no nível da conexão ou – 2 se ocorrer um erro no nível do ambiente.

# Observações

Você pode usar SQLGETPROP( ) para retornar o valor atual de uma configuração especificada.

> **Observação:** Você deve desabilitar a caixa de diálogo de login do Open Database Connectivity (ODBC) para suportar SQL pass through com o Microsoft Transaction Server. Para desabilitar a caixa de diálogo de login ODBC, use a instrução SQLSETPROP(cStatementHandle, 'DispLogin', 3) , onde cStatementHandle é o identificador de instrução retornado por SQLCONNECT( ) . Você também pode desabilitar a caixa de diálogo de login ODBC no Designer de conexão .

A opção ConnectTimeOut pode ser definida somente no nível do Visual FoxPro e não possui equivalente no nível da conexão. Você pode definir todas as outras opções no nível da conexão ou no nível do Visual FoxPro. Cada opção definida no nível do Visual FoxPro serve como valor padrão para conexões subsequentes.

# Exemplo

O exemplo a seguir mostra como SQLSETPROP( ) é usado para definir o tamanho do pacote para a conexão atual. SQLCONNECT( ) exibe a Caixa de diálogo Selecionar conexão ou fonte de dados para você escolher uma conexão, e a conexão é testada. O tamanho do pacote é definido; a configuração é testada; e os resultados são exibidos.

```foxpro
CLOSE ALL
CLEAR ALL
CLEAR
nHandle=SQLCONNECT()
IF nHandle > 0
   nSet=SQLSETPROP(nHandle, "PacketSize", 2048 )
   IF nSet > 0
      =MESSAGEBOX("PacketSize was set to 2048",0,"Connection Results")
   ELSE
      =MESSAGEBOX("Error setting PacketSize",0,"Connection Results")
   ENDIF
ELSE
   =MESSAGEBOX("No Connection",0,"Connection Results")
ENDIF
=SQLDISCONNECT(nHandle)
```
