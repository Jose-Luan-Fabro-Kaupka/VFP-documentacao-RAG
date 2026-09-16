# Comando @ ... GET - Botões de opção

Incluído para compatibilidade com versões anteriores. Use o OptionGroup Control em vez disso.

Cria um conjunto de botões de opção ou botões de opção com imagem.

```foxpro
@ row, column
GET memvar | field
FUNCTION expC1 | PICTURE expC2
	[FONT expC3 [, expN1]]
	[STYLE expC4]
	[DEFAULT expr]
	[SIZE expN2, expN3
		[, expN4]]
	[ENABLE | DISABLE]
	[MESSAGE expC5]
	[VALID expL1 | expN5]
	[WHEN expL2]
	[COLOR SCHEME expN6
	| COLOR color pair list]
```

#### Parâmetros
 row, column

 row e column são expressões numéricas com valores 0 ou maiores que determinam onde o primeiro botão em um conjunto de botões de opção aparece.

 A primeira linha é o número 0 na janela principal do FoxPro ou em uma janela definida pelo usuário. As linhas são numeradas de cima para baixo. No FoxPro for Windows, a linha 0 é a linha imediatamente abaixo da barra de menu do sistema FoxPro. No FoxPro for Macintosh, a linha 0 é a linha imediatamente abaixo da barra de título do FoxPro. No FoxPro for MS-DOS, a linha 0 é a linha que a barra de menu do sistema FoxPro ocupa. Consulte SET SYSMENU para informações sobre manipular a barra de menu do sistema para colocar saída na linha 0 no FoxPro for MS-DOS.

 A primeira coluna é o número 0 na janela principal do FoxPro ou em uma janela definida pelo usuário. As colunas são numeradas da esquerda para a direita.

 Quando o primeiro botão em um conjunto de botões de opção é direcionado a uma janela definida pelo usuário, as coordenadas de linha e coluna são relativas à janela definida pelo usuário, não à janela principal do FoxPro.

 No FoxPro for Windows e FoxPro for Macintosh, uma posição na janela principal do FoxPro ou em uma janela definida pelo usuário é determinada pela fonte da janela principal do FoxPro ou da janela definida pelo usuário. A maioria das fontes pode ser exibida em uma ampla variedade de tamanhos, e algumas são proporcionalmente espaçadas. Uma linha corresponde à altura da fonte atual; uma coluna corresponde à largura média de uma letra na fonte atual.

 No FoxPro for Windows e FoxPro for Macintosh, você pode posicionar o primeiro botão em um conjunto de botões de opção em uma janela com frações decimais para coordenadas de linha e coluna. No FoxPro for MS-DOS, frações decimais usadas para coordenadas de linha e coluna são arredondadas para o valor inteiro mais próximo.

GET memvar | field

 Quando você escolhe um botão de opção, sua escolha é armazenada na variável de memória ou elemento de array memvar ou no campo field. memvar ou field deve ser de tipo numérico ou de caractere.

 Se memvar ou field for de tipo numérico, um número correspondente à sua escolha de botão de opção é armazenado na variável de memória, elemento de array ou campo especificado com memvar ou field. Por exemplo, se você criar três botões de opção e escolher o segundo botão, 2 é armazenado. Se memvar ou field for de tipo caractere, o prompt do botão de opção que você escolher é armazenado na variável de memória, elemento de array ou campo especificado com memvar ou field.

 Seleção inicial do botão de opção

 Quando um conjunto de botões de opção aparece, o valor de memvar ou field determina qual botão de opção (se houver) é selecionado inicialmente.

 Se memvar ou field for numérico, o botão de opção correspondente ao valor numérico é selecionado inicialmente. Por exemplo, se memvar ou field for 1, o primeiro botão de opção que você definir é selecionado inicialmente. Se memvar ou field não corresponder a nenhum dos botões (o valor é menor que 1 ou maior que o número de botões de opção), nenhum botão é selecionado inicialmente.

 Se memvar ou field for de tipo caractere, uma comparação que diferencia maiúsculas de minúsculas é feita entre memvar ou field e cada prompt de botão de opção. Quando a comparação é feita, todos os caracteres especiais e quaisquer espaços iniciais ou finais são removidos dos prompts dos botões. Se uma correspondência for encontrada, o botão correspondente é selecionado inicialmente. Se uma correspondência não puder ser encontrada, nenhum botão é selecionado inicialmente.

