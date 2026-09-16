# Variável de sistema _GETEXPR

Especifica o programa executado quando você emite o comando GETEXPR ou invoca a caixa de diálogo Expression Builder no Visual FoxPro.

```foxpro
_GETEXPR = ProgramName
```

#### Parâmetros
 **ProgramName**
Especifica um programa executado quando você emite o comando GETEXPR ou invoca a caixa de diálogo Expression Builder no Visual FoxPro. Se o seu programa estiver em um diretório diferente do diretório padrão atual, inclua um caminho com o nome do programa.

# Observações

_GETEXPR contém a cadeia de caracteres vazia por padrão; a cadeia vazia indica que a caixa de diálogo Expression Builder padrão do Visual FoxPro é exibida quando o comando GETEXPR é executado ou quando você invoca a caixa de diálogo Expression Builder no Visual FoxPro.

Você pode criar seu próprio programa Expression Builder que é executado quando o comando GETEXPR é executado ou quando você invoca a caixa de diálogo Expression Builder no Visual FoxPro. Seu programa Expression Builder deve conter uma instrução LPARAMETERS ou PARAMETERS como primeira linha executável do programa para aceitar quatro parâmetros que o Visual FoxPro passa ao programa. Os parâmetros estão listados abaixo na ordem em que são passados:

| Parâmetro | Descrição |
| --- | --- |
| cExpressionType | Especifica o tipo da expressão. |
| cErrorMessageText | Especifica a mensagem de erro exibida se a expressão não for válida. |
| cDefaultExpression | Especifica a expressão padrão inicial no Expression Builder. |
| cCaptionText | Especifica o título que aparece no Expression Builder. |

Por exemplo, a seguinte pode ser a primeira linha executável do seu programa Expression Builder:

```foxpro
LPARAMETERS cExpressionType, cErrorMessageText, ;
   cDefaultExpression, cCaptionText
```

Se o seu programa Expression Builder for executado quando a caixa de diálogo Expression Builder for invocada no Visual FoxPro, os três primeiros parâmetros contêm a cadeia de caracteres vazia e o quarto parâmetro contém cCaptionText, o título que aparece no Expression Builder.

Observe que o Expression Builder do Visual FoxPro é uma caixa de diálogo modal. Seu programa Expression Builder deve definir as propriedades do formulário com os seguintes valores para criar uma caixa de diálogo modal:

| Propriedade do formulário | Valor da propriedade |
| --- | --- |
| AlwaysOnTop | True (.T.) |
| Desktop | True (.T.) |
| WindowType | 1 – Modal |
