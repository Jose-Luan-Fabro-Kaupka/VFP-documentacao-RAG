# Processando vários conjuntos de resultados

Seu aplicativo recupera vários conjuntos de resultados quando você usa a função SQLEXEC( ) para emitir mais de uma instrução SQL SELECT ou para executar um procedimento armazenado que emite várias instruções SELECT. Os resultados de cada instrução SQL SELECT são retornados em um cursor Visual FoxPro separado.

O nome padrão SQLRESULT é usado para o primeiro cursor; cursores subsequentes recebem nomes exclusivos indexando o nome padrão. Por exemplo, os nomes padrão para os cursores retornados por uma instrução SQLEXEC( ) que solicita três conjuntos de resultados são Sqlresult, Sqlresult1 e Sqlresult2.

No modo batch, se uma função retorna vários conjuntos de resultados, os respectivos nomes de cursor no Visual FoxPro têm sufixos exclusivos e podem ter até 255 caracteres. Por exemplo, o exemplo a seguir define a propriedade BatchMode para o modo batch e, em seguida, emite uma instrução SQLEXEC( ) contendo quatro instruções SQL SELECT que construem quatro conjuntos de resultados:

```foxpro
? SQLSETPROP(nConnectionHandle,'BatchMode', .T.)
? SQLEXEC(nConnectionHandle,'select * from authors ;
                     select * from titles ;
                     select * from roysched ;
                     select * from titleauthor','ITEM')
```

Quando a função acima termina o processamento, o Visual FoxPro retorna os quatro conjuntos de resultados como os cursores Visual FoxPro Item, Item1, Item2 e Item3.

Você pode alterar o nome padrão usando o parâmetro cCursorname com as funções SQLEXEC( ) ou SQLMORERESULTS( ). Se o nome que você especificar para um conjunto de resultados já foi usado, o novo conjunto de resultados substitui o cursor existente.

Quando seu aplicativo recupera vários conjuntos de resultados, você pode escolher entre processamento assíncrono ou síncrono e modos batch ou não batch.

# Usando processamento em modo batch

A propriedade BatchMode, definida com a função SQLSETPROP( ), controla como a função SQLEXEC( ) retorna vários conjuntos de resultados. O valor padrão é .T., para modo batch. O processamento em modo batch significa que o Visual FoxPro não retorna nenhum resultado de uma chamada SQLEXEC( ) ainda em execução até que todos os conjuntos de resultados individuais tenham sido recuperados.

# Usando processamento em modo não batch

Se você usar a função SQLSETPROP( ) para definir a propriedade BatchMode como .F., para modo não batch, cada conjunto de resultados é retornado individualmente. O primeiro conjunto de resultados é retornado pela chamada da função SQLEXEC( ). Seu aplicativo deve então chamar a função SQLMORERESULTS( ) repetidamente até que um valor de 2 seja retornado, indicando que não há mais resultados disponíveis.

No modo não batch, o nome do cursor pode ser alterado em cada chamada subsequente de SQLMORERESULTS( ). No exemplo anterior, se o primeiro nome de cursor em uma sequência SQLEXEC( ) for Item, e a segunda chamada SQLMORERESULTS( ) alterar o parâmetro cCursorName para Otheritem, os cursores resultantes serão nomeados Item, Item1, Otheritem e Otheritem1.

A próxima seção descreve o processamento em modo batch e não batch com detalhes síncronos e assíncronos adicionados. O diagrama a seguir fornece uma representação das quatro combinações de processamento possíveis. Os números 0, 1 e 2 representam os valores retornados quando você chama cada função.
 Modos de processamento síncrono e assíncrono do Visual FoxPro

O comportamento de cada tipo de processamento é explicado abaixo: os rótulos A, B, C e D referenciam o diagrama anterior. Cada explicação assume a execução de uma instrução que retornará três conjuntos de resultados, representados no diagrama por três faixas horizontais.

# Usando processamento síncrono

No modo síncrono, o controle não retorna ao seu aplicativo até que a execução de uma função seja concluída.

# A: Modo batch síncrono

Quando você executa uma instrução SQL pass-through de forma síncrona em modo batch, o controle não é retornado até que todos os conjuntos de resultados tenham sido recuperados. Você especifica o nome do primeiro cursor usando o parâmetro cCursorname na função original. Se o cursor que você especificar já existir, o conjunto de resultados substitui o cursor existente. Quando você solicita vários conjuntos de resultados em modo batch síncrono, o Visual FoxPro cria os nomes de cursores adicionais indexando exclusivamente o nome do primeiro cursor.

# B: Modo não batch síncrono

Quando você executa uma instrução SQL pass-through de forma síncrona em modo não batch, a primeira instrução recupera o primeiro conjunto de resultados e retorna 1. Você deve então chamar a função SQLMORERESULTS( ) repetidamente e, opcionalmente, especificar um novo nome para o cursor. Se você não especificar um novo nome para o cursor, vários nomes para vários conjuntos de resultados são criados indexando exclusivamente o nome base. Quando SQLMORERESULTS( ) retorna um valor de 2, não há mais resultados disponíveis.

# Usando processamento assíncrono

No modo assíncrono, seu aplicativo deve continuar chamando a mesma função SQL pass-through até que ela retorne um valor diferente de 0 (ainda em execução). O nome padrão do conjunto de resultados, `Sqlresult`, pode ser alterado explicitamente com o parâmetro cCursorname na primeira vez que você chamar a função. Se o nome que você especificar para um conjunto de resultados já foi usado, o novo conjunto de resultados substitui as informações no cursor existente.

# C: Modo batch assíncrono

Quando você executa de forma assíncrona em modo batch, cada chamada repetida da função original retorna 0 (ainda em execução) até que todos os vários conjuntos de resultados tenham sido retornados aos cursores especificados. Quando todos os resultados foram recuperados, o valor de retorno é o número de cursores ou um número negativo indicando um erro.

# D: Modo não batch assíncrono

Ao processar de forma assíncrona em modo não batch, a função SQLEXEC( ) retorna um valor de 1 quando conclui a recuperação de cada conjunto de resultados. Seu aplicativo deve então chamar a função SQLMORERESULTS( ) repetidamente até que um valor de 2 seja retornado, indicando que não há mais resultados disponíveis.

> **Dica:** Conjuntos de resultados remotos são recuperados em duas etapas: primeiro, o conjunto de resultados é preparado no servidor; depois o conjunto de resultados é buscado em um cursor Visual FoxPro local. No modo assíncrono, você pode chamar a função USED( ) para ver se o Visual FoxPro começou a buscar o cursor que você solicitou.
