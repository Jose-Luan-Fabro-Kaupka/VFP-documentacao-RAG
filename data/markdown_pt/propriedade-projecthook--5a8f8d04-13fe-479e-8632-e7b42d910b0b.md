# Propriedade ProjectHook

Uma referência de objeto ao objeto ProjectHook instanciado para um projeto.

```foxpro
Object.ProjectHook[ = oProjectHookClass]
```

# Valor de retorno
 **oProjectHookClass**
Especifica uma classe baseada na classe base ProjectHook do Visual FoxPro. Por padrão, contém uma referência de objeto à classe ProjectHook padrão especificada na guia Project da caixa de diálogo Project Information.

# Observações

Aplica-se a: Objeto Project (Visual FoxPro)

A propriedade ProjectHook contém o valor nulo se não foi atribuída uma classe baseada na classe base ProjectHook ou se o projeto não tem uma classe ProjectHook padrão (especificada na guia Project da caixa de diálogo Project Information). Atribuir o valor nulo à propriedade ProjectHook libera o objeto ProjectHook, mas não afeta a classe ProjectHook padrão do projeto.

Para obter mais informações sobre projetos, consulte Hooks do Project Manager.
