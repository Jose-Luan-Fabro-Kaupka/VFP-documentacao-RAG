# Propriedade ProjectHookLibrary

A biblioteca de classes visuais .vcx que contém a classe ProjectHook padrão para um projeto.

```foxpro
Object.ProjectHookLibrary[ = cLibraryName]
```

# Valor de retorno
 **cLibraryName**
Especifica uma biblioteca de classes visuais .vcx que contém uma classe baseada na classe base ProjectHook. Depois de especificar a biblioteca de classes visuais .vcx com esta propriedade, use a propriedade ProjectHookClass para especificar a classe padrão para o projeto. Para excluir a classe ProjectHook padrão de um projeto, defina a propriedade ProjectHookLibrary ou ProjectHookClass como a cadeia de caracteres vazia.

# Observações

Aplica-se a: Project Object (Visual FoxPro)

Você também pode especificar a classe ProjectHook padrão para um projeto na guia Project Tab, Project Information Dialog Box da caixa de diálogo Project Information Dialog Box.

Alterar a propriedade ProjectHookLibrary não instancia o novo objeto ProjectHook. A alteração entra em vigor na próxima vez que o projeto é aberto. Para alterar o objeto ProjectHook atual, use a propriedade ProjectHook.

Para obter mais informações sobre projetos, consulte Project Manager Hooks.
