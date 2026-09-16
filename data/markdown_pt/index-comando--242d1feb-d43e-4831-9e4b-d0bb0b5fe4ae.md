# INDEX Comando

Cria um arquivo de índice contendo um ou mais índices para exibir e acessar registros de tabelas em uma ordem especificada.

> **Nota:** Você não pode criar índices primários com o comando INDEX. Se você quiser criar um índice primário usando a linguagem Visual FoxPro, use os comandos SQL CREATE TABLE ou ALTER TABLE.

> **Caution:** Replacing an index key field changes the relative position for the current record in the index. Therefore, use caution if you perform an operation such as REPLACE ALL or SCAN ... ENDSCAN while changing the index for the scope. This also applies to REPLACE operations on indexes created with a FOR clause.

```foxpro
INDEX ON eExpression TO IDXFileName | TAG TagName [BINARY]
   [COLLATE cCollateSequence] [OF CDXFileName] [FOR lExpression]
   [COMPACT] [ASCENDING | DESCENDING] [UNIQUE | CANDIDATE] [ADDITIVE]
```

Parâmetros
 **eExpression**
Specifies an index expression that determines the order in which Visual FoxPro displays and processes records. eExpression can be a simple expression, such as the name of one or more fields from the current table, or a more complex expression containing Visual FoxPro functions, constants, and so on. Visual FoxPro generates index keys based on eExpression and stores them in an index file that you specify. The index file does not affect the physical order of how records are stored in the table. Note For a standalone index (.idx) file, the length of an index key must be between 1 and 100 characters. For a compound index (.cdx) file, the length of an index key must be between 1 and 240 characters. With some collating sequences, or when using double-byte character set (DBCS) characters, each character in the index expression uses two characters in the index key. In these cases, the length of the index expression is limited to 50 or 120 characters, respectively. Caution Avoid using RECNO( ) in the index expression for a table buffered cursor. Because RECNO( ) changes for new records when they are committed by TABLEUPDATE( ) , index corruption could occur. For more information about index expressions, see Index Creation Based on Expressions and Considerations for Creating Index Expressions .
**TO IDXFileName**
Especifica o nome de um arquivo de índice autônomo (.idx) para armazenar uma única chave de índice como gerada por eExpression . Dica Você pode substituir a extensão padrão do nome do arquivo do índice, incluindo uma extensão diferente ou alterando a extensão padrão do índice no arquivo de configuração Visual FoxPro. Ao criar arquivos de índice, observe as regras padrão do Windows para nomear arquivos, que incluem nomes de arquivos longos. Para mais informações sobre arquivos de índice, consulte Visual FoxPro Ficheiros de índice .
** TAG TagName**
Especifica o nome, ou tag, para o índice gerado por eExpression e armazenado em um arquivo índice composto (.cdx). Os nomes das etiquetas devem começar com uma letra ou sublinhado ( ) e podem consistir em qualquer combinação de até 10 letras, dígitos ou caracteres de sublinhado. Nota O número de tags em um arquivo .cdx é limitado apenas pela memória disponível e espaço em disco. Se um arquivo .cdx para a tabela já existe e está aberto, emitindo INDEX com TAG TagName adiciona uma tag ao arquivo .cdx aberto. Se você criar uma tag de índice sem especificar o nome do arquivo de índice, Visual FoxPro adiciona a tag automaticamente ao arquivo .cdx estrutural da tabela. Para mais informações sobre arquivos de índice, consulte Visual FoxPro Ficheiros de índice .
**[COLLATE cCollateSequence ]**
Specifies a collation sequence other than the default setting, MACHINE. cCollateSequence must be a valid Visual FoxPro collation sequence. For more information about setting collation sequences, see Optimizing International Applications and SET COLLATE Command .
** [OF CDXFileName ]**
Especifica o nome de um arquivo de índice composto não estrutural (.cdx) para armazenar o índice, ou tag, como gerado por eExpression . Omitindo esta cláusula cria um arquivo .cdx estrutural, enquanto incluindo esta cláusula cria um arquivo .cdx não estrutural. Para mais informações sobre arquivos de índice, consulte Visual FoxPro Ficheiros de índice .
**[FOR lExpression ]**
Specifies a filter expression that selects only those records that match the filter expression for display and access. Tip If lExpression can be optimized, Rushmore technology optimizes the FOR clause in the INDEX command. For best performance, use an expression that can be optimized in the FOR clause. For more information, see SET OPTIMIZE Command and Using Rushmore Query Optimization to Speed Data Access . For more information about filter expressions, see How to: Filter Data .
**[COMPACT]**
Cria um arquivo de índice compacto (.idx). Arquivos compactos .idx são pequenos e mais rapidamente acessíveis. Nota Ao criar um arquivo índice composto (.cdx), não é necessário incluir COMPACT . Os ficheiros de índice compostos são sempre compactos. Para obter mais informações, consulte Como: Criar índices menos frequentemente usados .
**[ASCENDING | DESCENDING]**
Specifies an order for displaying and accessing records indexed by a compound index (.cdx) file. ASCENDING specifies an ascending order for displaying and accessing records. By default, Visual FoxPro displays and accesses records in ascending order. However, you can include ASCENDING as a reminder of how records are displayed. DESCENDING specifies a descending order for displaying and accessing records. Note You cannot use DESCENDING when creating standalone index (.idx) files; however, you can specify a descending order for an .idx file using the SET INDEX and SET ORDER commands. For more information, see SET INDEX Command and SET ORDER Command .
**[UNIQUE | CANDIDATE]**
Cria um índice único ou candidato. UNIQUE armazena a chave de índice correspondente apenas para o primeiro registro que corresponde à expressão de índice especificada. A chave de índice é armazenada como a única chave em um arquivo autônomo (.idx) ou como uma tag de índice em um arquivo composto (.cdx). Quaisquer outras teclas de índice para registros que correspondam à expressão de índice são excluídas do arquivo de índice. Nota Usar UNIQUE não impede que registros duplicados sejam inseridos na tabela. Só impede que chaves de índice duplicadas sejam adicionadas ao ficheiro de índice. Quando um registro duplicado é alterado para que sua chave de índice seja alterada para um índice ativo UNIQUE, o índice ou tag de índice é atualizado. No entanto, Visual FoxPro não pode exibir ou acessar o próximo registro duplicado com a chave de índice original até que você use o comando REINDEX para reindexar o arquivo. Para mais informações, consulte REINDEX Comando . Usar UNIQUE é idêntico à execução SET UNIQUE ON antes de emitir INDEX ou REINDEX . Para mais informações, consulte SET UNIQUE Command . CANDIDATE armazena uma tag de índice para um arquivo estrutural composto (.cdx); caso contrário, Visual FoxPro gera uma mensagem de erro. Nota Os índices de candidatos não permitem valores duplicados em campos. Se você criar um índice candidato para um ou mais campos que contenham valores duplicados, Visual FoxPro gera um erro. Para mais informações sobre os índices candidatos, ver Visual FoxPro Tipos de Índice . Para mais informações sobre arquivos de índice, consulte Visual FoxPro Ficheiros de índice .
**[ADDITIVE]**
Keeps open any previously opened index files. Omitting the ADDITIVE clause closes any previously opened index files except the structural compound index (.cdx) files. Note The number of index files that you can keep open is limited only by memory and system resources. In Visual FoxPro, the FILES setting in the Windows Config.sys configuration file determines the total number of files you can open.
**[BINARY]**
Creates a binary index. For more information about binary indexes, see Visual FoxPro Index Types . Note When specifying an index expression for eExpression , you must specify a valid logical expression that does not evaluate to a null value. If the index expression for a binary index is changed so that it evaluates to a null value, Visual FoxPro generates an error. When using binary indexes, you cannot use the FOR clause to specify a filter expression or the ASCENDING , DESCENDING , UNIQUE , or CANDIDATE keywords. Visual FoxPro does not support the SET ORDER command when setting to a binary index tag. If you attempt to set order to a binary tag, Visual FoxPro generates an error, and the current order remains at its prior setting. Visual FoxPro does not support SEEK operations or standalone single-key (.idx) indexes with binary indexes.

