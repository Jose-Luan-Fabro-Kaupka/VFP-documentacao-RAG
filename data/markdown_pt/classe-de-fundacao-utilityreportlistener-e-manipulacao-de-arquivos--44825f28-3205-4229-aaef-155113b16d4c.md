# Classe de fundação UtilityReportListener e manipulação de arquivos

A classe UtilityReportListener adiciona opções de configuração em tempo de execução e manipulação de arquivos (verificação de nome de arquivo, gravação de arquivo) aos serviços principais fornecidos por sua classe pai, _ReportListener. Esta classe também fornece acesso a uma instância de FrxCursor, uma classe aproveitada do Report Builder Application, com tratamento de erro apropriado se não puder ser encontrada.

> **Observação:** UtilityReportListener não requer FrxCursor para funcionar; ele apenas fornece gerenciamento transparente de uma instância desta classe quando solicitado por uma subclasse. É responsabilidade das subclasses decidir quando e se precisam desta instância e se podem funcionar sem ela se não estiver disponível em tempo de execução.

| Categoria | Reporting |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Output\Report Listeners |
| Classe | UtilityReportListener |
| Classe base | ReportListener |
| Biblioteca de classes | _REPORTLISTENER.vcx |
| Classe pai | FXListener ( ReportListener FXListener Foundation Class ) |

# UtilityReportListener e sua tabela de configuração

UtilityReportListener lê registros de uma tabela de configuração para inicializar vários valores e comportamentos do ReportListener. Você pode escolher que UtilityReportListener execute essas tarefas quando a classe inicializa, no início de cada execução de relatório ou ambos. Você também pode chamar seu método setConfiguration explicitamente em outros momentos.

Os recursos de configuração em tempo de execução do UtilityReportListener aproveitam o mesmo formato de tabela de configuração que o Report Output Application usa para registrar ReportListeners personalizados para diferentes valores de ListenerType. Para obter informações sobre como o Report Output Application usa esta tabela, consulte Report Output Application.

> **Observação:** As classes usam o mesmo formato de tabela de configuração que o Report Output Application, mas não necessariamente a mesma tabela. Para determinar o comportamento desejado para uma instância de uma classe derivada de UtilityReportListener, use as propriedades e métodos da classe para especificar esse comportamento na tabela que o objeto usa, não na tabela que o Report Output Application usa.

Se você instanciar esta classe fora do Report Output Application, e se a tabela de configuração não parecer estar disponível, ela cria a estrutura de tabela apropriada. Se a classe estiver incorporada em um módulo (APP, DLL, EXE), ela cria esta tabela no mesmo diretório do módulo; caso contrário, criará a tabela no mesmo diretório da biblioteca de classes (VCX).

UtilityReportListener e suas subclasses usam o campo OBJTYPE na tabela de configuração para determinar quais registros pertencem a elas e para qual uso os registros devem ser colocados. Essas classes reservam um intervalo de valores no campo OBJTYPE, definido de 1000 a 1999.

Cada subclasse usa um único valor neste intervalo, determinado pela propriedade configurationObjType do UtilityReportListener, para designar registros na tabela que deseja usar para fins de configuração. UtilityReportListener usa um valor constante em REPORTLISTENER.H para definir seu próprio valor.

As tarefas de configuração podem definir qualquer propriedade ou invocar qualquer método em sua subclasse UtilityReportListener. Os registros na tabela de configuração com o valor correto de configurationObjType definem propriedades de classe ou invocam código de método de classe conforme o uso da tabela de configuração a seguir.

| Campo | Uso | Observações |
| --- | --- | --- |
| OBJTYPE | THIS.ConfigurationObjType | Determina quais registros na tabela o UtilityReportListener lê para definir valores de configuração ou acionar código de método de configuração. |
| OBJCODE | Precedência | Determina a ordem em que o UtilityReportListener executa as instruções dos registros de configuração. |
| OBJNAME | Propriedade ou Método | UtilityReportListener verifica OBJNAME para PEMSTATUS (existência e tipo). |
| OBJVALUE | Valor ou Argumentos | Se o valor OBJNAME é um nome de propriedade válido, UtilityReportListener usa este código para definir o valor da propriedade usando OBJVALUE: STORE EVAL(ObjValue) TO ("THIS."+ObjName) Se o valor OBJNAME é um nome de método válido para a classe, UtilityReportListener executa este código: EVAL("THIS."+ObjName+"("+ObjValue+")") |
| OBJINFO | Não usado | Reservado para documentação do usuário, comentários. Consulte a Dica abaixo para um exemplo. |

UtilityReportlistener ignora registros com OBJNAME ou OBJVALUE em branco e registros marcados DELETED(), independentemente de terem o valor OBJTYPE correto ou não.

> **Dica:** Quando UtilityReportListener gera uma tabela de configuração, ele fornece dois registros excluídos para mostrar a sintaxe correta para registros de configuração, usando o código a seguir:

