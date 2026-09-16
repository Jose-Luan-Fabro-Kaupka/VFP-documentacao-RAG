# Aprimoramentos de recursos de dados e XML

O Visual FoxPro contém as seguintes adições e melhorias aos seus recursos de dados:

# Capacidades SQL ampliadas

O Visual FoxPro contém muitos aprimoramentos para capacidades SQL. Para obter mais informações, consulte SQL Language Improvements.

# Novos tipos de dados

O Visual FoxPro inclui os seguintes novos tipos de campo e de dados:
 - Varchar Para armazenar texto alfanumérico sem incluir preenchimento por espaços adicionais no final do campo ou truncar espaços à direita, use o novo tipo de campo Varchar. Se você não deseja que campos Varchar sejam traduzidos entre code pages, use o tipo de campo Varchar (Binary). Para obter mais informações, consulte Varchar Field Type. Você pode especificar mapeamento de tipo Varchar entre tipos de fonte de dados ODBC, ADO e XML e objetos CursorAdapter e XMLAdapter usando a propriedade MapVarchar. Você também pode especificar mapeamento Varchar para tecnologia SQL pass-through e views remotas usando a configuração MapVarchar na função CURSORSETPROP( ). Para obter mais informações, consulte CURSORSETPROP( ) Function e CURSORGETPROP( ) Function.
- Varbinary Para armazenar valores binários e literais de comprimento fixo em campos e variáveis sem preencher o campo com bytes zero (0) adicionais ou truncar quaisquer bytes zero à direita inseridos pelo usuário, use o tipo de dados Varbinary. Internamente, literais binários do Visual FoxPro contêm um prefixo, 0h, seguido por uma cadeia de números hexadecimais e não são delimitados por aspas (""), diferentemente de cadeias de caracteres. Para obter mais informações, consulte Varbinary Data Type. Você pode especificar mapeamento de tipo binário entre tipos de fonte de dados ODBC, ADO e XML e objetos CursorAdapter e XMLAdapter usando a propriedade MapBinary. Você também pode especificar mapeamento binário para tecnologia SQL pass-through e views remotas usando a configuração MapBinary na função CURSORSETPROP( ). Para obter mais informações, consulte CURSORSETPROP( ) Function e CURSORGETPROP( ) Function.
- Blob Para armazenar dados binários com comprimento indeterminado, use o tipo de dados Blob. Para obter mais informações, consulte Blob Data Type.

Muitos dos elementos de linguagem do Visual FoxPro afetados por esses novos tipos de dados estão listados nos tópicos dos novos tipos de dados.

# Tag de índice binário baseada em expressões lógicas

O Visual FoxPro inclui um novo índice binário, ou bitmap, para criar índices baseados em expressões lógicas, por exemplo, índices baseados em registros excluídos. Um índice binário pode ser significativamente menor que um índice não binário e pode melhorar a velocidade de manutenção de índices. Você pode criar índices binários usando o Table Designer ou o comando INDEX. O Visual FoxPro também inclui aprimoramentos de otimização Rushmore no mecanismo SQL para registros excluídos.

Para obter mais informações, consulte Visual FoxPro Index Types, INDEX Command, ALTER TABLE - SQL Command e Indexes Based on Deleted Records.

# Convertendo tipos de dados com a função CAST( )

Você pode converter expressões de um tipo de dados para outro usando a nova função CAST( ). Usar CAST( ) permite criar instruções SQL mais compatíveis com o SQL Server.

Para obter mais informações, consulte CAST( ) Function.

# Obter cursor e contagem de registros afetados pela execução SQL Pass-Thru

Usando o parâmetro aCountInfo das funções SQLEXEC( ) e SQLMORERESULTS( ), você pode obter o nome do cursor criado e uma contagem dos registros afetados pela execução de uma instrução SQL pass-through.

Para obter mais informações, consulte SQLEXEC( ) Function) e SQLMORERESULTS( ) Function.

# Funcionalidade de rollback suportada quando uma conexão SQL Pass-Through é desconectada

O Visual FoxPro agora suporta a propriedade DisconnectRollback para uso com as funções SQLSETPROP( ), SQLGETPROP( ), DBSETPROP( ) e DBGETPROP( ). DisconnectRollback é uma propriedade em nível de conexão que faz com que uma transação seja revertida ou confirmada quando a função SQLDISCONNECT( ) é chamada para o último identificador de conexão associado à conexão.

A propriedade DisconnectRollback aceita um valor lógico.
 - False (.F.) - (Padrão) A transação será confirmada quando a função SQLDISCONNECT( ) for chamada para o último identificador de instrução associado à conexão.
