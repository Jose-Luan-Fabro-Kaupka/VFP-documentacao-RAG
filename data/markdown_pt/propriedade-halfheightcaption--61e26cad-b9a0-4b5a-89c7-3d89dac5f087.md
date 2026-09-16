# Propriedade HalfHeightCaption

Especifica se a legenda de um formulário tem metade da altura normal. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.HalfHeightCaption[ = lExpr]
```

# Valor de retorno
 **lExpr**
As configurações da propriedade HalfHeightCaption são: Configuração Descrição True (.T.) A legenda do formulário tem metade da altura normal. False (.F.) (Padrão) A legenda do formulário tem altura normal.

# Observações

Aplica-se a: Objeto Form | Variável de Sistema _SCREEN | Propriedade Height

Menus em formulários SDI (ShowWindow = 2) não são suportados quando a propriedade HalfHeightCaption do formulário está definida como true (.T.).
