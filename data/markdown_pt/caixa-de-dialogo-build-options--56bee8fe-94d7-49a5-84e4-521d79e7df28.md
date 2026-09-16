# Caixa de diálogo Build Options

Permite criar um aplicativo personalizado ou recompilar um projeto existente.

Esta caixa de diálogo aparece quando você escolhe Build no menu Project, que aparece quando um projeto está aberto, ou Build no Project Manager.

# Ação de compilação
 **Rebuild project**
Cria e compila um arquivo de projeto. Esta opção corresponde ao comando BUILD PROJECT. Para obter mais informações, consulte BUILD PROJECT Command .
**Application (app)**
Compila o projeto, recompila arquivos desatualizados e cria um arquivo de aplicativo (.app). Esta opção corresponde ao comando BUILD APP. Para obter mais informações, consulte BUILD APP Command .
**Win32 executable / COM Server (exe)**
Cria um arquivo executável (.exe) a partir de um projeto. Esta opção corresponde ao comando BUILD EXE. Para obter mais informações, consulte BUILD EXE Command .
**Single-threaded COM server (dll)**
Cria um arquivo de biblioteca de vínculo dinâmico (.dll) usando informações de classe do arquivo de projeto. Esta opção corresponde ao comando BUILD DLL que aponta para a biblioteca de tempo de execução, VFP VersionNumber R.dll. VersionNumber representa o número da versão desta versão do Visual FoxPro. Para obter mais informações, consulte BUILD DLL Command .
**Multi-threaded COM server (dll)**
Cria um arquivo de biblioteca de vínculo dinâmico (.dll) multithread usando informações de classe de um arquivo de projeto. Esta opção corresponde ao comando BUILD MTDLL que aponta para a biblioteca de tempo de execução, VFP VersionNumber T.dll. VersionNumber representa o número da versão desta versão do Visual FoxPro. Para obter mais informações, consulte BUILD MTDLL Command .

# Opções
 **Recompile All Files**
Recompila todos os arquivos no projeto, cria um arquivo de objeto para cada arquivo de origem e inclui mensagens de erro de compilação em um arquivo de erro (.err) durante o processo de compilação. Caso contrário, apenas arquivos que foram modificados desde a última compilação são recompilados. Para obter mais informações, consulte How to: View and Save Build Messages .
**Display Errors**
Exibe erros de compilação em uma janela de edição após a conclusão do processo de compilação e inclui mensagens de status de compilação e erro em um arquivo de erro (.err) durante o processo de compilação. Para obter mais informações, consulte How to: View and Save Build Messages .
**Run After Build**
Especifica se você deseja que o aplicativo seja executado após ser compilado.
**Regenerate Component IDs**
Instala e registra servidores Automation contidos no projeto. Quando selecionada, esta opção especifica que novos Globally Unique Identifiers (GUIDs) são gerados quando você compila um programa. Apenas as classes marcadas como OLE Public na caixa de diálogo Class Info do menu Class serão criadas e registradas. Esta opção é habilitada quando você marcou Build OLE DLL ou Build Executable e já compilou um programa contendo a palavra-chave OLEPublic. Para obter mais informações, consulte Class Info Dialog Box .
**Version**
Exibe a caixa de diálogo EXE Version, que permite especificar informações para o número da versão e o tipo de versão. Este botão está disponível quando você seleciona Build Executable ou Build OLE DLL na caixa de diálogo Build Options. Para obter mais informações, consulte EXE Version Dialog Box .
