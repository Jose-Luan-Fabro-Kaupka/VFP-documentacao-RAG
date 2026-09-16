# Comando @ ... GET - Spinners

Incluído para compatibilidade com versões anteriores. Use o controle Spinner em vez disso.

Cria um spinner.

```foxpro
@ row, column
GET memvar | field
SPINNER expN1 [, expN2
[, expN3]]
	[FUNCTION expC1]
	[PICTURE expC2]
	[FONT expC3 [, expN4]]
	[STYLE expC4]
	[DEFAULT expN5]
	[SIZE expN6, expN7]
	[ENABLE | DISABLE]
	[MESSAGE expC5]
	[RANGE [expN8] [, expN9]]
	[VALID expL1 | expN10
		[ERROR expC6]]
	[WHEN expL2]
	[COLOR SCHEME expN11
	| COLOR color pair list]
```

#### Parâmetros
 row, column

 Row e column são expressões numéricas com valores 0 ou maiores que determinam onde o spinner aparece.

 A primeira linha é o número 0 na janela principal do FoxPro ou em uma janela definida pelo usuário. As linhas são numeradas de cima para baixo. No FoxPro for Windows, a linha 0 é a linha imediatamente abaixo da barra de menus do sistema FoxPro. No FoxPro for Macintosh, a linha 0 é a linha imediatamente abaixo da barra de título do FoxPro.

 A primeira coluna é o número 0 na janela principal do FoxPro ou em uma janela definida pelo usuário. As colunas são numeradas da esquerda para a direita.

 Quando o spinner é direcionado a uma janela definida pelo usuário, as coordenadas de linha e coluna são relativas à janela definida pelo usuário, e não à janela principal do FoxPro.

 Uma posição na janela principal do FoxPro ou em uma janela definida pelo usuário é determinada pela fonte da janela principal do FoxPro ou da janela definida pelo usuário. A maioria das fontes pode ser exibida em uma ampla variedade de tamanhos, e algumas são proporcionais. Uma linha corresponde à altura da fonte atual; uma coluna corresponde à largura média de uma letra na fonte atual.

 Você pode posicionar o spinner em uma janela com frações decimais para as coordenadas de linha e coluna.

GET memvar | field

 O valor numérico contido em memvar ou field é o valor inicial exibido no spinner antes que READ ou READ CYCLE seja emitido.

 Quando você escolhe um valor no spinner, sua escolha é armazenada na variável de memória numérica ou elemento de array memvar ou no campo numérico field.

SPINNER expN1 [, expN2 [, expN3]]

 Os valores exibidos no spinner são especificados com expN1, expN2 e expN3.

 O valor exibido na caixa de texto do spinner é incrementado ou decrementado pelo valor especificado com expN1. Por exemplo, se expN1 é 2 e você clica na seta para cima ou para baixo, o valor na caixa de texto aumenta ou diminui em 2.

 O exemplo a seguir define um spinner para a variável de memória MCHOICE. O spinner incrementa de 1 com limite inferior de -5 e limite superior de 24. O valor inicial exibido é 3.

 @ 2,2 GET mchoice SPINNER 1, -5, 24 DEFAULT 3

 O valor mínimo que pode ser exibido no spinner é especificado com expN2, e o valor máximo que pode ser exibido é especificado com expN3. No entanto, usando o teclado você pode inserir um valor na caixa de texto que esteja fora do intervalo especificado com expN2 e expN3. Use VALID ou RANGE para controlar quais valores podem ser inseridos na caixa de texto com o teclado.

[FUNCTION expC1]