FUNCTION expC1 | PICTURE expC2

 Ao criar um conjunto de botões de opção, você deve incluir a cláusula FUNCTION, a cláusula PICTURE ou ambas. Não há vantagem para nenhum dos três métodos. A cláusula FUNCTION ou PICTURE contém o código de especificação de botão de opção *R e o texto para os prompts individuais dos botões de opção.

 A expressão de caracteres expC1 da cláusula FUNCTION deve começar com *R. Para criar os prompts dos botões de opção, inclua um espaço após *R seguido de uma lista dos prompts separados por ponto e vírgula. Um botão é criado para cada prompt. Por exemplo, a seguinte cláusula FUNCTION cria três botões de opção com os prompts None, Single e Double:

 ... FUNCTION '*R None;Single;Double' ...

 A expressão de caracteres expC2 da cláusula PICTURE usa a mesma sintaxe da expressão FUNCTION, exceto que a expressão PICTURE deve começar com @ seguido de *R. Por exemplo, a seguinte cláusula PICTURE cria três botões de opção com os prompts None, Single e Double:

 ... PICTURE '@*R None;Single;Double' ...

 Você também pode incluir as cláusulas FUNCTION e PICTURE para criar botões de opção. Se ambas forem incluídas, a expressão de caracteres expC1 da FUNCTION deve conter *R para criar os botões de opção e também pode incluir um espaço e alguns prompts de botões de opção. A expressão de caracteres expC2 da PICTURE pode incluir prompts para criar botões de opção adicionais.

 Os exemplos a seguir ilustram as várias formas de sintaxe que você pode usar para criar um conjunto de botões de opção. Os botões de opção começam na segunda linha e segunda coluna. Três botões de opção são criados com os prompts None, Single e Double. Um número correspondente ao botão escolhido é armazenado na variável de memória MCHOICE.

 Somente cláusula FUNCTION:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '*R None;Single;Double'

 READ

 STORE 1 TO mchoice

 STORE '*R None;Single;Double' TO mfunc

 @ 2,2 GET mchoice FUNCTION mfunc

 READ

 Somente cláusula PICTURE:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice PICTURE '@*R None;Single;Double'

 READ

 Cláusulas FUNCTION e PICTURE:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '*R' PICTURE ' None;Single;Double'

 READ

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '*R None;Single' PICTURE ';Double'

 READ

Botões de opção com prompts de imagem

 No FoxPro for Windows e FoxPro for Macintosh, o prompt de um botão de opção também pode ser o nome de um arquivo de imagem. No FoxPro for Macintosh, você pode usar um arquivo de imagem do tipo PICT ou um arquivo bitmap .BMP.

 Quando um botão de opção usa um arquivo de imagem como prompt, o botão de opção imita o comportamento de um botão de opção com prompt de texto. Por exemplo, o arquivo de imagem aparece, mas o botão de opção não é exibido. Como escolher um botão de opção, escolher o prompt de imagem armazena o valor do botão de opção em memvar ou field.

 Para usar um arquivo de imagem em um botão de opção, adicione B ao código de especificação do botão de opção. Os códigos de especificação das cláusulas FUNCTION e PICTURE que criam um botão de opção são *R e @*R, respectivamente. Para criar um botão de opção com prompts de imagem, use os códigos *RB e @*RB, seguidos de um espaço e do nome do arquivo de imagem. Se o arquivo de imagem não estiver localizado no diretório ou pasta padrão, inclua o caminho para o arquivo de imagem com o nome do arquivo de imagem.

 -------------------------------

 Observação - As imagens não são recortadas, reduzidas ou ampliadas para caber no botão de opção. Use a cláusula SIZE para ajustar o tamanho dos botões de opção para acomodar as imagens.

 -------------------------------

 Se você omitir a extensão do arquivo de imagem, o FoxPro for Macintosh primeiro procura um arquivo de imagem com o nome que você especificou e extensão .BMP. Se um arquivo de imagem com extensão .BMP e o nome que você especificou não for encontrado, o FoxPro for Macintosh então procura um arquivo com o nome que você especificou e extensão .PCT. Se um arquivo de imagem com extensão .PCT e o nome que você especificou não for encontrado, o FoxPro for Macintosh então procura um arquivo de imagem com o nome que você especificou sem extensão.