- True (.T.) - A transação é revertida quando a função SQLDISCONNECT( ) é chamada para o último identificador de instrução associado à conexão.

O exemplo a seguir mostra a propriedade DisconnectRollback definida nas funções DBSETPROP( ) e SQLSETPROP( ).

```foxpro
DBSETPROP("testConnection","CONNECTION","DisconnectRollback",.T.)
SQLSETPROP(con,"DisconnectRollback",.T.)
```

Para obter mais informações, consulte DisconnectRollback property in SQLSETPROP( ) Function.

# SQLIDLEDISCONNECT( ) desconecta temporariamente conexões SQL Pass-Through

Você pode usar a nova função SQLIDLEDISCONNECT( ) para permitir que uma conexão SQL Pass-Through seja temporariamente desconectada. Use a seguinte sintaxe.

```foxpro
SQLIDLEDISCONNECT( nStatementHandle )
```

O parâmetro nStatementHandle é definido como o identificador de instrução a ser desconectado ou 0 se todos os identificadores de instrução devem ser desconectados.

A função SQLIDLEDISCONNECT( ) retorna o valor 1 se for bem-sucedida; caso contrário, retorna -1.

A função falha se o identificador de instrução especificado estiver ocupado ou a conexão estiver em modo de confirmação manual. A função AERROR( ) pode ser usada para obter informações de erro.

O identificador de conexão desconectado é restaurado automaticamente se for necessário para uma operação. O nome da fonte de dados de conexão original é usado.

Se um identificador de instrução for temporariamente liberado, a propriedade OBDChstmt retorna 0; OBDChdbc retorna 0 se a conexão for temporariamente desconectada. Uma conexão compartilhada é temporariamente desconectada assim que todos os seus identificadores de instrução são temporariamente liberados.

Para obter mais informações, consulte SQLIDLEDISCONNECT( ) Function.

# Recuperando identificadores de instrução de conexão SQL ativos

Você pode recuperar informações para todos os identificadores de instrução de conexão SQL ativos usando a nova função ASQLHANDLES( ). ASQLHANDLES( ) cria e usa o array especificado para armazenar referências numéricas de identificadores de instrução que você pode usar em outras funções SQL do Visual FoxPro, como SQLEXEC( ) e SQLDISCONNECT( ). ASQLHANDLES( ) retorna o número de identificadores de instrução ativos em uso ou zero (0) se nenhum estiver disponível. Para obter mais informações, consulte ASQLHANDLES( ) Function.

# Obter o bookmark ADO do registro atual em um cursor baseado em ADO

A propriedade ADOBookmark agora é suportada pela função CURSORGETPROP( ). Use esta propriedade para obter o bookmark ActiveX® Data Objects (ADO) do registro atual em um cursor baseado em ADO.

Para obter mais informações, consulte ADOBookmark Property in CURSORGETPROP( ) Function.

Se uma tabela não estiver selecionada e um alias não for especificado, o Erro 52, "No table is open in the current work area," é gerado. Se o cursor selecionado não for válido, o Erro 1467, "Property is invalid for local cursors," é gerado.

# Obter o número de registros buscados

Você pode obter o número de registros buscados durante a execução SQL Pass-Through usando a nova propriedade de cursor RecordsFetched com a função CURSORGETPROP( ).

Especificar a propriedade de cursor RecordsFetched retornará o número de registros buscados de um cursor baseado em OBDC/ADO.

Se registros foram excluídos ou anexados localmente, a propriedade de cursor RecordsFetched pode não retornar o número atual de registros no cursor baseado em OBDC/ADO. Além disso, condições de filtro são ignoradas.

Para obter mais informações, consulte RecordsFetched Property in CURSORGETPROP( ) Function.

# Determinar se uma busca está completa

Você pode determinar se um processo de busca está completo para um cursor baseado em OBDC/ADO usando a nova propriedade de cursor FetchIsComplete com a função CURSORGETPROP( ). Somente leitura em tempo de design e em tempo de execução.

Esta propriedade não é suportada em cursores em nível de ambiente (área de trabalho 0), tabelas e views locais.

A propriedade de cursor FetchIsComplete retorna uma expressão lógica True (.T.) se o processo de busca estiver completo; caso contrário, False (.F.) é retornado.

Para obter mais informações, consulte FetchIsComplete Property in CURSORGETPROP( ) Function.

# ISMEMOFETCHED( ) determina se um Memo foi buscado

Você pode usar a função ISMEMOFETCHED( ) para determinar se um campo Memo ou General foi buscado quando você está usando busca de memo atrasada. Para obter mais informações sobre busca de memo atrasada, consulte Speeding Up Data Retrieval.

