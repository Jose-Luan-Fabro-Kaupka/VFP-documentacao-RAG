# Comando @ ... GET - Text Boxes

Incluído para compatibilidade com versões anteriores. Use o controle TextBox (Visual FoxPro) em vez disso.

Cria uma região de edição.

```foxpro
@ row, column
GET memvar | field
	[FUNCTION expC1]
	[PICTURE expC2]
	[FONT expC3 [, expN1]]
	[STYLE expC4]
	[DEFAULT expr1]
	[ENABLE | DISABLE]
	[MESSAGE expC5]
	[[OPEN] WINDOW window name]
	[RANGE [expr2] [, expr3]]
	[SIZE expN2, expN3]
	[VALID expL1 | expN4
		[ERROR expC6]]
	[WHEN expL2]
	[COLOR SCHEME expN5
	| COLOR color pair list]
```

#### Parâmetros
 row, column

 Row e column são expressões numéricas com valores 0 ou maiores que determinam onde a região de edição @ ... GET aparece.

 A primeira linha é o número 0 na janela principal do FoxPro ou em uma janela definida pelo usuário. As linhas são numeradas de cima para baixo. No FoxPro para Windows, a linha 0 é a linha imediatamente abaixo da barra de menu do sistema FoxPro. No FoxPro para Macintosh, a linha 0 é a linha imediatamente abaixo da barra de título do FoxPro. No FoxPro para MS-DOS, a linha 0 é a linha ocupada pela barra de menu do sistema FoxPro. Consulte SET SYSMENU para obter informações sobre manipular a barra de menu do sistema para que você possa colocar saída na linha 0 no FoxPro para MS-DOS.

 A primeira coluna é o número 0 na janela principal do FoxPro ou em uma janela definida pelo usuário. As colunas são numeradas da esquerda para a direita.

 Quando a região de edição @ ... GET é direcionada a uma janela definida pelo usuário, as coordenadas de linha e coluna são relativas à janela definida pelo usuário, não à janela principal do FoxPro.

 No FoxPro para Windows e no FoxPro para Macintosh, uma posição na janela principal do FoxPro ou em uma janela definida pelo usuário é determinada pela fonte da janela principal do FoxPro ou da janela definida pelo usuário. A maioria das fontes pode ser exibida em uma ampla variedade de tamanhos, e algumas são proporcionalmente espaçadas. Uma linha corresponde à altura da fonte atual; uma coluna corresponde à largura média de uma letra na fonte atual.

 No FoxPro para Windows e no FoxPro para Macintosh, você pode posicionar a região de edição @ ... GET em uma janela com frações decimais para coordenadas de linha e coluna. No FoxPro para MS-DOS, frações decimais usadas para coordenadas de linha e coluna são arredondadas para o valor inteiro mais próximo.

 memvar | field

 @ ... GET cria uma região de edição para a variável de memória ou elemento de matriz especificado em memvar ou o campo especificado em field.

 @ ... GET pode ser usado para criar uma região de edição para um campo memo. Quando você usa @ ... GET com um campo memo, a palavra Memo é exibida. Quando READ é emitido e o campo memo é selecionado, posicione o cursor na palavra Memo e pressione Ctrl+Home, Ctrl+PgUp ou Ctrl+PgDn para abrir a janela de edição de memo. Você também pode clicar duas vezes em Memo para abrir a janela de edição.

 Para sair da janela de edição de memo e salvar suas alterações de edição no FoxPro para MS-DOS, clique na caixa de fechamento da janela ou pressione Ctrl+W. Pressione Esc para descartar suas alterações.

 Para sair da janela de edição de memo e salvar suas alterações no FoxPro para Windows e no FoxPro para Macintosh, escolha Close no menu Control da janela ou pressione Ctrl+W. Pressione Esc para descartar suas alterações.

 -------------------------------

 Dica - Um método melhor para editar campos memo é usar @ ... EDIT em vez de @ ... GET. @ ... EDIT cria uma janela de edição de texto com uma barra de rolagem, e o conteúdo do campo memo é exibido quando @ ... EDIT é emitido.

 -------------------------------

