# Propriedade KeyPreview

Especifica se o evento KeyPress de um formulário intercepta os eventos KeyPress de um controle. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.KeyPreview[ = lExpr]
```

# Valor de retorno
 **lExpr**
As configurações da propriedade KeyPreview são: Configuração Descrição True (.T.) O formulário recebe eventos KeyPress primeiro e então o controle ativo recebe eventos KeyPress. False (.F.) (Padrão) O controle ativo recebe eventos KeyPress; o formulário não.

# Observações

Aplica-se a: Objeto Form | Objeto Page | Variável de sistema _SCREEN | Objeto ToolBar

A propriedade KeyPreview é usada para permitir que o formulário trate eventos KeyPress antes que o controle ativo os processe.

Você pode usar esta propriedade para criar um procedimento de tratamento de teclado para um formulário. Por exemplo, quando um aplicativo usa teclas de função, você pode processar as teclas no nível do formulário em vez de escrever código para cada controle que pode receber eventos de tecla.

Se um formulário não tem controles visíveis e habilitados, ele recebe automaticamente todos os eventos de teclado.
