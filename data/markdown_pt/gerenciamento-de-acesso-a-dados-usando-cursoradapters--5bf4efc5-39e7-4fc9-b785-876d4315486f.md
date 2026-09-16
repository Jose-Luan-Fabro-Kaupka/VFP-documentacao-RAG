# Gerenciamento de acesso a dados usando CursorAdapters

No Visual FoxPro, você pode recuperar dados de fontes de dados locais e remotas que tenham os seguintes tipos de fonte de dados usando cursor adapters:
 - Native
- Open Database Connectivity (ODBC)
- ActiveX Data Object (ADO)
- Extensible Markup Language (XML)

A classe CursorAdapter expande o suporte para trabalhar com diferentes tipos de fonte de dados como cursors nativos do Visual FoxPro. Objetos CursorAdapter fornecem as seguintes capacidades:
 - Usar diferentes fontes de dados dinamicamente.
- Usar a fonte de dados do objeto CursorAdapter ou o ambiente de dados.
- Compartilhar fontes de dados dentro dos limites da tecnologia de fonte de dados.
- Definir opcionalmente a estrutura do cursor associado a um objeto CursorAdapter.
- Controlar o carregamento de dados da fonte de dados em um cursor Visual FoxPro associado a um objeto CursorAdapter.
- Renderizar dados de diferentes fontes de dados em cursors Visual FoxPro baseados no tipo de fonte de dados.
- Controlar como os dados são adicionados, atualizados e excluídos com propriedades e métodos CursorAdapter.
- Adicionar objetos CursorAdapter a contêineres diferentes do ambiente de dados, como formulários, conjuntos de formulários e outros contêineres.
- Usar a classe CursorAdapter como uma classe autônoma sem um ambiente de dados associado.

Com objetos CursorAdapter, a fonte de dados é apenas um canal para a camada de tradução, que renderiza dados da fonte de dados em um cursor Visual FoxPro.

> **Observação:** O Visual FoxPro não suporta o uso de relações com objetos CursorAdapter. No entanto, você pode usar relações com cursors associados a cursor adapters.

Para obter mais informações sobre as classes CursorAdapter, DataEnvironment e Cursor, consulte CursorAdapter Class, DataEnvironment Object e Cursor Object.

# Interação com as funções TABLEUPDATE( ) e TABLEREVERT( )

A função TABLEUPDATE( ) reconhece e pode trabalhar com objetos CursorAdapter. TABLEUPDATE( ) delega suas operações ao cursor adapter associado ao cursor. TABLEREVERT( ) opera em objetos CursorAdapter da mesma forma que em outros cursors com buffer.

Para obter mais informações sobre como objetos CursorAdapter afetam o comportamento das funções TABLEUPDATE( ) e TABLEREVERT( ), consulte TABLEUPDATE( ) Function e TABLEREVERT( ) Function.

# Atualização automática e CursorAdapters

O Visual FoxPro gera automaticamente os comandos SQL INSERT, UPDATE e DELETE para views locais e remotas. Ao trabalhar com objetos CursorAdapter, você pode personalizar e controlar como o Visual FoxPro gera esses comandos SQL INSERT, UPDATE e DELETE.

Quando as propriedades InsertCmd, UpdateCmd e DeleteCmd do CursorAdapter estão vazias, o Visual FoxPro gera os comandos SQL correspondentes automaticamente. Você deve determinar se a geração automática desses comandos é apropriada para a fonte de dados que está usando. Para gerar os comandos SQL INSERT, UPDATE e DELETE automaticamente, você deve definir as seguintes propriedades específicas do CursorAdapter:
 - Tables
- KeyFieldList
- UpdatableFieldList
- UpdateNameList

As seguintes regras gerais se aplicam às propriedades Tables e UpdateNameList:
 - Tables Para habilitar a atualização automática, você deve fornecer uma lista de nomes de tabela na ordem exata em que deseja que apareçam nos comandos SQL INSERT, UPDATE e DELETE.
- UpdateNameList Você deve especificar uma lista delimitada por vírgulas consistindo em pares de nomes de campo local e remoto completo. Cada par de nomes consiste no nome do campo local seguido do nome completo do campo remoto. O nome completo do campo remoto aparece como <remote table name>.<remote field name>, onde <remote table name> corresponde ao nome da propriedade Tables.

Você também deve definir os campos-chave apropriados se definir as seguintes propriedades CursorAdapter como True (.T.):
 - AllowInsert
- AllowUpdate
- AllowDelete

Para obter mais informações sobre os comandos SQL usados para atualização automática, consulte INSERT - SQL Command, UPDATE - SQL Command e DELETE - SQL Command.

### Atualizações em lote

Objetos CursorAdapter usam atualização em lote se o valor da propriedade BatchUpdateCount do CursorAdapter for maior que 1, e uma das seguintes condições for verdadeira:
 - O objeto CursorAdapter está configurado para usar o mesmo identificador de instrução ODBC para todas as operações permitidas, ou seja, INSERT, UDPATE e DELETE, conforme definido pelas propriedades AllowInsert, AllowUpdate e AllowDelete.
- O objeto CursorAdapter está configurado para usar o mesmo objeto ADODB Command para todas as operações permitidas.
- O objeto CursorAdapter usa "XML" como tipo de fonte de dados para todas as operações permitidas.

Se a atualização em lote é usada, os seguintes eventos CursorAdapter não ocorrem:
 - BeforeInsert
