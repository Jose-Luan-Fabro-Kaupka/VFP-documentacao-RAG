# Guia Auto-Update, CursorAdapter Builder

Especifica como o objeto CursorAdapter atualiza automaticamente os registros na fonte de dados. Para obter mais informações, consulte Classe CursorAdapter.
 **Send updates**
Especifica se o objeto CursorAdapter está disponível para atualização. Send updates é selecionado por padrão.
**Auto-update**
Especifica se a capacidade de atualização automática do objeto CursorAdapter deve ser habilitada.
**Advanced**
Exibe a caixa de diálogo Advanced Update Properties, que contém quatro guias: Update, Delete, Insert e Conflict. As guias Update, Delete e Insert permitem especificar: Allow (update/delete/insert) Especifica se a operação de atualização, exclusão ou inserção é permitida. Selecionada por padrão. Update/Delete/Insert command Especifica um texto de comando personalizado de atualização, exclusão ou inserção. Esses comandos podem ser instruções SQL UPDATE / DELETE / INSERT, nomes de procedimentos armazenados, chamadas a métodos ou procedimentos personalizados etc. Update data source type Especifica um tipo de fonte de dados apropriado quando os comandos Update/Insert/Delete precisam de outro tipo. Observação Ao selecionar ADO ou ODBC, também é necessário informar a fonte de dados conforme especificado na guia Properties. A guia Conflict permite especificar: Conflict check type Especifica como tratar a verificação de conflitos durante uma atualização ou exclusão. Consulte a propriedade ConflictCheckType. Conflict check command Especifica um comando personalizado para verificar conflitos de atualização ou exclusão. Consulte a propriedade ConflictCheckCmd.
**Refresh**
Exibe a caixa de diálogo Refresh Properties, com as guias Record Refresh, Fields Refresh, Refresh After Insert e Refresh After Update. Record Refresh permite especificar: Refresh command O comando usado na atualização de registro executada pelo método RecordRefresh. Consulte RefreshCmd. Refresh data source type O tipo da fonte de dados usado pelo método RecordRefresh. Conforme o tipo selecionado, você pode selecionar ou criar uma fonte de dados específica. Consulte RefreshCmdDataSourceType. Fields Refresh permite especificar: Refresh timestamp Se os campos selecionados são atualizados automaticamente quando um comando Insert ou Update é executado. Consulte RefreshTimeStamp. Fields list Uma lista de campos ignorados pelo processo quando o método RecordRefresh é executado. Consulte RefreshIgnoreFieldList. As guias Refresh After Insert/Update permitem especificar: Insert/Update refresh command O comando para atualizar automaticamente o registro após um comando Insert/Update. Consulte InsertCmdRefreshCmd e UpdateCmdRefreshCmd. Fields list Os campos do cursor a atualizar após um comando Insert/Update, incluindo campos-chave. Consulte InsertCmdRefreshFieldList, InsertCmdRefreshKeyFieldList, UpdateCmdRefreshFieldList e UpdateCmdRefreshKeyFieldList. Refresh all fields Habilita a atualização de todos os campos da lista.
**Tables**
Especifica uma lista de tabelas para atualização, separada por vírgulas. Normalmente, o builder fornece essa lista.
**Key field column (key symbol)**
Exibe caixas de seleção para escolher campos de chave primária. Disponível somente quando Auto-update está selecionado.
**Automatic updating column (pencil symbol)**
Exibe caixas de seleção para escolher campos para atualização automática. Disponível somente quando Auto-update está selecionado.
**Cursor field**
Exibe os campos disponíveis para atualização automática. Disponível somente quando Auto-update está selecionado.
**Update name**
Especifica os nomes de campos, no formato tableName . FieldName, usados na atualização automática. Disponível somente quando Auto-update está selecionado. Consulte a propriedade UpdateNameList.
**Update all fields**
Especifica que todos os campos sejam selecionados e atualizados automaticamente. Ainda é necessário especificar um campo-chave.
**Update using**
Especifica o método de atualização preferido: SQL UPDATE ou SQL DELETE seguido de INSERT.
**SQL WHERE clause includes**
Especifica o tipo de cláusula WHERE usado na atualização: somente campos-chave, campos-chave e atualizáveis, campos-chave e modificados ou chave e timestamp. Consulte WhereType.
**Batch update count**
Define BatchUpdateCount.
**Compare memo**
Define CompareMemo como ligado ou desligado.
**Use transactions**
Especifica se o CursorAdapter usa transações ao enviar comandos Insert, Update ou Delete por ADO ou ODBC.
**Timestamp fields**
Especifica os campos de timestamp do cursor.
**Conversion functions**
Especifica uma lista, separada por vírgulas, de pares de nome de campo e nome de função separados por espaços.
**UpdateGram schema**
Especifica o nome e o local do esquema de mapeamento passados à função XMLUPDATEGRAM( ). Aplica-se somente quando CursorAdapter.DataSourceType é "XML".
