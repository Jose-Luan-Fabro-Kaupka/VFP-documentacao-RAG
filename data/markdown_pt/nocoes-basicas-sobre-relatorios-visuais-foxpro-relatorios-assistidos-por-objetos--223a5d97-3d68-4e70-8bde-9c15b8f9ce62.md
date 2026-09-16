# Noções básicas sobre relatórios visuais FoxPro Relatórios assistidos por objetos

O Visual FoxPro 9 apresenta a arquitetura assistida por objeto an para relatórios. Usando esta arquitetura e seus formulários de relatório existentes, você pode aprimorar o processo de relatório de várias maneiras, como:
 - Geração de vários resultados de saída durante a execução de um único relatório.
- Melhorar a qualidade de impressão e visualização.
- Conectar vários relatórios executados juntos para obter um resultado de saída.
- Ajustar o conteúdo do relatório de forma dinâmica durante o processamento dos dados.
- Geração de novos tipos de resultados não disponíveis anteriormente.

Este tópico discute os objetos que funcionam juntos para fornecer essas melhorias e descreve o que acontece durante a execução do relatório assistido por objeto an.

O Sistema de Relatórios do Visual FoxPro 9 é melhor descrito como as assistido por objetos em vez de than orientado a objetos. O mecanismo de relatório não é o objeto an. Porém, quando você usa a nova arquitetura, o Engine delega grande parte de seu trabalho aos objetos.

> **Observação:** O Report Designer também não incorpora referências a classes do Visual FoxPro definidas em bibliotecas de classes visual (arquivos .vcx) ou programas (arquivos .prg) como elementos de layout. Entretanto, usando a nova arquitetura em tempo de design, você pode usar instâncias de classes do Visual FoxPro para definir atributos de elementos de layout de relatório. Essas classes de modelo podem ser anexadas à definição do relatório e fornecer dinamicamente alterações de formatação no código do método and em tempo de execução. Para obter mais informações, consulte Relatório XML Extensões MemberData .

# Arquitetura de saída em tempo de execução

Nas versões anteriores do Visual FoxPro, o Report Engine era monolítico. Ele lidou com todo o processamento como uma única unidade. Ao projetar um relatório, você tinha a capacidade de anexar algum código em vários pontos, principalmente quando o Report Engine começava a processar ou terminava o processamento de uma faixa de layout de relatório.

No Visual FoxPro 9, o Report Engine manipula o movimento do ponteiro de registro através do escopo de dados do seu relatório e avalia expressões. Ele delega o processo de renderização dos resultados para uma nova classe base do Visual FoxPro, ReportListener. Como você pode derivar classes de ReportListener, você pode afetar a renderização de cada objeto individual em um relatório em um nível muito mais granular do que antes. Para obter mais informações, consulte ReportListener Objeto.

### Como fazer Invoke Relatório assistido por objeto

Você pode usar a cláusula OBJECT [TYPE <N>] no comando REPORT FORM ou LABEL para informar ao Report Engine qual objeto ReportListener-derived or tipo de objeto a ser usado. Você também pode instruir o Mecanismo de Relatório a usar um aplicativo cujo nome está armazenado em uma variável de sistema, _REPORTOUTPUT, para nomear um objeto appropriate para você. Se você tiver SET REPORTBEHAVIOR para o valor `90`, o Report Engine solicitará automaticamente o aplicativo cujo nome está armazenado em _REPORTOUTPUT para o objeto an, cada vez que você emitir um REPORT FORM ou Comando LABEL.Se você invocou um comando REPORT FORM ou LABEL com a intenção de fornecer uma visualização na tela, o Sistema de Relatório invoca o objeto another, o PreviewContainer, para exibir a visualização, após concluir seus trabalhos de avaliação e renderização do conteúdo do relatório. Como o PreviewContainer é uma instância do objeto Visual FoxPro, você pode criar visualizações para corresponder a uma ampla variedade de especificações e personalizá-las para seus aplicativos. Para obter mais informações sobre como criar o objeto an que corresponda aos requisitos de um PreviewContainer, consulte O contêiner de visualização API.

### Modos de processamento do sistema de relatórios

