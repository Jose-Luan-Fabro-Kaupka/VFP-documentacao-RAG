# Gerenciando conexões com SQL Pass-Through

Quando você cria uma view remota, escolhe um nome de fonte de dados ODBC ou um nome de conexão que é então usado como pipeline para o servidor remoto na ativação da view. Para acessar dados remotos diretamente com SQL pass-through, você deve ter o handle de uma conexão ativa. A handle is a value that refers to an object; in this case, the handle refers to a data source connection. To obtain a handle, you request a connection to the data source using the SQLCONNECT( ) Function or SQLSTRINGCONNECT( ) Function function. If the connection is successful, your application receives a connection handle for use in subsequent Visual FoxPro calls.

Seu aplicativo pode solicitar várias conexões para uma fonte de dados. You can also work with multiple ODBC data sources by requesting a connection to each data source you want to access. If you want to reduce the number of connections used, you can configure remote views to share the same connection. Você se desconecta de uma fonte de dados com a função SQLDISCONNECT( ).

> **Dica:** O Visual FoxPro depende da definição da fonte de dados ODBC armazenada no Windows para conectar a uma fonte de dados. If you change the name or the logon information for a data source, keep in mind that these changes might affect whether an application using that data source can connect to the desired remote server.

# Controlando propriedades de ambiente e conexão

O ambiente cliente/servidor é estabelecido cada vez que você abre o Visual FoxPro. The environment exists for that session of Visual FoxPro and disappears when you close Visual FoxPro. The client/server environment contains:
 - Propriedades globais que atuam como protótipos para novas conexões.
- Valores de erro para erros que ocorrem fora de uma conexão específica.

You can use a handle of 0, the environment handle, to refer to global property settings. You use the SQLSETPROP( ) Function function to control default property settings in the connection environment and properties within individual connections. The methods you use for entering SQLSETPROP( ) values are consistent for both the environment and individual connections:
 - Properties specified with one of two values can use a logical value (.F. or .T.) for eExpression .
- A property name can be abbreviated to its shortest unambiguous truncation. For example, you can use " Asynchronous ", " Asynch ", or "A" to specify the Asynchronous property. Property names aren't case-sensitive.

When you initiate a connection, the connection inherits default connection property values. You can use SQLSETPROP( ) to change these values.

# Definindo propriedades de conexão

Para visualizar as configurações atuais de uma conexão, use a função SQLGETPROP( ) Function com o handle de conexão respectivo. The following table lists the connection settings you can access with SQLGETPROP( ).
 Propriedades de conexão Visual FoxPro
| Para | Use esta configuração | Finalidade |
| --- | --- | --- |
| Exibir as informações usadas para criar a conexão ativa | ConnectString | The login connection string. |
| DataSource | The name of the data source as defined by ODBC. | |
| Password | The connection password. | |
| UserID | The user identification. | |
| Trabalhar com conexões compartilhadas | ConnectBusy | True (.T.) if a shared connection is busy; false (.F.) otherwise. |
| Controlar exibição da interface | DispLogin | Controls when the ODBC Login dialog box is displayed. |
| DispWarnings | Controls whether non-fatal warning messages are displayed or not. | |
| Controlar intervalos de tempo | ConnectTimeout | Specifies the time (in seconds) to wait before returning a connection time-out error. |
| IdleTimeout | Specifies the idle time-out interval (in seconds). Qualifying active connections are deactivated after the specified time interval. 1 | |
| WaitTime | Controls the amount of time in milliseconds that elapses before Visual FoxPro checks whether the SQL statement has completed executing. | |
| QueryTimeout | Controls the time (in seconds) to wait before returning a general time-out error. | |
| Gerenciar transações | Transactions | Determines how the connection manages transactions on the remote table. |
| Controlar busca de conjuntos de resultados em cursors de view | Asynchronous | Specifies if result sets are returned synchronously (the default) or asynchronously. |
| BatchMode | Specifies if SQLEXEC( ) returns result sets all at once (the default), or individually with SQLMORERESULTS( ). | |
| PacketSize | Specifies the size of the network packet used by the connection. | |
| Exibir handles ODBC internos | ODBChdbc 2 | The internal ODBC connection handle that can be used by external library files (.fll files) to call the ODBC API functions. |
| ODBChstmt 2 | The internal ODBC statement handle that can be used by external library files (.fll files) to call the ODBC API functions. | |

1. Se estiver em modo de transação manual, a conexão não é desativada.

2. If a connection is deactivated, the ODBChdbc and ODBChstmt values are no longer valid. Do not free or drop these values in a user library.