Observações

Um arquivo .cdx estrutural pode se dissociar de sua tabela se o arquivo de índice não puder ser localizado, excluído ou renomeado. Quando você abre uma tabela que tem um arquivo .cdx estrutural dissociado, aparece uma caixa de diálogo. Quando você clica em Cancelar na caixa de diálogo, a tabela não abre.

> ** Cuidado: ** Clicando em Ignorar abre a tabela; no entanto, ela também remove a bandeira do cabeçalho da tabela que indica que existe um arquivo estrutural associado (.cdx).

> **Dica: ** Para reassociar o arquivo estrutural .cdx, emita o seguinte comando e especifique o nome da tabela como TableName e o nome do arquivo estrutural .cdx dissociado como CDXFileName .

```foxpro
USE TableName INDEX CDXFileName
```

Se a tabela foi modificada, certifique-se de indexar a tabela novamente.

Para relatar o número de registros indexados durante o processo de indexação, defina o comando SET TALK para ON. Para especificar o intervalo de registro exibido durante a indexação, use o comando SET ODOMETER. Para mais informações, ver SET TALK Comando e SET ODOMETER Comando.

To obtain information about open index files, use the DISPLAY STATUS Command. DISPLAY STATUS lists the names of all open index files, their types, their index expressions, and the name of the master, or controlling, index file or tag. The number of index files that you can open is limited only by memory and system resources.

