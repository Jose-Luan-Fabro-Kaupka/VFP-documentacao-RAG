# Classe foundation Mail Merge Object

Esta classe personalizada usa o mecanismo Mail Merge Wizard para gerar um documento Microsoft Word Mail Merge.

| Category | Automation |
| --- | --- |
| Default Catalog | Visual FoxPro Catalog\Foundation Classes\Automation |
| Class | mailmerge |
| Base Class | Custom |
| Class Library | mailmrge.vcx |
| Parent Class | automation |
| Sample | ...\Samples\Solution\Ffc\Automate.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho Component Gallery Item, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, especifique a tabela FROM (cDataPath), o local e a versão do Word (cExe e cWordVersion) e outros valores de propriedade apropriados. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

| Properties, Events, Methods | Description |
| --- | --- |
| aWPMrg[2,0] property | Uma matriz de procedimentos para lidar com vários estilos de mesclagem. Padrão: .F. |
| cDataFile property | Uma cópia FoxPro 2.6 de uma tabela Visual FoxPro 3.0 ou posterior. Padrão: "" |
| cDataPath property | Especifica o caminho para a tabela FROM. Padrão: "" |
| cDataSrc property | Especifica a fonte de dados para a conexão ODBC. Padrão: "" |
| cDocName property | Especifica o nome do arquivo .doc existente. Padrão: "" |
| cExe property | Especifica o caminho completo para o aplicativo Microsoft Word. Padrão: "" |
| cODBCSource property | Especifica a cadeia de conexão ODBC. Padrão: "" |
| cSaveFile property | Especifica o arquivo para armazenar dados mesclados. Padrão: "" |
| CSQLstmt property | Uma instrução SQL para extrair dados. Padrão: "" |
| CSQLstmt2 property | Especifica uma instrução SQL adicional, se cSQLStmt for maior que 255 caracteres (para Microsoft Word). Padrão: "" |
| cWordVersion property | Especifica a versão do Microsoft Word instalada (por exemplo, '8'). Padrão: "" |
| lAlerted property | Especifica se um alerta de falha foi emitido. Padrão: .F. |
| lEnglish property | Verifica se o Microsoft Word reconhece comandos Word Basic em inglês. Padrão: .F. |
| lHasVerWord property | Verifica a presença do Microsoft Word. Padrão: .F. |
| nNewDoc property | Indica se um novo documento será usado (consulte Mailmrge.h). Padrão: 1 |
| nTemplate property | Especifica o tipo de documento principal. Aplica-se apenas ao Microfot Word. Consulte Mailmrge.h. Padrão: 1 |
| nWordProc property | Especifica o processador de texto selecionado. Consulte Mailmrge.h. Padrão: 1 |
| SysCh property | Especifica um canal DDE. Padrão: - 1 |
| CheckVer method | Verifica a versão do Microsoft Word em uso. Interno à classe. Sintaxe: CheckVer( ) Retorno: nenhum Argumentos: nenhum |
| GetMSW method | Recupera a linha de comando do Microsoft Word do registro. Sintaxe: GetMSW(m.cversion) Retorno: o caminho completo para o Microsoft Word Argumentos: m.cversion especifica a versão do Microsoft Word em uso. |
| MrgCommaDel method | Gera um arquivo de texto delimitado por vírgulas a partir de dados. Sintaxe: MrgCommaDel( ) Retorno: um arquivo delimitado por vírgulas Argumentos: nenhum |
| MrgWord method | Determina as versões do Microsoft Word a serem usadas na mesclagem. Sintaxe: MrgWord( ) Retorno: nenhum Argumentos: nenhum |
| MSWerr method | O manipulador de erros para uso enquanto o AppleScript está sendo executado. Sintaxe: MSWerr( ) Retorno: nenhum Argumentos: nenhum |
| GetSQLst method | Recupera a instrução SQL para extrair dados. Interno à classe. Sintaxe: GetSQLst( ) Retorno: nenhum Argumentos: nenhum |
| PrepData method | Determina o tipo de fonte de dados que está sendo usada para a mesclagem de correspondência e normaliza os dados para processamento. Interno à classe. Sintaxe: PrepData( ) Retorno: nenhum Argumentos: nenhum |
| SaveSQL method | Gera uma tabela de resultados SQL. Interno à classe. Sintaxe: SaveSQL( ) Retorno: nenhum Argumentos: nenhum |
| WzMMData method | Copia dados para um arquivo de texto. Interno à classe. Sintaxe: WzMMData( ) Retorno: nenhum Argumentos: nenhum |
| MakeFieldList | Interno à classe. |
| MailMergeWord8 | Interno à classe. |
| MailMergeWord6 | Interno à classe. |
| MSWmldlg | Interno à classe. |
| Startword | Interno à classe. |
| MailMergeMacWord6 | Interno à classe. |
| MMCleanup method | Fecha arquivos - Interno à classe. |
