# Notas de programação de servidores de automação

Para encontrar informações adicionais sobre como escrever servidores de automação, consulte os tópicos das seguintes áreas.

# Objetos Application

Um objeto Application não é exposto em uma biblioteca de tipos de servidor de automação; portanto, você não pode acessar os métodos DoCmd e Eval do objeto Application. No entanto, você pode expor o objeto Application criando uma propriedade personalizada e definindo seu valor como o objeto Application, ou pode fornecer um método que acessa o objeto Application.

> **Observação:** Propriedades de leitura/gravação do objeto Application, como AutoYield , são globais ao projeto. Portanto, certifique-se de que servidores multithread não presumam que os valores dessas configurações estão protegidos entre threads.

Para obter mais informações, consulte Application Object.

# Amostras de servidores de automação

Esta versão do Visual FoxPro inclui duas amostras de servidores de automação ISAPI, FoxWeb e FoxIS. Essas amostras gerenciam o retorno de registros selecionados do Visual FoxPro como HTML para um navegador da Internet. Para obter mais informações sobre essas amostras, consulte FoxISAPI Automation Server Samples.

> **Observação:** O FoxISAPI incluído no Visual FoxPro inclui melhorias projetadas especificamente para uso com novos servidores DLL multithread. Servidores DLL executados pelo FoxISAPI não devem usar o Pool Manager integrado.

# Arquivos de configuração

No Visual FoxPro, apenas arquivos de configuração, Config.fpw, incorporados em servidores EXE ou DLL serão usados durante a inicialização em tempo de execução. O arquivo de configuração armazena configurações críticas definidas no momento em que o Visual FoxPro é iniciado, tanto no produto quanto em tempo de execução. Antes do Visual FoxPro 6.0, o arquivo Config.fpw podia existir como um arquivo separado ou incorporado ao aplicativo (.app, .exe ou .dll). Se um arquivo Config.fpw for encontrado incorporado em um aplicativo, ele é usado. Caso contrário, o Visual FoxPro pesquisa nos caminhos normais por um arquivo Config.fpw separado.

Você ainda terá funcionalidade completa com aplicativos .app e .exe distribuídos normalmente.

Para obter mais informações, consulte Setting Configuration Options at Startup.

# Tratamento de páginas de código

Páginas de código são suportadas em todos os servidores e são específicas de um determinado projeto (.dll). Você pode definir a página de código padrão no arquivo Config.fpw; no entanto, ela é definida apenas na inicialização em tempo de execução. A página de código é global em todos os projetos. Além disso, todos os objetos que usam uma determinada instância do tempo de execução compartilham a mesma página de código.

Cada servidor tem seu próprio Config.fpw com uma configuração de página de código diferente. O Visual FoxPro impede alterar essa configuração depois que o tempo de execução foi iniciado, porque vários servidores .dll podem potencialmente alterar a página de código padrão de um tempo de execução. Portanto, uma vez definida, a página de código é permanente até que o tempo de execução seja liberado.

> **Dica:** Usuários que precisam de servidores, cada um com uma página de código exclusiva, podem colocar esses servidores, junto com uma cópia da biblioteca de tempo de execução VFP9T.dll, em uma pasta exclusiva. Um servidor sempre usará por padrão uma biblioteca de tempo de execução armazenada em sua pasta. Para obter mais informações, consulte VFP9T.DLL Run-Time Library .

# Considerações especiais de linguagem

Ao trabalhar com servidores de automação, esteja ciente da funcionalidade dos seguintes comandos, pois seu comportamento difere ligeiramente das operações normais do produto:
 - SET PROCEDURE command Este comando é exclusivo de cada thread individual, pois é armazenado no armazenamento local da thread. No entanto, o Visual FoxPro executa implicitamente um SET PROCEDURE para todo o servidor por padrão quando você instancia um servidor COM .exe ou .dll. Por exemplo: ? SET("PROCEDURE") C:\VFP\MYSERVER.DLL Isso torna possível acessar qualquer procedimento armazenado no servidor. Se um objeto existente na thread chamar SET PROCEDURE , o caminho de procedimento é redefinido para nada. No entanto, um novo objeto criado na mesma thread redefinirá automaticamente o caminho de procedimento para todo o servidor novamente.
- SET CLASS command Este comando funciona de forma semelhante ao SET PROCEDURE . Seu valor é mantido no armazenamento local da thread; no entanto, é inicializado para todo o conjunto de bibliotecas de classes em seu servidor .exe ou .dll. Por exemplo: ? SET("CLASS") C:\VFP\myClass.VCX ALIA
- CD , CHDIR , e SET DEFAULT commands Esses comandos alteram o diretório padrão de todo o processo, portanto afetam todas as threads que fazem parte do processo. Em vez de usar CD , CHDIR , e SET DEFAULT , use o comando SET PATH .
