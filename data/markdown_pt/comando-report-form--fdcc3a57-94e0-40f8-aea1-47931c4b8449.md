# Comando REPORT FORM

Exibe ou imprime um relatório especificado por um arquivo de definição de relatório (.frx), por exemplo, criado com o comando CREATE REPORT ou MODIFY REPORT.

O comando REPORT FORM pode interpretar arquivos de etiqueta do Visual FoxPro (formato lbx), bem como arquivos de relatório. Você também pode usar REPORT FORM para executar arquivos de relatório baseados em caracteres criados no FoxPro for MS-DOS.

```foxpro
REPORT FORM FileName1 | ? [ENVIRONMENT] [Scope]
   [FOR lExpression1] [WHILE lExpression2] [NOOPTIMIZE]
   [RANGE nStartPage [, nEndPage]]
   [HEADING cHeadingText] [SUMMARY] [NORESET] [PLAIN]
   [NOCONSOLE | OFF] [PDSETUP]
   [NAME ObjectName]
   [OBJECT oReportListener | TYPE iExpression]
   [TO OutputDestination [NODIALOG]]
   [PREVIEW [PreviewDestination] [NOWAIT] [WINDOW WindowName]]
```

#### Parâmetros
 **FileName1 | ?**
Especifica o nome de um arquivo de definição de relatório (.frx) ou exibe a caixa de diálogo Open para que você possa escolher um arquivo .frx. Por padrão, o relatório é exibido na janela de saída atual. Observação A extensão de nome de arquivo padrão para um arquivo de definição de relatório é .frx. Se o arquivo .frx não estiver no diretório ou pasta padrão, você deve incluir o nome do arquivo com o caminho. A partir do Visual FoxPro 7.0, FileName1 é incluído na mensagem de status, que aparece quando você inclui a cláusula TO. Para suprimir a mensagem de status, consulte a descrição da cláusula TO.
**[ENVIRONMENT]**
Abre e restaura todas as tabelas e relações no ambiente de dados associado ao relatório, mesmo quando AutoOpenTables está definido como False (.F.). Observação A palavra-chave ENVIRONMENT está incluída para compatibilidade com versões anteriores, por exemplo, relatórios convertidos de versões anteriores do FoxPro, como relatórios 2. x. Para restaurar o ambiente de dados associado a um relatório Visual FoxPro, defina a propriedade AutoOpenTables do ambiente de dados como True (.T.) (padrão). Para garantir que o ambiente do relatório seja fechado quando o relatório terminar de imprimir, defina a propriedade AutoCloseTables do ambiente de dados como True (.T.) (padrão). Para obter mais informações, consulte Propriedade AutoOpenTables e Propriedade AutoCloseTables .
**[ Scope ]**
Especifica um intervalo de registros a incluir no relatório. Apenas os registros que estão dentro do intervalo de escopo são incluídos no relatório. Observação Quando você inclui uma cláusula Scope, o escopo opera apenas na tabela na área de trabalho ativa. A tabela a seguir lista os valores possíveis para Scope . Scope Descrição ALL Incluir todos os registros. (Padrão) NEXT nRecords Incluir o próximo número nRecords de registros começando do registro atual. RECORD nRecordNumber Incluir apenas o registro especificado. REST Incluir um intervalo de registros começando do registro atual e terminando no último registro. Para obter mais informações sobre cláusulas de escopo, consulte Scope Clauses .
**[FOR lExpression1 ]**
Imprime dados apenas nos registros para os quais a expressão lógica especificada por lExpression1 é avaliada como True (.T.). Incluindo a cláusula FOR, você pode excluir registros que não deseja imprimir. Dica Se lExpression1 é uma expressão otimizável, a Rushmore Query Optimization otimiza REPORT FORM com a cláusula FOR. Para melhor desempenho, use uma expressão otimizável na cláusula FOR. Para obter mais informações, consulte Comando SET OPTIMIZE e Using Rushmore Query Optimization to Speed Data Access .
**[WHILE lExpression2 ]**
Imprime dados apenas enquanto a expressão lógica especificada por lExpression2 é avaliada como True (.T.).
**[NOOPTIMIZE]**
Impede a otimização Rushmore para REPORT FORM . Para obter mais informações, consulte Comando SET OPTIMIZE e Using Rushmore Query Optimization to Speed Data Access .
**[RANGE nStartPage [, nEndPage ]]**
Especifica um intervalo de páginas a imprimir ou outra saída. O parâmetro nStartPage especifica a primeira página a imprimir, enquanto o parâmetro nEndPage especifica a última página a imprimir. Se nEndPage for omitido, a última página a imprimir tem como padrão 32.767. Observação RANGE seleciona páginas para saída, enquanto cláusulas de escopo, FOR e WHILE selecionam registros. Esses critérios de seleção não têm efeito se você escolher imprimir da pré-visualização, a menos que tenha especificado o modo assistido por objetos usando a cláusula OBJECT ou SET REPORTBEHAVIOR 90 . No modo assistido por objetos, você pode imprimir o RANGE completo que especificou no comando REPORT FORM original ou algum subconjunto desse intervalo de páginas, usando os membros PrintPageCurrent, PrintRangeFrom e PrintRangeTo do ReportListener.CommandClauses. Para obter mais informações, consulte Método OnPreviewClose .
**[HEADING cHeadingText ]**
Especifica o texto a colocar como um cabeçalho adicional em cada página do relatório. Se você incluir a cláusula HEADING e a palavra-chave PLAIN, a palavra-chave PLAIN tem precedência.
**[SUMMARY]**
Suprime a impressão de linhas de detalhe para que apenas totais e subtotais sejam impressos.
**[NORESET]**
Especifica que as variáveis de sistema _PAGENO e _PAGETOTAL não são reinicializadas. A contagem de páginas do relatório atual começa nos valores atuais dessas duas variáveis. Para obter mais informações, consulte Variável de sistema _PAGENO e Variável de sistema _PAGETOTAL . Observação Se você usar as palavras-chave NORESET e RANGE juntas, deve calcular previamente quais páginas imprimir.
**[PLAIN]**
Suprime cabeçalhos de página, exceto no início do relatório.
**[NOCONSOLE | OFF]**
Suprime a exibição do relatório na janela principal do Visual FoxPro ou em uma janela definida pelo usuário ao imprimir o relatório ou enviá-lo a um arquivo. Observação Quando você usa o modo de saída assistido por objetos do Visual FoxPro 9.0, REPORT FORM não exibe o conteúdo do seu relatório na janela de saída atual, então as palavras-chave NOCONSOLE e OFF não têm efeito no comportamento nativo. No entanto, as palavras-chave estão disponíveis no objeto ReportListener.CommandClauses. Você pode avaliá-las em suas classes derivadas de ReportListener e optar por suprimir uma exibição do conteúdo do relatório ou outro feedback ao usuário baseado em seu conteúdo. Para obter mais informações, consulte Propriedade CommandClauses .
**[PDSETUP]**
Carrega uma configuração de driver de impressora. Você pode incluir PDSETUP para usar uma configuração de driver de impressora para imprimir relatórios baseados em caracteres criados no FoxPro for MS-DOS. PDSETUP é ignorado quando você imprime relatórios baseados em gráficos criados no Visual FoxPro.
**[NAME ObjectName ]**
Especifica um nome de variável de objeto para o ambiente de dados associado ao relatório. Observação O ambiente de dados e os objetos no ambiente de dados possuem propriedades e métodos, como o método AddObject, que precisam ser definidos ou chamados em tempo de execução. A variável de objeto fornece acesso a essas propriedades e métodos. Se você omitir a cláusula NAME, o Visual FoxPro usa o nome do arquivo de relatório, que pode ser referenciado em código associado a eventos, por padrão.
**[OBJECT oReportListener | TYPE iExpression ]**
Invoca o modo de saída assistido por objetos do Visual FoxPro. Use uma referência de objeto a um objeto derivado da classe base ReportListener, ou um valor numérico especificando um tipo de saída. A cláusula OBJECT em um comando REPORT FORM individual tem precedência sobre a configuração atual de SET REPORTBEHAVIOR . Para obter mais informações, consulte Objeto ReportListener , Propriedade ListenerType e Propriedade OutputType (Visual FoxPro) .
**[TO OutputDestination [NODIALOG]]**
Especifica um destino de saída para o relatório. Para suprimir mensagens de status que aparecem em tempo de execução, inclua a palavra-chave NODIALOG. Observação No modo de saída assistido por objetos, NODIALOG define a propriedade QuietMode do objeto ReportListener como .T. durante a execução do relatório. Para obter mais informações, consulte Propriedade QuietMode . A tabela a seguir descreve os valores possíveis de OutputDestination . OutputDestination Descrição [PRINTER [PROMPT] [NOPAGEEJECT] [NOEJECT]] Envia o relatório para a impressora. Para exibir a caixa de diálogo Print antes do início da impressão, inclua a palavra-chave PROMPT. No modo assistido por objetos, as opções habilitadas na caixa de diálogo Print são afetadas pelo valor do membro ReportListener.CommandClauses.PrintPageCurrent. Para especificar que o Visual FoxPro não force uma ejeção de folha no final de um relatório e deixe o trabalho de impressão aberto, inclua a palavra-chave NOPAGEEJECT. O próximo relatório impresso é adicionado ao trabalho de impressão aberto. Você deve garantir que a última execução de relatório não tenha uma cláusula NOPAGEEJECT para que o trabalho de impressão possa ser fechado. NOPAGEEJECT é válido apenas durante a execução do programa. É desconsiderado quando emitido na janela Command. Alterar entre orientações de página, como paisagem para retrato, entre relatórios não é suportado. Você pode encadear vários relatórios usando NOPAGEEJECT e ter números de página continuando de um relatório para o próximo. Esta é uma técnica útil para tarefas como envio de relatórios por fax. O comando REPORT FORM também permite uma palavra-chave NOEJECT, que o Visual FoxPro não suporta mais, mas era usada em versões DOS mais antigas do FoxPro e FoxBASE+. Esta palavra-chave não executa nenhuma função, mas não dispara um erro. [FILE] FileName2 [[ADDITIVE] ASCII] Especifica o nome de um arquivo de texto para enviar o relatório. A extensão de nome de arquivo padrão para o arquivo criado é .txt. Quando você omite a palavra-chave ASCII ou usa o modo de saída assistido por objetos do Visual FoxPro, grava códigos PostScript ou de outras impressoras no arquivo de texto junto com o conteúdo do seu relatório. Para criar um arquivo de texto ASCII a partir do arquivo de definição de relatório, SET REPORTBEHAVIOR 80 e inclua a palavra-chave ASCII. Observação Quando você inclui a palavra-chave ASCII, pode processar um relatório em um computador que não tenha configurações de driver de impressora instaladas. Sem a palavra-chave ASCII, um comando REPORT FORM emitido em um computador sem configurações de driver de impressora instaladas gera um erro. Um arquivo ASCII contém apenas texto. Se o relatório é uma definição de layout baseada em caracteres criada no FoxPro for MS-DOS, traços e sinais de mais podem ser incluídos para representar linhas e formas. Caso contrário, quaisquer configurações de fonte ou cor, gráficos, linhas, retângulos ou retângulos arredondados no arquivo de definição de relatório não aparecem no arquivo de texto ASCII. Você pode especificar o número de caracteres a colocar em cada linha e o número de linhas a colocar em cada página usando as variáveis de sistema _ASCIICOLS e _ASCIIROWS. Os valores padrão para essas variáveis de sistema correspondem a uma página retrato padrão. Para obter mais informações, consulte Variável de sistema _ASCIICOLS e Variável de sistema _ASCIIROWS . Para acrescentar novo conteúdo a um arquivo ASCII em vez de sobrescrevê-lo, preceda a palavra-chave ASCII com a palavra-chave ADDITIVE. As palavras-chave ADDITIVE e ASCII devem ser especificadas na ordem mostrada.
**[PREVIEW [ PreviewDestination ] [NOWAIT][WINDOW WindowName ]]**
Exibe o relatório na janela de pré-visualização em vez de imprimir o relatório. Por padrão, a janela de pré-visualização é modal, mas fornece acesso à barra de ferramentas Print Preview. A palavra-chave NOWAIT especifica que o Visual FoxPro não aguarda em tempo de execução o fechamento da janela de pré-visualização antes de continuar a execução do programa. Dica Relatórios e etiquetas baseados em caracteres criados no FoxPro MS-DOS possuem uma janela de pré-visualização especial baseada em caracteres. Este mecanismo não é afetado por SET REPORTBEHAVIOR e não suporta a cláusula OBJECT ou cláusulas relacionadas a WINDOW. Se você incluir WINDOW < WindowName >, a janela de pré-visualização assume as características da janela, como título, tamanho e assim por diante, que você especifica com WindowName . WindowName pode ser a propriedade name de um objeto form ou pode ser uma variável referenciando uma janela criada com DEFINE WINDOW . Para obter mais informações, consulte Comando DEFINE WINDOW . A tabela a seguir descreve os valores possíveis para PreviewDestination . Você pode usar a cláusula WINDOW sozinha ou em combinação com PreviewDestination . PreviewDestination Descrição [IN WINDOW WindowName ] Especifica uma janela para pré-visualizar um relatório. Se você incluir IN WINDOW < WindowName >, o relatório é pré-visualizado na janela que você especifica com WindowName . IN SCREEN Especifica que a pré-visualização é exibida na janela principal do Visual FoxPro e não pode ser movida para fora dela.

