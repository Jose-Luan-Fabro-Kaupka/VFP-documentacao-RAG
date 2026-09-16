# Visão geral do comando SET

O comando SET executa operações diferentes quando usado com várias palavras-chave.

```foxpro
SET [ [cSetCommand] [ON | OFF] | TO [eSetting] ]
```

# Observações

Quando nenhum argumento é passado, SET abre a janela Data Session. Essa janela oferece uma maneira fácil de abrir tabelas, estabelecer relações ou alterar configurações do Microsoft Visual FoxPro. Para obter mais informações, consulte Janela Data Session.

A tabela a seguir lista outras operações executadas pelo comando SET.

| Comando SET | Descrição |
| --- | --- |
| Comando SET ALTERNATE | Direciona para um arquivo de texto a saída de tela ou impressora criada com ?, ??, DISPLAY ou LIST. |
| Comando SET ANSI | Determina como são feitas comparações entre cadeias de comprimentos diferentes com o operador = em comandos SQL do Visual FoxPro. |
| Comando SET ASSERTS | Especifica se comandos ASSERT são avaliados ou ignorados. |
| Comando SET AUTOINCERROR | Especifica se tentativas de atualizar valores de um campo com incremento automático geram erro ou falham silenciosamente e prosseguem. |
| Comando SET AUTOSAVE | Determina se o Visual FoxPro grava os buffers de dados em disco ao sair de READ ou retornar à janela Command. |
| Comando SET BELL | Ativa ou desativa o sinal sonoro do computador e define seus atributos. |
| Comando SET BLOCKSIZE | Especifica como o Visual FoxPro aloca espaço em disco para armazenar campos memo. |
| Comando SET BROWSEIME | Especifica se o Input Method Editor é aberto ao navegar para uma caixa de texto em uma janela Browse. |
| Comando SET CARRY | Determina se o Visual FoxPro transporta dados do registro atual para um novo registro criado com INSERT, APPEND e BROWSE. |
| Comando SET CENTURY | Determina se o Visual FoxPro exibe o século em expressões de data e como interpreta datas com anos de apenas dois dígitos. |
| Comando SET CLASSLIB | Abre uma biblioteca de classes visuais (.vcx) que contém definições de classes. |
| Comando SET CLOCK | Determina se o relógio do sistema é exibido e especifica sua posição na janela principal do Visual FoxPro. |
| Comando SET COLLATE | Especifica uma sequência de ordenação para campos Character em operações posteriores de indexação e classificação. |
| Comando SET COLOR OF SCHEME | Especifica as cores de um esquema ou copia um esquema de cores para outro. |
| Comando SET COLOR SET | Carrega um conjunto de cores definido anteriormente. |
| Comando SET COMPATIBLE | Controla a compatibilidade com Microsoft FoxBASE+ e outras linguagens FoxPro. |
| Comando SET CONFIRM | Especifica se o usuário pode sair de uma caixa de texto digitando além do último caractere. |
| Comando SET CONSOLE | Habilita ou desabilita a saída para a janela principal do Visual FoxPro ou para a janela ativa definida pelo usuário em programas. |
| Comando SET COVERAGE | Ativa ou desativa a cobertura de código ou especifica o arquivo de texto que receberá essas informações. |
| Comando SET CPCOMPILE | Especifica a página de código para programas compilados. |
| Comando SET CPDIALOG | Especifica se a caixa de diálogo Code Page é exibida ao abrir uma tabela. |
| Comando SET CURRENCY | Define o símbolo monetário e sua posição na exibição de expressões Numeric, Currency, Float e Double. |
| Comando SET CURSOR | Determina se o ponto de inserção é exibido enquanto o Visual FoxPro aguarda entrada. |
| Comando SET DATABASE | Especifica o banco de dados atual. |
| Comando SET DATASESSION | Ativa a sessão de dados do formulário especificado. |
| Comando SET DATE | Especifica o formato de exibição de expressões Date e DateTime. |
| Comando SET DEBUG | Incluído para compatibilidade com versões anteriores. Torna as janelas Debug e Trace disponíveis ou indisponíveis no sistema de menus nas versões anteriores à 5.0. |
| Comando SET DEBUGOUT | Direciona a saída de depuração para um arquivo. |
| Comando SET DECIMALS | Especifica o número de casas decimais exibidas em expressões numéricas. |
| Comando SET DEFAULT | Especifica a unidade e o diretório padrão. |
| Comando SET DELETED | Especifica se o Visual FoxPro processa registros marcados para exclusão e se eles ficam disponíveis para outros comandos. |
| Comando SET DEVELOPMENT | Faz o Visual FoxPro comparar a data e a hora de criação de um programa com as de seu arquivo objeto compilado durante a execução. |
| Comando SET DEVICE | Direciona a saída de @ ... SAY para a tela, uma impressora ou um arquivo. |
| Comando SET DIRECTORY | Especifica a unidade e o diretório padrão. |
| Comando SET DISPLAY | Incluído para compatibilidade com versões anteriores. |
| Comando SET DOHISTORY | Determina se comandos de um programa são colocados na janela Debug Output. |
| Comando SET ECHO | Abre a janela Trace para depuração de programas. Incluído para compatibilidade com versões anteriores. |
| Comando SET ENGINEBEHAVIOR | Habilita a compatibilidade do mecanismo de dados SQL com Visual FoxPro 7.0, 8.0 ou 9.0. |
| Comando SET ESCAPE | Determina se pressionar ESC interrompe a execução de programas e comandos. |
| Comando SET EVENTLIST | Especifica os eventos a acompanhar na janela Debug Output ou em um arquivo indicado por SET EVENTTRACKING. |
| Comando SET EVENTTRACKING | Ativa ou desativa o acompanhamento de eventos ou especifica o arquivo de texto que receberá essas informações. |
| Comando SET EXACT | Especifica as regras usadas para comparar duas cadeias de comprimentos diferentes. |
| Comando SET EXCLUSIVE | Especifica se o Visual FoxPro abre arquivos de tabela para uso exclusivo ou compartilhado em uma rede. |
| Comando SET FDOW | Especifica o primeiro dia da semana. |
| Comando SET FIELDS | Especifica quais campos de uma tabela podem ser acessados. |
| Comando SET FILTER | Especifica uma condição que os registros da tabela atual devem atender para ficarem acessíveis. |
| Comando SET FIXED | Especifica se o número de casas decimais na exibição de dados numéricos é fixo. |
| Comando SET FULLPATH | Especifica se CDX( ), DBF( ), MDX( ) e NDX( ) retornam o caminho no nome do arquivo. |
| Comando SET FUNCTION | Atribui uma expressão (macro de teclado) a uma tecla de função ou combinação de teclas. |
| Comando SET FWEEK | Especifica os requisitos para a primeira semana do ano. |
| Comando SET HEADINGS | Determina se cabeçalhos de coluna são exibidos para campos e se informações de arquivo são incluídas quando TYPE exibe o conteúdo de um arquivo. |
| Comando SET HELP | Habilita ou desabilita a Ajuda online do Visual FoxPro ou especifica um arquivo de Ajuda. |
| Comando SET HOURS | Define o relógio do sistema no formato de 12 ou 24 horas. |
| Comando SET INDEX | Abre um ou mais arquivos de índice para uso com a tabela atual. |
| Comando SET KEY | Especifica acesso a um intervalo de registros com base nas chaves de índice. |
| Comando SET KEYCOMP | Controla a navegação por teclas no Visual FoxPro. |
| Comando SET LIBRARY | Abre um arquivo externo de biblioteca de API (interface de programação de aplicativos). |
| Comando SET LOCK | Habilita ou desabilita o bloqueio automático de arquivos em determinados comandos. |
| Comando SET LOGERRORS | Determina se o Visual FoxPro envia mensagens de erro de compilação para um arquivo de texto. |
| Comando SET MACKEY | Especifica uma tecla ou combinação que exibe a caixa de diálogo Macro Key Definition. |
| Comando SET MARGIN | Define a margem esquerda da impressora e afeta toda saída enviada a ela. |
| Comando SET MARK OF | Especifica um caractere de marca para títulos ou itens de menu, ou exibe ou limpa esse caractere. |
| Comando SET MARK TO | Especifica um delimitador para exibir expressões de data. |
| Comando SET MEMOWIDTH | Especifica a largura exibida de campos memo e expressões Character. |
| Comando SET MESSAGE | Define uma mensagem para exibição na janela principal ou barra de status gráfica, ou especifica o local das mensagens de barras e comandos de menu definidos pelo usuário. |
| Comando SET MULTILOCKS | Determina se vários registros podem ser bloqueados com LOCK( ) ou RLOCK( ). |
| Comando SET NEAR | Determina onde o ponteiro de registro é posicionado após FIND ou SEEK não localizar um registro. |
| Comando SET NOCPTRANS | Impede a conversão para outra página de código em campos selecionados de uma tabela aberta. |
| Comando SET NOTIFY | Habilita ou desabilita a exibição de determinadas mensagens do sistema. |
| Comando SET NULL | Determina como valores nulos são aceitos pelos comandos ALTER TABLE, CREATE TABLE e INSERT - SQL. |
| Comando SET NULLDISPLAY | Especifica o texto exibido para valores nulos. |
| Comando SET ODOMETER | Especifica o intervalo de atualização do contador de registros em comandos que processam registros. |
| Comando SET OLEOBJECT | Especifica se o Visual FoxPro pesquisa o Registro OLE quando um objeto não pode ser localizado. |
| Comando SET OPTIMIZE | Habilita ou desabilita a otimização de consultas Rushmore. |
| Comando SET ORDER | Designa um arquivo de índice ou tag controlador para uma tabela. |
| Comando SET PALETTE | Especifica se a paleta de cores padrão do Visual FoxPro é usada. |
| Comando SET PATH | Especifica um caminho para pesquisa de arquivos. |
| Comando SET PDSETUP | Carrega uma configuração de driver de impressora ou limpa a configuração atual. |
| Comando SET POINT | Determina o caractere de ponto decimal usado na exibição de expressões numéricas e monetárias. |
| Comando SET PRINTER | Habilita ou desabilita a saída para a impressora ou a direciona a um arquivo, porta ou impressora de rede. |
| Comando SET PROCEDURE | Abre um arquivo de procedimento. |
| Comando SET READBORDER | Determina se são colocadas bordas ao redor de caixas de texto criadas com @ ... GET. |
| Comando SET REFRESH | Determina se e com que frequência uma janela Browse é atualizada com alterações feitas por outros usuários da rede. |
| Comando SET RELATION | Estabelece uma relação entre duas tabelas abertas. |
| Comando SET RELATION OFF | Desfaz uma relação entre a tabela pai na área de trabalho atual e uma tabela filha relacionada. |
| Comando SET REPORTBEHAVIOR | Especifica o tipo de processamento do mecanismo de relatório usado ao executar REPORT FORM e LABEL tradicionais. |
| Comando SET REPROCESS | Especifica quantas vezes e por quanto tempo o Visual FoxPro tenta bloquear um arquivo ou registro após uma tentativa sem êxito. |
| Comando SET RESOURCE | Atualiza ou especifica um arquivo de recursos. |
| Comando SET SAFETY | Determina se o Visual FoxPro exibe uma caixa de diálogo antes de sobrescrever um arquivo ou se regras, valores padrão e mensagens de erro de tabelas ou campos são avaliados ao fazer alterações no Table Designer ou com ALTER TABLE. |
| Comando SET SECONDS | Especifica se os segundos são exibidos na parte de hora de um valor DateTime. |
| Comando SET SEPARATOR | Especifica o caractere que separa cada grupo de três dígitos à esquerda do ponto decimal em expressões numéricas e monetárias. |
| Comando SET SKIP | Cria uma relação um-para-muitos entre tabelas. |
| Comando SET SKIP OF | Habilita ou desabilita um menu, barra, título ou item de menu definido pelo usuário ou do sistema do Visual FoxPro. |
| Comando SET SPACE | Determina se um espaço é exibido entre campos ou expressões ao usar ? ou ??. |
| Comando SET SQLBUFFERING | Determina se os dados de uma instrução SQL SELECT se baseiam em dados armazenados em buffer ou gravados em disco. |
| Comando SET STATUS | Exibe ou remove a barra de status baseada em caracteres. |
| Comando SET STATUS BAR | Exibe ou remove a barra de status gráfica. |
| Comando SET STEP | Abre a janela Trace e suspende a execução do programa para depuração. |
| Comando SET STRICTDATE | Especifica se constantes Date e DateTime ambíguas geram erros. |
| Comando SET SYSFORMATS | Especifica se as configurações de sistema do Visual FoxPro para Windows são atualizadas com as configurações atuais do Microsoft Windows. |
| Comando SET SYSMENU | Habilita ou desabilita a barra de menus do sistema durante a execução e permite reconfigurá-la. |
| Comando SET TABLEPROMPT | Habilita ou desabilita a caixa de diálogo para abrir arquivo quando uma tabela não é localizada durante um comando de dados, como SELECT - SQL. |
| Comando SET TABLEVALIDATE | Especifica o nível de validação de tabela a executar. |
| Comando SET TALK | Determina se o Visual FoxPro exibe resultados de comandos. |
| Comando SET TEXTMERGE | Habilita ou desabilita a avaliação de campos, variáveis, elementos de matriz, funções ou expressões entre delimitadores de mesclagem de texto e permite especificar a saída. |
| Comando SET TEXTMERGE DELIMITERS | Especifica os delimitadores de mesclagem de texto. |
| Comando SET TOPIC | Especifica o tópico ou os tópicos a abrir ao invocar o sistema de Ajuda do Visual FoxPro. |
| Comando SET TOPIC ID | Especifica o tópico de Ajuda a exibir com base em sua identificação de contexto. |
| Comando SET TRBETWEEN | Habilita ou desabilita o rastreamento entre pontos de interrupção na janela Trace. |
| Comando SET TYPEAHEAD | Especifica o número máximo de caracteres que podem ser armazenados no buffer de antecipação de digitação. |
| Comando SET UDFPARMS | Especifica se o Visual FoxPro passa parâmetros para uma função definida pelo usuário (UDF) por valor ou por referência. |
| Comando SET UNIQUE | Especifica se registros com valores duplicados de chave são mantidos em um arquivo de índice. |
| Comando SET VARCHARMAPPING | Controla o mapeamento de expressões Character para tipos Varchar nos conjuntos de resultados de consultas e exibições. |
| Comando SET VIEW | Abre ou fecha a janela Data Session ou restaura o ambiente do Visual FoxPro de um arquivo de exibição. |
| Comando SET VOLUME | Mapeia designadores de unidade do MS-DOS (A:, B:, C: etc.) para volumes ou pastas no FoxPro para Macintosh. |
| Comando SET WINDOW OF MEMO | Incluído para compatibilidade com versões anteriores. |