Máscaras de imagem e botões de opção

 No FoxPro for Windows e FoxPro for Macintosh, um botão de opção com imagem tem três estados: up, down e disabled. O FoxPro controla automaticamente a aparência de um botão de opção com imagem quando está em cada um desses três estados, mas você pode substituir a aparência padrão usando uma máscara de imagem.

 Uma máscara é usada para controlar as áreas transparentes de um botão de opção com imagem. Por padrão, as áreas brancas são transparentes. Se uma máscara estiver presente, as áreas brancas da máscara, não do arquivo de imagem, são transparentes.

 Uma máscara é um arquivo de imagem monocromático. No FoxPro for Windows, uma máscara é um .BMP com extensão .MSK. No FoxPro for Macintosh, uma máscara pode ser um .BMP com extensão .MSK ou um arquivo do tipo PICT com extensão .PCM. A máscara deve ter o mesmo nome base do arquivo de imagem e a extensão apropriada. O FoxPro procura automaticamente uma máscara para um arquivo de imagem no mesmo diretório ou pasta onde o arquivo de imagem está localizado.

 Na maioria dos casos, uma máscara não é necessária. Se você não precisa que nada em sua imagem apareça branco ou seu arquivo de imagem tem um fundo branco, o botão de opção com imagem aparecerá como desejado nos estados up, down e disabled.

 Quando um botão de opção com imagem tem uma máscara e está no estado up ou down, quaisquer áreas brancas no arquivo de imagem aparecem transparentes, permitindo que a cor da face do botão apareça. No entanto, você pode manter a cor branca de certas áreas. Suponha que você tenha um arquivo de imagem com um cachorro em um fundo branco; o cachorro tem olhos brancos e a face do botão é vermelha. Você quer que o fundo do botão apareça vermelho, mas quer que os olhos do cachorro sejam brancos, não vermelhos. Faça uma máscara do mesmo tamanho do arquivo de imagem, mas que inclua apenas duas cores, preto e branco. Deixe o fundo da máscara branco, mas faça o cachorro — incluindo seus olhos — completamente preto. Quando o botão aparece, o fundo é vermelho para corresponder à face do botão, mas os olhos do cachorro são brancos.

 Quando um botão de opção com imagem está desabilitado, quaisquer áreas brancas no arquivo de imagem aparecem transparentes para que a cor da face do botão apareça. Quaisquer áreas não brancas aparecem cinza escuro. Se o botão tiver uma máscara, todas as áreas brancas na máscara são transparentes para que a cor da face do botão apareça, e todas as áreas pretas aparecem cinza escuro.

PICTURE and FUNCTION Options N, T, H, V, 2 and 3

 Opções adicionais podem ser combinadas com o código de especificação *R para modificar o comportamento (N e T) e a aparência (H, V, 2 e 3) dos botões de opção.

 Os códigos de especificação 2 (bidimensional) e 3 (tridimensional) estão disponíveis apenas no FoxPro for Macintosh.

 Opção Descrição

 N Não encerra o READ quando um botão de opção é escolhido. Este é o comportamento padrão.

 T Encerra o READ quando um botão de opção é escolhido.

 H Posiciona os botões de opção em uma linha horizontal.

 V Posiciona os botões de opção em uma coluna vertical. Esta é a orientação padrão.

 2 Cria botões de opção planos (bidimensionais) idênticos aos botões de opção em caixas de diálogo Macintosh. Este é o tipo padrão de botão de opção no FoxPro for Macintosh.

 3 Cria botões de opção tridimensionais idênticos aos botões de opção em caixas de diálogo FoxPro for Macintosh.

 Você pode combinar as opções T ou N com as opções H ou V e 2 ou 3. Por exemplo, a seguinte cláusula cria uma coluna vertical de botões de opção e não faz o READ encerrar quando um botão é escolhido:

 ... FUNCTION '*RNV ... '

 No FoxPro for Macintosh, a seguinte cláusula cria uma coluna vertical de botões de opção bidimensionais e não faz o READ encerrar quando um botão é escolhido:

 ... FUNCTION '*RNV2 ... '