FUNCTION expC1 | PICTURE expC2

 Ao criar uma região de edição de texto com @ ... GET, você pode incluir a cláusula FUNCTION, a cláusula PICTURE ou ambas para criar uma máscara de edição. Essas cláusulas contêm códigos especiais que controlam como a variável de memória, o elemento de matriz ou o campo é exibido e editado.

Códigos FUNCTION podem ser incluídos em uma cláusula PICTURE. Neste caso, a cláusula PICTURE deve começar com @. Além disso, uma cláusula PICTURE pode conter códigos FUNCTION, códigos PICTURE ou ambos. Como uma cláusula FUNCTION afeta toda a expressão, ela pode conter apenas códigos FUNCTION.

 Códigos de função

 --------------

 Código Finalidade

 ---- -------

 A Permite apenas caracteres alfabéticos (sem espaços ou símbolos).

 B Alinha à esquerda dados numéricos no campo de saída.

 D Usa o formato SET DATE atual.

 E Edita dados de tipo data como data BRITISH.

 I Centraliza texto em um campo.

 J Alinha à direita texto em um campo.

 K Seleciona um campo inteiro para edição quando o cursor é movido para o campo.

 L Exibe zeros à esquerda (em vez de espaços) na saída numérica. Use somente com dados numéricos.

 M
 list Cria várias escolhas predefinidas. A lista é uma coleção de itens separados por vírgulas. Itens individuais na lista não podem conter vírgulas incorporadas. Se memvar ou field inicialmente não contiver um dos itens da lista quando READ é emitido, o primeiro item da lista é exibido.

 Para rolar pela lista, pressione a barra de espaço ou digite a primeira letra de um item. Para escolher um dos itens e mover para o próximo controle, pressione Enter. Use somente com dados de caractere.

 R Exibe uma máscara de formato em uma região de edição @ ... GET. Esses caracteres de máscara não são armazenados no campo quando você sai da região de edição @ ... GET. Use somente com dados de caractere ou numéricos.

 Sn Limita a largura de exibição a n caracteres. Você pode rolar na região com as teclas de controle do cursor. Use somente com dados de caractere.

 T Remove espaços em branco à esquerda e à direita de memvar ou field.

 Z Exibe memvar ou field como em branco se seu valor numérico for 0. Use somente com dados numéricos.

 ! Converte caracteres alfabéticos para maiúsculas. Use somente com dados de caractere.

 , Exibe dados numéricos usando notação científica. Use somente com dados numéricos.

 $ Exibe dados em formato de moeda. O símbolo de moeda aparece antes ou depois do valor, dependendo da configuração atual de SET CURRENCY. Se CURRENCY estiver SET LEFT, o código de função $ não pode ser usado. Use somente com dados numéricos.

 Uma expressão PICTURE pode incluir quaisquer caracteres, mas somente os caracteres listados abaixo participam ativamente da exibição e edição.

 Códigos Picture

 -------------

 Código Finalidade

 ---- -------

 A Permite apenas caracteres alfabéticos.

 L Permite apenas dados lógicos.

 N Permite apenas letras e dígitos.

 X Permite qualquer caractere.

 Y Permite apenas Y, y, N e n lógicos. Converte y e n para Y e N, respectivamente.

 9 Permite apenas dígitos em dados de caractere. Permite dígitos e sinais em dados numéricos.

 # Permite dígitos, espaços em branco e sinais.

 ! Converte letras minúsculas em letras maiúsculas.

 $ Exibe o símbolo de moeda atual especificado por SET CURRENCY. Por padrão, o símbolo é colocado imediatamente antes ou depois do campo. No entanto, o símbolo de moeda e sua posição (SET CURRENCY), o caractere separador (SET SEPARATOR) e o caractere decimal (SET POINT) podem ser alterados. Só pode ser usado em @ ... GET quando SET CURRENCY é LEFT.

 * Asteriscos são exibidos na frente de um valor numérico. Use com um cifrão $ para proteção de cheque.

 . Especifica a posição do ponto decimal.

 , Use para separar dígitos à esquerda do ponto decimal.

