# Como: usar o Automated Test Harness

Você pode automatizar testes de seus aplicativos Visual FoxPro criando e executando scripts usando o Automated Test Harness. O Automated Test Harness grava e reproduz eventos de mouse e teclado usando a tecnologia Microsoft Active Accessibility (MSAA) e é instalado no diretório Microsoft Visual FoxPro VersionNumber\Tools\Test. Para informações adicionais, consulte o arquivo ReadMe, aatesthelp.htm, no diretório \Tools\Test.

### Para executar o Automated Test Harness
- Execute o Automated Test Harness de \Tools\Test\AATEST.APP -OU- Na Command window do Visual FoxPro, insira a linha a seguir: DO (HOME() + "tools\test\aatest")
- Para gravar o script, clique em Record na barra de ferramentas ou no menu Record. Uma lista de aplicativos disponíveis aparece.
- Selecione um aplicativo Visual FoxPro e, quando solicitado, insira um nome para seu script de texto. O aplicativo ou janela Visual FoxPro selecionado aparece e a ferramenta está pronta para gravar os eventos.
- Grave os eventos. Execute seu aplicativo como normalmente faria usando o teclado e o mouse. Certifique-se de ter passado por todos os elementos da interface do usuário, incluindo formulários, menus, janelas e caixas de diálogo.
- Quando terminar, clique em Stop na barra de ferramentas. Você também pode pausar e retomar a gravação conforme necessário.

Para visualizar o log de eventos, que foi selecionado ou gravado atualmente, clique em "Edit the script."

Para reproduzir scripts, selecione o script que deseja executar e clique em Play. Se o programa detectar um erro, você verá um prompt no aplicativo de teste.

Para ver o log de teste, selecione a guia Test Log.

> **Observação:** Somente uma instância da ferramenta de teste pode ser executada por instalação porque as tabelas de teste são abertas de forma exclusiva.