For more information on connection properties and their default settings, see SQLSETPROP( ) Function.

# Controlando configurações de propriedades de ambiente

Os valores que você define no ambiente Visual FoxPro usando handle 0 são usados como protótipos ou valores padrão para cada conexão ou anexo subsequente.

To view the current environment property settings, use SQLGETPROP( ) Function with 0 as the value for the handle.

O exemplo a seguir exibe a configuração atual da propriedade WaitTime do ambiente:

```foxpro
? SQLGETPROP(0, "WaitTime")
```

If you set the DispWarnings property to true (.T.), Visual FoxPro displays any environment errors from that point on, and also sets DispWarnings to true (.T.) for newly created connections.

Although the values you set for handle 0 are used as prototype values for each connection, you can also set custom properties for an individual connection by issuing SQLSETPROP( ) Function for that connection handle. The exceptions are the ConnectTimeout, PacketSize, and DispLogin properties, whose settings the connection inherits at connect time. If you change the setting of the ConnectTimeout, PacketSize, or DispLogin property, the new setting isn't used until you reconnect.

# Controlando objetos de conexão e view

Você pode controlar conexões e views definindo propriedades no objeto de conexão ou view. Properties that control databases, tables, table fields, view definitions, view fields, named connections, active connections, or active view cursors are called engine properties. You can display or set engine properties with one of the following Visual FoxPro functions:

| Para exibir propriedades de engine use | Para definir propriedades de engine use |
| --- | --- |
| CURSORGETPROP( ) | CURSORSETPROP( ) |
| DBGETPROP( ) | DBSETPROP( ) |
| SQLGETPROP( ) | SQLSETPROP( ) |

The function you use depends on whether you want to set properties on object 0 (connection 0 and cursor 0), the object definition in a database (named connection or view definition), or the active object (active connection or active view cursor). The following table lists objects and the functions you use to set properties on each object:

| Para definir propriedades para | Conexão | View |
| --- | --- | --- |
| Object 0 | SQLSETPROP( ) | CURSORSETPROP( ) |
| Object definition in a database | DBSETPROP( ) | DBSETPROP( ) |
| Active object | SQLSETPROP( ) | CURSORSETPROP( ) |

# Propriedades de engine

O diagrama a seguir lista propriedades de engine alfabeticamente junto com os objetos que usam cada propriedade.

The following table lists engine properties alphabetically along with the functions you can use to set those properties.

