# FoxIs, um servidor de Internet Visual FoxPro

FoxIs, localizado no diretório Visual FoxPro ...\Samples\Servers\Foxisapi\FoxIs, ilustra a criação de um .exe fora de processo ou .dll em processo com funcionalidade ISAPI que pode ser acessado dentro do Visual FoxPro como programa autônomo, de clientes Automation e de um navegador Web. Alterações que você faz em suas classes podem aprimorar o servidor Automation, independentemente de como é executado.

### Para open the FoxIs sample project
- Digite o seguinte na janela Command: MODIFY PROJECT (HOME(2) + 'servers\foxisapi\foxis\foxis')

# Executando o exemplo FoxIs

Você pode executar o exemplo FoxIs de quatro maneiras diferentes. Ao testar o código, é uma boa ideia executar o exemplo nesta ordem:

# Executando dentro do Visual FoxPro

Para executar o exemplo FoxIs dentro do Visual FoxPro, execute o código a seguir na janela Command.

```foxpro
SET DEFAULT TO (HOME(2) + 'servers\foxisapi\foxis\')
SET CLASSLIB TO employee
ox = CREATEOBJECT('employee')
ox.show
```

# Executando como executável independente

Você pode compilar o exemplo em um arquivo executável com a seguinte linha de código:

```foxpro
BUILD EXE foxis FROM foxis
```

O arquivo compilado, FOXIS.EXE, é um programa Windows que pode ser adicionado ao menu Iniciar do Windows, iniciado pelo Windows Explorer e assim por diante.

# Executando como servidor Automation

Depois que o exemplo FoxIs foi compilado em um .exe ou .dll, ele é registrado como servidor Automation no registro do Windows. Você pode criar um objeto baseado na classe employee de qualquer controlador OLE, por exemplo Excel, Visual Basic e Visual FoxPro:

```foxpro
ox = CREATEOBJECT('foxis.employee')
ox.SHOW
```

# Executando de um navegador Web

Você pode até executar o exemplo FoxIs de um navegador Web, que pode estar em outra máquina como um 286 executando MS-DOS, uma máquina Unix, um Macintosh ou um Personal Digital Assistant.

# Requisitos de sistema para uso na Internet

Para executar o exemplo FoxIs de um navegador Web, você deve estar executando:
 - Windows 98 ou Windows 2000 ou posterior.
- Um servidor Web compatível com ISAPI, como o Microsoft Personal Web Server para Windows 98 ou Microsoft Internet Information Services (IIS). O IIS vem com Windows 2000 e posterior e pode ser baixado de www.microsoft.com; o Personal Web Server também pode ser baixado de www.microsoft.com.

Se você estiver usando Windows 2000 ou posterior, precisa executar o utilitário DCOMCNFG para configurar o DCOM para conceder direitos ao serviço IIS para instanciar objetos OLE.

### Para configure Windows 2000 or later DCOM
- No prompt de comando, digite DCOMCNFG e pressione Enter.
- Na guia Applications, selecione o nome do servidor Automation. Quando você compila o servidor, o aplicativo é "employee" por padrão.
- Na guia Default Security da caixa de diálogo Distributed COM Configuration Properties, escolha Edit Default para cada área: Default Access Permissions, Default Launch Permissions e Default Configuration Permissions.
- Na caixa de diálogo Registry Value Permissions para cada área, escolha Add.
- Na caixa Add Names da caixa de diálogo Add Users and Groups, digite o nome do seu servidor WWW e seu nome de usuário de login. Você pode ver o nome do servidor na janela Microsoft Internet Service Manager Properties. Se o nome da sua máquina é MINE, a seguinte linha na caixa Add Names configura um usuário padrão: \MINE\IUSR_MINE Se o nome da sua máquina é MINE e você faz login como HOMER, a seguinte linha na caixa Add Names configura permissões para você ao fazer login: \MINE\HOMER

# Configurando o exemplo FoxIs para acesso à Internet

Para configurar o exemplo FoxIs, você precisa criar um .exe ou .dll do projeto FoxIs e depois copiar o arquivo para seu diretório Inetsvr\Scripts.