A sintaxe desta função é:

`ISMEMOFETCHED(cFieldName | nFieldNumber [, nWorkArea | cTableAlias ])`

A função ISMEMOFETCHED( ) retorna True (.T.) quando o campo Memo é buscado ou se dados locais são usados. ISMEMOFETCHED() retorna NULL se o ponteiro de registro estiver posicionado no início do cursor ou após o último registro.

Para obter mais informações, consulte ISMEMOFETCHED( ) Function.

# Cancelar busca ADO

No Visual FoxPro, agora você pode cancelar uma busca ADO demorada pressionando a tecla ESC.

# Suporte a nomes de tipo longos

O Visual FoxPro suporta o uso de nomes de tipo longos com as seguintes funções, comandos e propriedades.
 - CAST( ) Function
- ALTER TABLE - SQL Command
- CREATE CURSOR - SQL Command
- CREATE TABLE - SQL Command
- CREATE FROM Command
- CursorSchema Property
- DataType Property

A tabela a seguir lista os tipos de dados junto com seus nomes de tipo longos e nomes de tipo curtos.

| Data Type | Long Type Name | Short Type Name |
| --- | --- | --- |
| Character | Char, Character | C |
| Date | Date | D |
| DateTime | Datetime | T |
| Numeric | Num, Numeric | N |
| Floating | Float | F |
| Integer | Int, Integer | I |
| Double | Double | B |
| Currency | Currency | Y |
| Logical | Logical | L |
| Memo | Memo | M |
| General | General | G |
| Picture | Picture | P |
| Varchar | Varchar | V |
| Varbinary | Varbinary | Q |
| Blob | Blob | W |

O Visual FoxPro permite que nomes de tipo longos ambíguos sejam usados com os comandos ALTER TABLE, CREATE CURSOR, CREATE TABLE e CREATE FROM. Se o nome de tipo longo especificado não for um nome de tipo longo reconhecido, o Visual FoxPro truncará o nome especificado para o primeiro caractere.

# Suporte a transações para tabelas livres e cursores

Em versões anteriores do Visual FoxPro, transações usando o comando BEGIN TRANSACTION eram suportadas apenas para dados locais e remotos de bancos de dados. Transações envolvendo tabelas livres e cursores agora são suportadas por meio do uso das funções MAKETRANSACTABLE( ) e ISTRANSACTABLE( ). Para obter mais informações, consulte MAKETRANSACTABLE( ) Function e ISTRANSACTABLE( ) Function.

# Especificar um code page ao usar os comandos CREATE TABLE ou CREATE CURSOR

Você pode especificar um code page incluindo a cláusula CODEPAGE com os comandos CREATE CURSOR ou CREATE TABLE.

Quando a cláusula CODEPAGE é especificada, a nova tabela ou cursor tem um code page especificado por nCodePage. Um erro, 1914, "Code page number is invalid", é gerado se um code page inválido for especificado.

O exemplo a seguir cria uma tabela e exibe seu code page:

```foxpro
CREATE TABLE Sales CODEPAGE=1251 (OrderID I, CustID I, OrderAmt Y(4))
```

`? CPDBF( )`

Para obter mais informações, consulte CREATE CURSOR - SQL Command, CREATE TABLE - SQL Command e Code Pages Supported by Visual FoxPro.

# Converter tipos de dados Character e Memo usando o comando ALTER TABLE

O Visual FoxPro agora suporta conversão automática do tipo de dados character para o tipo de dados memo sem perda de dados ao usar o comando ALTER TABLE junto com a cláusula ALTER COLUMN. Esta conversão também é suportada ao fazer alterações estruturais usando o Table Designer. Para obter mais informações, consulte ALTER TABLE - SQL Command.

# Comando BLANK pode inicializar registros com valor padrão

Você pode inicializar campos no registro atual com seus valores padrão armazenados no contêiner de banco de dados da tabela (DBC) usando a opção DEFAULT [AUTOINC] ao limpar o registro com o comando BLANK. Para obter mais informações, consulte BLANK Command.

# Comando FLUSH grava dados explicitamente no disco

O Visual FoxPro agora inclui opções e parâmetros para o comando FLUSH e a função FFLUSH para que você possa salvar explicitamente todas as alterações feitas em todas as tabelas e índices abertos. Você também pode salvar alterações em uma tabela específica especificando uma área de trabalho, alias de tabela ou um caminho e nome de arquivo. Para obter mais informações, consulte FLUSH Command e FFLUSH( ) Function.

# Preencher um array com aliases usados por uma tabela especificada

