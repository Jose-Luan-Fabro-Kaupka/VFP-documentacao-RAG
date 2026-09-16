# Classe de fundação Table Mover

Esta subclasse da classe de fundação de caixa de listagem field mover carrega automaticamente tabelas e campos da fonte de dados atual.

| Categoria | Movers |
| --- | --- |
| Catálogo padrão | Catálogo Visual FoxPro/Classes de fundação/Controles de usuário |
| Classe | _tablemover |
| Classe base | Container |
| Biblioteca de classes | _mover.vcx |
| Classe pai | _fieldmover |
| Exemplo | ...\Samples\Solution\Ffc\movers.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do item da Galeria de componentes, selecione Adicionar ao projeto ou Adicionar ao formulário. Quando você adiciona a classe a um projeto, pode escolher entre adicionar a classe ou criar uma subclasse. Quando você adiciona a classe a um formulário, o Visual FoxPro abre um construtor para que você possa aceitar ou especificar os valores apropriados de cDBCTable, cDBCName, SkipGeneral, SkipMemo, AllowReadOnly e AllowQuery no formulário no Form Designer.

Consulte Diretrizes para usar classes de fundação do Visual FoxPro para obter mais informações sobre o uso de classes de fundação.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade AllowQuery | Especifica se consultas são permitidas. Padrão: .F. |
| Propriedade AllowViews | Especifica se views são permitidas. Padrão: .T. |
| Propriedade ExclDBF | Especifica o nome da tabela a excluir da lista. Padrão: "" |
| Propriedade ViewNoData | Especifica se exibir informações de view sem recuperar dados. Padrão: .T. |
| Método GetDBCAlias | Recupera o alias do arquivo de banco de dados (.dbc). Sintaxe: GetDBCAlias(cDBC) Retorno: nenhum Argumentos: cDBC especifica o alias do banco de dados. |
| Método GetDBCData | Recupera campos de tabela de banco de dados. Sintaxe: GetDBCData(cDBCName) Retorno: campos de dados Argumentos: cDBCName especifica o nome do banco de dados. |
| Método GetDBCName | Recupera o nome do banco de dados. Sintaxe: GetDBCName( ) Retorno: nenhum Argumentos: nenhum |
| Método GetDBCTable | Recupera a tabela de banco de dados. Sintaxe: GetDBCTable(cDBCTable) Retorno: nenhum Argumentos: cDBCTable especifica o nome curto da tabela. |
| Método GetFreeData | Recupera campos de tabela livre. Sintaxe: GetFreeData( ) Retorno: nenhum Argumentos: nenhum |
| Método MoverRefresh | Atualiza os movers. Sintaxe: MoverRefresh(lRefresh, lQuickPass, cSaveLstValue) Retorno: nenhum Argumentos: lRefresh especifica se repovoar caixas de listagem e popups. lQuickPass especifica se restaurar se o ambiente estiver inalterado. cSaveLstValue especifica o valor a restaurar. |
| Método OpenTable | Abre a fonte de dados. Sintaxe: OpenTable( ) Retorno: nenhum Argumentos: nenhum |
| Método UseTable | Trata qual tabela é aberta com USE e se a tabela é aberta exclusivamente. Sintaxe: UseTable(cGetDBF, lUseExcl) Retorno: nenhum Argumentos: cGetDBF especifica a tabela a usar. lUseExcl especifica se a tabela é aberta exclusivamente. |
| Método ExclusiveSet | Interno à classe. |
| Método RefreshCurrent | Interno à classe. |
| Método TableChange | Interno à classe. |