### Para set up the FoxIs Sample
- Abra o projeto FOXIS.
- Escolha o botão Build e depois escolha Build COM DLL.
- Copie Foxisapi.dll para sua pasta Inetsrv\Scripts.

# Testes preliminares

Você pode testar o aplicativo de exemplo FoxIs em vários níveis para verificar se está configurado corretamente.

### Para see if the code works
- No menu Program, escolha Do.
- Selecione Main.prg na pasta Visual FoxPro Samples\Servers\Foxisapi.
- Escolha Do.

### Para see if the .EXE works
- Na janela Command do Visual FoxPro, emita o seguinte comando: BUILD EXE Foxis.exe FROM foxis
- Clique duas vezes em Foxis.exe no Windows Explorer.

### Para see if the FoxIs Automation server works
- Execute os seguintes comandos: OX= CREATEOBJECT('FOXIS.EMPLOYEE') OX.Show && See if it works as a ISAPI Automation server ?OX.Startup( ) && See if it returns html

É muito mais fácil depurar servidores Automation de um controlador Automation (como o Visual FoxPro) antes de instanciá-lo no FoxIs.

# Configurar a página HTML

Para começar, você precisa de uma página HTML que contenha uma referência a uma URL. Por exemplo, pegue o código a seguir e coloque-o no arquivo Wwwroot\default.htm.

```foxpro
 VFP ISAPI AUTOMATION SERVER DEMO PAGE
```

Depois use um navegador (que pode estar na mesma máquina) e conecte-se a YourMachineName. Por exemplo, se o nome da sua máquina era "myMachine", digite "myMachine" como a URL para acessar. Isso exibirá a página Default.htm no servidor chamado "myMachine"

Um CreateObject("foxis.employee") é iniciado e o método Startup é invocado no objeto, que retorna uma página HTML gerada. Se o servidor Automation ISAPI ainda não foi compilado, o Foxisapi.dll retorna uma página HTML de erro.

Depois use seu navegador Web para acessar o href acima. Se você receber uma página HTML de erro que diz "Foxisapi error", então você sabe que a DLL está sendo carregada e funcionando.

```foxpro
 <FORM ACTION = "/scripts/foxisapi.dll/foxis.employee.cmd">
<INPUT NAME="Cmd" VALUE = "Reset">
<INPUT TYPE="submit" VALUE="Dos Command">
</FORM>
```

Você pode colocar qualquer comando MS-DOS válido e ele será executado na máquina do servidor. Se o comando é "Reset" (padrão), fará o servidor Automation ISAPI liberar a primeira instância assim como a própria, liberando completamente o servidor Automation ISAPI.

Além disso, você pode avaliar qualquer expressão Visual FoxPro. No entanto, se a expressão Visual FoxPro exibir uma interface modal, como a função MESSAGEBOX( ) faz, o servidor Automation ficará aguardando uma resposta que não pode ser fornecida. No entanto, para um .dll em processo, a interface modal é gerenciada automaticamente e o servidor Automation não ficará aguardando.

```foxpro
<FORM ACTION = "/scripts/foxisapi.dll/foxis.employee.cmd?FOXCMD">
<INPUT NAME="Cmd">
<INPUT TYPE="submit" VALUE="Fox Expression">
like "today is "+ cdow(date()) or 45 * 3 or SYS(2004)
</FORM>
```

# Depurando o servidor

Um serviço Windows NT não tem Desktop, portanto nenhuma interface do usuário aparecerá na máquina do servidor. Isso significa que você deve depurar seus aplicativos de servidor antes de implantá-los.

### Para trace through Foxisapi.dll with Visual C++ 5.0
- Abra Foxisapi.mak.
- Remova a marca de comentário da seguinte linha em HttpExtensionProc: // _asm int 3
- Recompile o projeto.
- Inicie o MSDEV com o id de processo (PID) do Inetinfo.exe. Você pode obter o id de processo no Windows Task Manager.

Este processo se aplica ao Windows 2000 ou posterior.

> **Dica:** Ao depurar, você não precisa desligar o servidor Web para alterar o servidor Automation. Você pode simplesmente encerrar o componente fora de processo enviando um valor reset ao método cmd, conforme descrito acima, ou usando as ferramentas Win32 SDK TLIST, KILL, PVIEW ou o Task Manager no Windows 2000 ou posterior.