O ReportListener processa um relatório ou rótulo em dois modos diferentes, dependendo do valor de sua propriedade ListenerType. Você pode pensar nesses dois modos como apropriados para impressão e apropriados para visualização, ou página por vez e todas as páginas de uma vez.

Em ambos os modos, sua classe ReportListener-derived tem a oportunidade de afetar a renderização de cada elemento do layout, à medida que cada elemento em cada banda é processado. Os modos diferem em como e quando sua classe derived obtém acesso aos resultados renderizados, ou páginas de saída, preparadas pela classe base ReportListener.

No modo página por vez, o ReportListener aciona um evento OutputPage enquanto prepara cada página, ao mesmo tempo em que envia cada página para a impressora ou fila de impressão. Sua turma derived tem acesso apenas à página que acabou de ser preparada e somente naquele momento. Este modo é eficiente se você precisar acessar cada página apenas uma vez. Por exemplo, você pode salvar cada página no disco como uma imagem. Para obter informações completas sobre os recursos e opções disponíveis, consulte OutputPage Método.

No segundo modo, todas as páginas de uma vez, o ReportListener prepara todas as páginas para renderização e as armazena em cache. Ele não aciona eventos OutputPage enquanto prepara as páginas. Quando a execução do relatório for concluída, você poderá invocar o método OutputPage para acessar qualquer página incluída na saída, por número de página. Você pode solicitar páginas em qualquer ordem, várias vezes.

O relatório agora está completamente preparado e pronto para visualização. Neste ponto, se você especificou um valor `1` para a propriedade Listenertype do ReportListener, o ReportListener invoca o objeto the referenciado em sua propriedade PreviewContainer para exibir a visualização.

Você pode armazenar uma referência ao objeto any que atenda aos requisitos do PreviewContainer API na propriedade this. Se ainda não tiver referência de objeto an, o Reportlistener solicita uma referência de objeto appropriate de um aplicativo cujo nome está armazenado em outra variável de sistema, _REPORTPREVIEW.

Quando todo o relatório é preparado, o ReportListener usa o método SetReport do PreviewContainer. Esta ação fornece ao PreviewContainer uma referência ao ReportListener e indica que o ReportListener está pronto para visualização. O controle PreviewContainer takes do processo de relatório neste ponto. Ele usa o método OutputPage do ReportListener para solicitar as páginas necessárias para exibição, conforme o usuário navega pelo relatório.

Para obter mais informações sobre como aproveitar o aplicativo de visualização de relatório padrão ou escrever um substituto, consulte Estendendo a funcionalidade de visualização de relatório.Se o usuário decidir imprimir a partir da interface de visualização, o PreviewContainer chamará o método OnPreviewClose do ReportListener com instruções apropriadas. O controle ReportListener resumes e imprime o cache das páginas preparadas anteriormente. Para obter mais informações, consulte OnPreviewClose Método.

Esta seção apresentou um tour pelos objetos que cooperam no relatório do modo assistido por objeto Visual FoxPro. A próxima seção discute os eventos que ocorrem durante a execução de um relatório, enquanto o Report Engine e o ReportListener preparam e renderizam o conteúdo do relatório. Ele fornece as informações necessárias para avaliar o status do relatório e escrever o código apropriado durante os diferentes estágios de preparação.

# Processamento de saída em tempo de execução

A narrativa de processamento a seguir descreve a execução completa do relatório. Conforme descrito na seção anterior, existem várias maneiras de garantir que um comando REPORT FORM ou LABEL seja processado com referência de objeto an. As diferentes formas de relatório assistido por objeto invoking não alteram a sequência de eventos the descrita nesta seção.

A classe base Report Engine e ReportListener processam o relatório em uma série de eventos que começa logo antes do evento BeforeReport e termina logo após o evento AfterReport. A classe base ReportListener também fornece dois eventos externos ou de estrutura, LoadReport e UnloadReport, que permitem que seu código pré e pós-processe o relatório.

> **Observação:** Para obter informações completas sobre eventos de membros do ReportListener, consulte as diversas entradas ReportListener Propriedades, métodos e eventos do objeto .

### Iniciando a execução do relatório

