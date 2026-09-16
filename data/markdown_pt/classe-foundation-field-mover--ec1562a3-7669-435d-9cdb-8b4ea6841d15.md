# Classe Foundation Field Mover

Esta é uma classe de list box mover super que carrega automaticamente campos da fonte de dados atual quando você a solta em um formulário.

| Categoria | Movers |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\User Controls |
| Classe | _fieldmover |
| Classe base | Container |
| Biblioteca de classes | _mover.vcx |
| Classe pai | _supermover |
| Exemplo | ...\Samples\Solution\Ffc\movers.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do item do Component Gallery, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro abre um builder para que você possa aceitar ou especificar os valores apropriados de SkipGeneral, SkipMemo e AllowReadOnly. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Diretrizes para usar Foundation Classes do Visual FoxPro para obter mais informações sobre o uso de foundation classes.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade AllowReadOnly | Permite uma fonte de dados somente leitura. Padrão: .F. |
| Propriedade AutoInit | Executa automaticamente quando carregado. Padrão: .T. |
| Propriedade CurrentAlias | O alias atual determinado por ALIAS( ). Padrão: "" |
| Propriedade CurrentDBC | O arquivo de banco de dados atual. Padrão: "" |
| Propriedade CursorType | Especifica o tipo de cursor. 1 = local view2 = remote view3 = table Padrão: 3 |
| Propriedade DBCTable | Nome da tabela no banco de dados. Padrão: "" |
| Propriedade MultiTable | Especifica se deve suportar várias tabelas. Padrão: .F. |
| Propriedade SkipGeneral | Especifica se campos General são incluídos na lista. Padrão: .F. |
| Propriedade SkipMemo | Especifica se campos Memo são incluídos na lista. Padrão: .F. |
| Propriedade TableType | Retorna o tipo de tabela - SYS(2029). Padrão: 0 |
| Método AcolScan | Varre uma coluna específica no array. Sintaxe: AcolScan(@wztarr, wztexpr, wztcol) Retorno: nenhum Argumentos: wztarr especifica o array a varrer. wztexpr especifica a expressão de destino para a qual varrer. wztcol especifica a coluna a varrer. |
| Método AddToArray | Adiciona sContents ao array, aAddToArray , em iRow . Sintaxe: AddToArray(@aAddToArray, sContents, iRow) Retorno: nenhum Argumentos: aAddToArray especifica o array ao qual adicionar um item. sContents especifica a adição ao array. iRow especifica em qual linha do array inserir sContents . |
| Método Alert | Exibe uma messagebox. Sintaxe: Alert(pMessage) Retorno: nenhum Argumentos: pMessage especifica a mensagem a ser exibida por MESSAGEBOX( ). |
| Método FieldChange | Acionado quando os campos selecionados mudam. Sintaxe: FieldChange(nButton) Retorno: nenhum Argumentos: nButton especifica o botão pressionado. |
| Método GetTableData | Recupera campos de uma tabela. aWizFlist contém a lista de campos, aCalcFields contém a lista de campos calculados, aPickFields contém a lista de campos selecionados. Sintaxe: GetTableData( ) Retorno: aWizFList , aCalcFields , aPickFields Argumentos: nenhum |
| Método InitData | Inicializa dados. Sintaxe: InitData( ) Retorno: nenhum Argumentos: nenhum |
| Método InitVars | Inicializa variáveis usadas por movers. Sintaxe: InitVars( ) Retorno: nenhum Argumentos: nenhum |
| Método JustStem | Recupera o stem do nome do arquivo. Sintaxe: JustStem(m.filename) Retorno: m.filename Argumentos: m.filename especifica o nome do arquivo do qual o stem é extraído. |
| Método SetDataProps | Define propriedades de dados da fonte de dados. Sintaxe: SetDataProps( ) Retorno: nenhum Argumentos: nenhum |
| Método UpdateStatusbar | Interno à classe. |
