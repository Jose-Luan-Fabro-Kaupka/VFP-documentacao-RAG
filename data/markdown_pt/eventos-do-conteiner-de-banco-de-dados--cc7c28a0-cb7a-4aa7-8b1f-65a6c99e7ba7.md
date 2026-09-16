# Eventos do contêiner de banco de dados

Eventos do contêiner de banco de dados (DBC) ocorrem quando ações são executadas em um banco de dados. Você pode adicionar código de procedimento a esses eventos que é executado quando eles ocorrem.

A tabela a seguir descreve os eventos DBC disponíveis.

| Eventos DBC | Descrição |
| --- | --- |
| DBC_Activate | Ocorre quando um banco de dados aberto se torna o banco de dados atual. |
| DBC_Deactivate | Ocorre quando um banco de dados deixa de ser o banco de dados atual. |
| DBC_BeforeAddRelation | Ocorre antes de adicionar uma relação ao banco de dados. |
| DBC_AfterAddRelation | Ocorre depois de adicionar uma relação ao banco de dados com sucesso. |
| DBC_BeforeAddTable | Ocorre antes de adicionar uma tabela a um banco de dados aberto. |
| DBC_AfterAddTable | Ocorre depois de adicionar uma tabela a um banco de dados aberto. |
| DBC_BeforeAppendProc | Ocorre antes de concluir a operação APPEND PROCEDURES no procedimento armazenado do DBC atual. Use para impedir a operação de anexação. Também use para descobrir o nome do DBC envolvido. |
| DBC_AfterAppendProc | Ocorre depois de concluir a operação APPEND PROCEDURES. |
| DBC_BeforeCloseTable | Ocorre antes de fechar uma tabela ou view. |
| DBC_AfterCloseTable | Ocorre depois de fechar uma tabela ou view. |
| DBC_BeforeCopyProc | Ocorre antes de iniciar a operação de copiar procedimento no DBC atual. Use para impedir a operação. Também use para descobrir o nome do DBC envolvido. |
| DBC_AfterCopyProc | Ocorre depois de concluir a operação de copiar procedimento no DBC atual. Use para descobrir o nome do DBC envolvido. |
| DBC_BeforeCreateConnection | Ocorre antes de criar uma conexão. Use para impedir a criação da conexão ou a abertura do designer de conexões. |
| DBC_AfterCreateConnection | Ocorre depois de criar uma conexão. |
| DBC_BeforeCreateOffline | Ocorre antes de colocar uma view offline. Use para impedir a view offline. |
| DBC_AfterCreateOffline | Ocorre depois de concluir a função CREATEOFFLINE( ). |
| DBC_BeforeCreateTable | Ocorre antes de criar uma tabela em um banco de dados aberto. |
| DBC_AfterCreateTable | Ocorre depois de criar uma tabela em um banco de dados aberto. |
| DBC_BeforeCreateView | Ocorre antes de criar uma view. Use para impedir que a view seja criada ou que o designer de views seja aberto. |
| DBC_AfterCreateView | Ocorre depois de criar uma view. |
| DBC_BeforeDBGetProp | Ocorre antes de executar DBGETPROP( ). |
| DBC_AfterDBGetProp | Ocorre depois de concluir DBGETPROP( ). |
| DBC_BeforeDBSetProp | Ocorre antes de executar DBSETPROP( ) ou quando a propriedade "Event" é alterada. |
| DBC_AfterDBSetProp | Ocorre depois de concluir DBSETPROP( ) ou quando a propriedade "Event" é alterada. |
| DBC_BeforeDeleteConnection | Ocorre antes de excluir uma conexão. |
| DBC_AfterDeleteConnection | Ocorre depois de excluir uma conexão. |
| DBC_BeforeDropOffline | Ocorre antes de retornar uma view para online. Use para impedir que a view offline volte a ficar online. |
| DBC_AfterDropOffline | Ocorre depois de concluir DROPOFFLINE( ). |
| DBC_BeforeDropRelation | Ocorre antes de remover uma relação de um banco de dados. |
| DBC_AfterDropRelation | Ocorre depois de remover uma relação de um banco de dados com sucesso. |
| DBC_BeforeDropTable | Ocorre antes de remover uma tabela do DBC e excluí-la do disco. |
| DBC_AfterDropTable | Ocorre depois de remover uma tabela do DBC e excluí-la do disco. |
| DBC_BeforeDropView | Ocorre antes de remover uma view do DBC. Use para impedir que a view seja removida. |
| DBC_AfterDropView | Ocorre depois de remover uma view do DBC. |
| DBC_BeforeModifyConnection | Ocorre antes de modificar uma conexão. |
| DBC_AfterModifyConnection | Ocorre depois de modificar uma conexão. |
| DBC_BeforeModifyProc | Ocorre antes de modificar um procedimento armazenado no DBC em um DBC aberto. Use para impedir a modificação. Também use para descobrir o nome do DBC atual. |
| DBC_AfterModifyProc | Ocorre depois de modificar e fechar o arquivo de procedimento armazenado do DBC. |
| DBC_BeforeModifyTable | Ocorre antes de modificar uma tabela. |
| DBC_AfterModifyTable | Ocorre depois de modificar uma tabela. |
| DBC_BeforeModifyView | Ocorre antes de modificar uma view. |
| DBC_AfterModifyView | Ocorre depois de modificar uma view. |
| DBC_BeforeOpenTable | Ocorre antes de abrir uma tabela ou view. |
| DBC_AfterOpenTable | Ocorre depois de abrir uma tabela ou view. |
| DBC_BeforeRemoveTable | Ocorre antes de remover uma tabela do DBC. |
| DBC_AfterRemoveTable | Ocorre depois de remover uma tabela do DBC. |
| DBC_BeforeRenameConnection | Ocorre antes de renomear uma conexão. |
| DBC_AfterRenameConnection | Ocorre depois de renomear uma conexão. |
| DBC_BeforeRenameTable | Ocorre antes de renomear uma tabela. |
| DBC_AfterRenameTable | Ocorre depois de renomear uma tabela. |
| DBC_BeforeRenameView | Ocorre antes de renomear uma view. |
| DBC_AfterRenameView | Ocorre depois de renomear uma view. |
| DBC_BeforeValidateData | Ocorre antes de executar VALIDATE DATABASE. Retorne .F. para impedir que o DBC seja validado. |
| DBC_AfterValidateData | Ocorre depois de concluir VALIDATE DATABASE. |
| DBC_ModifyData | Ocorre imediatamente depois que Modify Data é emitido. Use para impedir a abertura da janela Schema. Também pode abrir um banco de dados fechado. |
| DBC_OpenData | Ocorre quando um banco de dados é aberto ou quando um comando MODIFY DATABASE é emitido contra um banco de dados fechado. Use para fechar um banco de dados aberto. |
| DBC_CloseData | Fecha um banco de dados aberto. |
| DBC_PackData | Ocorre antes de executar PACK DATABASE. Use para impedir que o DBC seja compactado. |