```foxpro
INSERT INTO (ALIAS()) VALUES ;
  (OUTPUTCLASS_OBJTYPE_CONFIG,0,
   'DoMessage','"Welcome to the demo run!",64',
   'Sample initialization/config method call')
DELETE NEXT 1
INSERT INTO (ALIAS()) VALUES ;
  (OUTPUTCLASS_OBJTYPE_CONFIG,0,
   'TargetFileName','"xxx"',
   'Sample initialization/config property')
DELETE NEXT 1
```

# Observações

Provavelmente você não instanciará esta classe diretamente; instanciará uma das classes que derivam dela, como HtmlListener. Essas classes derivadas aproveitam os recursos base do UtilityReportListener, que são manipulação de arquivos e acesso a uma instância de objeto FrxCursor. Elas também expõem o recurso de tabela de configuração do UtilityReportListener para que você possa personalizar seu comportamento em tempo de execução, em muitos casos, sem precisar especificar essas alterações em seu código ou derivar subclasses delas.

A tabela a seguir lista propriedades e métodos públicos adicionados por esta classe à sua classe pai, _ReportListener.

| Propriedades e métodos | Descrição |
| --- | --- |
| configurationObjtype Property | Contém o valor reservado usado para indicar que uma linha da tabela de configuração fornece informações de configuração dinâmica em tempo de execução. Padrão 1000 |
| createConfigTable Method | Cria uma tabela de configuração sob demanda. Sintaxe: createConfigTable(cDBF [, lOverWrite] ) Valores de retorno: cDBF Parâmetros: cDBF é o nome de arquivo totalmente qualificado da tabela de configuração. lOverWrite indica se você deseja substituir a tabela de configuração se ela já existir. |
| frxCursor Property | Contém uma referência a um objeto auxiliar FRXCursor para auxiliar em cálculos em tempo de execução relacionados a metadados e estrutura FRX. Padrão .NULL. |
| getConfigTable Method | Avalia e fornece o nome da tabela de configuração atual, opcionalmente criando-a em disco se não estiver disponível. Sintaxe: getConfigTable(lForceExternal) Valores de retorno: cDBF Parâmetros: Se você definir lForceExternal como .T., isso indica que deseja ter uma tabela externa gravada em disco, mesmo se a classe puder encontrar uma versão integrada da tabela em seu módulo de código (APP, EXE ou DLL). |
| getPathForExternals Method | Determina o local em que a tabela de configuração atual e quaisquer outros arquivos externos necessários serão esperados. Sintaxe: getPathForExternals() Valores de retorno: cPath Parâmetros: Nenhum |
| loadFrxCursor Property | Determina se esta classe deve carregar dinamicamente uma instância da classe auxiliar. Padrão .F. |
| readConfiguration Property | Indica as condições sob as quais o código SetConfiguration será executado. 0=nunca 1 = quando a instância da classe Init é executada 2 = quando a instância da classe executa BeforeReport 3 = tanto em Init quanto em BeforeReport Padrão 0 |
| setConfiguration Method | Verifica a tabela de configuração atual para informações dinâmicas em registros do tipo apropriado e executa essas instruções se encontradas. Sintaxe: SetConfiguration() Valores de retorno: Nenhum Parâmetros: Nenhum |
| targetFileExt Property | Fornece a extensão de arquivo padrão para saída de arquivo. Padrão "TXT" |
| targetFileName Property | Fornece o nome de arquivo para o qual a saída será gravada. Um nome exclusivo é gerado para a instância da classe, que será substituído para execuções de relatório sucessivas se não ajustado pelo usuário. Padrão FORCEPATH (SYS(2015),SYS(2023)) |
| targetHandle Property | Fornece um identificador de arquivo de baixo nível, para o qual a saída é gravada diretamente quando a classe fornece dados brutos ao arquivo; caso contrário, reserva o arquivo durante a execução do relatório para que outras aplicações não gravem nele. Padrão -1 |
| verifyConfigTable Method | Confirma que o formato e o conteúdo da configuração atendem aos requisitos, ajustando se necessário. Sintaxe: verifyConfigTable(cAlias [, cFailureMsgTable [, cFailureMsgIndexes]]) Valores de retorno: logical Parâmetros: cAlias é o alias da tabela que você deseja validar. A tabela já deve estar aberta sob este alias quando você chamar o método. cFailureMsgTable fornece uma mensagem alternativa opcional para exibir se a tabela nomeada não puder ser verificada como tendo formato válido de tabela de configuração. Se você não fornecer esta mensagem, UtilityReportListener usa uma constante de cadeia de caracteres #DEFINEd em REPORTLISTENERS_LOCS.H. cFailureMsgIndexes fornece uma mensagem alternativa opcional para exibir se a tabela não tiver índices apropriados. Se você não fornecer esta mensagem, UtilityReportListener usa uma constante de cadeia de caracteres #DEFINEd em REPORTLISTENERS_LOCS.H. |
| verifyTargetFile Method | Garante que o nome de arquivo nomeado e seu local de rede estão disponíveis no início de uma execução de relatório baseada em arquivo. Sintaxe: verifyTargetFile() Valores de retorno: Nenhum Parâmetros: Nenhum |
