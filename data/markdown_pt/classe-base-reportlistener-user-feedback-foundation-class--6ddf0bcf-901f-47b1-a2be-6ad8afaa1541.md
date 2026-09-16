# Classe base ReportListener User Feedback Foundation Class

Esta classe fornece feedback configurável pelo usuário durante a execução de relatórios. A Report Output Application usa UpdateListener como sua classe ReportListener padrão designada para saída Print e Preview (valores ListenerType 0 e 1).

| Categoria | Reporting |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Output\Report Listeners |
| Classe | UpdateListener |
| Classe base | ReportListener |
| Biblioteca de classes | _REPORTLISTENER.vcx |
| Classe pai | _ReportListener ( ReportListener Base Foundation Class ) |

# Observações

O design do UpdateListener tem os seguintes objetivos:
 - Facilidade de localização e personalização. Todas as legendas e mensagens que UpdateListener exibe durante a execução de um relatório, bem como as dimensões de sua janela de exibição, são expostas como propriedades públicas. UpdateListener valida dinamicamente quaisquer alterações que você faz em sua configuração base e ajusta seus elementos de exibição para corresponder.
- Informações sofisticadas de feedback sobre o relatório em andamento. UpdateListener substitui as chamadas base ReportListener.UpdateStatus, que ocorrem em cada página, para exibir informações mais refinadas sobre o progresso do relatório de acordo com o escopo do relatório. Seu mecanismo de feedback distingue entre a passagem inicial de cálculo e a passagem subsequente de renderização, usando as propriedades ReportListener.TwoPassProcess e ReportListener.CurrentPass. Para obter mais informações, consulte ReportListener Object Properties, Methods, and Events .
- Disponibilidade de informações de tempo de relatório. UpdateListener usa suas propriedades reportStartRunDatetime e reportStopRunDatetime para exibir informações opcionais de tempo durante a execução de um relatório, mas você também pode usá-las após a conclusão da execução do relatório.
- Capacidade de pausar e continuar execuções de relatório. UpdateListener trata pressionamentos de Escape durante execuções de relatório para este propósito. Salva e restaura seu código de tratamento de teclas adequadamente.
- Sem dependências de classes externas. UpdateListener usa um único método protegido, createTherm(), para criar sua janela de feedback. Não há formulários ou classes de biblioteca externas; esta classe cria e configura a janela inteiramente dentro do código do método createTherm().

> **Observação:** Este objetivo de design decorre do uso da Report Output Application de UpdateListener como o ReportListener padrão para os formatos de saída tradicionais de relatórios e etiquetas (Print e Preview). Sua subclasse pode substituir createTherm() e adaptar o código do método DoStatus() que grava nele.

A tabela a seguir lista propriedades públicas adicionadas por esta classe à sua classe pai, _ReportListener. UpdateListener não adiciona métodos públicos.

