# Hierarquia de objetos Project

A hierarquia de projeto consiste na coleção Projects, objetos Project na coleção e um objeto ProjectHook associado a cada objeto de projeto. Um objeto Project contém uma coleção Files consistindo em arquivos de projeto e uma coleção Servers consistindo em Automation servers criados a partir do projeto.

O diagrama a seguir ilustra a hierarquia de projeto dentro do modelo de objetos do Visual FoxPro.
 Hierarquia Projects

Um objeto Project é instanciado quando um projeto é criado, aberto ou reconstruído, ou quando um arquivo de aplicativo (.app), biblioteca de vínculo dinâmico (.dll) ou executável (.exe) é compilado a partir do projeto. Quando um projeto associado a uma classe ProjectHook é aberto, um objeto ProjectHook é instanciado por padrão.

Quando um evento ocorre em um projeto, o objeto Project passa o evento ao objeto ProjectHook. O código do usuário no evento do objeto ProjectHook é executado e devolve o controle ao objeto Project. O valor retornado ao objeto Project pelo objeto ProjectHook determina se o objeto Project conclui a operação.

> **Dica:** Colocar NODEFAULT no código do evento impede que a ação padrão seja executada. Por exemplo, colocar NODEFAULT no evento QueryAddFile de um objeto ProjectHook impede que um arquivo seja adicionado a um projeto.

As seções a seguir contêm mais informações sobre a hierarquia de projeto:
 - Coleção Projects na hierarquia de projeto
- Objeto Project na hierarquia de projeto
- Objeto ProjectHook na hierarquia de projeto

# Coleção Projects na hierarquia de projeto

A coleção Projects fornece acesso direto a objetos Project, tornando possível manipular um projeto e os arquivos e servidores que o projeto contém. Quando um projeto é criado ou aberto ou quando um arquivo de aplicativo (.app), biblioteca de vínculo dinâmico (.dll) ou executável (.exe) é compilado a partir do projeto, um objeto de projeto é adicionado à coleção projects.

Você pode obter informações sobre um projeto na coleção Projects usando suas propriedades e métodos. Por exemplo, as linhas de código a seguir mostram duas maneiras de exibir os nomes de todos os projetos em uma coleção Projects. O primeiro exemplo usa a propriedade Count e o método Item de uma coleção Projects. O segundo exemplo usa o comando FOR EACH.

```foxpro
nProjectCount = Application.Projects.Count
FOR nCount = 1 TO nProjectCount
   ? Application.Projects.Item(nCount).Name
NEXT
FOR EACH oProj IN Application.Projects
   ? oProj.Name
ENDFOR
```

Para obter mais informações, consulte Coleção Projects (Visual FoxPro).

# Objeto Project na hierarquia de projeto

Um objeto Project é instanciado quando um projeto é criado, aberto ou reconstruído, ou quando um arquivo de aplicativo (.app), biblioteca de vínculo dinâmico (.dll) ou executável (.exe) é compilado a partir do projeto. Um objeto Project contém uma coleção Files consistindo em arquivos de projeto e uma coleção Servers consistindo em Automation servers criados a partir do projeto.

O objeto Project torna possível manipular um projeto programaticamente e acessá-lo através de um objeto Application. O objeto Application tem uma propriedade ActiveProject que fornece uma referência de objeto a um projeto aberto no Project Manager atualmente ativo.

Você pode manipular um objeto Project através de suas propriedades e métodos. Para obter mais informações, consulte Objeto Project (Visual FoxPro) e Objeto Application.

### Coleção Files

A coleção Files fornece acesso direto a um objeto File, o que torna possível manipular objetos File em um projeto enquanto o projeto está aberto. Você pode manipular um objeto File usando suas propriedades e métodos. Para obter mais informações, consulte Objeto File (Visual FoxPro).

Você pode adicionar arquivos a um projeto programaticamente. Por exemplo, a linha de código a seguir usa a propriedade ActiveProject de um objeto Application para adicionar um programa, Main.prg, ao projeto atualmente ativo:

```foxpro
Application.ActiveProject.Files.Add('Main.prg')
```

A linha de código a seguir adiciona Main.prg ao primeiro projeto na coleção Projects:

```foxpro
Application.Projects[1].Files.Add('Main.prg')
```

Você pode obter informações sobre um arquivo em uma coleção Files usando suas propriedades e métodos. Por exemplo, as linhas de código a seguir mostram duas maneiras de exibir os nomes de todos os arquivos em uma coleção Files. O primeiro exemplo usa a propriedade Count e o método Item de uma coleção Files. O segundo exemplo usa o comando FOR EACH.

```foxpro
nFileCount = Application.ActiveProject.Files.Count
FOR nCount = 1 TO nFileCount
   ? Application.ActiveProject.Files.Item(nCount).Name
NEXT
FOR EACH oProj IN Application.ActiveProject.Files
   ? oProj.Name
ENDFOR
```

Para obter mais informações, consulte Coleção Files (Visual FoxPro).

### Coleção Servers

A coleção Servers fornece acesso direto a um objeto Server, o que torna possível manipular objetos Server que um projeto contém. Você pode manipular uma coleção Servers através de suas propriedades e métodos. Para obter mais informações, consulte Coleção Servers.

Quando você compila um arquivo de biblioteca de vínculo dinâmico (.dll) ou executável (.exe) contendo um Automation server a partir do projeto, um objeto Server é adicionado à coleção Servers. Para obter mais informações sobre como criar Automation servers, consulte Como: criar Automation Servers em Compartilhamento de informações e adição de OLE.

> **Observação:** Um objeto Server não é instanciado até que o projeto contendo a classe OLEPUBLIC, especificada no comando DEFINE CLASS, seja compilado. Para obter mais informações, consulte Comando DEFINE CLASS .

Um objeto Server torna possível obter informações sobre Automation servers contidos em um projeto, por exemplo, informações de biblioteca de tipos. Essas informações também estão disponíveis na guia Servers na caixa de diálogo Informações do projeto. Para obter mais informações, consulte Guia Servers, caixa de diálogo Informações do projeto.

Você pode manipular um objeto Server em uma coleção Servers usando suas propriedades. Para obter mais informações, consulte Objeto Server.

# Objeto ProjectHook na hierarquia de projeto

Quando um projeto associado a uma classe ProjectHook é aberto, um objeto ProjectHook é instanciado por padrão.

> **Dica:** Para impedir que um objeto ProjectHook seja instanciado para o projeto, inclua a cláusula NOPROJECTHOOK nos comandos CREATE PROJECT e MODIFY PROJECT. Para mais informações, consulte Comando CREATE PROJECT e Comando MODIFY PROJECT .

O objeto ProjectHook permite acesso programático a eventos que ocorrem em um projeto. Por exemplo, você pode executar código ao adicionar um arquivo a um projeto. O objeto ProjectHook difere de um objeto Project, que contém todas as propriedades e métodos disponíveis na caixa de diálogo Informações do projeto. Para obter mais informações, consulte Caixa de diálogo Informações do projeto.

A classe ProjectHook padrão é especificada para novos projetos na guia Projects da caixa de diálogo Opções. Você pode substituir a classe ProjectHook padrão especificando uma classe project hook diferente para um projeto individual na caixa de diálogo Informações do projeto. No entanto, se nenhuma classe ProjectHook padrão for especificada na guia Projects, novos projetos não são associados a um objeto ProjectHook. Para obter mais informações, consulte Guia Projects, caixa de diálogo Opções.

Em tempo de execução, você pode usar a propriedade ProjectHook para especificar uma classe project hook para um projeto. Se você alterar a classe ProjectHook para um projeto, a nova classe ProjectHook não entra em vigor até que o projeto seja fechado e aberto novamente.

Você pode manipular um objeto ProjectHook através de propriedades, métodos e eventos. Para obter mais informações, consulte Objeto ProjectHook.
