# Comando @ ... GET - Check Boxes

Incluído para compatibilidade com versões anteriores. Use o CheckBox Control em vez disso.

Cria uma caixa de seleção ou uma caixa de seleção com imagem.

```foxpro
@ row, column
GET memvar | field
FUNCTION expC1 | PICTURE expC2
	[FONT expC3 [, expN1]]
	[STYLE expC4]
	[DEFAULT expr]
	[SIZE expN2, expN3]
	[ENABLE | DISABLE]
	[MESSAGE expC5]
	[VALID expL1 | expN4]
	[WHEN expL2]
	[COLOR SCHEME expN5
	| COLOR color pair list]
```

#### Parâmetros
 row, column

 row e column são expressões numéricas com valores 0 ou maiores que determinam onde a caixa de seleção aparece.

 A primeira linha é o número 0 na janela principal do FoxPro ou em uma janela definida pelo usuário. As linhas são numeradas de cima para baixo. No FoxPro for Windows, a linha 0 é a linha imediatamente abaixo da barra de menu do sistema FoxPro. No FoxPro for Macintosh, a linha 0 é a linha imediatamente abaixo da barra de título do FoxPro. No FoxPro for MS-DOS, a linha 0 é a linha que a barra de menu do sistema FoxPro ocupa. Consulte SET SYSMENU para informações sobre manipular a barra de menu do sistema para colocar saída na linha 0 no FoxPro for MS-DOS.

 A primeira coluna é o número 0 na janela principal do FoxPro ou em uma janela definida pelo usuário. As colunas são numeradas da esquerda para a direita.

 Quando a caixa de seleção é direcionada a uma janela definida pelo usuário, as coordenadas de linha e coluna são relativas à janela definida pelo usuário, não à janela principal do FoxPro.

 No FoxPro for Windows e FoxPro for Macintosh, uma posição na janela principal do FoxPro ou em uma janela definida pelo usuário é determinada pela fonte da janela principal do FoxPro ou da janela definida pelo usuário. A maioria das fontes pode ser exibida em uma ampla variedade de tamanhos, e algumas são proporcionalmente espaçadas. Uma linha corresponde à altura da fonte atual; uma coluna corresponde à largura média de uma letra na fonte atual.

 No FoxPro for Windows e FoxPro for Macintosh, você pode posicionar a caixa de seleção em uma janela com frações decimais para coordenadas de linha e coluna. No FoxPro for MS-DOS, frações decimais usadas para coordenadas de linha e coluna são arredondadas para o valor inteiro mais próximo.

 memvar | field

 Quando você marca ou desmarca uma caixa de seleção, sua escolha é armazenada em uma variável de memória, um elemento de array ou um campo, que você especifica com memvar ou field. O memvar ou field deve ser de tipo numérico ou lógico.

 Quando uma caixa de seleção é exibida inicialmente na tela ou em uma janela, a caixa está marcada se memvar ou field contém um valor numérico diferente de zero ou um valor true (.T.). A caixa não está marcada se memvar ou field é zero ou false (.F.).

 READ ou READ CYCLE ativa a caixa de seleção. O estado da caixa de seleção quando o READ é encerrado determina o valor armazenado na variável de memória, elemento de array ou field — 1 ou .T. se marcada e 0 ou .F. se desmarcada.

 FUNCTION expC1 | PICTURE expC2

 Ao criar uma caixa de seleção, você deve incluir a cláusula FUNCTION, a cláusula PICTURE ou ambas. Não há vantagem para nenhum dos três métodos. A cláusula FUNCTION ou a cláusula PICTURE contém o código de especificação de caixa de seleção *C.

 A expressão de caracteres expC1 da cláusula FUNCTION deve começar com *C. Para criar o prompt, inclua um espaço após *C seguido do texto do prompt. Por exemplo, esta cláusula cria uma caixa de seleção com o prompt Titles:

 ... FUNCTION '*C Titles' ...

 A expressão de caracteres expC2 da cláusula PICTURE usa a mesma sintaxe da expressão de caracteres da cláusula FUNCTION, exceto que a expressão da cláusula PICTURE deve começar com @ seguido de *C. Por exemplo, esta cláusula cria uma caixa de seleção com o prompt Titles:

 ... PICTURE '@*C Titles' ...

 Você também pode incluir as cláusulas FUNCTION e PICTURE para criar uma caixa de seleção. Se ambas são incluídas, a expressão de caracteres expC1 da FUNCTION deve conter *C para criar a caixa de seleção. A expressão de caracteres expC2 da PICTURE deve incluir o prompt. Por exemplo:

 ... FUNCTION '*C' PICTURE 'Titles' ...

 Os exemplos a seguir ilustram as várias formas de sintaxe que você pode usar para criar uma caixa de seleção. Em todos os exemplos, a caixa de seleção é colocada na segunda linha e coluna. O estado da caixa (marcada ou desmarcada) é armazenado na variável de memória MCHOICE. Cada exemplo cria a mesma caixa de seleção.

 Somente cláusula FUNCTION:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '*C Titles'

 READ

 STORE 1 TO mchoice

 STORE '*C Titles' TO mprompt

 @ 2,2 GET mchoice FUNCTION mprompt

 READ

 Somente cláusula PICTURE:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice PICTURE '@*C Titles'

 READ

 STORE 1 TO mchoice

 @ 2,2 GET mchoice PICTURE '@*C' + ' Titles'

 READ

 Cláusulas FUNCTION e PICTURE:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '*C' PICTURE ' Titles'

 READ

 Caixas de Seleção com Imagem

 No FoxPro for Windows e FoxPro for Macintosh, o prompt para uma caixa de seleção também pode ser o nome de um arquivo de imagem. No FoxPro for Windows, o arquivo de imagem pode ser um arquivo bitmap BMP. No FoxPro for Macintosh, você pode usar um arquivo de imagem do tipo PICT ou um arquivo bitmap BMP.

 Quando uma caixa de seleção usa um arquivo de imagem como prompt, a caixa de seleção imita o comportamento de uma caixa de seleção com prompt de texto. Por exemplo, o arquivo de imagem é exibido, mas a caixa de seleção não é exibida. Como marcar uma caixa de seleção, escolher a imagem alterna o valor de memvar ou field entre .T. e .F. ou 1 e 0.

 Para usar um arquivo de imagem em uma caixa de seleção, adicione B ao código de especificação de caixa de seleção. Os códigos de especificação das cláusulas FUNCTION e PICTURE que criam uma caixa de seleção são *C ou @*C, respectivamente. Para criar uma caixa de seleção com prompts de imagem, use os códigos *CB e @*CB, seguidos de um espaço e do nome do arquivo de imagem. Se o arquivo de imagem não estiver localizado no diretório ou pasta padrão, inclua o caminho para o arquivo de imagem com o nome do arquivo de imagem.

 -------------------------------

 Observação As imagens não são recortadas, reduzidas ou ampliadas para caber no botão da caixa de seleção. Use a cláusula SIZE para ajustar o tamanho do botão da caixa de seleção para acomodar a imagem.

 -------------------------------

 Se você omitir a extensão do arquivo de imagem, o FoxPro for Macintosh primeiro procura um arquivo de imagem com o nome que você especificou e extensão .BMP. Se um arquivo de imagem com extensão .BMP e o nome que você especificou não for encontrado, o FoxPro for Macintosh então procura um arquivo com o nome que você especificou e extensão .PCT. Se um arquivo de imagem com extensão .PCT e o nome que você especificou não for encontrado, o FoxPro for Macintosh então procura um arquivo de imagem com o nome que você especificou sem extensão.

 Máscaras de Imagem e Caixas de Seleção

 No FoxPro for Windows e FoxPro for Macintosh, uma caixa de seleção com imagem tem três estados: para cima, pressionada e desabilitada. O FoxPro controla automaticamente a aparência de uma caixa de seleção com imagem quando está em cada um desses três estados, mas você pode substituir a aparência padrão usando uma máscara de imagem.

 Uma máscara é usada para controlar as áreas transparentes de uma caixa de seleção com imagem. Por padrão, as áreas brancas são transparentes. Se uma máscara estiver presente, as áreas brancas da máscara, não do arquivo de imagem, são transparentes.

 Uma máscara é um arquivo de imagem monocromático. No FoxPro for Windows, uma máscara é um .BMP com extensão .MSK. No FoxPro for Macintosh, uma máscara pode ser um .BMP com extensão .MSK ou um arquivo do tipo PICT com extensão .PCM. A máscara deve ter o mesmo nome base que o arquivo de imagem e a extensão apropriada. O FoxPro procura automaticamente uma máscara para um arquivo de imagem no mesmo diretório ou pasta onde o arquivo de imagem está localizado.

 Na maioria dos casos, uma máscara não é necessária. Se você não precisa que nada em sua imagem apareça branco e seu arquivo de imagem tem fundo branco, a caixa de seleção com imagem aparecerá como desejado nos estados para cima, pressionada e desabilitada.

 Quando uma caixa de seleção com imagem tem uma máscara e está no estado para cima ou pressionada, quaisquer áreas brancas na imagem aparecem transparentes, permitindo que a cor da face do botão apareça. No entanto, você pode manter a cor branca de certas áreas.

 Suponha que você tenha uma imagem com um cachorro em fundo branco; o cachorro tem olhos brancos e a face do botão é vermelha. Você deseja que o fundo do botão apareça vermelho, mas deseja que os olhos do cachorro sejam brancos, não vermelhos. Faça uma máscara do mesmo tamanho que o arquivo de imagem, mas incluindo apenas duas cores, preto e branco. Deixe o fundo da máscara branco, mas torne o cachorro — incluindo seus olhos — completamente preto. Quando o botão é exibido, o fundo é vermelho para corresponder à face do botão, mas os olhos do cachorro são brancos.

 Quando uma caixa de seleção com imagem está desabilitada, quaisquer áreas brancas no arquivo de imagem aparecem transparentes para que a cor da face do botão apareça. Quaisquer áreas não brancas aparecem cinza escuro. Se o botão tem uma máscara, todas as áreas brancas na máscara são transparentes para que a cor da face do botão apareça, e todas as áreas pretas aparecem cinza escuro.

 Opções PICTURE e FUNCTION N, T, 2 e 3

 Opções adicionais podem ser combinadas com os códigos de especificação *C nas cláusulas FUNCTION ou PICTURE para modificar o comportamento (N e T) e a aparência (2 e 3) das caixas de seleção.

 Os códigos de especificação 2 (bidimensional) e 3 (tridimensional) estão disponíveis apenas no FoxPro for Macintosh.

 Opção Descrição

 ------ -----------

 N Não encerra o READ quando a caixa é escolhida. Este é o comportamento padrão.

 T Encerra o READ quando a caixa é escolhida.

 2 Cria uma caixa de seleção plana (bidimensional) idêntica às caixas de seleção nas caixas de diálogo do Macintosh. Este é o tipo padrão de caixa de seleção no FoxPro for Macintosh.

 3 Cria uma caixa de seleção tridimensional idêntica às caixas de seleção nas caixas de diálogo do FoxPro for Macintosh.

 Por exemplo, a cláusula a seguir cria uma caixa de seleção e não faz o READ encerrar quando a caixa de seleção é escolhida:

 ... FUNCTION '*CN ... '

 No FoxPro for Macintosh, a cláusula a seguir cria uma caixa de seleção tridimensional e não faz o READ encerrar quando a caixa de seleção é escolhida:

 ... FUNCTION '*CN3 ... '

 Caixas de Seleção com Recursos Especiais

 Você pode atribuir uma tecla de atalho à caixa de seleção ou desabilitar a caixa de seleção incluindo caracteres especiais ao definir o prompt.

 Teclas de Atalho

 Uma tecla de atalho permite escolher ou alterar imediatamente o estado da caixa de seleção. Para atribuir uma tecla de atalho, coloque uma barra invertida e um sinal de menor que (\<) antes do caractere desejado do prompt da caixa de seleção. A tecla de atalho é um caractere destacado (FoxPro for MS-DOS) ou sublinhado (FoxPro for Windows). No FoxPro for Macintosh, se KEYCOMP estiver definido como MAC (o padrão), a tecla de atalho não é destacada nem sublinhada; se KEYCOMP estiver definido como DOS ou WINDOWS a tecla de atalho é sublinhada.

 -------------------------------

 Observação - Uma tecla de atalho não escolhe a caixa de seleção se o objeto atual é um campo de entrada @ ... GET, uma região de edição de texto, um popup ou uma lista.

 -------------------------------

 Se o objeto atual é um campo de entrada @ ...GET ou uma região de edição de texto, pressionar a tecla de atalho insere a letra correspondente no campo ou na região de edição de texto. Se o objeto atual é um popup ou uma lista rolável, pressionar a tecla de atalho seleciona a primeira opção no popup ou lista cujo prompt começa com a letra correspondente à tecla de atalho.

 -------------------------------

 Observação - No FoxPro for Windows, se o objeto atual é um campo de entrada @ ... GET, região de edição de texto, popup ou lista e KEYCOMP estiver definido como WINDOWS, você pode pressionar Alt e a tecla de atalho para mover para a caixa de seleção e escolhê-la. Se você criar uma caixa de seleção com imagem, não pode criar uma tecla de atalho para a caixa de seleção com imagem.

 -------------------------------

 O exemplo a seguir cria uma caixa de seleção com o prompt Titles e atribui a tecla de atalho T a ela:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '*C' PICTURE ' \<Titles'

 READ

 Caixas de Seleção Desabilitadas

 Uma caixa de seleção desabilitada não pode ser selecionada ou escolhida e é exibida em cores desabilitadas. Para desabilitar uma caixa de seleção, coloque duas barras invertidas (\\) antes do prompt da caixa de seleção ou use a cláusula DISABLE. O exemplo a seguir desabilita a caixa de seleção criada anteriormente:

 STORE 1 TO mchoice1, mchoice2, mchoice3

 @ 2,2 GET mchoice1 FUNCTION '*C \\Titles'

 @ 4,2 GET mchoice2 FUNCTION '*C Titles' DISABLE

 @ 6,2 GET mchoice3 FUNCTION '*C Titles'

 READ

 FONT expC3 [, expN1]

 Inclua FONT para especificar uma fonte e tamanho de fonte para o prompt da caixa de seleção. A expressão de caracteres expC3 é o nome da fonte, e a expressão numérica expN1 é o tamanho da fonte. Por exemplo, o comando a seguir exibe o prompt em fonte Courier de 16 pontos:

 @ 2,2 GET mchoice FUNCTION '*C Titles' DEFAULT 1 ;

 FONT 'Courier',16

 Se você incluir a cláusula FONT mas omitir o tamanho da fonte expN1, uma fonte de 10 pontos é usada.

 No FoxPro for Windows, se a fonte que você especificar não estiver disponível, uma fonte com características semelhantes é substituída.

 No FoxPro for Macintosh, se a fonte que você especificar não estiver disponível, a fonte Chicago é usada.

 No FoxPro for MS-DOS, a cláusula FONT é ignorada.

 Se a cláusula FONT for omitida e a caixa de seleção for colocada na janela principal do FoxPro, a fonte da janela principal do FoxPro é usada. Se a cláusula FONT for omitida e a caixa de seleção for colocada em uma janela definida pelo usuário, a fonte da janela definida pelo usuário é usada.

 STYLE expC5

 No FoxPro for Windows e FoxPro for Macintosh, inclua a cláusula STYLE para especificar um estilo de fonte para uma caixa de seleção.

 O estilo de fonte é especificado com expC5.

 No FoxPro for Windows, se o estilo de fonte que você especificar não estiver disponível, um estilo de fonte com características semelhantes é substituído.

 No FoxPro for Macintosh, se a fonte que você especificar não estiver disponível, o estilo de fonte normal é usado.

 A cláusula STYLE é ignorada no FoxPro for MS-DOS.

 Caractere Estilo de Fonte

 --------- ----------

 B Bold

 C Condense*

 E Extend*

 I Italic

 N Normal

 O Outline

 Q Opaque

 S Shadow

 - Strikeout*

 T Transparent

 U Underline

 * Os estilos Condense e Extend estão disponíveis apenas no FoxPro for Macintosh. O estilo Strikeout está disponível apenas no FoxPro for Windows.

 Você pode incluir mais de um caractere para especificar uma combinação de estilos de fonte. Por exemplo, a cláusula a seguir especifica Bold Italic:

 STYLE 'BI'

 Se T for incluído para criar uma caixa de seleção transparente, a caixa de seleção é preenchida com a cor de fundo. Se Q for incluído, a caixa de seleção e o prompt da caixa de seleção são preenchidos com a cor de fundo.

 DEFAULT expr

 Quando você marca ou desmarca uma caixa de seleção, o estado da caixa é salvo em uma variável de memória, um elemento de array ou um campo. Se você especificar uma variável de memória que não existe, ela é criada automaticamente e inicializada se a cláusula DEFAULT for incluída. No entanto, um elemento de array não é criado se você especificar um elemento de array em uma cláusula DEFAULT. A cláusula DEFAULT é ignorada se a variável de memória já existir ou você especificar um campo.

 -------------------------------

 Observação - Se a cláusula DEFAULT for omitida e a variável de memória memvar não existir, a mensagem de erro "Variable not found" aparece.

 -------------------------------

 A expressão DEFAULT expr determina o tipo de variável de memória criada e seu valor inicial. Deve ser uma expressão numérica ou lógica. Aqui estão exemplos de cláusulas DEFAULT para caixas de seleção:

 @ 2,2 GET mchoice FUNCTION '*C Titles' DEFAULT .T.

 READ

 STORE .T. TO button

 @ 2,2 GET mchoice FUNCTION '*C Titles' DEFAULT button

 READ

 SIZE expN2, expN3

 A expressão numérica expN2 especifica a altura de uma caixa de seleção. Para caixas de seleção no FoxPro for MS-DOS, esta expressão é ignorada porque uma caixa de seleção tem sempre uma linha de altura. No entanto, você deve incluir expN2 se incluir expN3 para especificar a largura do prompt.

 No FoxPro for Windows e FoxPro for Macintosh, você pode especificar uma altura para a caixa de seleção. Se expN2 for 1, o retângulo de foco ao redor do prompt da caixa de seleção será recortado. Neste caso, inclua um valor maior para expN2.

 Por padrão, a largura de uma caixa de seleção é determinada pelo comprimento do texto do prompt. Você pode usar expN3 para tornar o prompt da caixa de seleção mais largo que o padrão. A expressão numérica expN3 especifica a largura (em colunas) de uma caixa de seleção.

 No FoxPro for Windows e FoxPro for Macintosh, a fonte da caixa de seleção determina o tamanho da caixa de seleção. A fonte da caixa de seleção é especificada com a cláusula FONT. Se a cláusula FONT for omitida, a caixa de seleção usa a fonte de sua janela pai (a janela principal do FoxPro ou uma janela definida pelo usuário).

 ENABLE | DISABLE

 Por padrão, uma caixa de seleção é habilitada quando READ é emitido. Você pode impedir que uma caixa de seleção seja ativada quando READ é emitido incluindo DISABLE. Uma caixa de seleção desabilitada não pode ser selecionada e é exibida em cores desabilitadas. Use SHOW GET ENABLE para habilitar uma caixa de seleção desabilitada.

 MESSAGE expC5

 A expressão de caracteres expC5 da cláusula MESSAGE aparece quando uma caixa de seleção é selecionada. A mensagem é centralizada por padrão na última linha da janela principal do FoxPro; o local da mensagem pode ser especificado com SET MESSAGE.

 No FoxPro for Windows e FoxPro for Macintosh, a mensagem é colocada na barra de status gráfica. Se a barra de status gráfica foi desativada com SET STATUS BAR OFF, a mensagem é centralizada na última linha da janela principal do FoxPro.

 VALID expL1 | expN4

 Você pode incluir uma expressão VALID opcional expL1 ou expN4 que é avaliada quando uma caixa de seleção é escolhida (marcada ou desmarcada). Ou seja, VALID não é avaliada quando você seleciona (move para) a caixa de seleção, mas quando você realmente escolhe a caixa de seleção.

 Tipicamente, expL1 ou expN4 é uma função definida pelo usuário. Com funções definidas pelo usuário você pode selecionar, habilitar ou desabilitar outros objetos, abrir uma janela Browse, abrir outra tela de entrada de dados ou mover para um novo registro. CLEAR READ pode ser incluído em uma função definida pelo usuário para encerrar o READ.

 expL1

 Quando um valor lógico expL1 é retornado à cláusula VALID, o valor lógico é ignorado e a caixa de seleção permanece o controle ativo. No entanto, você pode especificar uma função definida pelo usuário (UDF) que retorna um valor lógico à cláusula VALID e ativa outro objeto.

 O exemplo a seguir demonstra como uma UDF da cláusula VALID é executada quando uma caixa de seleção é escolhida. A caixa de seleção permanece o controle atual quando a UDF da cláusula VALID é executada porque um false lógico (.F.) é retornado pela UDF.

 CLEAR

 STORE 1 TO mchoice1, mchoice2, mchoice3

 @ 2,2 GET mchoice2

 @ 4,2 GET mchoice1 FUNCTION '*C \<Titles' ;

 VALID showmes() ;

 MESSAGE 'Execute the VALID. ' + ;

 'Select this check box using Spacebar.'

 @ 6,2 GET mchoice3

 READ CYCLE && Press Esc to exit the READ

 FUNCTION showmes

 WAIT WINDOW NOWAIT 'The VALID clause was executed.'

 RETURN .F.

 expN4

 Uma cláusula VALID que inclui uma expressão numérica expN4 é usada para especificar qual objeto é ativado após uma caixa de seleção ser escolhida. Objetos são campos de entrada @ ... GET, caixas de seleção, listas, popups, spinners, regiões de edição de texto e cada botão individual em um conjunto de botões push, radio e invisíveis.

 A expressão numérica tem um de três efeitos:

  Quando expN4 é 0, a caixa de seleção permanece o controle ativo.

  Quando expN4 é positivo, expN4 especifica o número de objetos a avançar. Por exemplo, quando a caixa de seleção é selecionada e VALID retorna 1, o próximo objeto é ativado. Se expN4 for maior que o número de objetos restantes, o READ é encerrado (a menos que READ CYCLE seja emitido para ativar os objetos).

  Quando expN4 é negativo, expN4 especifica o número de objetos a retroceder. Por exemplo, quando a caixa de seleção é selecionada e VALID retorna -1, o objeto anterior é ativado. Se expN4 retroceder além do primeiro objeto, o READ é encerrado (a menos que READ CYCLE seja emitido para ativar os objetos).

 O exemplo a seguir demonstra como uma UDF da cláusula VALID pode ativar outro objeto retornando um valor numérico. Quando a UDF da cláusula VALID é executada, a UDF retorna 2. O segundo objeto após a caixa de seleção é ativado. Como READ CYCLE foi emitido, o READ não é encerrado mesmo que restem menos de dois objetos.

 CLEAR

 STORE 1 TO mchoice1, mchoice2

 STORE 0 TO m.choice3

 @ 2,2 GET mchoice1

 @ 4,2 GET mchoice2

 @ 6,2 GET m.choice3 FUNCTION '*C \<Titles' ;

 VALID showmes() ;

 MESSAGE 'Execute the VALID. ' + ;

 'Select this check box using Spacebar.'

 READ CYCLE && Press Esc to exit the READ

 FUNCTION showmes

 WAIT WINDOW NOWAIT 'The VALID clause was executed.'

 RETURN 2

 WHEN expL2

 A cláusula WHEN opcional permite ou proíbe a seleção de uma caixa de seleção baseado no valor lógico de expL2, que deve avaliar para um true lógico (.T.) antes que uma caixa de seleção possa ser selecionada. Se expL2 avaliar para um false lógico (.F.), a caixa de seleção não pode ser selecionada e é ignorada se colocada entre outros objetos.

 No exemplo a seguir, a cláusula WHEN da caixa de seleção retorna um false lógico (.F.). A caixa de seleção é ignorada mesmo que não esteja desabilitada.

 CLEAR

 STORE 1 TO mchoice1, mchoice2

 STORE 0 TO mchoice3

 @ 2,2 GET mchoice1

 @ 4,2 GET mchoice2 FUNCTION '*C \<Titles' ;

 WHEN showmes()

 @ 6,2 GET mchoice3

 READ CYCLE && Press \ to exit the READ

 FUNCTION showmes

 WAIT WINDOW NOWAIT 'The WHEN clause was executed.'

 RETURN .F.

 COLOR SCHEME expN5 | COLOR color pair list

 Se você não incluir uma cláusula COLOR, as cores da caixa de seleção são determinadas pelo esquema de cores da janela principal do FoxPro; se uma caixa de seleção for colocada em uma janela definida pelo usuário, o esquema de cores da janela determina as cores da caixa de seleção.

 A cor de uma caixa de seleção pode ser especificada incluindo o número de um esquema de cores existente na cláusula COLOR SCHEME ou um conjunto de pares de cores na cláusula COLOR.

 Um esquema de cores é um conjunto de 10 pares de cores predefinidos. Os pares de cores em um esquema de cores podem ser alterados com SET COLOR OF SCHEME. No FoxPro for MS-DOS, os pares de cores em um esquema de cores também podem ser alterados no Color Picker.

 Um par de cores é um conjunto de duas letras separadas por uma barra. A primeira letra especifica a cor de primeiro plano e a segunda letra especifica a cor de fundo.

 Por exemplo, este par de cores especifica um primeiro plano vermelho em fundo branco:

 R/W

 Para uma lista de cores e suas letras de cor correspondentes, consulte SET COLOR Overview ou Color Table by Color Pair.

 Um par de cores também pode ser especificado com um conjunto de seis valores de cor RGB (Red Green Blue) separados por vírgulas. Os três primeiros valores de cor especificam a cor de primeiro plano e os três últimos valores de cor especificam a cor de fundo. Os valores de cor podem variar de 0 a 255.

 O par de cores R/W no exemplo acima também pode ser especificado com este par de cores RGB:

 RGB(255,0,0,255,255,255)

 Apenas os pares de cores 5, 6, 7, 9 e 10 em um esquema de cores ou lista de pares de cores afetam as cores da caixa de seleção. A cor de caixas de seleção com imagem é controlada pelo Windows

 Par de Cores Caixa de Seleção

 Número Atributo

 ---------- ---------

 5 Message

 6 Prompt de caixa de seleção selecionada - somente FoxPro for MS-DOS

 7 Teclas de atalho - somente FoxPro for MS-DOS

 9 Prompt de caixa de seleção habilitada

 10 Prompt de caixa de seleção desabilitada

 O exemplo a seguir mostra como substituir o esquema de cores da janela principal do FoxPro por outro esquema de cores predefinido:

 ACTIVATE SCREEN

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '*C Titles' COLOR SCHEME 4

 READ

 O exemplo a seguir cria caixas de seleção com o prompt Titles, a tecla de atalho T e as seguintes características de cor:

  Uma caixa selecionada é mostrada com prompt branco brilhante em fundo azul (W+/B).

  Caracteres de tecla de atalho são mostrados em vermelho em fundo azul (R/B) no FoxPro for MS-DOS. No FoxPro for Windows, o caractere da tecla de atalho é sublinhado.

  Uma caixa de seleção habilitada é mostrada com prompt amarelo em fundo azul (GR+/B).

  Uma caixa de seleção desabilitada é mostrada com prompt branco em fundo azul (W/B).

 Quando você pula um par de cores, deve incluir uma vírgula onde o par de cores é omitido.

 Aqui estão os comandos:

 CLEAR

 SET COLOR TO W/B

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '*C \<Titles' ;

 COLOR ,,,,,W+/B,R/B,,GR+/B,W/B

 @ 4,2 GET mchoice FUNCTION '*C \\Titles' ;

 COLOR ,,,,,W+/B,R/B,,GR+/B,W/B

 @ 6,2 GET mchoice FUNCTION '*C \<Titles' ;

 COLOR ,,,,,W+/B,R/B,,GR+/B,W/B

 READ

