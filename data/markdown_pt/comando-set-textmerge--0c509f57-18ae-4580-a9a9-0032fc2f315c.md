# Comando SET TEXTMERGE

Ativa ou desativa a avaliação de campos, variáveis, elementos de matriz, funções ou expressões delimitados por marcadores de mesclagem de texto e permite especificar a saída dessa mesclagem.

```foxpro
SET TEXTMERGE [ON | OFF] [TO [FileName] MEMVAR VarName [ADDITIVE]]
   [WINDOW WindowName] [SHOW | NOSHOW]
```

#### Parâmetros
**ON**
Especifica que quaisquer campos, variáveis, elementos de matriz, funções ou expressões entre delimitadores de mesclagem de texto sejam avaliados e enviados para a saída quando colocados depois de \ ou \\, ou entre TEXT e ENDTEXT. O exemplo curto a seguir demonstra como o conteúdo da variável gcTodayDate e das funções DATE( ) e TIME( ) é avaliado quando SET TEXTMERGE está ON. gcTodayDate, DATE( ) e TIME( ) são avaliados porque estão entre delimitadores de mesclagem de texto e SET TEXTMERGE está ON. CLEAR SET TALK OFF STORE 'Today is: ' TO gcTodayDate SET TEXTMERGE ON \<<gcTodayDate>> \\<<DATE( )>> \The time is: \\ <<TIME( )>> Esta é a saída do programa acima quando executado em 1º de janeiro: Today is: 01/01/98 The time is: 10:55:19
**OFF**
(Padrão) Especifica que quaisquer campos, variáveis, elementos de matriz, funções ou expressões sejam enviados literalmente para a saída com os delimitadores de mesclagem de texto que os envolvem. Observe a diferença na saída quando SET TEXTMERGE está OFF no exemplo anterior: CLEAR SET TALK OFF STORE 'Today is: ' TO gcTodayDate SET TEXTMERGE OFF \<<gcTodayDate>> \\<<DATE( )>> \The time is: \\ <<TIME( )>> Esta é a saída desse programa: <<gcTodayDate>><<DATE( )>> The time is: <<TIME( )>>
**TO [ FileName ]**
Especifica que a saída de \, \\ e TEXT ... ENDTEXT seja direcionada para um arquivo de texto, além da janela principal do Visual FoxPro, que é o padrão. Você também pode direcionar a saída para um arquivo de texto incluindo FileName. Se não existir um arquivo com esse nome, um novo será criado. Se já existir um arquivo com o mesmo nome e SET SAFETY estiver ON, você poderá optar por substituir o arquivo existente. O arquivo de texto é aberto como arquivo de baixo nível e seu identificador é armazenado na variável de sistema _TEXT. Você pode fechar o arquivo emitindo SET TEXTMERGE TO sem argumentos adicionais. Se o identificador de outro arquivo tiver sido armazenado anteriormente em _TEXT, esse arquivo será fechado.
**MEMVAR VarName**
Especifica uma variável para conter os dados da saída de TEXTMERGE. Como SET TEXTMERGE é uma configuração global e pode abranger vários procedimentos ou métodos, MEMVAR VarName pode perder o escopo. O comando funcionará mesmo quando a variável estiver fora do escopo, mas não retornará conteúdo. Você pode controlar o escopo de MEMVAR VarName declarando a variável como PUBLIC ou PRIVATE. Essa cláusula também pode criar um comportamento recursivo, que pode ser controlado com o comando SET TEXTMERGE TO, como no exemplo a seguir: USE LABELS STORE "" to myVar, myVar2 SET TEXT ON NOSHOW SET TEXTMERGE TO MEMVAR myVar && TEXTMERGE begins on the next line. \Hey Now \<<date()>> SCAN \ <<name>> ENDSCAN * Remove comments from SET TEXTMERGE TO line to eliminate recursive * error with myVar and myVar2. * SET TEXTMERGE TO TEXT TO myVar2 Here's some HTML. This is HTML <<date()>> ENDTEXT SET TEXTMERGE OFF USE CLEAR ? myVar && But has also stored the TEXTMERGE contents to variables ? myVar2
**ADDITIVE**
Especifica que a saída de \, \\ e TEXT ... ENDTEXT seja acrescentada a um arquivo ou variável de memória existente. Para obter mais informações sobre como direcionar a saída da mesclagem de texto para um arquivo, consulte Variável de sistema _TEXT.
**WINDOW WindowName**
Especifica que a saída de \, \\ e TEXT ... ENDTEXT seja direcionada para uma janela definida pelo usuário, em vez da janela principal do Visual FoxPro, que é o padrão. WindowName especifica o nome da janela para a qual a saída será direcionada. A janela deve ser criada com DEFINE WINDOW antes que a saída possa ser enviada a ela. A janela não precisa estar ativa nem visível.
**SHOW | NOSHOW**
(Padrão) SHOW exibe a saída da mesclagem de texto. NOSHOW suprime sua exibição. Por padrão, a saída gerada por \, \\ e TEXT ... ENDTEXT é enviada para a janela principal do Visual FoxPro ou para uma janela ativa definida pelo usuário.

# Observações

Os comandos \, \\ e TEXT ... ENDTEXT são usados para mesclar texto com o conteúdo de tabelas, variáveis, elementos de matriz e os resultados de funções e expressões. Se um campo, variável, elemento de matriz, função ou expressão estiver entre delimitadores de mesclagem de texto (por padrão, << e >>), ele poderá ser avaliado e mesclado ao texto. Esse recurso permite produzir cartas, programas e modelos que criam programas.

SET TEXTMERGE determina como são avaliados os campos, variáveis, elementos de matriz, funções ou expressões entre delimitadores de mesclagem de texto. Também permite direcionar a saída da mesclagem para a janela principal do Visual FoxPro, uma janela definida pelo usuário ou um arquivo.

Campos memo podem ser usados para aninhar texto mesclado. Se um campo memo contiver nomes de campos, variáveis, elementos de matriz, funções ou expressões entre os delimitadores atuais, eles serão avaliados e enviados para a saída com o conteúdo do campo memo. O nome do campo memo também deve estar entre delimitadores de mesclagem de texto.
