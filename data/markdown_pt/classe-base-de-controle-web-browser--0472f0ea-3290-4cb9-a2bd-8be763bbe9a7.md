# Classe base de controle Web Browser

Esta subclasse do controle de navegador do Microsoft Internet Explorer fornece pontos de integração para código do Visual FoxPro e pode ser adicionada a um formulário.

| Categoria | Internet |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Internet |
| Classe | _Webbrowser4 |
| Biblioteca de classes | _webview.vcx |
| Classe pai | olecontrol |
| Exemplo | ...\Samples\Solution\Ffc\Webvwr.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou selecione Add to Project ou Add to Form no menu de atalho do item da Component Gallery. Em um formulário, o Visual FoxPro coloca o logotipo do Internet Explorer. Especifique uma URL apropriada no método Navigate. Em um projeto, você pode adicionar a classe ou criar uma subclasse.

Consulte Diretrizes para usar classes base do Visual FoxPro para obter mais informações.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| aHistory[1,2] property | Matriz do histórico de endereços URL. Padrão: .F. |
| aParam[1,0] property | Matriz de parâmetros de URL. Padrão: .F. |
| aScripts[1,0] property | Matriz de scripts do Visual FoxPro. Padrão: .F. |
| cAlias property | Retorna o alias da tabela selecionada. Definida automaticamente por OpenTable. Padrão: "" |
| cBeforeURL property | Especifica a URL atual antes da recuperação completa do documento. Padrão: "" |
| cBlankHTMLFile property | Especifica um arquivo .htm vazio. Padrão: Blank.htm |
| cDBF property | Retorna o nome do arquivo da tabela selecionada. Definida automaticamente por OpenTable. Padrão: "" |
| cDBFPath property | Retorna o caminho da tabela selecionada. Definida automaticamente por OpenTable. Padrão: "" |
| cFilename property | Retorna o nome do arquivo do documento atual. Padrão: "" |
| cFilepath property | Retorna o caminho do documento atual. Padrão: "" |
| cLasturl property | Especifica a última URL. Padrão: "" |
| cNewURL property | Especifica a URL antes da recuperação completa do documento. Padrão: "" |
| cParam property | Especifica a cadeia de parâmetros da URL. Padrão: "" |
| cParamdelimiter property | Especifica o caractere delimitador dos parâmetros da URL. Padrão: & |
| cParseFileExt property | Lista de extensões analisadas no modo de pré-processamento. Padrão: htm;html;asp |
| cProgramPath property | Especifica o caminho da classe do controle. Padrão: "" |
| cSourceFile property | Especifica o nome do arquivo do documento atual. Padrão: "" |
| cSourceFilename property | Especifica o nome do arquivo do documento de origem atual. Padrão: "" |
| cSourceFilepath property | Especifica o caminho do documento de origem atual. Padrão: "" |
| cSourceHTML property | Especifica o texto HTML do documento de origem atual. Padrão: "" |
| cSourceURL property | Especifica a URL do documento de origem atual. Padrão: "" |
| cTempFilename property | Especifica o nome do arquivo temporário. Padrão: "" |
| cTempFilePrefix property | Prefixo do nome do arquivo temporário. Padrão: _temp |
| cURL property | URL atual. Padrão: "" |
| cUserID property | ID de usuário definido pelo usuário e não usado internamente. Padrão: "" |
| cUserName property | Nome de usuário definido pelo usuário e não usado internamente. Padrão: "" |
| cVersion property | Especifica a versão da subclasse. Padrão: "Web Browser 04.01.0006" |
| cVFPScript property | Especifica o arquivo de programa de script do Visual FoxPro. Padrão: "" |
| cVFPScriptTable property | Especifica o arquivo de tabela de scripts do Visual FoxPro. Padrão: "" |
| cVFPSprotocol property | Especifica a cadeia de protocolo padrão dos scripts. Padrão: vps: |
| lBlankHTMLStartup property | Especifica se o navegador inicia com página em branco. Padrão: .F. |
| lBusy property | Modo ocupado do navegador. Padrão: .F. |
| lDebug property | Especifica se o navegador executa no modo Debug. Padrão: .F. |
| lDesign property | Especifica se o navegador executa no modo de design. Padrão: .F. |
| lDHTML property | Especifica se há suporte a HTML dinâmico. Padrão: .T. |
| lHistoryEnabled property | Especifica se o rastreamento do histórico está habilitado. Padrão: .F. |
| lParseSource property | Especifica se o modo de análise da origem está habilitado. Padrão: .F. |
| lRefresh property | Especifica se o controle é atualizado por Refresh. Padrão: .F. |
| lRefreshDeactivate property | Especifica se RefreshDeactivate é executado automaticamente em LostFocus. Padrão: .F. |
| lRefreshMode property | Especifica se o modo de atualização do documento está habilitado. Padrão: .F. |
| lRelease property | Especifica se Release foi executado e o objeto está sendo liberado da memória. Padrão: .F. |
| lRunCodeMode property | Especifica se o modo de execução de código está habilitado. Padrão: .F. |
| lVFPsScript property | Especifica se o modo de script do Visual FoxPro está habilitado. Padrão: .F. |
| lViewSourceMode property | Especifica se o modo de exibição da origem está habilitado. Padrão: .F. |
| nDataSessionID property | Especifica a sessão de dados da tabela selecionada, definida por OpenTable. Padrão: 0 |
| nHistoryCount property | Especifica o comprimento da matriz de histórico. Padrão: 0 |
| nParamCount property | Especifica o comprimento da matriz de parâmetros. Padrão: .F. |
| nRecno property | Especifica o número do registro atual da tabela selecionada, definido por OpenTable. Padrão: 0 |
| nScriptCount property | Especifica o comprimento da matriz de scripts. Padrão: 0 |
| nUserLevel property | Nível de usuário definido pelo usuário e não usado internamente. Padrão: 0 |
| oAction property | Objeto de ação definido pelo usuário e não usado internamente. Padrão: .NULL. |
| oHost property | Formulário host, equivalente a THISFORM. Padrão: .NULL. |
| oSource property | Objeto de origem definido pelo usuário e não usado internamente. Padrão: .NULL. |
| oUser property | Objeto de usuário definido pelo usuário e não usado internamente. Padrão: .NULL. |
| uResult property | Especifica o valor Variant do resultado. Padrão: .T. |
| uReturn property | Especifica o valor Variant de retorno. Padrão: .T. |
| uValue property | Valor Variant definido pelo usuário e não usado internamente. Padrão: .T. |
| AddProp method | Adiciona uma propriedade. Sintaxe: AddProp(tcName, tcProperty, tuValue). tcName especifica o nome; tcProperty, a propriedade; tuValue, o valor. |
| BeforeNavigate method | Fornece um evento BeforeNavigate. Sintaxe: BeforeNavigate(URL, flags, targetframename, postdata, headers, cancel). URL é a página; flags controla histórico, cache e nova janela; targetframename é o quadro; postdata são dados HTTP Post; headers são cabeçalhos HTTP; cancel indica cancelamento. |
| BeforeRetrieval method | Identifica o evento anterior à recuperação. Sintaxe: BeforeRetrieval(URL, flags, targetframename, postdata, headers, cancel). Os argumentos têm os mesmos significados de BeforeNavigate. |
| BrowseTable method | Navega pela tabela selecionada com base em cAlias. Sintaxe: BrowseTable(tcAlias, tcClauses) |
| CloseTable method | Fecha a tabela selecionada com base em cAlias. Sintaxe: CloseTable(tcAlias) |
| EditScript method | Edita um script do Visual FoxPro. Sintaxe: EditScript(tcScriptName). tcScriptName especifica o nome. |
| EditString method | Abre uma cadeia em uma janela de edição. Sintaxe: EditString(tcString, tcTitle, tlNoEdit). Os argumentos especificam a cadeia, o título e se ela é editável. |
| EraseTempFile method | Apaga o arquivo temporário atual. Sintaxe: EraseTempFile( ). Retorno: nenhum. Argumentos: nenhum. |
| FileToString method | Retorna o conteúdo de um arquivo como cadeia. Sintaxe: FileString(tcFileName). tcFileName especifica o arquivo. |
| FrameBeforeNavigate method | Fornece um evento FrameBeforeNavigate. Sintaxe: FrameBeforeNavigate(URL, flags, targetframename, postdata, headers, cancel). Os argumentos têm os mesmos significados de BeforeNavigate. |
| GetHTML method | Retorna o HTML do documento atual. Sintaxe: GetHTML(tcName, tcAlias). tcName especifica o documento; tcAlias, o alias de cVFPScriptTable. |
| GetSourceFile method | Retorna o nome do arquivo do documento de origem atual. Sintaxe: GetSourceFile( ). Sem argumentos. |
| GetSourceHTML method | Retorna o HTML do documento de origem atual. Sintaxe: GetSourceHTML( ). Sem argumentos. |
| GoBack method | Volta um hiperlink no histórico. Sintaxe: GoBack( ). Sem retorno ou argumentos. |
| GoForward method | Avança um hiperlink no histórico. Sintaxe: GoForward( ). Sem retorno ou argumentos. |
| Msgbox method | Manipula caixas de mensagem. Sintaxe: Msgbox(tcMessage, tnType,tcTitle). Especifica mensagem, tipo e título. |
| NavigateComplete method | Fornece um evento NavigateComplete. Sintaxe: NavigateComplete(URL). URL especifica a página. |
| NewWindow method | Fornece um evento NewWindow. Sintaxe: NewWindow(URL, flags, targetframename, postdata, headers, processed). Os argumentos especificam página, opções, quadro, dados Post, cabeçalhos e processamento. |
| OpenTable method | Abre a tabela e a ativa como atual definindo cAlias. Sintaxe: OpenTable(tcFileName, tcAlias,tlExclusive, tcFilter). Especifica arquivo, alias, uso EXCLUSIVE e filtro. |
| OpenVFPScript method | Abre a tabela de scripts do Visual FoxPro. Sintaxe: OpenVFPScript( ). |
| ParseSource method | Analisa o código-fonte do documento HTML. Sintaxe: ParseSource(URL, flags, targetframename, postdata, headers, cancel). Os argumentos têm os mesmos significados de BeforeNavigate. |
| RefreshDeactivate method | Usado quando o controle perde o foco. Sintaxe: RefreshDeactivate( ). Sem argumentos. |
| RefreshMode method | Define o modo de atualização. Sintaxe: Refresh( ). Sem argumentos. |
| RefreshSource method | Atualiza a origem. Sintaxe: RefreshSource( ). Sem retorno ou argumentos. |
| ReleaseHost method | Libera o formulário host. Sintaxe: ReleaseHost( ). Sem argumentos. |
| RunAction method | Executa um método específico do objeto de oAction. Sintaxe: RunAction(tcMethod). tcMethod especifica o método. |
| RunCode method | Executa um bloco de código do Visual FoxPro sem compilação. Sintaxe: RunCode(tcCode). |
| RunScript method | Executa um script do Visual FoxPro. Sintaxe: RunScript(tcScript, tcAlias). Especifica o script e o alias de seu arquivo. |
| SetBusyState method | Define o estado ocupado. Sintaxe: SetBusyState(tlBusy). tlBusy indica se há download em andamento. |
| SetParam method | Define parâmetros de URL. Sintaxe: SetParam(tcParam). |
| SkipRecord method | Pula registros da tabela selecionada com base em cAlias. Sintaxe: SkipRecord(tnRecords). tnRecords é a quantidade. |
| StringToFile method | Salva uma cadeia em arquivo. Sintaxe: StringToFile(tcText, tcFileName). Especifica o texto e o arquivo de destino. |
| TrimExt method | Retorna um nome sem extensão. Sintaxe: TrimExt(tcFileName, tlPlatformType). Retorno: cFilename. tlPlatformType indica DOS ou Unix. |
| TrimFile method | Retorna o caminho do arquivo especificado. Sintaxe: TrimFile(tcFileName, lPlatType). lPlatType indica DOS ou Unix. |
| TrimPath method | Retorna o nome sem caminho. Sintaxe: TrimPath(tcFileName, tlTrimExt, tlPlatformType). Os argumentos especificam arquivo, remoção da extensão e plataforma. |
| ValidateURL method | Valida a URL. Sintaxe: ValidateURL(tcURL). |
| ValidURL method | Retorna a URL validada. Sintaxe: ValidURL(tcURL). |
| VFPS method | Executa um script do Visual FoxPro com base na URL. Sintaxe: VFPS(tcCommand). |
| VFPScript method | Executa um script específico. Sintaxe: VFPScript( tcName , tcAlias , tnCode ). Os argumentos especificam arquivo, alias da tabela e código. |
| ViewSource method | Exibe a origem do documento atual. Sintaxe: ViewSource(tlNoWait, tlNoEdit). Os argumentos indicam pausa e possibilidade de edição. |
| WaitWindow method | Encapsula uma janela Wait. Sintaxe: WaitWindow(tcText, tlWait). Especifica o texto e se o programa pausa. |
| WildcardMatch method | Retorna verdadeiro (.T.) se o padrão curinga corresponder à cadeia. Sintaxe: WildcardMatch(tcMatchExpList, tcExpressionSearched, tlMatchAsIs). Retorno: lMatch. Os argumentos especificam padrão, expressão alvo e correspondência exata. |
