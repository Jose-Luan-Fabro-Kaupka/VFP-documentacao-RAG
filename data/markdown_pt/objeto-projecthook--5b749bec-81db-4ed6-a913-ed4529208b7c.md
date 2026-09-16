# Objeto ProjectHook

Instanciado sempre que um projeto é aberto, fornecendo acesso programático a eventos do projeto.

```foxpro
ProjectHook
```

# Observações

Um objeto ProjectHook é uma classe base do Visual FoxPro que é instanciada por padrão sempre que um projeto é aberto. (Você pode incluir a cláusula NOPROJECTHOOK em CREATE PROJECT e MODIFY PROJECT para impedir que um objeto ProjectHook seja instanciado para o projeto.)

O objeto ProjectHook permite acesso programático a eventos que ocorrem em um projeto. Por exemplo, você pode executar código sempre que um arquivo é adicionado a um projeto. Observe que você pode especificar uma classe de hook de projeto padrão para novos projetos na guia Projects da caixa de diálogo Options ou pode especificar uma classe de hook de projeto padrão para um projeto individual na caixa de diálogo Project Information. Em tempo de execução, você pode usar a propriedade ProjectHook para especificar uma classe de hook de projeto para um projeto, como no exemplo a seguir:

```foxpro
MODIFY PROJECT MyProject
_VFP.Projects('MyProject.pjx').ProjectHook = ;
   NewObject('MyProjectHook', 'MyClass.vcx')
```

Uma classe base ProjectHook pode ser criada com CREATE CLASS, CREATEOBJECT( ) ou NEWOBJECT( ).

Para obter mais informações sobre projetos, consulte Hooks do Project Manager.