O novo parâmetro cTableName da função AUSED( ) torna possível filtrar o array criado para conter apenas os aliases sendo usados para uma tabela especificada.

`AUSED(ArrayName [, nDataSessionNumber [, cTableName ]])`

O parâmetro cTableName aceita os seguintes formatos para especificar uma tabela, da maior para a menor prioridade.
 - DatabaseName!TableName ou DatabaseName!ViewName
- Path\DatabaseName!TableName ou Path\DatabaseName!ViewName
- Nome de tabela ou view definido no DBC no DBC atual na sessão de dados atual
- Nome de arquivo simples ou completo

Para obter mais informações, consulte AUSED( ) Function.

# Obter último valor de auto-incremento com GETAUTOINCVALUE( )

Você pode usar a nova função GETAUTOINCVALUE( ) para retornar o último valor gerado para um campo autoincrementado dentro de uma sessão de dados. Para obter mais informações, consulte GETAUTOINCVALUE( ) Function.

# SET TABLEPROMPT controla prompt para selecionar tabela

O novo comando SET TABLEPROMPT controla se o Visual FoxPro solicita ao usuário com a Open Dialog Box (Visual FoxPro) para selecionar uma tabela quando uma especificada não pode ser encontrada, como em SELECT - SQL Command. Para obter mais informações, consulte SET TABLEPROMPT Command.

# Usar SET VARCHARMAPPING para controlar mapeamentos do conjunto de resultados de consulta

Para consultas como SELECT - SQL Command, dados de caracteres são frequentemente manipulados usando funções e expressões do Visual FoxPro. Como o comprimento do valor do campo resultante pode ser importante para certos usos de aplicativo, é valioso ter esses dados Character mapeados para dados Varchar no conjunto de resultados. O comando SET VARCHARMAPPING controla se dados Character são mapeados para um tipo de dados Character ou Varchar. Para obter mais informações, consulte SET VARCHARMAPPING Command.

# SET TABLEVALIDATE expandido

Quando um cabeçalho de tabela é bloqueado durante a validação, tentativas de abrir a tabela, por exemplo, com o comando USE, geram a mensagem "File is in use (Error 3)." Se o cabeçalho da tabela não puder ser bloqueado para uma operação de abertura de tabela, você pode suprimir esta mensagem definindo o terceiro bit para o comando SET TABLEVALIDATE. Você também deve definir o primeiro bit para validar a contagem de registros quando a tabela abre. Portanto, você precisa definir o comando SET TABLEVALIDATE com um valor de 5. Além disso, uma opção de quarto bit (valor de 8) está disponível para operações Insert que verifica o cabeçalho da tabela antes que o registro anexado seja salvo no disco e o cabeçalho da tabela seja modificado.

Para obter mais informações, consulte SET TABLEVALIDATE Command.

# SET REFRESH pode especificar taxas de atualização mais rápidas

Você pode especificar frações de segundo para o parâmetro nSeconds2 até um mínimo de 0,001 segundos. Você também pode especificar os seguintes valores para o segundo parâmetro opcional:
 - -1 - Sempre ler dados de um disco.
- 0 - Sempre usar dados no buffer de memória, mas não atualizar o buffer.

A caixa de seleção Table refresh interval na guia Data da caixa de diálogo Options agora também aceita valores fracionários.

Para obter mais informações, consulte SET REFRESH Command e Data Tab, Options Dialog Box.

# SET REFRESH pode diferenciar valores para cada cursor

Você pode usar a nova propriedade Refresh com a função CURSORGETPROP( ) para diferenciar os valores SET REFRESH para cursores individuais. A configuração padrão é -2, que é um valor global. Este valor não está disponível com o comando SET REFRESH.

A propriedade Refresh está disponível nos níveis Data Session e Cursor. A configuração padrão para o nível Data Session é -2 e o valor padrão para o nível Cursor é a configuração do nível da sessão atual. Se a configuração do nível global for definida como 0, a configuração do nível Cursor é ignorada.

Se uma tabela não estiver selecionada no momento e um alias não for especificado, o Erro 52, "No table is open in the current work area," é gerado.

Para obter mais informações, consulte Refresh Property in CURSORGETPROP( ) Function.

# SET( ) determina configurações do comando SET REPROCESS

Agora você pode usar a seguinte sintaxe com a função SET( ) para determinar como o comando SET REPROCESS foi declarado.

| SET Command | Value Returned |
| --- | --- |
| REPROCESS, 2 | Current session setting type (0 - attempts, 1 - seconds) |
| REPROCESS, 3 | System session setting type (0 - attempts, 1 - seconds) |

Para obter mais informações, consulte SET( ) Function e SET REPROCESS Command.

