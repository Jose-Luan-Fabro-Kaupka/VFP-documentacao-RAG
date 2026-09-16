# Servidores Automation no Visual FoxPro

Você pode criar, compilar, distribuir e acessar servidores Automation no Visual FoxPro.

# Criando servidores Automation

Você pode criar servidores Automation como classes definidas pelo usuário OLE public em arquivos de programa (.prg) ou bibliotecas de classes visuais (.vcx). Você pode ter quantas classes OLE public quiser em um projeto de aplicativo.

# Compilando servidores Automation

Depois de criar um servidor Automation, você pode compilá-lo como um componente out-of-process ou in-process. Um componente out-of-process é um arquivo executável (.exe) que roda em seu próprio processo. Um componente in-process é um arquivo de biblioteca de vínculo dinâmico (.dll) que roda no mesmo espaço de endereço de processo do cliente que o chama. A comunicação entre um aplicativo cliente e um servidor out-of-process é chamada de comunicação entre processos.

Quando você compila um servidor Automation como um arquivo executável (.exe), não perde nenhuma funcionalidade de arquivos executáveis normais. Você pode executar o arquivo executável, fornecer uma interface do usuário e qualquer outra funcionalidade disponível para um aplicativo. Além disso, aumenta a extensibilidade do seu aplicativo ao permitir que outros aplicativos usem a funcionalidade que você fornece no servidor Automation.

Ao compilar servidores Automation, considere o seguinte:
 - Servidores in-process podem ser mais rápidos porque não há sobrecarga de comunicação entre processos.
- Servidores out-of-process podem ser implantados remotamente, enquanto servidores in-process não podem.
- Um servidor in-process e o cliente compartilham um espaço de endereço de processo; portanto, qualquer erro grave no servidor in-process encerra o cliente. Erros em um servidor out-of-process encerram apenas o servidor.

A compilação de um servidor Automation cria três arquivos:
 - Um arquivo .exe ou .dll.
- Um arquivo de biblioteca de tipos (.tlb). O arquivo de biblioteca de tipos é um arquivo binário que lista todas as classes publicadas no seu servidor Automation, junto com suas propriedades, métodos e eventos. Navegadores de objetos OLE leem essas informações e as apresentam em uma interface legível. Para obter mais informações, consulte Binding Type Libraries .
- Um arquivo de registro (.vbr) O arquivo de registro lista os IDs globais exclusivos (GUID) das classes no seu servidor. Observação Um arquivo de registro .vbr é igual a um arquivo de registro .reg, exceto que o arquivo .vbr não inclui caminhos codificados.

# Distribuindo servidores Automation do Visual FoxPro

Quando você distribui um servidor Automation (.dll), deve incluir os seguintes arquivos:
 - VFP VersionNumber R.dll ou VFP VersionNumber T.dll, onde VersionNumber representa o número da versão desta release do Visual FoxPro.
- VFP VersionNumber RENU.dll
- GDIPlus.dll
- MSVCR70.dll

Se você estiver distribuindo um servidor Automation como um arquivo executável (.exe), consulte Preparation for Distributing Applications. Para obter mais informações sobre bibliotecas de tempo de execução, consulte VFP9R.DLL Run-Time Library e VFP9T.DLL Run-Time Library.

# Acessando servidores Automation do Visual FoxPro

Qualquer aplicativo que possa criar objetos Automation pode criar objetos com base no seu servidor Automation, definir propriedades que não sejam HIDDEN ou PROTECTED e chamar métodos. Por exemplo, supondo que seu servidor se chame `foxole` e contenha uma classe chamada `person` com um método GetName, o seguinte código poderia ser executado no Visual FoxPro:

```foxpro
oTest = CREATEOBJECT("foxole.person")
cName = oTest.GetName()
```

Código semelhante poderia ser executado no Microsoft Excel ou Visual Basic:

```foxpro
Set oTest = CreateObject("foxole.person")
cName$ = oTest.GetName()
```

# Tratando erros em servidores Automation do Visual FoxPro

A única interação com os objetos fornecidos por um servidor Automation ocorre pelos métodos e propriedades das classes expostas. Quando um aplicativo cliente chama um método de um objeto e ocorre um erro no servidor Automation, o método retorna um valor de erro ou gera um erro no aplicativo cliente.

O aplicativo cliente decide se alerta o usuário ou prossegue com outro caminho de execução. O servidor Automation em si nunca interage com o usuário. Isso permite que a localização do servidor Automation seja transparente para o aplicativo cliente. O servidor Automation pode ser local, executando no computador do usuário, ou você pode usar o recurso Remote Automation do Visual FoxPro para executá-lo em um servidor de rede.

Quando um servidor Automation do Visual FoxPro gera um erro, o servidor Automation define o objeto COM ErrorInfo usando IErrorInfo e cancela a saída do método atual. O cliente Automation pode liberar o servidor Automation do Visual FoxPro ou, se o cliente tiver acesso ao objeto COM ErrorInfo, tratar a exceção com base nessas informações. Para obter mais informações, consulte _ErrorInfo( ) API Library Routine.

A função COMRETURNERROR( ) trata erros que ocorrem em um servidor Automation. Você pode usar COMRETURNERROR( ) no método Error para preencher a estrutura de exceção COM com informações que os clientes Automation podem usar para determinar a origem dos erros do servidor Automation. Para obter mais informações, consulte COMRETURNERROR( ) Function.