# A classe ISForm

O "motor" do exemplo é a classe ISForm em Isapi.vcx.

# Pontos de entrada na classe ISForm

Os métodos a seguir podem ser chamados do navegador Web, por meio de Foxisapi.dll, para retornar páginas HTML.

| Método | Retorna |
| --- | --- |
| Cmd | Avaliação de uma expressão Visual FoxPro ou os resultados de um comando MS-DOS. |
| DoSave | Salva as alterações do usuário nos dados e retorna a página HTML employee. |
| Skipit | As informações do employee para o employee especificado na tabela. Skipit recebe informações de cookie passadas como parâmetro do navegador Web, verifica a tabela cookies para encontrar o número de registro anterior e move o ponteiro de registro para frente ou para trás em relação ao número de registro armazenado na tabela cookies. O novo número de registro é gravado de volta na tabela cookies e o método GenHTML é chamado. |
| Startup | As informações do employee para o primeiro employee na tabela. Startup cria um novo id de cookie para o usuário e o envia de volta como uma área de entrada oculta no HTML. |

# Mantendo o servidor ativo

Normalmente, para cada solicitação de um cliente Web, o servidor Automation é instanciado, gera uma página HTML e é liberado com a chamada Release( ) em CallObject( ) em Foxisapi.cpp. Isso significa que todo o runtime do Visual FoxPro será iniciado e encerrado para cada solicitação.

Se o servidor Automation ISAPI estiver registrado como Multi-Use e Release( ) não for chamado, a primeira solicitação iniciará o servidor, mas solicitações subsequentes usarão a mesma instância do servidor, melhorando muito o desempenho. Código em Foxisapi.dll e nos métodos Load, Cmd, DoSave, Startup e Skipit do ISForm gerencia a manutenção da mesma instância do servidor ativa.

# Variáveis na DLL

Duas variáveis são declaradas: pdispObj e pdispDoRelease. Quando o servidor é criado inicialmente, pdispObj é o handle dispatch para o objeto OLE. A variável pdispDoRelease é definida com o mesmo valor de pdispObj e passada por referência como parâmetro para o método do servidor ISForm solicitado pelo navegador Web. Código no servidor Automation ISForm do Visual FoxPro pode alterar o valor de pdispDoRelease.

> **Dica:** Para obter mais informações about this sample, see the comments in the code in ISForm and Foxisapi.cpp.

# O evento Load do formulário

Quando o ISForm é criado, código no evento Load cria duas variáveis public, gpInstance e gpDisp. Na primeira vez que o servidor ISForm é carregado, a variável gpInstance é definida como 1. Instâncias subsequentes incrementam esta variável. Quando uma instância é liberada, gpInstance é decrementada.

# Os métodos de ponto de entrada

Quando um método (Cmd, DoSave, Skipit ou Startup) do ISForm é invocado por meio de Foxisapi.dll, a .dll passa um ponteiro dispatch por referência como parâmetro para o método.

Na primeira vez que o servidor é executado, a contagem de instâncias é definida como 1 e o ponteiro dispatch é armazenado na variável global. Então o valor 0 é armazenado no ponteiro dispatch.

```foxpro
IF m.gnInstance = 1
   IF TYPE('pDisp') $ 'NI'
      gpDisp = m.pDisp
      pDisp = 0
   ENDIF
ENDIF
```

Neste ponto, duas variáveis apontam para o mesmo valor de ponteiro dispatch: gpDisp no servidor Automation ISForm e pdispObj em Foxisapi.dll. O valor de pdispDoRelease na .dll é 0, conforme alterado no servidor Automation ISForm.

Nas vezes subsequentes em que o servidor é chamado, a contagem de instâncias é incrementada, um novo pdispObj é gerado na .dll, armazenado em pdispDoRelease e passado por referência ao método solicitado. Como o valor gnInstance não é 1, a variável gpDisp não é alterada. A partir deste ponto, gpDisp no servidor Automation mantém um valor diferente de pdispObj e pdispDoRelease na .dll.

# Liberando o servidor