Quando um comando REPORT FORM ou LABEL é processado, o Mecanismo de Relatório primeiro verifica se um comando previous inclui a palavra-chave NOPAGEEJECT. Esta palavra-chave indica que vários relatórios estão sendo processados ​​juntos e que alguma saída já está na fila para eventual exibição ou impressão.

Se não houver NOPAGEJECT anterior, o valor da propriedade OutputPageCount do ReportListener será redefinido para `0`.

Em seguida, o Report Engine cria a sessão de dados especial do ReportListener e fornece seu valor DataSessionID ao ReportListener, usando a propriedade FRXDataSession do ReportListener. Ele também atribui a propriedade CommandClauses do ReportListener; embora nem todas as propriedades CommandClauses estejam imediatamente disponíveis. Para obter mais informações, consulte CommandClauses Propriedade.

O mecanismo agora invoca o evento LoadReport do ReportListener e avalia o valor de retorno de qualquer código de usuário fornecido no evento this. Se LoadReport retornar um valor False (`.F.`), o processamento do relatório não continuará.

> **Dica:** Se desejar fazer alterações no relatório ou na tabela de etiquetas ou no driver de impressora atual, LoadReport é sua oportunidade de fazer isso. Você também pode alterar dinamicamente o valor do membro ReportListener.CommandClauses.Prompt e de outros membros ReportListener.CommandClauses relacionados ao destino de saída.

Após LoadReport, o Engine está pronto para investigar o conteúdo do relatório ou tabela de rótulos. Se especificado na tabela, o mecanismo prepara uma sessão de dados privada para armazenar os dados do relatório. Ele armazena o valor DataSessionID dos dados a serem processados ​​durante o relatório na propriedade CurrentDataSession do ReportListener.O Report Engine agora muda para FRXDataSession e fornece uma cópia somente leitura do relatório ou tabela de rótulos, usando o alias `FRX`, nesta sessão.

> **Dica:** O Report Engine e o ReportListener não usam esta cópia do relatório ou da tabela de definição de rótulo; na verdade, eles nunca mais mudam para esta sessão durante a execução do relatório. O Report Engine lê o conteúdo da tabela em uma estrutura separada para uso próprio.

O Report Engine alterna a sessão de dados de volta para CurrentDataSession que contém os dados a serem processados ​​durante a execução do relatório. Agora está pronto para iniciar seu processamento interno.

> **Observação:** Nesta seção, você aprendeu sobre duas sessões de dados usadas durante a execução de um relatório (CurrentDataSession e FRXDataSession). É mais importante entender essas duas sessões de dados quando você começa a escrever o código ReportListener. No entanto, outras sessões de dados podem estar envolvidas na execução do relatório. A a seção posterior deste tópico descreve os tipos relevantes de sessões de dados com mais detalhes.

### Iniciando o processamento interno da execução do relatório

Se o ReportListener estiver definido como um valor ListenerType de `1` (impressão) e se você tiver usado a cláusula PROMPT no relatório ou rótulo do comando processing, ou se você tiver definido o valor ReportListener.CommandClauses.Prompt como `.T.` no LoadReport evento, a caixa de diálogo Configurar impressão será exibida neste momento. Os valores iniciais nesta caixa de diálogo refletem quaisquer instruções RANGE usadas no comando processing; no entanto, a impressão efetiva RANGE para o relatório e os valores dos membros ReportListener.CommandClauses relacionados podem ser alterados pelas escolhas do usuário na caixa de diálogo.

Quando o usuário fecha a caixa de diálogo, o Report Engine abre a fila de impressão, se necessário, a menos que o usuário tenha cancelado a impressão. Ele também verifica as configurações atuais da impressora (mesmo que nenhuma impressão seja solicitada) para determinar as dimensões atuais da página. Se você usou a palavra-chave NODIALOG no comando processing, mas não definiu a propriedade ReportListener.QuietMode como True (`.T.`), a propriedade the será automaticamente definida como True (`.T.`) para o saldo da execução do relatório. Em seguida, o Report Engine chama o evento BeforeReport.