FONT expC3 [, expN1]

 A expressão de caractere expC3 é o nome da fonte e a expressão numérica expN1 é o tamanho da fonte.

 Por exemplo, este pequeno programa de exemplo exibe o campo CONTACT para edição. No FoxPro para Windows e no FoxPro para Macintosh, o texto na região de edição é exibido em fonte Courier de 16 pontos:

 CLOSE DATABASES

 USE customer

 DO CASE

 CASE _WINDOWS OR _MAC

 @ 2, 2 GET contact FONT 'Courier',16

 CASE _DOS

 @ 2, 2 GET contact

 ENDCASE

 READ

 Se você incluir a cláusula FONT, mas omitir o tamanho da fonte expN1, uma fonte de 10 pontos é usada.

 No FoxPro para Windows, se a fonte especificada não estiver disponível, uma fonte com características semelhantes é substituída.

 No FoxPro para Macintosh, se a fonte especificada não estiver disponível, a fonte Chicago é usada.

 No FoxPro para MS-DOS, a cláusula FONT é ignorada.

 Se a cláusula FONT for omitida e a região de edição for colocada na janela principal do FoxPro, a fonte da janela principal do FoxPro é usada. Se a cláusula FONT for omitida e a região de edição for colocada em uma janela definida pelo usuário, a fonte da janela definida pelo usuário é usada.

STYLE expC4

 No FoxPro para Windows e no FoxPro para Macintosh, inclua a cláusula STYLE para especificar um estilo de fonte para uma região de edição @ ... GET.

 O estilo da fonte é especificado com expC4. Se a cláusula STYLE for omitida, o estilo de fonte normal é usado.

 No FoxPro para Windows, se o estilo de fonte especificado não estiver disponível, um estilo de fonte com características semelhantes é substituído.

 No FoxPro para Macintosh, se a fonte especificada não estiver disponível, o estilo de fonte normal é usado.

 A cláusula STYLE é ignorada no FoxPro para MS-DOS.

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

 * Os estilos Condense e Extend estão disponíveis somente no FoxPro para Macintosh. O estilo Strikeout está disponível somente no FoxPro para Windows.

 Se você incluir T para criar uma região de edição transparente, a cor de fundo é ignorada pela região.

 Você pode incluir mais de um caractere para especificar uma combinação de estilos de fonte. Por exemplo, o programa curto a seguir cria uma região de edição de texto @ ... GET. O campo CONTACT aparece na região de edição em Bold Italic no FoxPro para Windows e no FoxPro para Macintosh.

 CLOSE DATABASES

 CLEAR

 USE customer

 DO CASE

 CASE _WINDOWS OR _MAC

 @ 2, 2 GET contact STYLE 'BI'

 CASE _DOS

 @ 2, 2 GET contact

 ENDCASE

 READ

DEFAULT expr1

 Se você especificar uma variável de memória para a região de edição @ ... GET que não existe, ela é criada e inicializada automaticamente se você incluir DEFAULT. No entanto, um elemento de matriz não é criado se você especificar um elemento de matriz em uma cláusula DEFAULT. A cláusula DEFAULT é ignorada se a variável de memória já existir ou você especificar um campo.

 -------------------------------

 Observação - Se a cláusula DEFAULT não for incluída e a variável de memória memvar não existir, a mensagem de erro "Variable not found" aparece.

 -------------------------------

 A expressão DEFAULT expr1 determina o tipo de variável de memória criada e seu valor inicial.

