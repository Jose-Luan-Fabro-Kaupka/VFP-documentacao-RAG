# Guia File Locations, caixa de diálogo Options

Contém e especifica locais de diretório para programas e arquivos usados pelo Visual FoxPro. Para obter informações sobre como alterar e salvar configurações, consulte How to: View and Change Environment Settings.

# Lista de tipos de arquivo
 **Beautify**
Especifica o nome do arquivo do aplicativo chamado quando você escolhe Beautify no menu Tools e é definido como Beautify.app por padrão. Quando você abre um programa ou arquivo de texto em uma janela de edição, o comando Beautify aparece no menu Tools. Esta opção corresponde à _BEAUTIFY System Variable .
**Builders**
Especifica o nome do arquivo do aplicativo chamado quando você escolhe Builder no menu de atalho ao trabalhar no Form Designer. Um builder consiste em uma ou mais caixas de diálogo que ajudam a definir propriedades para um controle específico ou combinar cláusulas para criar uma expressão específica. This option corresponds to the _BUILDER System Variable . Builders podem ser exibidos automaticamente se você escolher a opção Builder lock na guia Forms, Options Dialog Box .
**Class Browser**
Especifica o nome do arquivo do aplicativo chamado quando você escolhe Class Browser no menu Tools e é definido como Browser.app por padrão. This file corresponds to the _BROWSER System Variable .
**Code References**
Especifica o nome do aplicativo chamado quando você escolhe Code References no menu Tools ou quando seleciona o comando Look Up Reference ou View Definition no menu de atalho na janela de edição de um programa. This file corresponds to the _FOXREF System Variable and is set to FoxRef.app by default.
**Component Gallery**
Especifica o nome do arquivo do aplicativo chamado quando você escolhe Component Gallery no menu Tools e é definido como Gallery.app por padrão. This option corresponds to the _GALLERY System Variable .
**Converter**
Especifica o nome do arquivo do aplicativo chamado quando você abre um formulário, relatório ou outro componente de aplicativo criado em uma versão anterior do FoxPro ou Visual FoxPro. O aplicativo especificado converte o componente para o formato de arquivo atual. This option corresponds to the _CONVERTER System Variable .
**Coverage Profiler**
Especifica o nome do arquivo do aplicativo chamado quando você escolhe Coverage Profiler no menu Tools e é definido como Coverage.app, que cria a saída de coverage e profiler do Debugger, por padrão. This option corresponds to the _COVERAGE System Variable .
**CrossTab Generator**
Especifica o nome e o local do programa que cria tabelas cruzadas.
**Default Directory**
Especifica o diretório padrão do Visual FoxPro. This option corresponds to the SET DEFAULT Command .
**Default Include File**
Especifica um arquivo de cabeçalho padrão de constantes de tempo de compilação predefinidas incluídas automaticamente com classes, formulários ou conjuntos de formulários definidos pelo usuário. Esta opção está vazia por padrão e corresponde à _INCLUDE System Variable .
**Expression Builder**
Especifica o nome do arquivo do aplicativo chamado quando você emite o comando GETEXPR ou abre a caixa de diálogo Expression Builder a partir do Visual FoxPro. This option is empty by default and corresponds to the _GETEXPR System Variable . Para obter mais informações, consulte Expression Builder Dialog Box .
**FoxCode**
Especifica o nome e o local da tabela que fornece funcionalidade IntelliSense e é definida como FoxCode.dbf por padrão. This option corresponds to the _FOXCODE System Variable .
**FoxTask**
Especifica o nome e o local da tabela que contém registros de lista de tarefas e é definida como FoxTask.dbf por padrão. This option corresponds to the _FoxTask System Variable .
**HTML Generator**
Especifica o nome do arquivo do aplicativo chamado quando você escolhe Save As HTML no menu File e é definido como Genhtml.prg por padrão. This option corresponds to the _GENHTML System Variable .
**Help File**
Especifica o nome e o local do arquivo de Ajuda padrão que abre quando você escolhe Microsoft Visual FoxPro Help no menu Help ou pressiona F1 e é definido como dv_FoxHelp.chm por padrão. This option corresponds to the SET HELP Command . Note Se a extensão do nome do arquivo for .hlp, a Ajuda gráfica é usada. Se a extensão do nome do arquivo for .dbf, a Ajuda no estilo .dbf é usada. Se nenhuma extensão for especificada, o padrão é Ajuda gráfica.
**IntelliSense Manager**
Especifica o nome e o local do programa chamado quando você escolhe IntelliSense Manager no menu Tools e é definido como FoxCode.app, que fornece IntelliSense do Visual FoxPro, por padrão. This option corresponds to the _CODESENSE System Variable .
**Menu Builder**
Especifica o nome do arquivo do programa menu builder e é definido como GenMenu.prg por padrão. This option corresponds to the _GENMENU System Variable .
**Menu Designer**
Especifica um aplicativo externo de design de menu. This option corresponds to the _MENUDESIGNER System Variable .
**ObjectBrowser**
Especifica o nome e o local do programa chamado quando você escolhe Object Browser no menu Tools e é definido como ObjectBrowser.app por padrão. This option corresponds to _ObjectBrowser System Variable .
**Report Builder**
Especifica o nome do arquivo do programa invocado em resposta a eventos de builder nos designers Report e Label. This option corresponds to _REPORTBUILDER System Variable .
**Report Output**
Especifica o nome do arquivo do programa invocado pelo mecanismo de relatório no modo assistido por objetos para obter uma referência Reportlistener quando nenhuma foi especificada. This option corresponds to _REPORTOUTPUT System Variable .
**Report Preview**
Especifica o nome do arquivo do programa invocado por objetos Reportlistener para obter uma referência de contêiner de preview quando nenhuma foi especificada. This option corresponds to _REPORTPREVIEW System Variable .
**Resource File**
Especifica se o Visual FoxPro armazena seu estado atual, como macros, tamanho e localização de janelas e assim por diante, em um arquivo de recursos e, em caso afirmativo, qual arquivo usar. Esta opção é definida como FoxUser.dbf por padrão. Note Se esta configuração não for especificada, o Visual FoxPro redefine o estado do sistema para o padrão cada vez que você inicia o programa. Além disso, algumas opções na caixa de diálogo Options ficarão indisponíveis. This option corresponds to the SET RESOURCE Command .
**Samples Directory**
Especifica o diretório que contém os arquivos de amostra do Visual FoxPro. This option corresponds to the _SAMPLES System Variable .
**Search Path**
Especifica os diretórios que o Visual FoxPro pesquisa por arquivos que não encontra no diretório padrão e está vazio por padrão. Os diretórios especificados devem ser separados por vírgulas ou ponto e vírgula. This option corresponds to the SET PATH Command . Tip Para procurar e selecionar vários diretórios, na caixa de diálogo Change File Location, clique no botão de reticências (...). Ponto e vírgula são inseridos automaticamente ao procurar e selecionar vários diretórios.
**Startup Program**
Especifica o nome do arquivo do aplicativo chamado quando você inicia o Visual FoxPro e é definido como vazio por padrão. This option corresponds to the _STARTUP System Variable .
**TaskList**
Especifica o nome e o local do programa chamado quando você escolhe Task List no menu Tools e é definido como TaskList.app, que gerencia a lista de tarefas, por padrão. This option corresponds to the _TASKLIST System Variable .
**TaskPane**
Especifica o nome e o local do programa chamado quando você escolhe Task Pane no menu Tools e é definido como TaskPane.app, que exibe áreas que contêm informações e expõem tarefas essenciais para uso fácil, por padrão. This option corresponds to _TASKPANE System Variable .
**Temporary Files**
Especifica o diretório no qual o Visual FoxPro salva arquivos temporários, por exemplo, ao classificar ou indexar. Como arquivos temporários podem crescer bastante, especifique um diretório com bastante espaço livre. Para melhor desempenho, especifique uma unidade rápida; por exemplo, em um ambiente multiusuário, você pode especificar uma unidade local.
**Toolbox**
Especifica o nome e o local do programa chamado quando você escolhe Toolbox no menu Tools e é definido como Toolbox.app, que exibe itens e conjuntos de ferramentas para criar aplicativos, por padrão. This option corresponds to the _TOOLBOX System Variable .
**Wizards**
Especifica o nome do arquivo do aplicativo chamado quando você executa ou escolhe um assistente no menu Tools. This option corresponds to the _WIZARD System Variable .