> **Dica:** chegamos à sequência de eventos que compreende a execução do relatório nativo do Visual FoxPro. Os métodos ReportListener GetPageHeight e GetPageWidth possuem valores de retorno válidos. Todos os membros CommandClauses estão preparados. Você pode usar o método CancelReport do ReportListener a partir de agora até o final do AfterReport, se precisar interromper e encerrar prematuramente a execução do relatório.

Depois do BeforeReport, o Report Engine e o ReportListener fazem a avaliação inicial de vários aspectos do relatório ou da tabela de rótulos. Por exemplo, eles verificam se você usou a variável de sistema _PAGETOTAL em expressões de relatório. Nesse caso, o valor da propriedade TwoPassProcess do ReportListener é definido como True (`.T.`). O valor da propriedade CurrentPass do ReportListener também está definido como `0` neste momento. Para obter mais informações, consulte CurrentPass Propriedade e TwoPassProcess Propriedade.> **Observação:** Você pode definir o valor da propriedade TwoPassProcess como True ( .T. ) manualmente se desejar forçar a ocorrência de duas passagens. O ReportListener respeitará esta atribuição manual se você defini-la antes de chamar o comando REPORT FORM ou LABEL, no evento LoadReport, ou no evento BeforeReport.

### Tratamento do conteúdo do relatório

O Report Engine e o ReportListener concluíram a fase de configuração. Eles agora processam todos os eventos de banda relevantes para o relatório. Entre os eventos BeforeBand e AfterBand de cada banda, eles processam cada elemento de layout pertencente à banda. Cada elemento de layout possui os seguintes eventos potenciais:
 - Um evento EvaluateContents, se for um elemento Campo ou Expressão.
- Um evento AdjustObjectSize, se for um elemento Shape ou Image. Se a Forma ou Imagem não couber na página, é possível que o evento this seja repetido em tentativas adicionais nas páginas subsequentes.
- Zero a muitos eventos de Renderização, para todos os tipos de elementos de layout. Um elemento não aciona um evento Render se sua expressão Print When for avaliada como True ( .T. ). Caso contrário, aciona pelo menos um evento Render e potencialmente mais, se abranger bandas e páginas.

Se a propriedade ReportListener.TwoPassProcess for True (`.T.`), o Report Engine e o ReportListener serão executados duas vezes em todos os eventos de banda e elemento. Na primeira vez, eles avaliam expressões e posicionamento nas páginas de saída sem realmente renderizar nada. Este é um pré-processamento ou passo de cálculo. Ele permite que o mecanismo de relatório calcule um valor _PAGETOTAL para uso na saída de renderização na segunda passagem ou renderização. A passagem de pré-processamento também oferece uma oportunidade para o seu código calcular outros valores.

> **Dica:** Você pode usar a classe ReportListener Debug Foundation para examinar detalhadamente o processamento de eventos do relatório run. Use a propriedade the da classe Verbose para examinar o conteúdo do membro CommandClauses do ReportListener em diferentes pontos do resultado e receber informações estendidas sobre os parâmetros do objeto de vários métodos.

### Finalizando a execução do relatório

A banda do relatório final processada é uma banda de rodapé de página ou uma banda de resumo; mesmo se você usar o método CancelReport do ReportListener, o Sistema de Relatório terminará de processar uma página inteira antes de interromper o relatório.

Após os processos finais da banda do relatório, o ReportListener e o Report Engine iniciam os procedimentos de limpeza.

A sessão de dados privados do relatório, se houver, é fechada antes da ocorrência do evento AfterReport. Para garantir que o ReportListener sempre tenha uma sessão de dados válida para a qual possa retornar, se o relatório usar uma sessão de dados privada, o CurrentDataSession do ReportListener será redefinido para `1`, o valor padrão, neste momento. Se o relatório não tiver uma sessão de dados privada, CurrentDataSession estará fora do controle do Report System's e não será alterado.

O evento AfterReport do ReportListener é invocado em seguida. Após o AfterReport, a saída fornecida nativamente é finalizada. Se um fluxo de impressão foi aberto para esta saída, ele será fechado agora. Neste momento, o método CancelReport deixa de ter qualquer efeito no processamento interno; não há mais "execução de relatório" do ponto de vista do Report Engine.O valor da propriedade ReportListener.QuietMode é restaurado para False (`.F.`), se tiver sido desativado temporariamente como resultado da palavra-chave NODIALOG.

