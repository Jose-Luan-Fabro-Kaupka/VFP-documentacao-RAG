# Função ALINES( )

Copia cada linha em uma expressão de caracteres ou campo memo para uma linha correspondente em uma matriz.

```foxpro
ALINES(ArrayName, cExpression [, nFlags] [, cParseChar [, cParseChar2 [, ...]]])
```

#### Parâmetros
 **ArrayName**
Especifica o nome da matriz para armazenar as linhas copiadas na expressão de caracteres ou campo memo. Observação Se a matriz especificada não existir, o Visual FoxPro cria automaticamente a matriz. Se a matriz existir, mas não for grande o suficiente para conter todas as linhas no campo memo, o Visual FoxPro aumenta automaticamente o tamanho da matriz. Se a matriz for maior do que o necessário, o Visual FoxPro trunca a matriz. Observação Quando usada com valores binários, como Varbinary e Blob , ALINES( ) cria uma matriz com elementos do tipo Varbinary.
**cExpression**
Especifica a expressão de caracteres ou campo memo contendo as linhas a copiar para a matriz. Todas as expressões de caracteres diferenciam maiúsculas de minúsculas. Observação Se cExpression for a cadeia vazia ou o valor nulo, uma matriz com uma única linha é criada e a linha contém a cadeia vazia. Você pode usar expressões de dois bytes.
**[, nFlags ]**
Observação Em versões anteriores do Visual FoxPro, nFlags era a opção lTrim. A opção lTrim corresponde a um valor de 1 para nFlag . O código anterior será executado de forma idêntica no Visual FoxPro 9.0. A tabela a seguir descreve os valores para nFlags . Valor de bit (aditivo) Descrição 0 1 (Padrão) Remove espaços à esquerda e à direita das linhas, ou para valores Varbinary e Blob, remove zeros à direita (0) em vez de espaços. 1 2 Inclui o último elemento na matriz mesmo se o elemento estiver vazio. 2 4 Não inclui elementos vazios na matriz. 3 8 Especifica análise que não diferencia maiúsculas de minúsculas. 4 16 Inclui os caracteres de análise na matriz.
**[, cParseChar [, cParseChar2 [, ...]]]**
Especifica uma ou mais cadeias de caracteres que terminam os elementos em cExpression . Quando cParseChar é especificado, a linha é interrompida quando cParseChar é encontrado, e a próxima linha continua com o caractere seguinte a cParseChar . Observação O número máximo de cadeias permitidas em cParseChar é 23. Você pode usar um caractere de avanço de linha (CHR(10)) ou retorno de carro (CHR(13)) para indicar o fim de uma linha. Você também pode indicar o fim da linha com qualquer combinação desses dois caracteres, por exemplo, (CHR(10) + CHR(13) ou CHR(13) + CHR(10)). O comportamento padrão de ALINES( ) é ignorar CHR(13) e CHR(10) quando você especifica um ou mais valores para cParseChar , a menos que você também especifique os caracteres de fim de linha. Observação Quando cParseChar é omitido para entrada Varbinary ou Blob, ALINES( ) trata o valor hexadecimal 0hA (10) como retorno de carro e descontinua a linha nesse local. O valor 0hA não é salvo no elemento da matriz resultante e pode resultar em um valor binário incorreto. Por exemplo, dado o valor binário 0hFE0AF2, ALINES( ) cria uma matriz de dois elementos com os valores 0hFE e 0hF2.

# Valor de retorno

Numérico. ALINES( ) retorna o número de linhas na matriz, ou, de forma idêntica, o número de linhas na expressão de caracteres ou campo memo.

# Observações

ALINES( ) oferece uma maneira fácil de analisar linhas em uma expressão de caracteres ou campo memo. Embora você também possa usar MLINES( ) para analisar uma expressão de caracteres ou campo memo, ALINES( ) é mais rápido e requer menos programação. Além disso, ALINES( ) não é afetado pelo valor de SET MEMOWIDTH.

A primeira linha da expressão de caracteres ou campo memo é copiada para a primeira linha da matriz, a segunda linha da expressão de caracteres ou campo memo é copiada para a segunda linha da matriz, e assim por diante.

Você deve ter memória suficiente para copiar as linhas em um campo memo grande para uma matriz. O Visual FoxPro gera uma mensagem de erro se você não tiver memória suficiente.

Se você deseja realizar uma análise que não diferencia maiúsculas de minúsculas, pode seguir um dos exemplos a seguir:

```foxpro
? ALINES(aMyArray, UPPER(employee.notes), "R.")
```

- OU -

```foxpro
? ALINES(aMyArray, employee.notes, "R.", "r.")
```

# Exemplo

O exemplo a seguir abre a tabela Employee no banco de dados de amostra Testdata.dbc. ALINES( ) é usada para copiar as linhas no campo memo Notes para uma matriz chamada aMyArray, e depois o conteúdo da matriz é exibido. Vários caracteres de análise são especificados em cada uma das instruções ALINES( ).

```foxpro
CLOSE DATABASES
CLEAR
SET TALK OFF
OPEN DATABASE (HOME(2) + "data\testdata")
USE employee  && Open Employee table
? ALINES(aMyArray, employee.notes)            && Displays 1
? ALINES(aMyArray, employee.notes, CHR(13))   && Displays 1
? ALINES(aMyArray, employee.notes, " ")       && Displays 75
? ALINES(aMyArray, employee.notes, ".")       && Displays 7
? ALINES(aMyArray, employee.notes, ",")       && Displays 4
? ALINES(aMyArray, employee.notes, ".", ",")  && Displays 10
? ALINES(aMyArray, employee.notes, 8, "m")    && Displays 14
? ALINES(aMyArray, employee.notes, "m")       && Displays 11
? ALINES(aMyArray, employee.notes, "M")       && Displays 4
```
