# Classe base ReportListener Base Foundation

A classe _ReportListener serve como superclasse para as outras classes em _REPORTLISTENER.VCX, semelhante às superclasses para outras classes base do Visual FoxPro disponíveis em _BASE.VCX.

| Categoria | Reporting |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Output\Report Listeners |
| Classe | _ReportListener |
| Classe base | ReportListener |
| Biblioteca de classes | _REPORTLISTENER.vcx |
| Classe pai | ReportListener ( Objeto ReportListener ) |

# Observações

_ReportListener adiciona tratamento de erros semelhante às classes _BASE e inclui outros recursos principais específicos das responsabilidades dos objetos ReportListener ao auxiliar o Report Engine durante a execução de um comando REPORT FORM ou LABEL FORM.

Essas responsabilidades incluem:
 - Tratamento de DataSession . Object-Assisted Reporting requer manipulação potencial de várias sessões de dados diferentes.
- Avaliação do estado do relatório . _ReportListener dá às suas classes descendentes a capacidade de determinar se certas operações são seguras de executar em um determinado momento. Por exemplo, durante uma execução de relatório, não é seguro alternar entre impressoras diferentes.
- Cadeia de responsabilidade. _ReportListener implementa um padrão Chain of Responsibility, também conhecido como successorship , para permitir vários formatos de saída durante uma execução de relatório.
- Gerenciamento de vários relatórios . Você pode usar _ReportListener como um wrapper orientado a objetos para um comando REPORT FORM ou uma coleção de comandos REPORT FORM em sequência.

A tabela a seguir lista propriedades e métodos públicos adicionados por esta classe à sua classe pai, ReportListener.

