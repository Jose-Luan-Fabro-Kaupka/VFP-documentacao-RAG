# Propriedade Desktop

Especifica se um formulário pode aparecer em qualquer lugar da área de trabalho do Windows ou está contido na janela principal do Visual FoxPro. Disponível em tempo de design; somente leitura em tempo de execução.

```foxpro
Object.Desktop[ = lExpr]
```

# Valor de retorno
 **lExpr**
As configurações da propriedade Desktop são: Setting Description True (.T.) O formulário pode estar em qualquer lugar da área de trabalho do Windows. False (.F.) (Padrão) O formulário está contido na janela principal do Visual FoxPro.

# Observações

Aplica-se a: Form Object | _SCREEN System Variable

A propriedade Desktop é ignorada se a propriedade ShowWindow estiver definida como 2 – As Top-Level form.

Você não deve usar a propriedade Desktop ao criar aplicativos Single Document Interface (SDI) nos quais você pode querer ocultar a janela da área de trabalho do Visual FoxPro (_SCREEN). Em vez disso, defina a propriedade ShowWindow como 2 para criar um formulário de nível superior.
