# Propriedade MDIForm

Especifica se o formulário é compatível com interface de documentos múltiplos (MDI).

# Sintaxe

```foxpro
Object.MDIForm [= lValue]
```

# Valor da propriedade
 **IExpr**
As configurações para a propriedade MDIForm são: Configuração Descrição True (.T) O formulário será combinado com um formulário pai quando maximizado. False (.F) (Padrão) O formulário está sempre em uma janela separada.

# Observações

Defina a propriedade MDIForm de um formulário como True (.T.) se você deseja que o formulário filho seja combinado com o pai quando maximizado, ou como False (.F.) se a janela filha deve ser mantida como uma janela separada quando maximizada.