Botões de opção com recursos especiais

 Você pode atribuir uma tecla de atalho a um botão de opção ou desabilitar um botão de opção. Para atribuir esses recursos especiais a um botão de opção, você deve incluir caracteres especiais ao definir o prompt. Os caracteres especiais são removidos quando o prompt é armazenado em memvar ou field.

Teclas de atalho

 No FoxPro for MS-DOS, uma tecla de atalho é uma letra destacada em um prompt de botão de opção que você pode digitar para escolher imediatamente o botão de opção. Pressionar a tecla de atalho seleciona o botão de opção e o escolhe. Para atribuir uma tecla de atalho, coloque uma barra invertida e um sinal de menor (\<) antes do caractere desejado do prompt do botão de opção.

 Uma tecla de atalho não escolhe o botão de opção se o objeto atual for um campo GET, uma região de edição de texto, um popup ou uma lista.

 Se o objeto atual for um campo de entrada @ ... GET ou uma região de edição de texto, pressionar a tecla de atalho insere o caractere no campo ou na região de edição de texto. Se o objeto atual for um pop-up ou uma lista, pressionar a tecla de atalho seleciona a primeira opção no popup ou lista cujo prompt começa com o caractere da tecla de atalho.

 No FoxPro for Windows, uma tecla de atalho é uma letra sublinhada no prompt do botão de opção que você pode digitar para escolher imediatamente o botão de opção. Se o objeto atual for um campo de entrada @ ... GET, uma região de edição de texto, um popup ou uma lista e KEYCOMP estiver definido como WINDOWS, você pode pressionar a tecla Alt e a tecla de atalho para escolher o botão de opção.

 No FoxPro for Macintosh, a configuração KEYCOMP determina se as teclas de atalho são sublinhadas. Se KEYCOMP estiver definido como DOS ou WINDOWS, as teclas de atalho são sublinhadas. Se KEYCOMP estiver definido como MAC, as teclas de atalho não são sublinhadas, mas ainda estão disponíveis.

 O exemplo a seguir cria três botões de opção com os prompts None, Single e Double e atribui as teclas de atalho N a None, S a Single e D a Double:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '*R' PICTURE '\<None;\<Single;\<Double'

 READ

Botões de opção desabilitados

 Você pode desabilitar um botão de opção para que não possa ser selecionado ou escolhido. Botões desabilitados são exibidos em cores desabilitadas. Para desabilitar um único botão de opção, coloque duas barras invertidas (\\) antes do prompt do botão. Para desabilitar um conjunto de botões de opção, use DISABLE, que é discutido mais adiante nesta seção.

 O botão de opção com o prompt Single está desabilitado neste exemplo:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '*R' PICTURE 'None;\\Single;Double'

 READ

FONT expC3 [, expN1]

 A expressão de caracteres expC3 é o nome da fonte, e a expressão numérica expN1 é o tamanho da fonte. Por exemplo, a seguinte cláusula pode ser usada para exibir os prompts dos botões de opção em fonte Courier de 16 pontos:

 FONT 'Courier', 16

 Se você incluir a cláusula FONT, mas omitir o tamanho da fonte expN1, uma fonte de 10 pontos é usada.

 No FoxPro for Windows, se a fonte que você especificar não estiver disponível, uma fonte com características de fonte semelhantes é substituída.

 No FoxPro for Macintosh, se a fonte que você especificar não estiver disponível, a fonte Chicago é usada.

 No FoxPro for MS-DOS, a cláusula FONT é ignorada.

 Se a cláusula FONT for omitida e os botões de opção forem colocados na janela principal do FoxPro, a fonte da janela principal do FoxPro é usada. Se a cláusula FONT for omitida e os botões de opção forem colocados em uma janela definida pelo usuário, a fonte da janela definida pelo usuário é usada.

