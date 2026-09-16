# Comando @ ... TO

Incluído para compatibilidade com versões anteriores. Use o controle Shape em vez disso.

Desenha uma caixa, círculo ou elipse usando coordenadas especificadas.

```foxpro
@ row1, column1
TO row2, column2
	[DOUBLE | PANEL
	| border string]
	[PATTERN expN1]
	[PEN expN2 [, expN3]]
	[STYLE expC]
	[COLOR SCHEME expN4
	| COLOR color pair list]
```

#### Parâmetros
 row1, column1 ... row2, column2
 row1, column1 são as coordenadas do canto superior esquerdo da caixa. row2, column2 são as coordenadas do canto inferior direito da caixa. Se row1 e row2 são iguais, uma linha horizontal é desenhada. Se column1 e column2 são iguais, uma linha vertical é desenhada.

 DOUBLE | PANEL | border string

 Se DOUBLE é incluído, a caixa é desenhada com uma borda de linha dupla. Se PANEL é incluído, a caixa é desenhada com uma borda sólida.

 border string é um conjunto de caracteres que especificam partes da caixa nesta ordem: topo, base, lado esquerdo, lado direito, canto superior esquerdo, canto superior direito, canto inferior esquerdo, canto inferior direito.

 Especifique os caracteres na border string usando uma das formas a seguir e separe-os com vírgulas:

 Caracteres literais entre delimitadores de cadeia (aspas simples ou duplas ou colchetes).

 @ 1,10 TO 22,45 '=', '=', '|', '|', '+', '+', '+', '+'

 Expressões de caractere ou variáveis delimitadas com vírgulas.

 STORE '=' TO END

 STORE '|' TO SIDE

 STORE '+' TO CORNER

 @ 1,10 TO 22,45 END,END,SIDE,SIDE,CORNER,CORNER,CORNER,CORNER

 O valor ASCII dos caracteres especificados em funções CHR().

 STORE CHR(61) TO END

 STORE CHR(124) TO SIDE

 STORE CHR(43) TO CORNER

 @ 1,10 TO 22,45 END,END,SIDE,SIDE,CORNER,CORNER,CORNER,CORNER

 @ 1,10 TO 22,45 CHR(61),CHR(61),CHR(124),CHR(124);

 CHR(43),CHR(43),CHR(43),CHR(43)

 Você pode desenhar a caixa com um único caractere incluindo o caractere superior e omitindo os caracteres restantes. Este exemplo desenha uma caixa usando asteriscos:

 STORE '*' TO BOX_CHAR

 @ 1,10 TO 22,45 BOX_CHAR

 -------------------------------

 Observação - Se SET BORDER está definido como NONE e você não inclui DOUBLE, PANEL ou uma border string, a caixa é desenhada sem borda.

 -------------------------------

 PATTERN expN1

 PATTERN aceita um argumento numérico de 0 a 7 que especifica o padrão que preenche o objeto. Este argumento numérico corresponde aos padrões de preenchimento disponíveis para um objeto com o Screen Builder.

 -------------------------------

 Observação - O padrão é desenhado na cor de fundo, então você deve incluir a cláusula COLOR com uma cor de fundo diferente para tornar o padrão visível.

 -------------------------------

 expN1 Padrão

 ------- -------

 0 Nenhum

 1 Sólido

 2 Linhas horizontais

 3 Linhas verticais

 4 Diagonais para frente

 5 Diagonais para trás

 6 Trama cruzada

 7 Trama cruzada inclinada

 A cláusula PATTERN é ignorada no FoxPro para MS-DOS.

 PEN expN2 [, expN3]

 Inclua a cláusula PEN para especificar o contorno de um objeto. A largura da caneta usada para desenhar o contorno é especificada com expN2, e o tipo de caneta é especificado com expN3. Observe que uma linha de 1 ponto é sempre criada se você incluir expN3 para especificar um tipo de caneta.

 A tabela a seguir lista valores para expN2 e expN3 e as larguras e tipos de caneta correspondentes.

 expN2 Largura da caneta

 ------- ---------

 0 Hairline*

 1 1-point*

 2 2-point

 3 3-point

 4 4-point

 5 5-point

 6 6-point

 * Linhas desenhadas com as canetas hairline e 1-point podem ser exibidas com 1 ponto de largura com alguns drivers de exibição e hardware.

 expN3 Tipo de caneta

 ------- --------

 0 Nenhum

 1 Pontilhado

 2 Tracejado

 3 Traço-ponto

 4 Traço-ponto-ponto

 100 Retângulo 3-D

 A cláusula PEN é ignorada no FoxPro para MS-DOS.

 No FoxPro para Macintosh, apenas linhas sólidas e pontilhadas são suportadas; incluir 1, 2, 3 ou 4 cria uma linha pontilhada. O tipo de caneta 100 é suportado apenas no FoxPro para Macintosh e cria retângulos tridimensionais. Quando você inclui 100 para o tipo de caneta, quaisquer cláusulas adicionais que incluir (PATTERN, STYLE, COLOR, etc.) são ignoradas.

 STYLE expC

 O tipo de objeto criado (retângulo, retângulo arredondado, círculo ou elipse) é especificado por expC. Objetos criados com @ ... TO são opacos por padrão; inclua T em expC para criar um objeto transparente.

 Inclua um número de 0 a 99 em expC para especificar a curvatura da borda do objeto: 0 especifica nenhuma curvatura e cria cantos quadrados; 99 especifica a curvatura máxima e cria círculos e elipses.

