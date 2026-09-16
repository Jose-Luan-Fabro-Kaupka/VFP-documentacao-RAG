# Propriedade ProjectHookClass

A classe ProjectHook padrão para um projeto.

```foxpro
Object.ProjectHookClass[ = cClassName]
```

# Valor de retorno
 **cClassName**
Especifica a classe ProjectHook padrão para um projeto. Antes de especificar uma classe ProjectHook para um projeto, especifique a biblioteca de classes visuais .vcx que contém a classe ProjectHook com a propriedade ProjectHookLibrary. Para excluir a classe ProjectHook padrão de um projeto, defina a propriedade ProjectHookClass ou ProjectHookLibrary como a cadeia de caracteres vazia.

# Observações

Aplica-se a: objeto Project (Visual FoxPro)

Você também pode especificar a classe ProjectHook padrão para um projeto na guia Project da caixa de diálogo Project Information Dialog Box.

Alterar a propriedade ProjectHookClass não instancia o novo objeto ProjectHook. A alteração entra em vigor na próxima vez que o projeto é aberto. Para alterar o objeto ProjectHook atual, use a propriedade ProjectHook.

Para obter mais informações sobre projetos, consulte Project Manager Hooks.
