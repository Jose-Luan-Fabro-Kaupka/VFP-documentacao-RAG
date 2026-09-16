# Classe básica Error Object

Esta classe é um manipulador de erros genérico que funciona tanto para código orientado a objetos quanto procedural. Ela é usada com uma estrutura de aplicação gerada pelo Assistente de Aplicações.

| Categoria | Aplicação |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Application |
| Classe | _error |
| Classe base | Custom |
| Biblioteca de classes | _app.vcx |
| Classe pai | _custom |
| Exemplo | ...\Samples\Solution\Ffc\error.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do item da Galeria de Componentes, selecione Add to Project ou Add to Form. Ao adicionar a classe a um formulário, o Visual FoxPro coloca seu ícone no formulário. Você pode então especificar os valores apropriados das propriedades e acessar sua funcionalidade a partir de objetos de entrada e saída. Ao soltar a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Diretrizes para usar classes básicas do Visual FoxPro para obter mais informações.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Método GetMessageBoxTitle | Retorna o controle realmente ativo, loRealActiveControl, nos casos em que o controle ativo atual é um Grid. Sintaxe: GetActiveControlRef(toActiveControl) Retorno: ERROR_MESSAGEBOX_TITLE_LOC Argumentos: nenhum |
| Propriedade cCurrentMessage. | Especifica a mensagem de erro. Padrão: "" |
| Propriedade cCurrentMethod | Especifica o método em que ocorreu o erro. Padrão: "" |
| Propriedade iCurrentError | Especifica o número do erro. Padrão: 0 |
| Propriedade iCurrentLine | Especifica a linha em que ocorreu o erro. Padrão: 0 |
| Propriedade cCurrentClass | Especifica a classificação definida pelo objeto de erro para esse número de erro. Padrão: "" |
| Propriedade lServer | Verifica _VFP.StartMode para determinar se qualquer feedback modal deve ser evitado devido à forma como o Visual FoxPro foi iniciado. Padrão: (BETWEEN(_VFP.StartMode,1,3))) |
| Propriedade cLogAlias | Especifica o nome do alias do log. Padrão: "" |
| Propriedade cLogDBF | Especifica o nome do arquivo de log (DBF) criado pelo objeto _error. Padrão: "" |
| Propriedade lUserCancelled | Permite que o programa externo execute as operações de limpeza necessárias antes da liberação. Padrão: .F. |
| Método HandleMain | Rotina que trata o erro. Sintaxe: HandleMain(tiError, tcMethod, tiLine) Retorno: nenhum. Argumentos: tiError especifica o número do erro; tcMethod, o nome do método atual; tiLine, o número da linha atual. |
| Método OKToReport | Classe abstrata para avaliar se o erro deve ser relatado. Sintaxe: OKToReport( ) Retorno: nenhum Argumentos: nenhum |
| Método isTrivial | Especifica se um erro é trivial. Sintaxe: IsTrivial(tlWantDialog box) Retorno: nenhum. Argumentos: tlWantDialog box especifica uma caixa de diálogo opcional a exibir. |
| Método isFatal | Especifica se um erro é fatal. Sintaxe: isFatal( ) Retorno: nenhum. Argumentos: tlWantDialog box especifica uma caixa de diálogo opcional a exibir. |
| Método GetMessageBoxTitle | Destina-se a ser preenchido por sua subclasse ou instância com informações específicas da aplicação. Sintaxe: GetMessageBoxTitle( ) Retorno: nenhum Argumentos: nenhum |
| Método DisplayErrorLog | Exibe o log de erros. Sintaxe: DisplayErrorLog( ) Retorno: nenhum Argumentos: nenhum |
| Método OKToContinue | Avalia um erro para determinar se a execução do programa deve continuar. Sintaxe: OKToContinue( ) Retorno: nenhum Argumentos: nenhum |
| Método SetLog | Determina o nome da tabela e do alias do log de erros ou os cria. Sintaxe: SetLog( ) Retorno: cLogAlias. A tabela de log tem o seguinte formato:CREATE TABLE (THIS.cLogDBF) ; (errstamp t, ; listing m,; usernotes m) Argumentos: nenhum |
| Propriedade cCurrentErrorParam | Interna à classe. |
| Propriedade aErrorClass[1,3] | Interna à classe. |
| Propriedade aErrors[1,6] | Interna à classe. |
| *FillArrays. | Interno à classe. |
| Método LogErrorReport | Interno à classe. |
| Método GetErrorAttribute | Interno à classe. |
| Método isGoodErrorLog | Interno à classe. |
| Método UserHandlesError | Interno à classe. |
| Método UserCancelled | Interno à classe. |
| Método FillLogRecord | Interno à classe. |
| Método DoErrorLogUI | Interno à classe. |