# Registrar saída de SYS(3054) usando SYS(3092)

Você pode usar a nova função SYS(3092) em conjunto com SYS(3054) para registrar a saída resultante em um arquivo.

`SYS( 3092 [, cFileName [, lAdditive ]])`

O parâmetro cFileName especifica o arquivo para ecoar a saída de SYS(3054). Enviar uma cadeia de caracteres vazia para cFileName desativará o registro de saída no arquivo.

O valor padrão para lAdditive é False (.F.). Isso especifica que a nova saída substituirá o conteúdo anterior do arquivo especificado. Para anexar nova saída ao arquivo especificado, defina lAdditive como True (.T.).

SYS(3092) retorna o nome do arquivo de eco atual se estiver ativo; caso contrário, retorna uma cadeia de caracteres vazia.

SYS(3054) e SYS(3092) são configurações globais — em um runtime multithread elas têm escopo por thread. Cada função pode ser alterada independentemente da outra.

Essas funções não estão disponíveis no Visual FoxPro OLE DB Provider.

Para obter mais informações, consulte SYS(3054) - Rushmore Query Optimization Level e SYS(3092) - Output Rushmore Query Optimization Level.

# Limpar memória em cache para área de trabalho específica usando SYS(1104)

Você pode opcionalmente especificar o alias ou a área de trabalho de uma tabela ou cursor especificado para o qual a memória em cache é limpa. Para obter mais informações, consulte SYS(1104) - Purge Memory Cache.

# Novos tipos de tabela para SYS(2029)

A função SYS(2029) retorna novos valores para tabelas que contêm campos Autoinc, Varchar, Varbinary ou Blob. Para obter mais informações, consulte SYS(2029) - Table Type.

# Mapear dados Unicode remotos para ANSI usando SYS(987)

Use SYS(987) para mapear dados Unicode remotos recuperados por meio de SQL pass-through ou views remotas para ANSI. Esta função pode ser usada para recuperar dados Varchar remotos como ANSI para uso com campos Memo. Esta configuração é uma configuração global em todas as sessões de dados e deve ser usada com cuidado. Para obter mais informações, consulte SYS(987) - Map Remote Data to ANSI.

# Dicas de Memo e campo em BROWSE ou Grid

Quando o ponteiro do mouse é posicionado sobre uma célula de campo Memo em uma janela Browse ou controle Grid, uma janela Memo Tip exibe o conteúdo do campo Memo.

Para outros tipos de campo, posicionar o ponteiro do mouse sobre o campo exibe o conteúdo do campo em uma janela Field Tip quando o campo tem tamanho menor que seu conteúdo.

Janelas Memo Tip exibem no máximo 4 kilobytes de texto e não são exibidas para dados binários. Uma janela Memo Tip é exibida até que o ponteiro do mouse seja movido do campo Memo. A variável de sistema _TOOLTIPTIMEOUT determina por quanto tempo uma janela Field Tip é exibida.

Você pode desabilitar Memo Tips definindo a propriedade ShowTips de _SCREEN como False (.F.).

Memo e Field Tips também serão exibidos para controles Grid se tanto _SCREEN quanto a propriedade ShowTips do formulário estiverem definidos como True (.T.). Além disso, a propriedade ToolTipText do controle Textbox da coluna da grade do campo deve conter uma cadeia de caracteres vazia.

# Especificar code pages

Você pode especificar o code page usado para decodificar dados quando XML está sendo analisado e para codificar dados quando XML codificado em UTF-8 é gerado. As seguintes alterações de linguagem estão disponíveis:
 - Parâmetro nCodePage Para especificar code pages, você pode usar o parâmetro nCodePage para os seguintes métodos XMLToTable: ToCursor Method ChangesToCursor Method ApplyDiffgram Method XMLTable.ToCursor ( [ lAppend [, cAlias [, nCodePage ]]] ) XMLTable.ChangesToCursor( [ cAlias [, lIncludeUnchangedData [, nCodePage ]]] ) XMLTable.ApplyDiffgram( [ cAlias [, oCursorAdapter [, lPreserveChanges [, nCodePage ]]]] )