# Observações

Quando você usa o modo de saída assistido por objetos do Visual FoxPro, todas as cláusulas do comando REPORT FORM estão disponíveis para seu ReportListener em seu objeto membro CommandClauses, com a exceção das cláusulas de seleção de registros (scope, FOR e WHILE). Você pode usar o atributo CommandClauses.RecordTotal para informações sobre o escopo da execução do relatório, ou atribuir esses valores ao seu objeto ReportListener antes de executar seu relatório. O tópico Propriedade CommandClauses fornece mais informações sobre como cada cláusula é representada no objeto membro CommandClauses.

# Exemplos

### Exemplo 1

O exemplo a seguir mostra como executar um trabalho de impressão de relatório em lote com dois relatórios. O Visual FoxPro executa o conjunto de relatórios duas vezes para obter uma contagem total de páginas, que é armazenada na variável de sistema _PAGETOTAL para habilitar expressões Page X of Y nos layouts de relatório.

> **Observação:** Você pode garantir que o relatório seja executado duas vezes incluindo _PAGETOTAL em suas expressões de relatório. Se você não precisa de _PAGETOTAL, mas deseja que as duas passagens sejam executadas para outros cálculos, pode usar o modo de saída assistido por objetos e definir a propriedade TwoPassProcess do ReportListener como .T. . Para obter mais informações, consulte Propriedade TwoPassProcess .

