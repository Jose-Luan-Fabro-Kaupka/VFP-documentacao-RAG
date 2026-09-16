# Comando GETEXPR

Exibe a caixa de diálogo Expression Builder para que você possa criar uma expressão e armazená-la em uma variável ou elemento de matriz.

```foxpro
GETEXPR [cCaptionText] TO MemVarName
   [TYPE cExpressionType [; cErrorMessageText]]
   [DEFAULT cDefaultExpression]
```

#### Parâmetros
 **cCaptionText**
Especifica o título que aparece no Expression Builder. O título pode ser usado para lembrar o usuário sobre o tipo de expressão a ser criada.
**TO MemVarName**
Especifica a variável ou o elemento de matriz em que a expressão é armazenada. Se a variável ainda não existir, o Visual FoxPro a cria. GETEXPR não cria um elemento de matriz. Se você sair do Expression Builder pressionando ESC ou escolhendo Cancel , a cadeia de caracteres vazia é armazenada na variável ou no elemento de matriz. Se uma expressão padrão for criada com a cláusula DEFAULT, a expressão padrão é armazenada na variável se você sair do Expression Builder pressionando ESC ou escolhendo Cancel .
**TYPE cExpressionType [ ; cErrorMessageText ]**
Especifica o tipo da expressão. A tabela a seguir lista o caractere a especificar em cExpressionType para cada tipo de expressão: cExpressionType Tipo de expressão C Character D Date T DateTime N Numeric F Float I Integer B Double Y Currency L Logical Você pode especificar a mensagem de erro cErrorMessageText a ser exibida se a expressão não for válida. Se cErrorMessageText for incluído com cExpressionType , cExpressionType e cErrorMessageText devem ser separados por ponto e vírgula (;). A combinação de cExpressionType , o ponto e vírgula e cErrorMessageText deve estar entre aspas simples ou duplas em pares correspondentes.
**DEFAULT cDefaultExpression**
Permite exibir a expressão padrão inicial no Expression Builder. Você pode aceitar a expressão padrão ou substituí-la pela sua própria expressão especificada com cDefaultExpression . cDefaultExpression é armazenado na variável ou no elemento de matriz se você sair do Expression Builder pressionando ESC ou escolhendo Cancel .

# Exemplo

No exemplo a seguir, GETEXPR é usado para obter uma expressão LOCATE do tipo adequado. Se LOCATE for bem-sucedido, o nome da empresa é exibido; caso contrário, uma mensagem é exibida.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE customer  && Opens Customer table
GETEXPR 'Enter condition to locate ' TO gcTemp;
   TYPE 'L' DEFAULT 'COMPANY = ""'
LOCATE FOR &gcTemp
IF FOUND()
   DISPLAY
ELSE
   ? 'Condition ' + gcTemp + ' was not found '
ENDIF
```