# Observações

Caixas de seleção com imagem são suportadas no FoxPro for Windows e FoxPro for Macintosh.

Com esta variação de @ ... GET, você pode criar uma caixa de seleção ou uma caixa de seleção com imagem. Uma caixa de seleção é usada para alternar entre dois estados, como true (.T.) e false (.F.) ou sim e não.

Se você usar o Screen Builder para criar suas telas de entrada de dados, pode não precisar usar este comando. O Screen Builder gera automaticamente os comandos que criam caixas de seleção e caixas de seleção com imagem.

Uma caixa de seleção é uma caixa com texto descritivo à sua direita. A cadeia de caracteres de texto, chamada prompt, indica o que a caixa de seleção controla. O texto do prompt é especificado pela cláusula FUNCTION ou PICTURE. Quando uma condição é true, um X é exibido. Apenas uma caixa de seleção pode ser criada em um único @ ... GET. Emita READ ou READ CYCLE para ativar uma caixa de seleção.

Você pode criar uma caixa de seleção com imagem no FoxPro for Windows e FoxPro for Macintosh. Uma imagem em um botão substitui a caixa de seleção e o prompt da caixa de seleção.

No FoxPro for MS-DOS, pressionar a barra de espaço ou Enter ou clicar na caixa de seleção alterna a caixa de seleção de um estado para o outro.

No FoxPro for Windows, pressionar a barra de espaço ou Enter ou clicar na caixa de seleção alterna a caixa de seleção de um estado para o outro se KEYCOMP estiver definido como DOS. Se KEYCOMP estiver definido como WINDOWS, que é o padrão do FoxPro for Windows, você pode alternar o estado da caixa de seleção pressionando a barra de espaço ou clicando na caixa de seleção. Pressione Enter para mover para o próximo objeto.

No FoxPro for Macintosh, clique na caixa de seleção para alternar a caixa de seleção de um estado para o outro. Se KEYCOMP estiver definido como DOS ou WINDOWS e a caixa de seleção tiver o foco, você pode pressionar a barra de espaço para alternar a caixa de seleção de um estado para o outro.