- Propriedades CodePage e UseCodePage Use a propriedade CodePage e a propriedade UseCodePage para especificar code pages quando você usa as seguintes classes: XMLAdapter Class XMLTable Class XMLField Class XMLAdapter.CodePage = nValue XMLTable.CodePage = nValue XMLField.CodePage = nValue
- Flag 32768 A flag 32768 está disponível para as seguintes funções e classe: CursorAdapter Class XMLTOCURSOR( ) Function CURSORTOXML( ) Function XMLUPDATEGRAM( ) Function CursorAdaptor.Flags = nCodePage XMLTOCURSOR( eExpression | cXMLFile [, cCursorName [, nFlags ]]) CURSORTOXML(nWorkArea | cTableAlias, cOutput [, nOutputFormat [, nFlags [, nRecords [, cSchemaName [, cSchemaLocation [, cNameSpace ]]]]]]) XMLUPDATEGRAM( [ cAliasList [, nFlags [, cSchemaLocation]]]) O parâmetro nCodePage deve corresponder a um code page reconhecido pelo Visual FoxPro.

Para obter mais informações, consulte Code Pages Supported by Visual FoxPro.

# Propriedade MapVarchar mapeia para tipos de dados Varchar, Varbinary e Blob

Para as classes CursorAdapter e XMLAdapter, você pode usar a propriedade MapVarchar para mapear para tipos de dados Varchar. Para mapear para tipos de dados Varbinary e Blob, você pode usar a propriedade MapBinary.

A função XMLTOCURSOR( ) contém várias novas flags para suportar mapeamento de tipos de campo XML Char e base64Binary para novos tipos de dados Fox.

Para obter mais informações, consulte MapVarchar Property e MapBinary Property.

# Tratando verificações de conflito com propriedades da classe CursorAdapter

Você pode tratar melhor conflitos ao executar operações de atualização e exclusão usando os comandos especificados pelas propriedades UpdateCmd e DeleteCmd para objetos CursorAdapter usando as novas propriedades ConflictCheckType e ConflictCheckCmd para objetos CursorAdapter.

Você pode usar ConflictCheckType para especificar como tratar uma verificação de conflito durante uma operação de atualização ou exclusão. Quando ConflictCheckType é definido como 4, você pode usar ConflictCheckCmd para especificar um comando personalizado a ser anexado ao final dos comandos nas propriedades UpdateCmd e DeleteCmd.

> **Observação:** O Visual FoxPro 8.0 Service Pack 1 inclui as propriedades ConflictCheckType e ConflictCheckCmd.

Para obter mais informações, consulte ConflictCheckType Property e ConflictCheckCmd Property.

# Tratamento aprimorado de DataEnvironment com propriedades UseCursorSchema e NoData

Você pode especificar configurações padrão para chamadas CursorFill Method feitas sem os dois primeiros parâmetros definindo essas propriedades. Para obter mais informações, consulte UseCursorSchema Property e NoData Property.

# Suporte a campo Timestamp

A nova propriedade TimestampFieldList permite especificar uma lista de campos timestamp para o cursor criado pelo CursorAdapter. Para obter mais informações, consulte TimestampFieldList Property.

# Suporte a atualização automática

Há vários cenários em que você pode querer que os dados do cursor sejam atualizados de uma fonte de dados remota após uma operação Insert/Update ter ocorrido. Estes incluem os seguintes cenários:
 - Uma tabela tem um campo auto-incremento que também funciona como chave primária.
- Uma tabela tem um campo timestamp, e esse campo deve ser atualizado do banco de dados após cada Insert/Update para permitir atualizações subsequentes bem-sucedidas do registro quando WhereType=4 (key and timestamp).
- Uma tabela contém alguns campos que têm valores DEFAULT ou triggers definidos que causarão alterações.

As seguintes novas propriedades foram adicionadas à classe CursorAdapter para suporte a Auto-Refresh:

| Property | Description |
| --- | --- |
| InsertCmdRefreshFieldList | List of fields to refresh after Insert command executes. |
| InsertCmdRefreshCmd | Specifies the command to refresh the record after Insert command executes. |
| InsertCmdRefreshKeyFieldList | List of key fields to refresh in record after Insert command executes. |
| UpdateCmdRefreshFieldList | List of fields to refresh after Update command executes. |
| UpdateCmdRefreshCmd | Specifies the command to refresh the record after Update command executes. |
| UpdateCmdRefreshKeyFieldList | List of key fields to refresh the record after Update command executes. |
| RefreshTimestamp | Enables automatic refresh for fields in TimestampFieldList during Insert/Update. |

Para obter mais informações sobre como o Visual FoxPro atualiza dados remotos usando um CursorAdapter, consulte Data Access Management Using CursorAdapters. Consulte também InsertCmdRefreshCmd Property, InsertCmdRefreshFieldList Property, InsertCmdRefreshKeyFieldList Property, UpdateCmdRefreshCmd Property, UpdateCmdRefreshFieldList Property, UpdateCmdRefreshKeyFieldList Property e RefreshTimeStamp Property.

# Atualização de registro sob demanda