ENABLE | DISABLE

 Incluir DISABLE impede o acesso a uma região de edição @ ... GET. A região de edição é exibida nas cores desabilitadas e não pode ser selecionada.

 Por padrão, regiões de edição @ ... GET estão habilitadas. Você pode incluir ENABLE como lembrete em um programa de que uma região de edição GET pode ser acessada.

 -----------------------------------

 Observação - Se todos os GETs em uma janela definida pelo usuário estiverem desabilitados, a janela não permanecerá no topo. Se todos os GETs no READ atual estiverem desabilitados, o READ é encerrado.

 -----------------------------------

MESSAGE expC5

 A expressão de caractere expC5 da cláusula MESSAGE aparece quando a região de edição @ ... GET é selecionada. No FoxPro para MS-DOS, a mensagem é centralizada na última linha da janela principal do FoxPro e cancela temporariamente qualquer expressão SET MESSAGE.

 No FoxPro para Windows e no FoxPro para Macintosh, a mensagem é colocada na barra de status no estilo Windows. Se a barra de status no estilo Windows foi desativada com SET STATUS BAR OFF, a mensagem é colocada na última linha da janela principal do FoxPro.

[OPEN] WINDOW window name

 Inclua a cláusula WINDOW para editar um campo memo em uma janela definida pelo usuário. A janela definida pelo usuário deve primeiro ser criada com DEFINE WINDOW. A palavra Memo é exibida quando você emite @ ...GET WINDOW.

 Para abrir a janela de edição de memo, clique duas vezes em Memo ou posicione o cursor na palavra Memo e pressione Ctrl+Home, Ctrl+PgUp ou Ctrl+PgDn.

 Se OPEN for incluído, a janela de edição de memo é aberta automaticamente quando READ ou READ CYCLE é emitido.

 Para sair da janela e salvar suas alterações de edição no FoxPro para MS-DOS, clique na caixa de fechamento da janela (se disponível) ou pressione Ctrl+W. Pressione Esc para descartar suas alterações.

 Para sair da janela e salvar suas alterações de edição no FoxPro para Windows, escolha Close no menu Control da janela (se disponível) ou pressione Ctrl+W. Pressione Esc para descartar suas alterações.

 Para sair da janela e salvar suas alterações de edição no FoxPro para Macintosh, clique na caixa de fechamento ou pressione Ctrl+W. Pressione Esc para descartar suas alterações.

 -------------------------------

 Dica - Um método melhor para editar campos memo é usar @ ... EDIT em vez de @ ... GET. @ ... EDIT cria uma janela de edição de texto com uma barra de rolagem, e o conteúdo do campo memo é exibido quando @ ... EDIT é emitido.

 -------------------------------

RANGE [expr2] [, expr3]

 Use a cláusula RANGE com dados de caractere, data e numéricos para especificar um intervalo de valores aceitáveis. Se o valor inserido na região de edição @ ... GET não estiver dentro do intervalo especificado, uma mensagem mostrando o intervalo correto é exibida. Para substituir a mensagem de intervalo padrão, use ON READERROR.

 O limite inferior do intervalo é especificado com expr2, o limite superior com expr3. expr2 e expr3 devem ser expressões de caractere, numéricas ou de data que correspondam aos dados na variável de memória, elemento de matriz ou campo. expr2 ou expr3 pode ser omitido, mas não ambos. Se um limite for omitido, os dados inseridos são verificados apenas contra o limite especificado.

 -------------------------------

 Observação - O intervalo não é verificado se você pressionar Enter sem alterar a variável de memória, o elemento de matriz ou o campo.

 -------------------------------

SIZE expN2, expN3

 SIZE permite controlar o comprimento e a altura de uma região de edição de texto @ ... GET. Por padrão, uma região de edição de texto tem uma linha de altura. O tamanho da região é determinado pelo comprimento da variável de memória, elemento de matriz ou campo ou por uma cláusula PICTURE.

 A altura da região de edição de texto em linhas é especificada com expN2 e a largura em colunas é especificada com expN3.

 No FoxPro para Windows e no FoxPro para Macintosh, a fonte da região de edição determina o tamanho da região de edição. A fonte da região de edição é especificada com a cláusula FONT. Se a cláusula FONT for omitida, a região de edição usa a fonte de sua janela pai (a janela principal do FoxPro ou uma janela definida pelo usuário).