NORESET especifica que os números de página continuam imprimindo com o próximo relatório. NOPAGEEJECT especifica que a primeira página do segundo relatório continue imprimindo no verso da última página do primeiro relatório.

```foxpro
REPORT FORM myReport1.frx TO PRINTER NOPAGEEJECT
REPORT FORM myReport2.frx TO PRINTER NORESET
MESSAGEBOX("You printed " + ;
   TRANSFORM(_PAGETOTAL)+" pages.")
```

### Exemplo 2

O exemplo a seguir mostra como você pode visualizar uma pré-visualização antes de enviar o relatório para uma impressora.

```foxpro
REPORT FORM myReport1.frx TO PRINTER PROMPT NODIALOG PREVIEW
```

Para tornar a janela de pré-visualização não modal, o código a seguir inclui a palavra-chave NOWAIT:

```foxpro
REPORT FORM myReport1.frx PREVIEW NOWAIT
```

Para pré-visualizar os resultados em uma janela específica, o código a seguir inclui a cláusula WINDOW para especificar uma janela chamada MyWindow que você criou anteriormente com o comando DEFINE WINDOW:

```foxpro
REPORT FORM myReport1.frx PREVIEW WINDOW MyWindow
```

### Exemplo 3

O exemplo a seguir mostra como enviar um relatório para um arquivo ASCII. As variáveis de sistema _ASCIIROWS e _ASCIICOLS definem o número de linhas e caracteres por linha na página ASCII. O comando REPORT FORM imprime um relatório chamado MyReport.frx em um arquivo ASCII chamado MyFile.txt.

```foxpro
SET REPORTBEHAVIOR 80
_ASCIIROWS = nLines
_ASCIICOLS = nChars
REPORT FORM MyReport.frx TO FILE MyFile.txt ASCII
```
