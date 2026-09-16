# Exemplo de impressão em formato de catálogo

Arquivo: ...\Samples\Solution\Reports\Wrapping.frx

O relatório de exemplo Wrapping.frx imprime um diretório de funcionários e mostra como você pode envolver texto em torno de gráficos, alternar a posição de impressão dos controles e flutuar controles abaixo de campos que se expandem. O ambiente de dados deste relatório contém a tabela EMPLOYEE do Testdata.dbc no projeto Solution.

# O layout do relatório

A banda Title contém o nome e a descrição do relatório. A banda Detail contém os controles de campo e etiqueta que imprimem para cada registro. Para cada registro, o relatório exibe as seguintes quatro categorias de informações:
 - Nome e cargo do funcionário
- Biografia
- Caixa de informações de referência rápida, como telefone e endereço
- Fotografia

Após imprimir o nome e o cargo, este relatório envolve o texto da biografia em torno da fotografia, alterna informações da esquerda para a direita e flutua a caixa pela página em relação à biografia.

# Envolver texto em torno de gráficos

Para envolver o campo memo em torno da imagem, o relatório usa dois controles de campo para exibir o conteúdo do campo memo. O primeiro controle está acima da imagem para exibir duas linhas de texto. O segundo campo também tem tamanho para mostrar duas linhas de texto, mas é mais estreito e posicionado ao lado da imagem.

O primeiro controle de campo imprime todas as palavras do campo memo até a posição em que deve ocorrer uma quebra para continuar as palavras no segundo controle. A expressão é mostrada abaixo.

```foxpro
LEFTC(employee.notes,nWrapCharPos)
```

O segundo controle de campo imprime as palavras restantes do campo memo. A expressão para o segundo controle de campo é mostrada abaixo.

```foxpro
LTRIM(RIGHTC(employee.notes,(nMemoLen-(nWrapCharPos))))
```

As expressões dos controles usam variáveis de relatório para determinar as palavras que os controles exibem do campo memo.
 - nFirstMemoLen determina o número de caracteres que podem ser exibidos no primeiro campo sem truncamento. Para este relatório, o valor da variável é sempre 185. Se você usar isso no seu próprio relatório, precisará alterar essa constante para corresponder ao número máximo de caracteres que deseja acima da imagem.
- nMemoLen determina o comprimento do campo memo para o registro atual. A expressão desta variável é LENC (employee.notes).
- nSpace determina a posição do caractere do primeiro espaço após os caracteres exibidos no primeiro controle. A expressão desta variável é AT_C(CHR(32),RIGHTC(employee.notes,(nMemoLen - nFirstMemoLen))).
- nWrapCharPos determina a posição do caractere dentro do campo memo onde a quebra deve ocorrer. A expressão desta variável é nSpace + nFirstMemoLen.

# Alternar a posição dos objetos impressos

Neste relatório, as posições da biografia do funcionário, do grupo de referência rápida e da fotografia alternam da esquerda para a direita em cada registro. Para alternar as posições, o relatório tem dois conjuntos de controles para as partes do relatório que alternam. Como dois controles são usados para envolver o texto da biografia, o primeiro controle não alterna e, portanto, não precisa ser incluído nos dois conjuntos.

Um conjunto de controles especifica a impressão com a fotografia no lado esquerdo. Um segundo conjunto especifica a impressão com a fotografia no lado direito. Os controles em ambos os conjuntos usam uma variável de relatório, nCounter, que calcula uma contagem que determina quando o conjunto deve imprimir. Um conjunto imprime quando o valor de nCounter é 0; o outro quando o valor é 1. A expressão Print When para o primeiro conjunto de controles é `MOD(nCounter,2) = 0`. Para o segundo conjunto, a expressão é `MOD(nCounter,2) = 1`.

# Flutuar controles abaixo de controles que se expandem

Este relatório imprime a caixa de informações que imprime abaixo da biografia. Como o comprimento da biografia varia com cada registro, o controle que exibe as informações da biografia ao lado da imagem é definido para expandir e usa apenas o espaço necessário para imprimir o conteúdo do campo. A caixa que imprime abaixo da biografia flutua pela página dependendo do comprimento da biografia. Esta caixa é um grupo de controles de campo, etiqueta e retângulo. Para evitar que a biografia imprima sobre o grupo, a posição do campo de cada um dos controles no grupo é definida para flutuar.
