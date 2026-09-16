# Add-Ins do Coverage Profiler

Add-Ins são arquivos de código (geralmente .prg ou .scx) que fornecem uma maneira fácil de ajustar o Coverage Profiler. A subclasse cov_standard do mecanismo de coverage, que compreende a interface do usuário do Coverage.app, mostra apenas uma pequena parte do que você pode fazer com o mecanismo. O mecanismo analisa o log de coverage; cov_standard apenas exibe os resultados de uma entre muitas maneiras que você poderia querer vê-los.

Você poderia criar uma subclasse diferente de cov_engine com uma exibição muito diferente. Por exemplo, sua subclasse poderia exibir uma caixa de diálogo que executa consultas contra as estatísticas de coverage coletadas pelo mecanismo. As opções de exibição poderiam fornecer uma visão do código marcado para um conjunto filtrado de entradas de log, ou apenas um gráfico dos resultados de profiling.

Você pode não querer subclassificar cov_engine para criar uma nova interface do zero porque a classe cov_engine fornece um processo mais fácil. Você pode adicionar funcionalidade a cov_standard, ou a qualquer subclasse de cov_engine, usando Add-Ins. Cov_standard expõe esse recurso por meio de um botão na caixa de diálogo principal do Coverage Profiler. Quando você executa um Add-In em uma instância de cov_standard como o Coverage Profiler, o Add-In pode manipular as capacidades de cov_engine, as tabelas de coverage, bem como cov_standard. Add-Ins também podem adicionar novas caixas de diálogo e recursos à interface visual de cov_standard.

# Escrevendo Add-Ins

Você pode escrever Add-Ins para aprimorar a interface padrão ou pode subclassificar cov_standard para criar sua própria interface totalmente nova.

# Aprimorando o aplicativo padrão

A lista a seguir inclui recursos que você pode querer fornecer por meio de Add-Ins:
 - Adicionar um recurso visível à caixa de diálogo principal.
- Adicionar uma caixa de diálogo ao formset do mecanismo de coverage (consulte a limitação abaixo sobre como garantir que sua caixa de diálogo apareça no lugar certo).
- Exibir uma caixa de diálogo separada que acessa um recurso do mecanismo Coverage (consulte a limitação abaixo sobre como garantir que sua caixa de diálogo apareça no lugar certo).
- Fornecer uma interface de consulta que usa a tabela Source e apresenta uma lista de todas as linhas que atendem aos seus critérios, e filtra ou ordena os resultados. Observação Você pode usar os métodos Adjust... (AdjustCoverageFilenameCursor(), AdjustSourceCursor() e AdjustTargetCursor()) do Engine para adicionar campos às tabelas Source e Target quando o mecanismo as cria, e usar esses campos em seus Add-Ins.
- Adicionar nomes de arquivos ao cursor IgnoredFiles, para eliminar esses arquivos da análise. Isso pode economizar tempo de análise.
- Usar o hook Init especial para Add-Ins.
- Registrar Add-Ins para recuperação e acesso fácil a uma lista de Add-Ins. A classe de caixa de diálogo modal cov_AddInDialog na subclasse padrão do mecanismo de coverage apresenta caixas de diálogo previamente registradas em uma lista suspensa. Quando você define a opção lRegisterAdd-In do mecanismo de coverage como ON, o nome de caminho completo dos Add-Ins executados com sucesso é adicionado ao Registro do Windows para que você possa executar esses Add-Ins novamente facilmente. A classe UI padrão também permite definir essa propriedade na caixa de diálogo Coverage Profiler Options . O objeto Coverage Engine mantém uma lista de todos os Add-Ins registrados na propriedade aAddIns.
- Usar as informações finais do campo coverage.log, callstack, para projetar sua própria interface ou sua própria visão do log de coverage.

Ao escrever Add-Ins, considere as seguintes informações:
 - Você pode usar qualquer um dos tipos de arquivo suportados como Add-Ins. Os tipos de arquivo suportados são .qpr, .qpx, .mpr, .mpx, .app, .exe, .scx, fxp, .prg e .procedures (se os procedimentos já estiverem disponíveis em uma biblioteca de procedimentos aberta).