| Propriedade de engine | Aplica-se a |
| --- | --- |
| Asynchronous | Connection definitions: see DBSETPROP( ) . Active connections: see SQLSETPROP( ) . |
| BatchMode | Connection definitions: see DBSETPROP( ) . Active connections: see SQLSETPROP( ) . |
| BatchUpdateCount 1 | View definitions: see DBSETPROP( ) . Active view cursors: see CURSORSETPROP( ) . |
| Buffering | Active view cursors: see CURSORSETPROP( ) . |
| Caption | Fields in tables, fields in view definitions: see DBSETPROP( ) . |
| Comment | Databases, tables, fields in tables, view definitions, fields in view definitions, connection definitions: see DBSETPROP( ) . |
| CompareMemo | View definitions: see DBSETPROP( ) . Active view cursors: see CURSORSETPROP( ) . |
| ConnectBusy | Active connections: see SQLGETPROP( ) . |
| ConnectHandle | Active view cursors: see CURSORGETPROP( ) . |
| ConnectName 1 | View definitions: see DBSETPROP( ) . Active connections: see SQLGETPROP( ) . Active view cursors: see CURSORGETPROP( ) . |
| ConnectString | Connection definitions: see DBSETPROP( ) . Active connections: see SQLGETPROP( ) . |
| ConnectTimeout | Connection definitions: see DBSETPROP( ) . Active connections: see SQLSETPROP( ) . |
| Database | Active view cursors: see CURSORGETPROP( ) . |
| DataSource | Connection definitions: see DBSETPROP( ) . Active connections: see SQLGETPROP( ) . |
| DataType | Fields in view definitions: see DBSETPROP( ) . |
| DefaultValue | Fields in tables, fields in view definitions: see DBSETPROP( ) . |
| DeleteTrigger | Tables: see DBGETPROP( ) . |
| DispLogin | Connection definitions: see DBSETPROP( ) . Active connections: see SQLSETPROP( ) . |
| DispWarnings | Connection definitions: see DBSETPROP( ) . Active connections: see SQLSETPROP( ) . |
| FetchAsNeeded | View definitions: see DBSETPROP( ) . Active view cursors: see CURSORGETPROP( ) . |
| FetchMemo 1 | View definitions: see DBSETPROP( ) . Active view cursors: see CURSORGETPROP( ) . |
| FetchSize 1 | View definitions: see DBSETPROP( ) . Active view cursors: see CURSORSETPROP( ) . |
| IdleTimeout | Connection definitions: see DBSETPROP( ) . Active connections: see SQLSETPROP( ) . |
| InsertTrigger | Tables: see DBGETPROP( ) . |
| KeyField | Fields in view definitions: see DBSETPROP( ) . |
| KeyFieldList 2 | Active view cursors: see CURSORSETPROP( ) . |
| MaxRecords 1 | View definitions: see DBSETPROP( ) . Active view cursors: see CURSORSETPROP( ) . |
| ODBCHdbc | Active connections: see SQLGETPROP( ) . |
| ODBCHstmt | Active connections: see SQLGETPROP( ) . |
| Offline | View definitions: see DBGETPROP( ). |
| PacketSize | Connection definitions: see DBSETPROP( ) . Active connections: see SQLSETPROP( ) . |
| ParameterList | View definitions: see DBSETPROP( ) . Active view cursors: see CURSORSETPROP( ) . |
| Password | Connection definitions: see DBSETPROP( ) . Active connections: see SQLGETPROP( ) . |
| Path | Tables: see DBGETPROP( ) . |
| Prepared | View definitions: see DBSETPROP( ) . |
| PrimaryKey | Tables: see DBGETPROP( ) . |
| QueryTimeout | Connection definitions: see DBSETPROP( ) . Active connections: see SQLSETPROP( ) . |
| RuleExpression | Tables, fields in tables, view definitions, fields in view definitions: see DBSETPROP( ) . |
| RuleText | Tables, fields in tables, view definitions, fields in view definitions: see DBSETPROP( ) . |
| SendUpdates 2 | View definitions: see DBSETPROP( ) . Active view cursors: see CURSORSETPROP( ) . |
| ShareConnection | View definitions: see DBSETPROP( ) . Active view cursors: see CURSORGETPROP( ) . |
| SourceName | Active view cursors: see CURSORGETPROP( ) . |
| SourceType | View definitions: see DBGETPROP( ) . Active view cursors: see CURSORGETPROP( ) . |
| SQL | View definitions: see DBGETPROP( ) . Active view cursors: see CURSORGETPROP( ) . |
| Tables 2 | View definitions: see DBSETPROP( ) . Active view cursors: see CURSORSETPROP( ). |
| Transactions | Connection definitions: see DBSETPROP( ) . Active connections: see SQLSETPROP( ) . |
| Updatable | Fields in view definitions: see DBSETPROP( ) . |
| UpdatableFieldList 2 | Active view cursors: see CURSORSETPROP( ) . |
| UpdateName | Fields in view definitions: see DBSETPROP( ) . |
| UpdateNameList 2 | Active view cursors: see CURSORSETPROP( ) . |
| UpdateTrigger | Tables: see DBGETPROP( ) . |
| UpdateType | View definitions: see DBSETPROP( ) . Active view cursors: see CURSORSETPROP( ) . |
| UseMemoSize 1 | View definitions: see DBSETPROP( ) . Active view cursors: see CURSORGETPROP( ) . |
| UserID | Connection definitions: see DBSETPROP( ) . Active connections: see SQLGETPROP( ) . |
| Version | Databases: see DBGETPROP( ) . |
| WaitTime | Connection definitions: see DBSETPROP( ) . Active connections: see SQLSETPROP( ) . |
| WhereType | View definitions: see DBSETPROP( ) . Active view cursors: see CURSORSETPROP( ) . |

1. Propriedade principalmente útil para views remotas; a configuração não tem efeito no desempenho de views locais. You can set this property on local views if you want to pre-set the property on the local view and then upsize later to create a remote view.

2. A propriedade deve ser definida para que atualizações sejam enviadas à fonte de dados remota.

# Usando transações com dados remotos

Você pode envolver transações em torno de atualizações, exclusões e inserções em dados remotos usando um de dois métodos:
 - Modo de transação automático
- Modo de transação manual

The transaction mode you select determines how Visual FoxPro handles transactions on your local machine.

# Transações aninhadas

O Visual FoxPro suporta transações aninhadas em até cinco níveis para dados locais. A single level of transaction support is built into SQL pass-through.

If your server supports multiple levels of transactions, you can use SQL pass-through to manage transaction levels explicitly. Explicit transaction management is complex, however, because it can be difficult to control the interaction between the built-in transaction and the timing of remote server transactions. For more information on explicit transaction management, see your ODBC documentation.