Exemplo

Exemplo 1

The following example closes all databases with the CLOSE DATABASES command and opens the Visual FoxPro sample database, TestData.dbc, with the OPEN DATABASE command and the Customer table with the USE command.

The INDEX command creates a standalone index (.idx) file named Complist based on the Company field. The CLEAR command clears the Visual FoxPro main window, and the DISPLAY STATUS command displays information about the index file, Complist.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\TestData')
USE Customer
INDEX ON Company TO Complist
CLEAR
DISPLAY STATUS
```

Exemplo 2

The following example closes all databases with the CLOSE DATABASES command and opens the Visual FoxPro sample database, TestData.dbc, with the OPEN DATABASE command and the Customer table with the USE command.

The INDEX command creates a standalone index (.idx) file named CityComp from a substring of the first five characters of the City field and the first six characters of the Company field using the SUBSTR( ) function. This index file orders records in the table primarily according to the City field and secondarily according to the Company field. Visual FoxPro clears the main Visual FoxPro window with the CLEAR command, and the DISPLAY STATUS command displays information about the index file, CityComp.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\TestData')
USE Customer
INDEX ON SUBSTR(City,1,5) + SUBSTR(Company,1,6) TO CityComp
CLEAR
DISPLAY STATUS
```

Exemplo 3

The following example closes all databases with the CLOSE DATABASES command, and opens the Visual FoxPro sample database, TestData.dbc, with the OPEN DATABASE command and the Customer table with the USE command.

Os comandos INDEX criam um arquivo de índice composto estrutural (.cdx) com duas tags: um baseado no campo Endereço chamado Endereço e outro baseado no campo Empresa chamado Empresa. Se um arquivo de índice composto estrutural foi criado anteriormente para a tabela, as duas tags são adicionadas ao arquivo existente.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\TestData')
USE Customer
INDEX ON company TAG company
INDEX ON address TAG address
CLEAR
DISPLAY STATUS
```

Veja também
- CANDIDATE( ) Function
- PRIMARY( ) Function
- UNIQUE( ) Function
- ATAGINFO( ) Function
- CDX( ) Function