Para forçar uma liberação, pdispDoRelease não pode ser 0 e deve ser um valor diferente de pdispObject. O seguinte texto HTML envia um valor ao servidor que afeta uma liberação:

```foxpro
 <FORM ACTION = "/scripts/foxisapi.dll/foxis.employee.cmd">
<INPUT NAME="Cmd" VALUE = "Reset">
<INPUT TYPE="submit" VALUE="Dos Command">
</FORM>
```

O código a seguir no método cmd define o valor pdispDoRelease para o valor dispatch da primeira instância.

```foxpro
CASE 'RESET'$upper(m.p1)
   m.pDisp= m.gpDisp
```

O código na .dll agora liberará a instância atual e a instância original que foi mantida em existência para evitar que o runtime do Visual FoxPro precise ser recarregado cada vez que o servidor era chamado.

# Enviando HTML de volta ao cliente

O método GenHTML da classe ISForm é chamado de cada um dos métodos de ponto de entrada. O HTML retornado do método GenHTML é retornado ao navegador Web por meio do Internet Information Services.

Se o parâmetro mode passado ao método GenHTML não é "FORM", o método GenHTML simplesmente consulta o valor em uma tabela e envia HTML pré-formatado.

```foxpro
IF m.mode != 'FORM'
   =SEEK(m.mode,'html')
   rv = html.html
  RETURN m.rv
ENDIF
```

Se o parâmetro mode é "FORM", código em GenHTML identifica cada um dos labels e textboxes no formulário, os ordena de cima para baixo e da esquerda para a direita, avalia os Captions e ControlSources dos controles e usa as capacidades de mesclagem de texto do Visual FoxPro para construir o texto HTML apropriado para aproximar a exibição do formulário.

Se você adicionar labels e text boxes adicionais ao formulário, eles são automaticamente exibidos no HTML gerado.

# Criando e usando cookies

Como servidor Web, este aplicativo pode ser acessado dezenas de vezes por vários clientes, e precisamos rastrear o estado do usuário. Neste caso, rastreamos apenas o número de registro atual para esse usuário. Poderíamos apresentar ao usuário uma tela de login e usar o nome de usuário como chave para o cookie, mas em vez disso geramos um valor de cookie no método MakeCookie e o passamos como valor oculto no HTML enviado de volta ao usuário. Cada vez que o usuário escolhe ir para um registro diferente, podemos ler o valor do cookie da cadeia HTTP enviada à .dll, localizar o cookie na tabela Cookies, encontrar o número de registro atual e mover o número de registro em relação a este número.

A seguinte propriedade e métodos são usados no processo de manipulação de cookies:
 - Cookie property
- GetCookie method
- MakeCookie method
- WriteCookieInfo method

# Tratamento de erros

Se ocorrer um erro, código no evento Error da classe ISForm chama o método GenHTML com um parâmetro "ERROR." GenHTML lê o texto HTML pré-formatado para erros e o retorna ao código do evento Error. O código do evento Error substitui informações de erro por placeholders no HTML:

```foxpro
   LOCAL rv
   rv = THIS.GenHTML('ERROR')
   rv = strtran(m.rv,'%METHOD%',m.cMethod)
   rv = strtran(m.rv,'%ERRORNO%',STR(m.nError,4))
   rv = strtran(m.rv,'%ERRORMSG%',Message(1))
   rv = strtran(m.rv,'%LINENO%',STR(m.nLine,4))
   THIS.ErrorHTML = m.rv
```

Quando a propriedade ErrorHTML não está vazia, GenHTML envia o valor de ErrorHTML de volta ao cliente.

# Tabelas usadas no exemplo FoxIs

Além da tabela employee usada para entrada e exibição de dados, o exemplo FoxIs usa as tabelas a seguir.

| Tabela | Descrição |
| --- | --- |
| HTML | Contém texto HTML a ser enviado de volta ao navegador Web como cabeçalho para avaliações FoxCMD e DosCMD ou em caso de erro. |
| Cookies | Mantém o controle dos números de registro para vários navegadores Web. O valor exclusivo do campo cookie é passado como valor oculto no texto HTML enviado a um usuário específico. |