No Visual FoxPro 8.0, a função REFRESH( ) fornece funcionalidade de atualização de registro sob demanda para views locais e remotas; no entanto, não suporta isso para o CursorAdapter. O Visual FoxPro 9.0 amplia o suporte REFRESH( ) para o CursorAdapter e fornece algumas capacidades adicionais:

| Member | Description |
| --- | --- |
| RecordRefresh method | Refreshes the current field values for the target records. Use the CURVAL( ) Function to determine current field values. |
| BeforeRecordRefresh event | Occurs immediately before the RecordRefresh method is executed. |
| AfterRecordRefresh event | Occurs after the RecordRefresh method is executed. |
| RefreshCmdDataSourceType property | Specifies the data source type to be used for the RecordRefresh method. |
| RefreshCmdDataSource property | Specifies the data source to be used for the RecordRefresh method. |
| RefreshIgnoreFieldList property | List of fields to ignore during RecordRefresh operation |
| RefreshCmd property | Specifies the command to refresh rows when RecordRefresh is executed. |
| RefreshAlias property | Specifies the alias of read-only cursor used as a target for the refresh operation. |

Para obter mais informações, consulte RecordRefresh Method, BeforeRecordRefresh Event, AfterRecordRefresh Event, RefreshCmdDataSourceType Property, RefreshCmdDataSource Property, RefreshIgnoreFieldList Property, RefreshCmd Property e RefreshAlias Property.

# Busca de Memo atrasada

A classe CursorAdapter tem uma propriedade FetchMemo, que quando definida como False (.F.) no Visual FoxPro 9.0 coloca o cursor no modo Delayed Memo Fetch semelhante a Remote Views. O modo Delayed Memo Fetch impede que o conteúdo de campos Memo seja buscado usando CursorFill Method ou CursorRefresh Method. Uma tentativa de buscar conteúdo para um campo Memo é feita quando o aplicativo tenta acessar o valor. Os seguintes aprimoramentos do CursorAdapter fornecem suporte para Delayed Memo Fetch:

| Member | Description |
| --- | --- |
| DelayedMemoFetch method | Performs a delayed Memo field fetch for a target record in a cursor in a CursorAdapter object. |
| FetchMemoDataSourceType property | Specifies the data source type used for the DelayedMemoFetch method. |
| FetchMemoDataSource property | Specifies the data source used for the DelayedMemoFetch method. |
| FetchMemoCmdList property | Specifies a list of Memo field names and their associated fetch commands. |

Para obter mais informações, consulte DelayedMemoFetch Method, FetchMemoDataSourceType Property, FetchMemoDataSource Property e FetchMemoCmdList Property.

# Propriedade UseTransactions

A nova propriedade UseTransactions especifica se o CursorAdapter deve usar transações ao enviar comandos Insert, Update ou Delete por meio de ADO ou ODBC. Para obter mais informações, consulte UseTransactions Property.

# Restrições DEFAULT e CHECK respeitadas

No Visual FoxPro 9.0, valores DEFAULT e restrições CHECK em nível de tabela e de campo são suportados para fontes de dados XML, Native, ADO e ODBC. No Visual FoxPro 8.0, valores DEFAULT e restrições CHECK em nível de tabela e de campo são suportados apenas para uma fonte de dados XML. Para que os valores DEFAULT e as restrições CHECK sejam aplicados a um cursor, chame o método CursorFill com o parâmetro lUseSchema definido como True (.T.). Para obter mais informações, consulte CursorSchema Property.

# Conversão de tipo de dados remoto para dados lógicos

Quando você move dados entre um servidor remoto e o Visual FoxPro, o Visual FoxPro usa tipos de dados ODBC ou ADO para mapear tipos de dados remotos para tipos de dados locais do Visual FoxPro. No Visual FoxPro 9.0, certos tipos de dados ODBC e ADO agora podem ser mapeados para um tipo de dados lógico em views remotas e no objeto CursorAdapter. Para obter mais informações, consulte Data Type Conversion Control.

# Propriedade ADOCodePage

Ao trabalhar com uma fonte de dados ADO para seu CursorAdapter, você pode querer especificar um code page para usar na tradução de dados de caracteres. A nova propriedade ADOCodePage permite especificar este code page. Para obter mais informações, consulte ADOCodePage Property.

# Ler e gravar documentos XML aninhados

Você pode ler e gravar em seu banco de dados relacional em documentos XML usando aninhamento para tratar as relações entre tabelas. Você realiza isso usando a propriedade RespectNesting da classe XMLAdapter. A classe XMLTable tem o método Nest, o método Unnest e as seguintes propriedades para tratar aninhamento.
 - FirstNestedTable Property