| Propriedades | Descrição |
| --- | --- |
| includeSeconds Property | Indica se a mensagem de feedback padrão do usuário deve incluir dados de tempo. Padrão .T. |
| initStatusText Property | Fornece a mensagem do usuário mostrada quando o feedback do usuário aparece pela primeira vez. Padrão "Initializing... " Observações : Consulte REPORTLISTENERS_LOCS.H, que fornece o valor localizável para o qual esta propriedade é definida no método Init da classe. |
| prepassStatusText Property | Fornece uma mensagem de feedback do usuário para uso quando o relatório está em uma passagem de pré-geração para calcular _PAGETOTAL. Padrão "Running calculation prepass... " Observações : Consulte REPORTLISTENERS_LOCS.H, que fornece o valor localizável para o qual esta propriedade é definida no método Init da classe. |
| reportStartRunDatetime Property | Um valor datetime indicando quando a última execução de geração de relatório começou. Padrão DTOT({}) |
| reportStopRunDatetime Property | Um valor datetime para uso na conclusão de uma execução de relatório, vazio durante um relatório, armazenando quando a última execução de geração de relatório terminou. Padrão DTOT({}) |
| runStatusText Property | Fornece uma mensagem do usuário mostrada durante o curso de uma execução de relatório. Padrão "Creating output..." Observações : Consulte REPORTLISTENERS_LOCS.H, que fornece o valor localizável para o qual esta propriedade é definida no método Init da classe. |
| secondsText Property | Fornece a mensagem de texto incluída para descrever o valor de tempo na mensagem de feedback padrão do usuário durante um relatório, quando IncludeSeconds é .T. Padrão SPACE(1) + "secs " Observações : Consulte REPORTLISTENERS_LOCS.H, que fornece o valor localizável para o qual esta propriedade é definida no método Init da classe. |
| thermCaption Property | Mantém uma expressão avaliada para uso na mensagem de feedback do usuário mostrada durante a execução de um relatório. Se esta expressão incluir "cMessage," o conteúdo do argumento fornecido a DoStatus será incluído no resultado da avaliação. Este valor sobrepõe a barra de progresso do UpdateListener. Padrão [cMessage+ " "+ TRANSFORM(INT(THIS.PercentDone*100)) + "%" + IIF(NOT THIS.IncludeSeconds, "" , " "+TRANSFORM(IIF(THIS.IsRunning,DATETIME(), THIS.ReportStopRunDateTime)-THIS.ReportStartRunDateTime)+" " + THIS.SecondsText)] Observações : Quando você ajusta este valor, UpdateListener tenta avaliar um resultado, incluindo um valor "dummy" para cMessage se necessário. Se não puder avaliar seu resultado no momento em que você define o valor da propriedade, manterá o valor anterior. |
| thermFormCaption Property | Mantém o valor usado para definir o título do formulário de feedback do usuário. Padrão "" Observações : UpdateListener avalia este valor no início de cada execução de relatório. Se você definiu um valor não vazio, UpdateListener não ajusta sua configuração. Se você não fornecer um valor, UpdateListener define o valor usando a propriedade ReportListener.PrintJobName. Se sua propriedade PrintJobName estiver vazia, usa ReportListener.CommandClauses.File , o nome do arquivo de relatório em execução. Ao valor resultante adiciona uma cadeia de caracteres localizável, por padrão "Press Esc to cancel... " , para indicar a capacidade do usuário de pausar ou cancelar o relatório com esta tecla. |
| thermFormHeight Property | Mantém a altura do formulário de feedback do usuário, em pixels. Padrão 40 |
| thermFormWidth Property | Mantém a largura do formulário de feedback do usuário, em pixels. Padrão 356 |
| thermMargin Property | Mantém o valor (em pixels) usado para determinar a diferença entre o tamanho da janela de feedback do usuário e a barra de termômetro que exibe. Padrão 5 |

# Exemplo

O exemplo a seguir desativa o feedback padrão para um HTMLListener e encadeia com um UpdateListener para o mesmo feedback do usuário que você obteria para impressão ou visualização por padrão.

O código ajusta a legenda do formulário de feedback e instrui UpdateListener a não incluir segundos no feedback do usuário para este relatório. Depois mostra brevemente o formulário de feedback, para que você possa verificar os resultados dessas alterações, usando UpdateListener.initStatusText para fornecer uma mensagem.

O código de exemplo então executa um relatório, mostrando o formulário de feedback do UpdateListener para atualizar o usuário sobre o progresso enquanto o arquivo HTML é gerado.

Após a execução do relatório, o código abre o arquivo HTML em uma janela VisualFoxPro para verificação rápida. Exibe os resultados de tempo da execução do relatório, aproveitando a versão aumentada do método ReportListener.DoMessage de _ReportListener e HtmlListener.AppName para fornecer um título para a janela de mensagem.

```foxpro
LOCAL oUpdate, oHtml
* create the ReportListeners:
oHtml = NEWOBJECT("HtmlListener","_REPORTLISTENER.VCX")
oUpdate = NEWOBJECT("UpdateListener","_REPORTLISTENER.VCX")
* customize them both:
oHtml.QuietMode = .T.
oUpdate.ThermFormCaption = "My Listener Demo"
oUpdate.IncludeSeconds = .F.
oUpdate.DoStatus(oUpdate.initStatusText)
WAIT WINDOW TIMEOUT 3 "Notice the window title... "
* make one the successor of the other:
oHtml.successor = oUpdate
* run the report:
REPORT FORM ? OBJECT oHtml
* show results:
MODIFY FILE (oHtml.TargetFileName) NOWAIT
oUpdate.DoMessage("Total Report Time: "  + ;
                  TRANSFORM(oUpdate.reportStopRunDatetime - ;
                            oUpdate.reportStartRunDatetime) + ;
                  Update.secondsText,0,oHTML.appName )
```