| Propriedades e métodos | Descrição |
| --- | --- |
| Método addReport | Adiciona à coleção ReportFileNames da classe, associando opcionalmente cláusulas REPORT FORM e um ReportListener para o relatório especificado. Sintaxe: addReport(cFRXName [, cClauses[, toListener]] ) Valores de retorno: Nenhum Parâmetros: cFRXName fornece o nome do arquivo de relatório ou etiqueta a executar. cClauses fornece as cláusulas opcionais para esta execução de relatório, incluindo escopo, intervalo e instruções de janela. oListener fornece uma referência opcional a ser adicionada por _ReportListener ao executar este relatório específico. |
| Propriedade appName | Contém uma cadeia de nome de aplicativo para uso em feedback ao usuário. Padrão "VFP Report Listener" Observações : Consulte REPORTLISTENERS_LOCS.H, que fornece o valor localizável ao qual esta propriedade é definida no método Init da classe. Classes descendentes em _REPORTLISTENERS.vcx substituem esta configuração com valores adicionais #DEFINEd em REPORTLISTENERS_LOCS.H. |
| Método clearErrors | Redefine o status de erro da classe. Sintaxe: clearErrors() Valores de retorno: Nenhum Parâmetros: Nenhum. Observações: Algumas subclasses podem não funcionar normalmente após uma execução de relatório falhar. Este método é útil para redefinir o estado de _ReportListener antes de uma execução de relatório subsequente. |
| Método getLastErrorMessage | Fornece informações sobre o último erro que ocorreu. Sintaxe: getLastErrorMessage() Valores de retorno: cErrorMessage Parâmetros: Nenhum. |
| Propriedade isSuccessor | Indica se este ReportListener está encadeado a um ou mais outros para fornecer saída durante uma execução de relatório. Quando .T., este ReportListener não foi o objeto referenciado nas cláusulas OBJECT do comando REPORT FORM. Padrão .F. |
| Propriedade lIgnoreErrors | Fornece um sinalizador para determinar como esta classe trata atividades subsequentes a um erro. Padrão .F. Observações: Esta propriedade garante que _ReportListener e suas classes descendentes sigam o modelo de tratamento de erros _BASE. |
| Método prepareErrorMessage | Organiza valores comuns de informação de erro (nError, cMethod, nLine, cName, cMessage, cCodeLine) em uma cadeia coerente para apresentação ao usuário. Sintaxe: prepareErrorMessage(nError, cMethod, nLine, cName, cMessage, cCodeLine) Valores de retorno: cErrorMessage Parâmetros: Você pode derivar todos os parâmetros deste método, exceto cName, de funções nativas de tratamento de erros do Visual FoxPro ou das propriedades equivalentes de um objeto da Classe Exception (Visual FoxPro) . O parâmetro cName representa o nome que você deseja apresentar na cadeia de mensagem de erro como identificador do seu aplicativo. Por exemplo: LOCAL oListener, oError oListener = ; NEWOBJECT("_ReportListener", ; "_REPORTLISTENER") TRY * … run some commands here CATCH TO oError IF NOT (ISNULL(oError)) oListener.DoMessage(; oListener.PrepareErrorMessage(; oListener.ErrorNo, ; oListener.Procedure, ; oListener.LineNo, ; "My application", ; oError.Message, ; oError.LineContents)) ENDIF FINALLY * more commands here ENDTRY |
| Método removeReports | Remove nomes de arquivos de relatório, bem como cláusulas associadas e referências ReportListener das várias coleções desta classe. Sintaxe: removeReports() Valores de retorno: Nenhum Parâmetros: Nenhum. |
| Propriedade reportUsesPrivateDataSession | Fornece um sinalizador para indicar se este relatório compartilha a sessão de dados da qual foi executado ou mantém uma sessão de dados privada. Padrão .F. |
| Método runReports | Executa uma série de comandos REPORT FORM de acordo com as instruções nas coleções internas ReportFileNames, ReportClauses e ReportListeners. Opcionalmente limpa a coleção após a execução e emite os comandos REPORT FORM sem referências OBJECT. Sintaxe: . runReports([lRemoveReportsAfterRun[, lOmitListenerReferences]]) Valores de retorno: Nenhum Parâmetros: lRemoveReportsAfterRun determina se a coleção interna de relatórios da classe é limpa depois que o método runReports executa sua sequência de comandos REPORT FORM. lOmitReferences determina se o método inclui referências OBJECT em cada comando REPORT FORM. Observações: Especificar .T. como o segundo argumento deste método tem precedência sobre qualquer referência ReportListener que o método poderia adicionar aos seus comandos REPORT FORM unilateralmente. No entanto, isso não significa necessariamente que seus relatórios serão executados sem assistência de ReportListener. Se você usou o comando SET REPORTBEHAVIOR 90 antes de usar este método, o Report Engine ainda obterá uma referência a um ReportListener do tipo apropriado do Report Output Application e a adicionará aos seus comandos REPORT FORM. Você também pode ter especificado a cláusula OBJECT para um ou mais comandos REPORT FORM quando adicionou esses comandos à coleção de relatórios de _ReportListener. Se você não especificou tlOmitReferences como .T. , _ReportListener verifica cada comando REPORT FORM antes de executá-lo para ver se você já incluiu uma cláusula OBJECT no comando. Se você fez isso, sua cláusula OBJECT entra em vigor; o ReportListener que você especificou será a referência de objeto usada para este comando. Se você não incluiu uma cláusula OBJECT, você pode ter armazenado em sua coleção interna ReportListener ao adicionar este comando REPORT FORM à coleção interna. _ReportListener adiciona esta referência ao seu comando REPORT FORM se necessário. Se você não especificou um ReportListener ao adicionar o relatório e não especificou lOmitReferences como .T. , _ReportListener adiciona uma referência a si mesmo em uma cláusula OBJECT <ref> no comando REPORT FORM. |
| Método setSuccessorDynamicProperties | Fornece um gancho para a classe compartilhar informações alteradas pelo Report Engine com uma sucessão de ReportListeners durante uma execução de relatório. Sintaxe: setSuccessorDynamicProperties() Valores de retorno: Nenhum Parâmetros: Nenhum. Observações: Abstrato neste nível de classe. |
| Propriedade sharedGdiplusGraphics | Fornece uma cópia de leitura/gravação do handle GDIPlusGraphics do Engine que o ReportListener pode compartilhar com uma cadeia de sucessão. Padrão 0 |
| Propriedade sharedOutputPageCount | Fornece uma cópia de leitura/gravação da propriedade OutputPageCount do Engine que o ReportListener pode compartilhar com uma cadeia de sucessão. Padrão 0 |
| Propriedade sharedPageHeight | Compartilha informações coletadas pelo método GetPageHeight com outros ReportListeners vinculados em uma cadeia de sucessão. Padrão 0 |
| Propriedade sharedPageNo | Fornece uma cópia de leitura/gravação da propriedade PageNo do Engine que o ReportListener pode compartilhar com uma cadeia de sucessão. Padrão 0 |
| Propriedade sharedPageTotal | Fornece uma cópia de leitura/gravação da propriedade PageTotal do Engine que o ReportListener pode compartilhar com uma cadeia de sucessão. Padrão 0 |
| Propriedade sharedPageWidth | Compartilha informações coletadas pelo método GetPageWidth com outros ReportListeners vinculados em uma cadeia de sucessão. Padrão 0 |
| Propriedade successor | Armazena uma referência de objeto ao próximo ReportListener em uma cadeia de sucessão. Padrão .NULL. Observações: Consulte o tópico sobre UpdateListener ( Classe base ReportListener User Feedback Foundation ) para um exemplo de ReportListeners em uma cadeia de sucessão. |

# Exemplo

O exemplo de código a seguir mostra como você pode usar _ReportListener para gerenciar uma coleção de comandos REPORT FORM. XmlListener é uma subclasse de _ReportListener, portanto pode usar essa capacidade. Neste exemplo, você encadeia dois relatórios para gerar um único documento XML.

```foxpro
LOCAL ox
ox = NEWOBJECT("XmlListener","_ReportListener")
ox.AddReport(GETFILE("frx"),"NOPAGEEJECT")
ox.AddReport(GETFILE("frx")
ox.RunReports(.T.)
```