[PICTURE expC2]

 Ao criar spinners, você pode incluir a cláusula FUNCTION, a cláusula PICTURE ou ambas. Não há vantagem em nenhum dos três métodos. As cláusulas FUNCTION e PICTURE controlam como memvar ou field aparece e é editado na caixa de texto.

 A tabela a seguir mostra como a cláusula FUNCTION expC1 determina como os valores são exibidos na caixa de texto do spinner.

 expC1 Finalidade

 ------- -------

 B Alinha o valor à esquerda na caixa de texto.

 I Centraliza o valor na caixa de texto.

 J Alinha o valor à direita na caixa de texto.

 K Seleciona o valor inteiro para edição quando o cursor é movido para o spinner.

 L Exibe zeros à esquerda antes do valor.

 Z Exibe o valor como em branco se for 0.

 ^ Exibe o valor usando notação científica.

 $ Exibe o valor em formato de moeda. O símbolo da moeda aparece à esquerda ou à direita do valor, dependendo da configuração de SET CURRENCY.

 A expressão de caracteres da cláusula PICTURE expC2 determina quais valores podem ser inseridos na caixa de texto, como os valores são exibidos e a aparência do spinner. A expressão da cláusula PICTURE expC2 opera em caracteres individuais no spinner. Você deve incluir caracteres de máscara suficientes para permitir a entrada do valor mais alto que você antecipa, além de quaisquer sinais ou símbolos.

 As especificações 2 (bidimensional) e 3 (tridimensional) estão disponíveis apenas no FoxPro for Macintosh.

 expC2 Finalidade

 ------- -------

 9 Permite inserir dígitos e sinais ().

 # Permite inserir dígitos, espaços em branco e sinais ().

 $ Exibe o símbolo de moeda atual (especificado com SET CURRENCY).

 * Asteriscos são exibidos à esquerda do valor.

 . Um ponto especifica a posição do ponto decimal.

 , Vírgulas podem ser incluídas para separar dígitos à esquerda do ponto decimal.

 2 Cria um spinner plano (bidimensional) idêntico aos spinners nas caixas de diálogo do Macintosh. Este é o tipo de spinner padrão no FoxPro for Macintosh.

 3 Cria um spinner tridimensional idêntico aos spinners nas caixas de diálogo do FoxPro for Macintosh.

FONT expC3 [, expN4]

 A expressão de caracteres expC3 é o nome da fonte, e a expressão numérica expN4 é o tamanho da fonte. Por exemplo, o comando a seguir exibe o texto no spinner em fonte Courier de 16 pontos:

 @ 2, 2 GET mchoice SPINNER 1, 1, 10 DEFAULT 3 FONT 'Courier', 16

 Se você incluir a cláusula FONT, mas omitir o tamanho da fonte expN4, uma fonte de 10 pontos é usada.

 Se a cláusula FONT for omitida e o spinner for colocado na janela principal do FoxPro, a fonte da janela principal do FoxPro é usada. Se a cláusula FONT for omitida e o spinner for colocado em uma janela definida pelo usuário, a fonte da janela definida pelo usuário é usada.

 Se a fonte que você especificar não estiver disponível, uma fonte com características semelhantes é substituída.

STYLE expC4

 No FoxPro for Windows e no FoxPro for Macintosh, inclua a cláusula STYLE para especificar um estilo de fonte para o spinner. Se o estilo de fonte que você especificar não estiver disponível, um estilo de fonte com características semelhantes é substituído.

O estilo de fonte é especificado com expC4. Se a cláusula STYLE for omitida, o estilo de fonte padrão é usado.

 Caractere Estilo de fonte

 --------- ----------

 B Negrito

 C Condense*

 E Extend*

 I Itálico

 N Normal

 O Outline

 Q Opaque

 S Shadow

 - Strikeout*

 T Transparent

 U Sublinhado

 * Os estilos Condense e Extend estão disponíveis apenas no FoxPro for Macintosh. O estilo Strikeout está disponível apenas no FoxPro for Windows.

 Você pode incluir mais de um caractere para especificar uma combinação de estilos de fonte. Por exemplo, o comando a seguir exibe o texto no spinner em Negrito Itálico:

 @ 2, 2 GET mchoice SPINNER 1, 1, 10 DEFAULT 3 STYLE 'BI'

