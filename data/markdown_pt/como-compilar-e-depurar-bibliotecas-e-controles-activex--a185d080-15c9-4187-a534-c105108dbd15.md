# Como: compilar e depurar bibliotecas e controles ActiveX

Depois de criar um projeto no Visual Studio, você pode compilá-lo e depurá-lo. Os procedimentos a seguir são para o Visual Studio 6.0. Para as informações mais recentes, leia a documentação da versão que você está usando.

# Compilando o projeto

Antes de compilar seu projeto, você precisa estabelecer as configurações do projeto. Algumas das configurações que você faz dependem de se deseja criar uma versão de depuração ou de release do controle ou biblioteca. Como regra, crie versões de depuração do programa até estar satisfeito de que funciona corretamente, depois crie uma versão de release.

### Para especificar uma versão de depuração ou release
- No menu Build, escolha Set Default Configuration.
- Escolha se está criando uma versão de depuração ou release do controle.
- Escolha OK .

### Para estabelecer configurações do projeto
- No menu Build, escolha Settings .
- Em Settings For , escolha se está criando uma versão de depuração ou release do programa.
- Clique na guia C/C++ e faça estas configurações: Na lista Category, escolha Code Generation . Na lista Calling Convention, escolha _fastcall . Na lista Use run-time library, escolha Multithreaded DLL .
- Escolha a guia Link e na caixa de texto Object/Library Modules, adicione uma das bibliotecas a seguir: Se estiver compilando um .ocx, adicione OCXAPI.LIB do diretório API do Visual FoxPro. Se estiver compilando um .fll, adicione WINAPIMS.LIB do diretório API do Visual FoxPro.
- Desmarque Ignore all default libraries .
- Escolha OK .

### Para garantir que o compilador encontre os arquivos necessários
- No menu Tools, escolha Options .
- Clique na guia Directories.
- Na lista Show directories for, escolha Include files .
- Na barra de ferramentas Directories, clique no botão Add.
- Adicione o diretório com Pro_ext.h.
- Na lista Show directories for, escolha Library files .
- Na barra de ferramentas Directories, clique no botão Add.
- Adicione o diretório com Ocxapi.lib do diretório API do Visual FoxPro (ao criar um controle) ou adicione Winapims.lib do diretório API do Visual FoxPro (ao criar um FLL)
- Na caixa de diálogo Options, escolha OK .

Depois de especificar as configurações, você pode compilar e vincular seu programa.

### Para compilar e vincular um arquivo .ocx
- No menu Build, escolha Build projname.ocx .

Quando você compila e vincula o arquivo .ocx, o Visual C++ registra automaticamente o controle no computador em que foi compilado. Se por algum motivo você precisar registrar o controle manualmente, pode fazer isso usando o procedimento a seguir.

### Para registrar o controle ActiveX
- No menu Tools do Microsoft Development Environment, escolha Register Control . -ou-
- Declare e chame DLLRegisterServer( ) do seu programa.

Depurar um controle ActiveX ou biblioteca FLL no contexto de um aplicativo Visual FoxPro completo é mais difícil do que depurá-lo separadamente do aplicativo. É uma boa ideia criar um programa de teste simples para testar a operação do seu controle ou biblioteca.

### Depuração com o Microsoft Development Environment

O Microsoft Visual C++ versão 4.0 e superior oferece um ambiente de depuração integrado que facilita definir pontos de interrupção e percorrer seu código passo a passo. Você pode até executar o Visual FoxPro a partir do Visual C++.

### Para iniciar a depuração com o Microsoft Visual C++
- No menu Build, escolha Settings .
- Na caixa de diálogo Project Settings, clique na guia Debug.
- Na caixa de texto Executable for debug session, digite o caminho e o nome do arquivo executável (.exe) do Visual FoxPro. Por exemplo, você pode digitar a linha a seguir com a substituição apropriada para o número da versão do Visual FoxPro: C:\Program Files\Microsoft Visual FoxPro < versionNumber >\Vfp< versionNumber >.exe
- Escolha OK .
- Defina um ponto de interrupção em sua biblioteca.
- No menu Build, escolha Debug . Depois, no submenu escolha Go .
- Quando o Visual Studio exibir uma mensagem dizendo " VFP9.exe does not contain debugging information," escolha Yes para continuar.

Para obter mais informações sobre depuração no Visual C++, consulte o conjunto de documentação do Visual C++.

### Depuração com outros depuradores

Você deve conseguir depurar um controle ou biblioteca com qualquer depurador que trate corretamente um INT 3 (Rotina de biblioteca de API _BreakPoint( )) incorporado em seu programa. Você pode usar qualquer depurador para depuração simbólica, desde que possa fazer tudo o seguinte:
 - Criar uma tabela de símbolos a partir de um arquivo map.
- Carregar a tabela de símbolos independentemente do programa.
- Realocar os símbolos para um novo endereço.

### Para depurar uma biblioteca
- Adicione uma chamada _BreakPoint( ) à rotina no ponto onde a depuração começará.
- Compile o controle ou biblioteca.
- Invoque seu depurador.
- Se seu depurador suporta símbolos, carregue a tabela de símbolos de sua biblioteca.
- Inicie o Visual FoxPro.
- Chame sua rotina de biblioteca a partir do Visual FoxPro.
- Quando o ponto de interrupção for atingido, faça ajustes na base de símbolos para alinhar seus símbolos com o local real onde a biblioteca foi carregada.
- Incremente o registrador de ponteiro de instrução (IP) em 1 para pular a instrução INT 3.
- Continue a depuração como em um programa normal. Observação Sempre remova quaisquer pontos de interrupção especificados em seu depurador antes de liberar seu produto.
