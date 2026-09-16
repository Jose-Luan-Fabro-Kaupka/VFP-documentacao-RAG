# Função CURSORSETPROP( )

Especifica configurações de propriedade para uma tabela Visual FoxPro ou um cursor.

```foxpro
CURSORSETPROP( cProperty [, eExpression] [,cTableAlias | nWorkArea])
```

#### Parâmetros
 **cProperty**
Especifica a propriedade de tabela ou cursor a definir. Buffering é a única propriedade que você pode especificar para uma tabela Visual FoxPro.
**eExpression**
Especifica o valor da propriedade que você especifica com cProperty. Se você omitir eExpression, a propriedade é definida para seu valor padrão. A tabela a seguir lista as propriedades que você pode especificar para cProperty e uma descrição dos valores que eExpression pode assumir. Property eExpression values AllowSimultaneousFetch Applies when using remote views, a shared connection, and to cursors created using ODBC. .T. - Permit similarly configured cursors sharing the connection to fetch rows simultaneously. .F. - Do not permit similarly configured cursors sharing the connection to fetch rows simultaneously. AutoIncError .T. - Generate an error message when attempting to insert or update values in a field that uses automatically incrementing field values. .F. - Does not generate an error message but does not use the value specified when attempting to insert or update the value in a field that uses automatically incrementing field values, which uses the appropriate incremented value. Applies to cursors and sessions. BatchUpdateCount* Specifies the number of update statements to send to the remote data source for buffered tables. The default value is 1. Adjusting this value can greatly increase update performance when using automatic updating. Buffering 1 – Sets row and table buffering off. Record locking and data writing are identical to earlier FoxPro versions. (Default) 2 – Sets pessimistic row buffering on. 3 – Sets optimistic row buffering on. 4 – Sets pessimistic table buffering on. 5 – Sets optimistic table buffering on. SET MULTILOCKS must be ON for all Buffering modes except 1 (off). CompareMemo .T. - Include memo fields of type Memo, General, or Picture in the WHERE clause for updates. .F. – Do not include memo fields in the WHERE clause for updates. Applies when automatic updating is used. FetchAsNeeded .T. – Fetch records only when needed, such as when record pointer moves to a row that has not been fetched. .F. – Fetch additional data during idle time. Note FetchAsNeeded does not apply when progressive fetching is disabled (FetchSize is -1). FetchMemo* .T. – Fetch memo fields with the view results. .F. – Do not fetch memo fields with the view results. FetchSize* Specifies the number of rows progressively fetched from the remote table result set. The default value is 100 rows. Setting FetchSize to –1 retrieves the complete result set, limited by the MaxRecords setting. Note Progressive fetching holds the connection until all rows are retrieved. Use caution coding with FetchSize if ShareConnection is True (.T.). KeyFieldList Specifies a comma-delimited list of primary fields for the cursor. No default. You must include a list of field names for updates to work when using automatic updating. MapBinary .T. - At the session level, SQL Pass-Through maps SQL_BINARY, SQL_VARBINARY, and SQL_LONGVARBINARY ODBC types to Varbinary or Blob data type. For remote views, the CREATE SQL VIEW command maps the SQL_LONGVARBINARY ODBC data source type to Blob type, and it maps SQL_BINARY and SQL_VARBINARY ODBC data source types to Varbinary type when the precision of the corresponding column in the data source is less than or equal to 254 bytes. When precision is greater than 254 bytes, these types map to Blob type. .F. - SQL Pass-Through maps SQL_BINARY and SQL_VARBINARY ODBC types to Caractere type. (Default) For remote views, the CREATE SQL VIEW command maps SQL_BINARY and SQL_VARBINARY ODBC data source types to Memo type. Note MapBinary is read/write for nWorkArea set to 0, read-only for SQL Pass-Through cursors, and invalid for table cursors ( nWorkArea equal to or greater than 1). MapVarchar .T. - At the session level, SQL Pass-Through maps SQL_WVARCHAR and SQL_VARCHAR ODBC types to Varchar type. For remote views, CREATE SQL VIEW command maps SQL_WVARCHAR and SQL_VARCHAR ODBC data source types to Varchar type. .F. - SQL Pass-Through maps SQL_WVARCHAR and SQL_VARCHAR ODBC types to Caractere type. (Default) For remote views, CREATE SQL VIEW command maps SQL_WVARCHAR and SQL_VARCHAR ODBC data source types to Caractere type. Note MapVarchar is read/write for nWorkArea set to 0, read-only for SQL Pass-Through cursors, and invalid for table cursors ( nWorkArea equal to or greater than 1). MaxRecords* Specifies the maximum number of rows fetched when returning result sets. The default value is – 1, and all rows are returned. A value of 0 specifies that the view is executed but no results are fetched. ParameterList Specifies a semi-colon delimited list of view parameters and parameter types. For views only. Prepared .T. - Prepare SQL statements for subsequent REQUERY( ) function calls. .F. - Do not prepare SQL statements for subsequent REQUERY( ) calls. (Default). REQUERY( ) is used to retrieve data again for a SQL view. For additional information about preparing SQL statements, see SQLPREPARE( ) Function . Refresh Specifies a numeric refresh value for an individual cursor in the current data session or an initial refresh value for newly opened cursors in the current data session. Use the SET DATASESSION Command to select a specific data session, and use the cTableAlias or nWorkArea parameter to specify a specific cursor. Use nWorkArea = 0 to change the initial refresh value for all newly opened cursors. Any cursors that are already open will not be affected by the new refresh setting. SET REFRESH Command allows you to specify a global refresh value. By default, the CURSORSETPROP( ) Refresh setting is -2, which indicates that the current global SET REFRESH value is used. The global SET REFRESH value is specified with its second parameter, nSeconds2 . You can set the CURSORSETPROP( ) Refresh setting to the same values as the nSeconds2 parameter in SET REFRESH. Note The CURSORSETPROP( ) Refresh setting will be ignored if the nSeconds2 parameter is currently set to zero in the SET REFRESH command. SendUpdates .T. – Specifies that a SQL update query is sent to update tables when an update is made using the view. .F. – Specifies that a SQL update query is not sent to update tables. Tables Specifies a comma-delimited list of the names of remote tables. No default. You must include a list of table names for updates to work when using automatic updating. UpdatableFieldList Specifies a comma-delimited list of fields in the view. This list can include fields from local and remote tables. You must include a list of fields for updates to work when using automatic updating. UpdateNameList Specifies a comma-delimited list of remote field names and the local field names assigned to the cursor. Use this option to specify valid Visual FoxPro names for fields in the cursor that have invalid Visual FoxPro field names. UpdateType 1 – Update old data with new data. (Default) 2 – Update by deleting old data and inserting new data. UseMemoSize* Specifies the minimum size in bytes for result columns to return in memo fields. For example, if the width of a column result is greater than the value of UseMemoSize, the column result is stored in a memo field. UseMemoSize can vary from 1 to 255 bytes. The default value is 255 bytes. WhereType The WHERE clause for updates to remote tables. WhereType can assume the following values: 1 or DB_KEY (from FOXPRO.H). The WHERE clause used to update remote tables consists of only the primary fields specified with the KeyFieldList property. 2 or DB_KEYANDUPDATABLE (from FOXPRO.H). The WHERE clause used to update remote tables consists of the primary fields specified with the KeyFieldList property and any updatable fields. 3 or DB_KEYANDMODIFIED (from FOXPRO.H). The WHERE clause used to update remote tables consists of the primary fields specified with the KeyFieldList property and any other fields that are modified. (Default) 4 or DB_KEYANDTIMESTAMP (from FOXPRO.H). The WHERE clause used to update remote tables consists of the primary fields specified with the KeyFieldList property and a comparison of the time stamps. * This property is primarily used for remote views; setting it has no effect on local views. However, you can preset this property for local views that will be upsized.
**cTableAlias**
Especifica o alias da tabela ou cursor para o qual a propriedade é definida.
**nWorkArea**
Especifica a área de trabalho da tabela ou cursor para o qual a propriedade é definida. Se você especificar 0 para nWorkArea, CURSORSETPROP( ) define a configuração de ambiente usada para todas as tabelas ou cursores subsequentes. Observação Buffering não é aplicado a tabelas abertas implicitamente, por exemplo, usando comandos SQL INSERT/UPDATE/DELETE.