DEFAULT expN5

 Quando você sai de um spinner, o valor no spinner é salvo na variável de memória, elemento de array ou campo que você especificar. Se você especificar uma variável de memória que não existe, ela é criada automaticamente e inicializada com expN5 se você incluir DEFAULT. No entanto, um elemento de array não é criado se você especificar um elemento de array em uma cláusula DEFAULT. A cláusula DEFAULT é ignorada se a variável de memória já existir ou se você especificar um campo.

 -------------------------------

 Observação - Se a cláusula DEFAULT não for incluída e memvar não existir, a mensagem de erro "Variable not found" aparece.

 -------------------------------

SIZE expN6, expN7

 A expressão SIZE expN6 especifica a altura do spinner. A altura do spinner é um múltiplo da altura da fonte atual ou da fonte que você especificar ao criar o spinner. Por exemplo, se expN6 é 2, a altura do spinner é duas vezes a altura da fonte atual ou da fonte que você especificar.

 A expressão numérica expN7 especifica a largura do spinner. A largura do spinner é um múltiplo da largura média de uma letra na fonte atual ou na fonte que você especificar ao criar o spinner. Por exemplo, se expN7 é 2, a largura do spinner é duas vezes a largura média de uma letra na fonte atual ou na fonte que você especificar.

 A fonte do spinner determina o tamanho do spinner. A fonte do spinner é especificada com a cláusula FONT. Se a cláusula FONT for omitida, o spinner usa a fonte da janela pai (a janela principal do FoxPro ou uma janela definida pelo usuário).

ENABLE | DISABLE

 Os spinners são habilitados quando READ ou READ CYCLE é emitido. Você pode impedir que um spinner seja selecionado incluindo DISABLE. O spinner é desabilitado quando READ ou READ CYCLE é emitido.

 Spinners desabilitados não podem ser selecionados e são exibidos nas cores de desabilitado. Use SHOW GET ENABLE para habilitar um spinner desabilitado.

MESSAGE expC5

 A expressão de caracteres opcional da cláusula MESSAGE expC5 aparece quando o spinner é selecionado. A mensagem é colocada na barra de status gráfica. Se a barra de status gráfica foi desativada com SET STATUS BAR OFF, a mensagem é colocada na última linha da janela principal do FoxPro.

RANGE [expN8] [, expN9]

 Use a cláusula RANGE para especificar um intervalo de valores aceitáveis do spinner. Se o valor inserido na caixa de texto do spinner não estiver dentro do intervalo especificado, uma mensagem mostrando o intervalo correto aparece. Para substituir a mensagem de intervalo padrão, crie uma rotina usando ON READERROR.

 O limite inferior do intervalo é especificado com expN8, o limite superior com expN9. expN8 ou expN9 pode ser omitido, mas não ambos. Se um limite for omitido, essa extremidade do intervalo não é verificada.

 O intervalo não é verificado se você pressionar Enter sem alterar o valor inicial do spinner.

VALID expL1 | expN10 [ERROR expC6]

 Você pode incluir uma expressão VALID opcional expL1 ou expN10 que é avaliada quando você tenta sair do spinner.

 -------------------------------

 Observação - Diferentemente da verificação RANGE, a verificação VALID é sempre executada quando você tenta sair do spinner, a menos que você saia pressionando Esc. A verificação RANGE é executada apenas quando uma alteração é feita no valor inicial do spinner.

 -------------------------------

 Normalmente, expL1 ou expN10 é uma função definida pelo usuário. Com uma função definida pelo usuário, você pode selecionar, habilitar ou desabilitar outros objetos, abrir uma janela Browse, abrir outra tela de entrada de dados ou mover para um novo registro. CLEAR READ pode ser incluído na função definida pelo usuário para encerrar o READ.

 expL1

 Se expL1 for avaliado como verdadeiro lógico (.T.), o valor no spinner é considerado correto e o spinner é encerrado.

 Se expL1 for avaliado como falso (.F.), o valor inserido no spinner é considerado incorreto e o spinner permanece o controle ativo. Uma mensagem aparece na barra de status gráfica orientando você a reinserir os dados após pressionar a barra de espaço.

 expN10

 Uma cláusula VALID que inclui uma expressão numérica é usada para especificar qual objeto é ativado após um spinner ser escolhido. Os objetos incluem campos de entrada @ ... GET, caixas de seleção, listas, popups, spinners, regiões de edição de texto e cada botão individual em um conjunto de botões push, de opção e invisíveis.

  Quando expN10 = 0, o spinner permanece o objeto ativo e as mensagens MESSAGE expC5 e ERROR expC6 são suprimidas. Uma rotina especial de mensagem de erro pode ser escrita como parte de uma função definida pelo usuário chamada pela cláusula VALID.

  Quando expN10 é positivo, expN10 especifica o número de objetos a avançar. Por exemplo, quando o spinner é selecionado e VALID retorna 1, o próximo objeto é ativado. Se expN10 for maior que o número de objetos restantes, o READ é encerrado (a menos que READ CYCLE seja emitido para ativar os objetos).

  Quando expN10 é negativo, expN10 especifica o número de objetos a retroceder. Por exemplo, quando o spinner é selecionado e VALID retorna -1, o objeto anterior é ativado. Se expN10 retroceder além do primeiro objeto, o READ é encerrado (a menos que READ CYCLE seja emitido para ativar os objetos).