- NestedInto Property
- NextSiblingTable Property

Para obter mais informações, consulte XMLAdapter Class e XMLTable Class.

# Método LoadXML pode aceitar qualquer documento XML

O método LoadXML aceita qualquer documento XML com um schema válido. Anteriormente, o método exigia que o schema seguisse o formato de um dataset gerado pelo Visual Studio. Quando você usa o método LoadXML para ler um documento XML com um schema diferente de um dataset gerado pelo Visual Studio, as propriedades XMLName e XMLPrefix do XMLAdapter são definidas como vazias (""). A propriedade XMLNamespace do XMLAdapter torna-se igual ao valor do atributo Namespace de destino para o nó schema e cada elemento XML torna-se um complexType e é mapeado para um objeto XMLTable. A propriedade XMLNamespace é definida como namespaceURI para o elemento.

Se você definir a propriedade RespectNesting do XMLAdapter como True (.T.), a declaração do elemento de nível superior é ignorada se for referenciada por algum outro elemento complexo. Para esse caso, o objeto XMLTable para o elemento referenciado é aninhado no XMLTable para o elemento que o referencia.

Para obter mais informações, consulte LoadXML Method.

# Expressões XPath podem acessar documentos XML complexos

Você pode usar expressões XPath para acessar documentos XML complexos e as novas propriedades para ler os nós dentro do documento. Por exemplo, você pode querer filtrar nós de registro, restaurar relações baseadas em campos de chave estrangeira, usar o texto de um elemento como dados para um campo ou acessar XML que usa vários namespaces XML. As seguintes propriedades fornecem a capacidade de ler o XML no nível XMLAdapter, no nível XMLTable ou no nível XMLField.
 - DeclareXMLPrefix Property
- SelectionNamespaces Property
- XMLNameIsXPath Property

Você pode usar a tabela a seguir para determinar o nó dentro do documento XML no qual deseja começar a leitura.

Por exemplo, se você usar uma expressão XPath na propriedade XMLName para um XMLAdapter, a leitura começa no primeiro nó

| To read | Class | Context node |
| --- | --- | --- |
| From the first found XML node: | XMLAdapter | IXMLDOMElement property |
| All found XML nodes and use each node as a single record: | XMLTable | XMLAdapter object |
| The first found XML node and use its text as a field value: | XMLField | XMLTable object |

Os seguintes métodos não suportam o uso de expressões XPath na propriedade XMLName:
 - Os métodos ApplyDiffgram e ChangesToCursor não suportam expressões XPath para objetos XMLAdapter e XMLTable.
- O método ToCursor não suporta uma expressão XPath para XMLAdapter quando a propriedade IsDiffgram está definida como True (.T.).
- O método ToXML não suporta expressões XPath para objetos XMLAdapter e XMLTable e ignora objetos XMLField que usam expressões XPath.

Para obter mais informações sobre expressões XPath, consulte XPath Reference no Microsoft Core XML Services (MSXML) 4.0 SDK na biblioteca MSDN em http://msdn.microsoft.com/library.

# Funções Cursor to XML

O suporte para as seguintes funções foi adicionado ao OLE DB Provider for Visual FoxPro:
 - CURSORTOXML( ) Function
- XMLTOCURSOR( ) Function
- XMLUPDATEGRAM( ) Function

Quando usadas no OLE DB Provider for Visual FoxPro, a propriedade _VFP VFPXMLProg não é suportada para as funções CURSORTOXML( ), XMLTOCURSOR( ) e XMLUPDATEGRAM( ) porque a variável de sistema _VFP não é suportada no OLE DB Provider.

# EXECSCRIPT suportado no Visual FoxPro OLE DB Provider

Você pode usar a função EXECSCRIPT( ) com o Visual FoxPro OLE DB Provider. Para obter mais informações, consulte EXECSCRIPT( ) Function.

# Retornando um rowset de um cursor no Visual FoxPro OLE DB Provider

Você pode usar as novas funções SETRESULTSET( ), GETRESULTSET( ) e CLEARRESULTSET( ) para marcar um cursor ou tabela que foi aberto pelo Visual FoxPro OLE DB Provider, recuperar a área de trabalho do cursor marcado e limpar o sinalizador de marcação de um cursor marcado. Ao marcar um cursor ou tabela, você pode recuperar um rowset criado a partir do cursor ou tabela marcado de um procedimento armazenado de contêiner de banco de dados (DBC) quando o OLE DB Provider completa a execução do comando.

Para obter mais informações, consulte SETRESULTSET( ) Function, GETRESULTSET( ) Function e CLEARRESULTSET( ) Function.