STYLE expC4

 No FoxPro for Windows e FoxPro for Macintosh, inclua a cláusula STYLE para especificar um estilo de fonte para os prompts dos botões de opção. Se o estilo de fonte que você especificar não estiver disponível, um estilo de fonte com características semelhantes é substituído.

 O estilo de fonte é especificado com expC4. Se a cláusula STYLE for omitida, o estilo de fonte normal é usado.

 Caractere Estilo de fonte

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

 Você pode incluir mais de um caractere para especificar uma combinação de estilos de fonte. Por exemplo, a seguinte cláusula especifica Bold Italic:

 STYLE 'BI'

 A cláusula STYLE é ignorada no FoxPro for MS-DOS.

DEFAULT expr

 Quando você escolhe um botão de opção, sua escolha é salva na variável de memória, elemento de array ou campo que você especificar. Se você especificar uma variável de memória que não existe, ela é automaticamente criada e inicializada se você incluir a cláusula DEFAULT. No entanto, um elemento de array não é criado se você especificar um elemento de array em uma cláusula DEFAULT. A cláusula DEFAULT é ignorada se a variável de memória já existir ou se você especificar um campo.

 Se a cláusula DEFAULT não for incluída e memvar não existir, a mensagem de erro "Variable not found" aparece.

 A expressão DEFAULT expr determina o tipo de variável de memória criada e seu valor inicial. expr deve ser de tipo numérico ou caractere. Aqui estão exemplos de cláusulas DEFAULT para botões de opção:

 @ 2,2 GET mchoice FUNCTION '*R' + ;

 'None;Single;Double' DEFAULT 'Single'

 READ

 @ 2,2 GET mchoice FUNCTION '*R None;Single;Double' ;

 DEFAULT 2

 READ

SIZE expN2, expN3 [, expN4]

 A cláusula size expN2 especifica a altura em linhas dos botões de opção. No FoxPro for MS-DOS, um botão de opção tem sempre uma linha de altura, portanto a expressão numérica expN2 é ignorada.

 Por padrão, a largura de cada botão individual é determinada pelo comprimento do texto do prompt do botão de opção. expN3 especifica a largura (em colunas) de cada botão de opção.

 Por padrão, nenhuma linha é colocada entre botões verticais e uma única coluna é colocada entre botões horizontais. O espaçamento entre botões de opção em linhas é especificado com expN4.

 No FoxPro for Windows e FoxPro for Macintosh, a fonte do botão de opção determina o tamanho da região de edição. A fonte do botão de opção é especificada com a cláusula FONT. Se a cláusula FONT for omitida, os botões de opção usam a fonte da janela pai (a janela principal do FoxPro ou uma janela definida pelo usuário).

 Este exemplo demonstra como a cláusula SIZE controla o espaçamento dos botões:

 CLEAR

 @ 2,2 GET mchoice1 FUNCTION '*R'+ '\<None;\<Single;\<Double' ;

 DEFAULT 'None' SIZE 1, 12, 1

 @ 2,16 GET mchoice2 FUNCTION '*R'+ '\<None;\<Single;\<Double' ;

 DEFAULT 'None' SIZE 1, 12, 3

 READ

ENABLE | DISABLE

 Os botões de opção são habilitados por padrão quando READ ou READ CYCLE é emitido. Você pode impedir que um conjunto de botões de opção seja selecionado quando READ ou READ CYCLE é emitido incluindo DISABLE.

 Botões de opção desabilitados não podem ser selecionados e são exibidos nas cores desabilitadas. Para desabilitar botões de opção individuais em vez de um conjunto inteiro, consulte "Botões de opção desabilitados" anteriormente nesta seção. Use SHOW GET ENABLE para habilitar um conjunto de botões de opção desabilitados.