Se o valor da propriedade ReportListener.ListenerType for 1, o ReportListener invoca o PreviewContainer para exibir a saída do relatório neste ponto, seguido por UnloadReport após o controle PreviewContainer returns para o ReportListener. Se o valor da propriedade ListenerType não for `1`, o método UnloadReport do ReportListener ocorre imediatamente.

Após o evento UnloadReport, o Engine fecha a sessão de dados especial na qual abriu uma cópia do relatório ou tabela de rótulos. Ele redefine a propriedade ReportListener.FRXDataSession para seu valor padrão, `-1`, neste momento, significando que não há nenhuma sessão válida que atenda a esse propósito entre as execuções do relatório.

O ReportListener.TwoPassProcess é redefinido para seu valor padrão de `.F.`. Ao colocar a propriedade this de volta em seu estado padrão, o ReportListener possibilita que você reatribua explicitamente esse valor antes da próxima vez que usar a instância do ReportListener. O valor da propriedade ReportListener.CurrentPass não é redefinido; seu valor atual oferece uma maneira de avaliar o que aconteceu na execução do relatório anterior.

A menos que você tenha usado a palavra-chave NOPAGEEJECT nesta execução de relatório, os métodos ReportListener GetPageWidth e GetPageHeight param de provar valores úteis neste ponto.

Nº de sessões de dados associadas with Execuções de relatórios assistidos por objetos

Quando cada evento ReportListener começa, a sessão de dados é aquela na qual o objeto ReportListener foi criado originalmente. Esta sessão de dados nem sempre é a mesma sessão de dados na qual você emitiu o comando REPORT FORM ou LABEL. A classe ReportListener Base Foundation usa o termo ListenerDataSession, com uma propriedade protegida associada member, para descrever e manipular a sessão de dados na qual foi originada.

Nos eventos de enquadramento da execução do relatório (LoadReport e UnloadReport), você deve retornar ao ListenerDataSession ao concluir qualquer sequência de código que alterne a sessão de dados. O Report Engine esperará encontrar o objeto ReportListener neste estado na conclusão desses eventos. Consulte Comando SET DATASESSION para obter mais informações sobre como alternar entre sessões de dados.

À medida que os eventos progridem através de outros eventos de relatório e do processamento interno do Report Engine, seu código ReportListener normalmente alterna entre as sessões de dados indicadas pela propriedade CurrentDataSession e pela propriedade FRXDataSession do ReportListener. Alternar entre essas duas sessões de dados permite fazer referência aos arquivos de dados do relatório, bem como à cópia do relatório ou da tabela de rótulos à medida que você gera a saída, conforme necessário.O Report Engine também fornece informações sobre uma quarta sessão de dados: a sessão de dados na qual você emitiu o comando REPORT FORM ou LABEL. Você encontra esse valor DataSessionID como uma propriedade StartDataSession member do objeto CommandClauses Property. Normalmente não é necessário fazer referência a esta quarta sessão de dados no código ReportListener. Ele é fornecido caso você precise fazer referência ao ambiente em que ocorreu o comando the. Por exemplo, você pode querer verificar a configuração de uma configuração ambiental no escopo da sessão, como SET("DELETED"). Para obter mais informações, consulte Personalizando o ambiente de uma sessão de dados.

O StartDataSession do comando REPORT FORM ou LABEL pode ser a mesma sessão de dados referenciada pela propriedade CurrentDataSession do ReportListener. No entanto, se a tabela do relatório especificar uma sessão de dados privada para a execução do relatório, CurrentDataSession e StartDataSession não serão iguais. O StartDataSession também pode ser a sessão na qual o ReportListener foi criado, se o seu objeto ReportListener tiver como escopo um formulário ou objeto session. No entanto, um ReportListener geralmente tem escopo global, por exemplo, criado pelo aplicativo de saída de relatório ou por um objeto manager pertencente ao seu aplicativo. Nesse caso, StartDataSession e ListenerDataSession não estão relacionados.