# Valor de retorno

Tipo de dados Logical. CURSORSETPROP( ) returns True (.T.) if Visual FoxPro successfully sets the property you specify. Visual FoxPro generates an error if the property you specify cannot be set.

# Observações

A configuração da propriedade Buffering para CURSORSETPROP( ) determina como o Visual FoxPro realiza bloqueio de registros e buffer de atualização. Para obter informações adicionais sobre bloqueio de registros e buffer de atualização, consulte Buffering Data.

A configuração da propriedade WhereType para CURSORSETPROP( ) determina como as atualizações são realizadas em tabelas remotas. Para obter informações adicionais sobre atualizações de tabelas remotas, consulte Developing Databases.

Você pode usar CURSORSETPROP( ) para substituir a propriedade FetchSize na função SQLSETPROP( ) para um cursor. Esta propriedade é herdada do handle de conexão do cursor por padrão.

Use CURSORGETPROP( ) para retornar as configurações de propriedade atuais para uma tabela Visual FoxPro ou um cursor criado para uma tabela.

Se CURSORSETPROP( ) é emitido sem os argumentos opcionais cTableAlias ou nWorkArea, a configuração de propriedade é especificada para a tabela ou cursor aberto na área de trabalho atualmente selecionada.

# Exemplo

Quando um cursor é aberto, o valor padrão da propriedade AutoIncError é lido do valor padrão da sessão, que é a configuração padrão da sessão de dados atual. O exemplo a seguir mostra como você pode definir o valor padrão AutoIncError para cada sessão especificando 0 (sessão padrão) como o último parâmetro:

```foxpro
CURSORSETPROP("AutoIncError", .T., 0)
```

A sessão padrão é usada ao abrir uma nova sessão de dados private ou cursor. O exemplo a seguir mostra como você pode definir a configuração AutoIncError do cursor ou tabela para cada tabela usando o parâmetro cTableAlias ou nWorkArea como o último parâmetro:

```foxpro
CURSORSETPROP("AutoIncError", .F. , cTableAlias | nWorkArea )
```

O exemplo a seguir demonstra como você pode habilitar buffer de tabela otimista com CURSORSETPROP( ). MULTILOCKS é definido como ON, um requisito para buffer de tabela. A tabela "Customer" no banco de dados "testdata" é aberta, e CURSORSETPROP( ) é usado para definir o modo de buffer como buffer de tabela otimista (5). Uma caixa de mensagem é exibida mostrando o resultado da operação.

```foxpro
CLOSE DATABASES
CLEAR
SET MULTILOCKS ON
OPEN DATABASE (HOME(2) + 'data\testdata')
USE Customer     && Open Customer table.
* Set buffering mode and store logical result
lSuccess=CURSORSETPROP("Buffering", 5, "Customer")
IF lSuccess = .T.
   =MESSAGEBOX("Operation successful!",0,"Operation Status")
ELSE
   =MESSAGEBOX("Operation NOT successful!",0,"Operation Status")
ENDIF
```