MESSAGE expC5

 A expressão de caracteres expC5 da cláusula MESSAGE aparece quando um botão de opção é selecionado. No FoxPro for MS-DOS, a mensagem é centralizada por padrão na última linha da janela principal do FoxPro. A localização da mensagem pode ser alterada com SET MESSAGE.

 No FoxPro for Windows e FoxPro for Macintosh, a mensagem é colocada na barra de status baseada em gráficos. Se a barra de status baseada em gráficos tiver sido desativada com SET STATUS BAR OFF, a mensagem é colocada na última linha da janela principal do FoxPro.

VALID expL1 | expN5

 Você pode incluir uma expressão VALID opcional expL1 ou expN5 que é avaliada quando um botão de opção é escolhido. Ou seja, VALID não é avaliado quando você seleciona (move para) um botão de opção, mas quando você realmente escolhe o botão de opção pressionando Enter, Spacebar ou clicando no botão de opção.

 Tipicamente, expL1 ou expN5 é uma função definida pelo usuário (UDF). Com uma função definida pelo usuário (UDF), você pode selecionar, habilitar ou desabilitar outros objetos, abrir uma janela Browse, abrir outra tela de entrada de dados ou mover para um novo registro. CLEAR READ pode ser incluído na função definida pelo usuário para encerrar o READ.

 expL1

 Quando um valor lógico é retornado à cláusula VALID, o valor lógico é ignorado e os botões de opção permanecem o controle ativo. No entanto, você pode especificar uma UDF que retorna um valor lógico à cláusula VALID e ativa outro objeto.

 expN5

 Uma cláusula VALID que inclui uma expressão numérica é usada para especificar qual objeto é ativado após um botão de opção ser escolhido. Objetos são campos de entrada @ ... GET, check boxes, listas, popups, spinners, regiões de edição de texto e cada botão individual em um conjunto de push, radio e invisible buttons.

 A expressão expN5 tem um de três efeitos:

  Quando expN5 = 0, o botão de opção escolhido permanece o botão ativo.

  Quando expN5 é positivo, expN5 indica o número de objetos a avançar. Por exemplo, quando o último botão de opção em um conjunto de botões de opção é selecionado e VALID retorna 1, o próximo objeto é ativado. Se expN5 for maior que o número de objetos restantes, o READ é encerrado (a menos que READ CYCLE seja emitido para ativar os objetos).

  Quando expN5 é negativo, expN5 indica o número de objetos a retroceder. Por exemplo, quando o primeiro botão de opção em um conjunto de botões de opção é selecionado e VALID retorna -1, o objeto anterior é ativado. Se expN5 retroceder além do primeiro objeto, o READ é encerrado (a menos que READ CYCLE seja emitido para ativar os objetos).

WHEN expL2

 A cláusula WHEN permite ou proíbe a seleção de um conjunto de botões de opção com base no valor lógico de expL2, que deve avaliar como true (.T.) lógico antes que os botões de opção possam ser selecionados. Se expL2 avaliar como false (.F.) lógico, os botões de opção não podem ser selecionados e são ignorados se colocados entre outros objetos.

