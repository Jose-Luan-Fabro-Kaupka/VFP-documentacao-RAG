# Função GETOBJECT( )

Ativa um objeto Automation e cria uma referência ao objeto.

```foxpro
GETOBJECT(cFileName | Moniker [, cClassName])
```

#### Parâmetros
 **cFileName**
Especifica o caminho completo e o nome do arquivo a ser ativado. O aplicativo não precisa ser especificado, porque as bibliotecas de vínculo dinâmico OLE determinam o aplicativo a iniciar com base no nome do arquivo fornecido. Por exemplo, o código a seguir inicia o Microsoft Excel, abre um arquivo chamado BUDGET.XLS e cria uma referência por meio de uma variável de objeto chamada MBUDVAR: MBUDVAR = GETOBJECT('C:\EXCEL\WORK\BUDGET.XLS')
**Moniker**
O identificador de um objeto COM que implementa a interface IMoniker. Um moniker pode ser qualquer um dos seguintes tipos: file, item, generic composite, anti-, pointer e URL. Para obter detalhes sobre monikers COM, pesquise por "IMoniker" na Microsoft Developer Network.
**cClassName**
Especifica o nome da classe do objeto a ser recuperado. Alguns aplicativos podem armazenar mais de um tipo de objeto no mesmo arquivo, permitindo que você use o nome da classe para especificar o objeto a ser ativado. Por exemplo, se um aplicativo de processamento de texto armazena seus documentos, definições de macro e objetos ToolBar no mesmo arquivo, você pode criar uma referência ao arquivo de documento com o seguinte comando: MDOCFILE = GETOBJECT('C:\WRDPROC\MYDOC.DOC','WrdProc.Document') Com alguns aplicativos servidor, cada vez que você emite GETOBJECT( ), uma instância adicional do aplicativo é iniciada, usando memória adicional. Se o aplicativo já estiver em execução, você pode evitar que instâncias adicionais do aplicativo sejam iniciadas omitindo FileName e incluindo ClassName, como neste exemplo: oleApp = GETOBJECT(, "Excel.Application")

# Retorno

Referência de objeto

# Observações

Use GETOBJECT( ) para ativar um objeto Automation de um arquivo e atribuir uma referência ao objeto por meio de uma variável de memória ou elemento de matriz.

Se você especificar um arquivo ou nome de classe inválido, um erro OLE é exibido e a função GETOBJECT( ) retorna uma cadeia de caracteres vazia.

# Exemplo

Por exemplo, em uma rede que implementou Active Directory Services, você pode consultar a rede para obter informações sobre um usuário específico.

```foxpro
   *  Replace "DomainName" with the domain name, and "UserLoginID"
   *  with the login ID of the user you are looking up.
   oUser = GetObject("WinNT://DomainName/UserLoginID,user")
   ? oUser.FullName
```