VALID expL1 | expN4

 Use VALID para validar a entrada. Quando você tenta sair da região de edição GET, a expressão VALID é avaliada.

 Uma cláusula VALID simplifica muito a validação de dados quando usada com uma função definida pelo usuário (UDF). Se uma UDF é chamada em uma cláusula VALID em @ ... GET, a UDF deve retornar um valor lógico ou numérico.

 -------------------------------

 Observação - Diferentemente da cláusula RANGE, uma cláusula VALID é sempre executada quando você sai da região de edição GET, a menos que pressione Esc. A cláusula RANGE é executada somente quando uma alteração é feita na variável de memória, elemento de matriz ou campo.

 -------------------------------

 expL1

 Se expL1 avaliar para true lógico (.T.), a entrada é considerada correta e a região de edição é encerrada.

 Se expL1 avaliar para false (.F.), o valor inserido é considerado incorreto e uma mensagem é exibida orientando você a reinserir os dados após pressionar a barra de espaço.

 Se uma rotina de validação UDF realizar uma substituição em um campo e a rotina de validação retornar false, a substituição do campo ocorre, mas o valor anterior do campo é restaurado quando você retorna da UDF para a região de edição GET.

 expN4

 Uma cláusula VALID que inclui uma expressão numérica é usada para especificar qual objeto é ativado após você sair da região de edição GET. Objetos são campos de entrada @ ... GET, caixas de seleção, listas, popups, spinners, regiões de edição de texto e cada botão individual em um conjunto de botões push, radio e invisíveis. A expressão numérica expN4 tem um dos três efeitos:

 Quando expN4 é 0, o cursor permanece na região de edição GET. As mensagens de erro MESSAGE expC5 e ERROR expC6 são suprimidas. Uma rotina especial de mensagem de erro pode ser escrita como parte de uma UDF chamada por VALID.

 Se uma rotina de validação UDF realizar uma substituição em um campo e a rotina de validação retornar 0, a substituição do campo ocorre, mas o valor anterior do campo é restaurado quando você retorna à região de edição GET.

 Quando expN4 é positivo, expN4 especifica o número de objetos a avançar. Por exemplo, quando o cursor está posicionado em uma região de edição GET e VALID retorna 1, o próximo objeto é ativado. Se expN4 for maior que o número de objetos restantes, o READ é encerrado (a menos que READ CYCLE seja emitido para ativar os objetos).

 Quando expN4 é negativo, expN4 especifica o número de objetos a retroceder. Por exemplo, quando o cursor está posicionado em uma região de edição GET e VALID retorna -1, o objeto anterior é ativado. Se expN4 retroceder além do primeiro objeto, o READ é encerrado (a menos que READ CYCLE seja emitido para ativar os objetos).

ERROR expC6

 ERROR expC6 permite especificar uma mensagem de erro personalizada exibida quando uma cláusula VALID avalia para false (.F.). O FoxPro exibe expC6 no lugar da mensagem de erro padrão.

WHEN expL2

WHEN permite ou proíbe o acesso a uma região de edição GET com base no valor de expL2, que deve ser true (.T.) antes que a região de edição GET possa ser acessada. Se WHEN for especificado e expL2 for false (.F.), a região de edição GET não pode ser acessada e o próximo objeto é ativado.