COLOR SCHEME expN6 | COLOR color pair list

 Se você não incluir uma cláusula COLOR, as cores dos botões de opção são determinadas pelo esquema de cores da janela principal do FoxPro; se os botões de opção forem colocados em uma janela definida pelo usuário, o esquema de cores da janela determina as cores dos botões de opção.

 As cores dos botões de opção podem ser especificadas incluindo o número de um esquema de cores existente na cláusula COLOR SCHEME ou um conjunto de pares de cores na cláusula COLOR.

 Um esquema de cores é um conjunto de 10 pares de cores predefinidos. Os pares de cores em um esquema de cores podem ser alterados com SET COLOR OF SCHEME. No FoxPro for MS-DOS, os pares de cores em um esquema de cores também podem ser alterados no Color Picker.

 Um par de cores é um conjunto de duas letras separadas por uma barra. A primeira letra especifica a cor de primeiro plano e a segunda letra especifica a cor de fundo.

 Por exemplo, este par de cores especifica um primeiro plano vermelho em um fundo branco:

 R/W

 Para uma lista de cores e suas letras de cor correspondentes, consulte SET COLOR Overview ou Color Table by Color Pair.

 Um par de cores também pode ser especificado com um conjunto de seis valores de cor RGB (Red Green Blue) separados por vírgulas. Os três primeiros valores de cor especificam a cor de primeiro plano e os três últimos valores de cor especificam a cor de fundo. Os valores de cor podem variar de 0 a 255.

 O par de cores R/W no exemplo acima também pode ser especificado com este par de cores RGB:

 RGB(255,0,0,255,255,255)

 A tabela a seguir lista os pares de cores e o que cada par de cores na lista controla.

 Par de cores Botão de opção

 Número Atributo

 ---------- ------------

 5 Mensagem

 6 Prompt de opção selecionado

 7 Teclas de atalho

 9 Prompt de opção habilitado

 10 Prompt de opção desabilitado

 Este exemplo mostra como substituir um esquema de cores por outro esquema de cores predefinido:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '*R None;Single;Double';

 COLOR SCHEME 4

 READ

 O exemplo a seguir cria botões de opção None, Single e Double com as teclas de atalho N para None e S para Single. Além disso, os botões têm as seguintes características de cor:

  O botão selecionado é exibido com um prompt branco brilhante em um fundo azul (W+/B).

  Caracteres de tecla de atalho são exibidos em vermelho em um fundo azul (R/B).

  Botões habilitados são exibidos com um prompt amarelo em um fundo azul (GR+/B).

  Botões desabilitados são exibidos com um prompt branco em um fundo azul (W/B).

 Quando você pula um par de cores, deve incluir uma vírgula onde o par de cores é omitido.

 Aqui estão os comandos:

 STORE 1 TO mchoice

 @ 2,2 GET mchoice FUNCTION '*R \<None;\<Single;\\Double';

 COLOR ,,,,,W+/B,R/B,,GR+/B,W/B

 READ

# Observações

Esta variação de @ ... GET cria um conjunto de botões de opção. Como seu nome sugere, botões de opção são semelhantes aos botões de um rádio de carro — escolher um botão torna sua escolha atual e libera sua escolha anterior. Uma marca ao lado de um botão de opção indica que é a escolha atual.

Se você usar o Screen Builder para criar suas telas de entrada de dados, talvez não precise usar este comando. O Screen Builder gera automaticamente os comandos que criam botões de opção e botões de opção com imagem.

A cadeia de caracteres de texto à direita de cada botão é chamada de prompt. O texto do prompt é especificado com a cláusula FUNCTION ou PICTURE. Emita READ ou READ CYCLE para ativar os botões.

Você pode criar botões de opção com imagem no FoxPro for Windows e FoxPro for Macintosh. Imagens substituem os prompts dos botões de opção.

# Exemplo

```foxpro
CLOSE DATABASES
SET TALK OFF
CLEAR
USE customer
*** Define and activate window for GET information. ***
DEFINE WINDOW one FROM 3, 5 TO 13, 33 FLOAT DOUBLE COLOR SCHEME 5
ACTIVATE WINDOW one
*** Define a set of radio buttons. ***
@ 1,2 GET mchoice FUNCTION '*RNV Next;Prior;Top;Bottom';
	SIZE 1, 10, 1 DEFAULT 'Next'
*** Define a set of push buttons to terminate the READ. ***
@ 3,15 GET okcancel FUNCTION '*V \!OK;\?Cancel' DEFAULT 1;
	SIZE 1, 10, 1
READ CYCLE
*** If Cancel was selected, ***
IF okcancel = 2
	WAIT WINDOW 'Cancel Selected' NOWAIT
ELSE
*** If OK is selected, move record pointer to user's choice. ***
	DO CASE
		CASE mchoice = 'Next'
			SKIP
			IF EOF()
				SKIP -1
			ENDIF
		CASE mchoice = 'Prior'
			IF !BOF()
				SKIP -1
			ENDIF
		CASE mchoice = 'Top'
			GO TOP
		CASE mchoice = 'Bottom'
			GO BOTTOM
	ENDCASE
*** Display user's choice ***
	WAIT WINDOW mchoice + ' Selected' NOWAIT
ENDIF
CLEAR WINDOW
```
