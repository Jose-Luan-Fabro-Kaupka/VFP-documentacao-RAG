# Método NewObject

Adiciona uma nova classe ou objeto a um objeto diretamente de uma biblioteca de classes visuais .vcx ou programa.

```foxpro
Object.NEWOBJECT(cObjectName, cClassName [, cModule [, cInApplication
   [, eParameter1, eParameter2, ...]]])
```

# Observações
 **cObjectName**
Especifica o nome usado para referenciar a classe ou objeto recém-adicionado.
**cClassName**
Especifica a classe ou objeto da qual a nova classe ou objeto é adicionado.
**cModule**
Especifica uma biblioteca de classes visuais .vcx ou programa Visual FoxPro (.prg, .mpr, .app, .exe e assim por diante) contendo a classe ou objeto especificado com cClassName. O padrão é uma biblioteca de classes visuais .vcx; você deve incluir uma extensão se especificar um programa. Observação Uma biblioteca de classes pode ter um alias. Para especificar uma classe ou objeto de uma biblioteca de classes com alias, inclua o alias da biblioteca de classes seguido de um ponto e o nome do objeto. Se cModule for omitido, ou for a cadeia de caracteres vazia ou o valor nulo, o Visual FoxPro procura a classe ou objeto na seguinte ordem: Classes base do Visual FoxPro. Definições de classe definidas pelo usuário na memória na ordem em que foram carregadas. Classes no programa atual. Bibliotecas de classes abertas com SET CLASSLIB. Classes em arquivos de procedimento abertos com SET PROCEDURE. Classes na cadeia de execução de programa do Visual FoxPro. O registro OLE se SET OLEOBJECT estiver ON.
**cInApplication**
Especifica o aplicativo Visual FoxPro (.exe ou .app) contendo a biblioteca de classes visuais .vcx que você especifica com cClassLibName. Você deve incluir uma extensão para o aplicativo. CInApplication é ignorado se cModule for omitido, ou se cInApplication for a cadeia de caracteres vazia ou o valor nulo.
**eParameter1 , eParameter2 , ...**
Especifica parâmetros opcionais que são passados ao procedimento do evento Init da classe ou objeto.

# Observações

Aplica-se a: Objeto Column | Controle CommandGroup | Objeto Container | Objeto Custom | Objeto DataEnvironment | Objeto Form | Objeto FormSet | Controle Grid | Controle OptionGroup | Objeto Page | Controle PageFrame | Variável de sistema _SCREEN | Objeto ToolBar | Objeto Session

O método NEWOBJECT permite adicionar uma nova classe ou objeto a um objeto sem abrir uma biblioteca de classes visuais .vcx ou arquivo de procedimento.