- O formset Coverage Engine tem uma barra de ferramentas "invisível". Se seu Add-In for não visual, você pode usar essa barra de ferramentas para contê-lo. Se seu Add-In for um controle visual, o contêiner membro .Cov_tools da caixa de diálogo principal da subclasse padrão provavelmente é o lugar mais conveniente para colocá-lo. Isso permite que a posição e o tamanho da barra de ferramentas sejam automaticamente sincronizados com o restante da caixa de diálogo quando ela é redimensionada.
- Todos os métodos do mecanismo que usam as tabelas Source e Target aceitam argumentos opcionais que permitem apontar esses métodos para os aliases apropriados enquanto você trabalha com eles. Você também pode alterar o conteúdo atual das propriedades cSourceAlias e cTargetAlias para corresponder ao par de cursors em que você está interessado. Isso permite comparar várias execuções de log Coverage entre si dentro da mesma interface.
- Limitações: Add-Ins devem aceitar um parâmetro (o mecanismo Coverage passa uma referência a si mesmo). Um Add-In deve ser um dos tipos de arquivo permitidos, listados acima. Procedimentos que você usa como Add-Ins devem estar disponíveis em uma biblioteca de procedimentos carregada no momento (consulte Comando SET PROCEDURE ) na Ajuda. O Engine não usa a sintaxe IN FileName e não chama procedimentos ou arquivos .prg como funções e RETURN seus valores. Ele não usa as palavras-chave NAME ou LINK no comando DO FORM; você pode gerenciar a referência você mesmo ou permitir que o Engine escopo um formulário para você tornando seu formulário um membro do formset Engine. Se você executar um Add-In na inicialização, deve usar uma referência porque a variável pública _oCoverage ainda não está disponível. Em outros momentos, você pode usar a referência da variável pública dentro do seu próprio código, se preferir. Quando você escreve um Add-In como um formulário, se criar o formulário como ShowWindow = 1 e executar Coverage em seu próprio frame, seus formulários Add-In devem ser exibidos no frame Coverage. Se você usar .RunAddIn da janela Command, certifique-se de que o frame coverage seja o frame MDI ativo antes de instanciar seus formulários.

# Subclassificar a classe Cov_Standard

Você pode subclassificar o mecanismo de coverage ou sua subclasse padrão. A lista a seguir descreve a estrutura do conjunto de arquivos de origem do projeto COVERAGE.

| Arquivo | Descrição |
| --- | --- |
| Coverage.prg | Um "wrapper" para o objeto coverage, que instancia o objeto. |
| Coverage.vcx Coverage.vct | Todas as classes para o mecanismo e sua subclasse padrão. |
| Cov_short.mnx Cov_short.mnt | Menu de atalho. |
| Cov_pjx.frx Cov_pjx.frt | Mecanismo padrão para entregar resultados no nível do projeto. |
| Coverage.h | Arquivo de cabeçalho para todo o código Coverage, incorporando os seguintes elementos: *— Constantes de caractere Coverage para log e parsing: #INCLUDE COV_CHAR.H *— Cadeias de caracteres localizadas Coverage (pode usar algumas constantes de log e parsing): #INCLUDE COV_LOCS.H *— Constantes de componente de caixa de diálogo comum Coverage: #INCLUDE COV_DLGS.H *— Especificações e requisitos Coverage: #INCLUDE COV_SPEC.H *— Constantes de objeto de registro Coverage: #INCLUDE COV_REGS.H *— Opções ajustáveis Coverage: #INCLUDE COV_TUNE.H |

O conjunto de arquivos de origem do projeto COVERAGE também inclui vários arquivos .ico .bmp e .msk.

Use o arquivo COV_TUNE.H (contendo comentários e explicações apropriados) para se familiarizar com as opções disponíveis sem reescrever código.

Como o uso de Add-In é governado pela classe base do mecanismo de coverage, qualquer outra subclasse de coverage que você criar pode usar Add-Ins da mesma maneira que a subclasse padrão.

A subclasse do mecanismo de coverage instanciada pelo Coverage.app padrão não aumenta o método RunAddIn( ) do mecanismo de coverage de nenhuma forma. No entanto, ela invoca uma caixa de diálogo modal para permitir que o usuário escolha um Add-In antes de invocar o método RunAddIn( ) do mecanismo de coverage. A caixa de diálogo modal recebe uma referência ao objeto Coverage e define a propriedade cAddIn do mecanismo de coverage.

Se você escrever sua própria subclasse do mecanismo de coverage, certifique-se de que sua subclasse possa usar a mesma classe de caixa de diálogo modal (cov_AddInDialog) para lidar com Add-Ins como o aplicativo Coverage padrão; a caixa de diálogo não depende de nenhum recurso da subclasse padrão.

Você pode chamar uma caixa de diálogo modal diferente, definir o nome do arquivo cAddIn diretamente na propriedade cAddIn ou substituir o conteúdo da propriedade cAddIn passando o nome do arquivo Add-In que deseja executar ao método RunAddIn( ).

Seja como for que você acesse um Add-In para executar em sua subclasse, você pode investigar a lista de Add-Ins registrados no Coverage.app verificando os nomes de arquivo na propriedade aAddIns do mecanismo de coverage.

Para obter detalhes sobre as Properties, Events e Methods do mecanismo de coverage, consulte Coverage Engine Object na Ajuda.