COLOR SCHEME expN5 | COLOR color pair list

 Se você não incluir uma cláusula COLOR, as cores de uma região de edição @ ... GET são determinadas pelo esquema de cores da janela principal do FoxPro; se uma região de edição @ ... GET for colocada em uma janela definida pelo usuário, o esquema de cores da janela determina as cores da região de edição.

 Somente o segundo par de cores em um esquema de cores ou lista de pares de cores afeta a cor de uma região de edição @ ... GET.

 A cor de uma região de edição @ ... GET pode ser especificada incluindo o número de um esquema de cores existente na cláusula COLOR SCHEME ou um conjunto de pares de cores na cláusula COLOR.

 Um esquema de cores é um conjunto de 10 pares de cores predefinidos. Os pares de cores em um esquema de cores podem ser alterados com SET COLOR OF SCHEME. No FoxPro para MS-DOS, os pares de cores em um esquema de cores também podem ser alterados no Color Picker.

 Um par de cores é um conjunto de duas letras separadas por uma barra. A primeira letra especifica a cor de primeiro plano e a segunda letra especifica a cor de fundo.

 Por exemplo, este par de cores especifica primeiro plano vermelho em fundo branco:

 R/W

 Para uma lista de cores e suas letras de cor correspondentes, consulte SET COLOR Overview ou Color Table by Color Pair.

 Um par de cores também pode ser especificado com um conjunto de seis valores de cor RGB (Red Green Blue) separados por vírgulas. Os três primeiros valores de cor especificam a cor de primeiro plano e os três últimos valores de cor especificam a cor de fundo. Os valores de cor podem variar de 0 a 255.

 O par de cores R/W no exemplo acima também pode ser especificado com este par de cores RGB:

 RGB(255,0,0,255,255,255)

 Somente os pares de cores 2, 5, 6 e 10 em um esquema de cores ou lista de pares de cores afetam as cores da região de edição @ ... GET.

 Par de cores Região de edição

 Número Atributo

 ---------- --------------

 2 Região de edição @ ... GET

 5 Mensagem

 6 Região de edição @ ... GET selecionada

 10 Região de edição @ ... GET desabilitada

# Observações

OPEN WINDOW está incluído para compatibilidade com versões anteriores. Use @ ... EDIT em vez disso.

Use este comando para criar uma região de edição para o conteúdo de uma variável de memória, elemento de matriz ou campo. Use READ ou READ CYCLE para ativar regiões de edição @ ... GET.

Você pode combinar @ ... SAY e @ ... GET em um único comando. Se as cláusulas SAY e GET estiverem incluídas, especifique um único conjunto de coordenadas row, column onde a saída @ ... SAY começa. Um espaço é inserido automaticamente entre a saída @ ... SAY e a região de edição @ ... GET.

Se você usar o Screen Builder para criar suas telas de entrada de dados, talvez não precise usar @ ... GET ou @ ... SAY. O Screen Builder gera automaticamente os @ ... GETs ou @ ... SAYs.

# Exemplo

O exemplo a seguir demonstra como você pode combinar @ ... SAY e @ ... GET em um único comando e as cláusulas COLOR, PICTURE, RANGE e WHEN. Duas tabelas são abertas e uma relação é definida entre as tabelas CUSTOMER e OFFICES para extrair informações de ambas as tabelas.

```foxpro
SET TALK OFF
CLEAR
CLOSE DATABASES
USE customer IN 0			&& Parent
USE offices  IN 0 ORDER ono	&& Child
SET RELATION TO ono INTO offices	&& Set the relation
@  1, 0 TO 18, 79 DOUBLE
@  3, 13 SAY 'Company: '	GET company COLOR gr+/b, r/w
@  5, 13 SAY 'Contact: '	GET contact COLOR gr+/b, r/w
@  7, 13 SAY 'Address: '	GET address COLOR gr+/b, r/w
@  9, 13 SAY 'City: '		GET city COLOR gr+/b, r/w
@ 11, 13 SAY 'State: '		GET state PICTURE '!!' COLOR gr+/b, r/w
@ 11, 28 SAY 'Zip: '		GET zip COLOR gr+/b, r/w
@ 15, 13 SAY 'Ytdsales: '
@ 15, 23 GET offices.ytdsales PICTURE '999999.99' RANGE 100,999999  ;
	MESSAGE 'Enter ytdsales from 100 to 999999.'
READ
CLEAR
```
