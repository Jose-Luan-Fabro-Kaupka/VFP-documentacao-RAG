# Método SetViewPort

Define os valores das propriedades ViewPortLeft e ViewPortTop para um formulário.

```foxpro
Object.SetViewPort(nLeft, nTop)
```

#### Parâmetros
 **nLeft**
Especifica o valor da propriedade ViewPortLeft para o formulário.
**nTop**
Especifica o valor da propriedade ViewPortTop para o formulário.

# Observações

Aplica-se a: Form Object

O método SetViewPort retorna true (.T.) se as propriedades ViewPortLeft e ViewPortTop forem definidas com sucesso; caso contrário, false (.F.) é retornado. O método SetViewPort é ignorado para formulários que não contêm barras de rolagem.

A unidade de medida das propriedades ViewPortLeft e ViewPortTop é determinada pela configuração da propriedade ScaleMode do formulário – pixels (o padrão) ou foxels.