ERROR expC6

 A cláusula ERROR permite especificar uma mensagem de erro personalizada que aparece quando a cláusula VALID é avaliada como falso (.F.). expC6 aparece no lugar da mensagem de erro padrão.

WHEN expL2

 A cláusula WHEN opcional permite ou proíbe a seleção de um spinner com base no valor lógico de expL2, que deve ser avaliado como verdadeiro lógico (.T.) antes que o spinner possa ser selecionado. Se expL2 for avaliado como falso lógico (.F.), o spinner não pode ser selecionado e é ignorado se estiver entre outros objetos.

COLOR SCHEME expN11 | COLOR color pair list

 Se você não incluir uma cláusula COLOR, as cores do spinner são determinadas pelo esquema de cores da janela principal do FoxPro; se um spinner for colocado em uma janela definida pelo usuário, o esquema de cores da janela determina as cores do spinner.

 As cores de um spinner podem ser especificadas incluindo o número de um esquema de cores existente na cláusula COLOR SCHEME ou um conjunto de pares de cores na cláusula COLOR.

 Um esquema de cores é um conjunto de 10 pares de cores predefinidos. Os pares de cores em um esquema de cores podem ser alterados com SET COLOR OF SCHEME.

 Um par de cores é um conjunto de duas letras separadas por uma barra. A primeira letra especifica a cor de primeiro plano e a segunda letra especifica a cor de fundo.

 Por exemplo, este par de cores especifica primeiro plano vermelho em fundo branco:

 R/W

 Para uma lista de cores e suas letras de cor correspondentes, consulte SET COLOR Commands Overview ou Color Table by Color Pair.

 Um par de cores também pode ser especificado com um conjunto de seis valores de cor RGB (Red Green Blue) separados por vírgulas. Os três primeiros valores de cor especificam a cor de primeiro plano e os três últimos valores de cor especificam a cor de fundo. Os valores de cor podem variar de 0 a 255.

 O par de cores R/W no exemplo acima também pode ser especificado com este par de cores RGB:

 RGB(255,0,0,255,255,255)

# Observações

@ ... GET Spinners é suportado no FoxPro for Windows e no FoxPro for Macintosh.

Um spinner é um controle que permite "girar" por um conjunto de valores numéricos exibidos em uma caixa de texto.

Se você usar o Screen Builder para criar suas telas de entrada de dados, talvez não precise usar este comando. O Screen Builder gera automaticamente os comandos que criam spinners.

Clicar nas setas para cima e para baixo altera o valor numérico. Você também pode inserir um valor diretamente na caixa de texto do spinner. Quando o valor desejado aparecer na caixa de texto, pressione Enter ou Tab para mover para o próximo objeto.

Usar a sintaxe de spinner no FoxPro for MS-DOS cria uma região de edição @ ... GET numérica. Você deve inserir um valor numérico na região de edição com o teclado. O valor de incremento (expN1), os valores de limite inferior e superior (expN2, expN3) e as cláusulas FONT e STYLE são ignorados.
