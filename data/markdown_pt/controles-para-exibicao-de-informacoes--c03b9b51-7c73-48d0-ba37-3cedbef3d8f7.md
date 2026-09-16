# Controles para exibição de informações

Um dos princípios de bom design é tornar visíveis as informações relevantes. Você pode usar os seguintes controles para exibir informações aos seus usuários:
 - Images
- Labels
- Text Boxes
- Edit Boxes
- Shapes

# Usando Images

O controle Image permite adicionar imagens (.bmp e outros arquivos gráficos) ao seu formulário. Um controle Image tem o conjunto completo de propriedades, eventos e métodos que outros controles possuem; portanto, um controle Image pode ser alterado dinamicamente em tempo de execução. Os usuários podem interagir com imagens clicando, clicando duas vezes e assim por diante. Para detalhes sobre tipos de arquivo gráfico válidos, consulte Suporte a gráficos no Visual FoxPro.

A tabela a seguir lista algumas das propriedades principais de um controle Image.

| Propriedade | Descrição |
| --- | --- |
| Picture | A imagem (arquivo .bmp) a ser exibida. |
| BorderStyle | Se há uma borda visível para a imagem. |
| Stretch | Se Stretch estiver definido como 0 – Clip, partes da imagem que se estendem além das dimensões do controle Image não são exibidas. Se Stretch estiver definido como 1 - Isometric, o controle Image preserva as dimensões originais da imagem e exibe o máximo possível da imagem que as dimensões do controle Image permitirem. Se Stretch estiver definido como 2 - Stretch, a imagem é ajustada para corresponder exatamente à altura e largura do controle Image. |

# Usando Labels

Labels diferem de text boxes porque:
 - Não podem ter uma fonte de dados.
- Não podem ser editados diretamente.
- Não podem receber foco por tabulação.

Você pode alterar programaticamente as propriedades Caption Property (Visual FoxPro) e Visible Property (Visual FoxPro) de labels para adaptar a exibição da label à situação em questão.

# Propriedades comuns de Label

As propriedades de label a seguir são comumente definidas em tempo de design.

| Propriedade | Descrição |
| --- | --- |
| Caption | O texto exibido pela label. |
| AutoSize | Se o tamanho da label é ajustado ao comprimento do Caption. |
| BackStyle | Se a label é Opaque ou Transparent. |
| WordWrap | Se o texto exibido na label pode quebrar em linhas adicionais. |

# Usando Text e Edit Boxes para exibir informações

Defina a propriedade ReadOnly de text e edit boxes para exibir informações que o usuário pode visualizar, mas não editar. Se você apenas desabilitar um edit box, o usuário não conseguirá rolar pelo texto.

# Usando Shapes e Lines

Shapes e lines ajudam a agrupar visualmente elementos do seu formulário. Pesquisas mostraram que associar itens relacionados ajuda os usuários a aprender e entender uma interface, o que facilita o uso do seu aplicativo.

As propriedades Shape a seguir são comumente definidas em tempo de design.

| Propriedade | Descrição |
| --- | --- |
| Curvature | Um valor entre 0 (ângulos de 90 graus) e 99 (círculo ou oval). |
| FillStyle | Se a forma é transparente ou tem um padrão de preenchimento de fundo especificado. |
| SpecialEffect | Se a forma é simples ou 3D. Isso só tem efeito quando a propriedade Curvature está definida como 0. |

As propriedades Line a seguir são comumente definidas em tempo de design.

| Propriedade | Descrição |
| --- | --- |
| BorderWidth | Quantos pixels de largura tem a linha. |
| LineSlant | Quando a linha não é horizontal ou vertical, a direção da inclinação. Os valores válidos para esta propriedade são uma barra ( / ) e uma barra invertida ( \ ). |

# Usando gráficos de formulário para exibir informações

Você pode exibir informações graficamente em um formulário usando os seguintes métodos de formulário.

| Método | Descrição |
| --- | --- |
| Circle | Desenha uma figura circular ou arco em um formulário. |
| Cls | Limpa gráficos e texto de um formulário. |
| Line | Desenha uma linha em um formulário. |
| Pset | Define um ponto em um formulário para uma cor específica. |
| Print | Imprime uma cadeia de caracteres em um formulário. |

Para ver exemplos que demonstram gráficos de formulário, execute Solution.app no diretório Visual FoxPro ...\Samples\Solution. Na visualização em árvore, clique em Forms e depois em Form graphics.