A cláusula STYLE é ignorada no FoxPro para MS-DOS.

 COLOR SCHEME expN4 | COLOR color pair list

 A cor do objeto que você cria com @ ... FILL pode ser especificada incluindo o número de um esquema de cores existente na cláusula COLOR SCHEME ou um conjunto de pares de cores na cláusula COLOR.

 Um esquema de cores é um conjunto de 10 pares de cores predefinidos. Os pares de cores em um esquema de cores podem ser alterados com SET COLOR OF SCHEME. No FoxPro para MS-DOS, os pares de cores em um esquema de cores também podem ser alterados no Color Picker.

 Um par de cores é um conjunto de duas letras separadas por uma barra. A primeira letra especifica a cor de primeiro plano e a segunda letra especifica a cor de fundo.

 Por exemplo, este par de cores especifica um primeiro plano vermelho em um fundo branco:

 R/W

 Para uma lista de cores e suas letras de cor correspondentes, consulte SET COLOR Commands Overview ou Color Table by Color Pair.

 Um par de cores também pode ser especificado com um conjunto de seis valores RGB (Red Green Blue) separados por vírgulas. Os três primeiros valores de cor especificam a cor de primeiro plano e os três últimos valores de cor especificam a cor de fundo. Os valores de cor podem variar de 0 a 255.

 O par de cores R/W no exemplo acima também pode ser especificado com este par de cores RGB:

 RGB(255,0,0,255,255,255)

 Apenas o primeiro par de cores no esquema de cores especificado ou na lista de pares de cores determina a cor do objeto.

 A primeira cor no par de cores é a cor da caneta, a segunda cor é a cor de preenchimento. Por exemplo, o seguinte cria uma elipse com um interior vermelho sólido e um contorno azul:

 @ 2,2 TO 12,22 STYLE '99' ;

 PATTERN 1 PEN 2 COLOR 'B/R'

 Se você omitir a cláusula color, a porção retangular é limpa. Uma área também pode ser limpa com @ ... CLEAR.

# Observações

Use este comando para desenhar uma caixa. Se você omitir as cláusulas opcionais, a caixa é desenhada com uma linha simples para a borda e as cores atuais.

No FoxPro para Windows e FoxPro para Macintosh, você pode desenhar retângulos, retângulos arredondados, círculos e elipses incluindo as cláusulas PATTERN, PEN e STYLE. Essas cláusulas são opcionais e podem ser incluídas em qualquer combinação. Se uma cláusula PATTERN, PEN ou STYLE é incluída com uma cláusula DOUBLE ou PANEL, a cláusula DOUBLE ou PANEL é ignorada.

A cláusula PATTERN especifica um padrão de preenchimento para objetos desenhados. A cláusula PEN especifica a largura e o tipo do contorno de um objeto. STYLE permite criar um objeto transparente ou opaco e especificar a curvatura para bordas de retângulo, círculos e elipses.

Importante No FoxPro para Windows e FoxPro para Macintosh, se FoxFont é a fonte atual e as cláusulas PATTERN, PEN e STYLE não são incluídas, retângulos são desenhados com os caracteres de desenho de caixa FoxFont. Isso fornece compatibilidade com versões anteriores do FoxPro.

Se FoxFont não é a fonte atual, ou se FoxFont é a fonte atual e uma cláusula PATTERN, PEN ou STYLE é incluída, retângulos são desenhados usando gráficos. Um retângulo desenhado com os caracteres de desenho de caixa FoxFont e o mesmo retângulo desenhado com gráficos são desenhados em posições ligeiramente diferentes.