- AfterInsert
- BeforeUpdate
- AfterUpdate
- BeforeDelete
- AfterDelete

Se uma atualização falhar para um lote, o Visual FoxPro tenta enviar uma atualização separada para cada linha no lote; no entanto, os eventos listados ainda não ocorrem.

Para obter mais informações, consulte BatchUpdateCount Property.

### Atualização automática e ActiveX Data Objects (ADO)

Ao trabalhar com ADO, você pode enviar atualizações usando dois métodos diferentes:
 - Use o objeto CursorAdapter para enviar atualizações com o objeto ADO RecordSet usado pelo método CursorFill do CursorAdapter. Ao realizar atualizações automáticas usando um ADO RecordSet, as seguintes regras se aplicam ao definir as propriedades InsertCmdDataSource , UpdateCmdDataSource e DeleteCmdDataSource do CursorAdapter: O ADO RecordSet deve ser leitura/gravação e ter bookmarks disponíveis. Bookmarks estão sempre disponíveis ao usar um objeto RecordSet do lado do cliente. Bookmarks podem estar disponíveis ao usar cursors server-side Keyset ou Static quando suportados pelo OLE DB Provider. As atualizações são realizadas campo a campo. Para cada registro atualizado, o objeto CursorAdapter localiza o registro original no ADO RecordSet, altera os valores dos campos atualizáveis e chama o método Update do ADO RecordSet. O objeto CursorAdapter não chama o método UpdateBatch do ADO RecordSet; portanto, seu aplicativo deve chamar explicitamente UpdateBatch quando apropriado. Ao usar este método, você deve configurar o objeto CursorAdapter da seguinte forma: THIS.DataSourceType="ADO" THIS.UpdateCmdDataSourceType="" Você também pode usar os builders DataEnvironment e CursorAdapter para construir um formulário atualizável ou biblioteca de classes DataEnvironment e CursorAdapter e usar a guia AutoUpdate no CursorAdapter Builder para especificar campos-chave, campos de atualização e outras informações necessárias.
- Use o objeto CursorAdapter para enviar atualizações diretamente ao banco de dados usando um comando de atualização personalizado ou gerado automaticamente. Ao realizar atualizações automáticas diretamente, o objeto CursorAdapter precisa de um objeto ADO Command com sua propriedade ActiveConnection definida para um objeto ADO Connection aberto. Ao usar este método, você deve configurar o objeto CursorAdapter da seguinte forma: THIS.UpdateCmdDataSourceType="ADO" THIS.UpdateCmdDataSource=NewADODBCommandObject Definir THIS.DataSourceType="ADO" não se aplica ao usar este método.

### Atualização automática e XML

Objetos CursorAdapter não geram automaticamente comandos SQL INSERT, UPDATE ou DELETE como fazem para outras fontes de dados quando a fonte de dados é XML, devido às numerosas maneiras de gerar XML. No entanto, você pode usar o objeto CursorAdapter para gerar um XML UpdateGram e atribuí-lo à propriedade UpdateGram do CursorAdapter.

Embora o objeto CursorAdapter possa gerar o XML UpdateGram, você deve implementar a operação de atualização real usando os protocolos apropriados, como SQL XML usando HTTP, SQL XML OLE DB ou XML Web service para .NET.

As seguintes regras se aplicam ao trabalhar com fontes de dados XML e gerar XML UpdateGrams:
 - Você deve especificar texto de comando para as propriedades InsertCmd , UpdateCmd e DeleteCmd do CursorAdapter que o Visual FoxPro possa executar para a operação de inserção, atualização ou exclusão apropriada. Se estiver usando atualização em lote, ou seja, a propriedade BatchUpdateCount do CursorAdapter é maior que 1, UpdateCmd é executado apenas uma vez por lote.
- As seguintes propriedades CursorAdapter devem ser definidas como "XML": InsertCmdDataSourceType UpdateCmdDataSourceType DeleteCmdDataSourceType Se essas propriedades não estiverem definidas como "XML", o Visual FoxPro executa o texto de comando nas propriedades UpdateCmd, InsertCmd ou DeleteCmd, mas não gera um XML UpdateGram.
- Para construir o XML UpdateGram corretamente, o CursorAdapter exige que as propriedades Tables, UpdatableFieldList e UpdateNameList contenham valores válidos. O CursorAdapter pode gerar um UpdateGram de várias tabelas especificando as tabelas e campos nas propriedades Tables, UpdatableFieldList e UpdateNameList conforme apropriado. Portanto, você pode atualizar um cursor que representa uma junção de várias tabelas usando a função XMLUPDATEGRAM( ). Para obter mais informações, consulte XMLUPDATEGRAM( ) Function .
- O CursorAdapter usa a propriedade WhereType para gerar a seção before do XML UpdateGram. Portanto, ao realizar uma operação de atualização ou exclusão, as propriedades KeyFieldList e UpdatableFieldList devem conter os campos-chave apropriados. Para obter mais informações, consulte WhereType Property .
- Se o buffer de linha estiver habilitado, ou BatchUpdateCount for 1, o Visual FoxPro cria um XML UpdateGram para cada operação de atualização, inserção ou exclusão. Se o buffer de tabela estiver habilitado e estiver usando atualização em lote, ou seja, BatchUpdateCount é maior que 1, o Visual FoxPro cria um XML UpdateGram para todo o lote de alterações. Neste modo, você deve chamar a função TABLEUPDATE( ) conforme esperado para iniciar a atualização e a geração do XML UpdateGram.
