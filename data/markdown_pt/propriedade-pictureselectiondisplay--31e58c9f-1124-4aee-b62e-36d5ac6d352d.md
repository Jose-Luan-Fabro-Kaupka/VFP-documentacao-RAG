# Propriedade PictureSelectionDisplay

Especifica como uma imagem aparece na porção de caixa de texto de um controle ComboBox.

> **Observação:** Você pode especificar uma imagem definindo a propriedade Picture do controle para um nome de arquivo de imagem.

```foxpro
Combobox.PictureSelectionDisplay = nExpr
```

#### Parâmetros
 **nExpr**
Tipo de dados numérico. A tabela a seguir lista os valores de nExpr. nExpr Descrição 0 (None) Não exibe a imagem na caixa de texto de um combo box. (Padrão) 1 (Clip) A imagem é recortada para a mesma altura da caixa de texto de um combo box. A largura da imagem permanece a mesma. 2 (Isometric) A imagem é redimensionada para caber na altura da caixa de texto de um combo box, mantendo suas proporções originais. 3 (Stretch) A imagem é redimensionada para caber na altura da caixa de texto de um combo box, mas não mantém suas proporções originais. A largura da imagem permanece a mesma.

# Observações

Aplica-se a: ComboBox Control

Se a propriedade Style do combo box estiver definida como 0 (Drop-down ComboBox), as imagens são exibidas na caixa de texto do combo box com o seguinte comportamento:
 - Quando a porção de lista do combo box não está visível e você está digitando texto diretamente no combo box, a imagem padrão, se especificada, aparece até que o texto corresponda a um item na lista. Se não existir correspondência, a imagem padrão aparece mesmo quando o controle perde o foco.
- A propriedade Margin do combo box especifica o espaçamento do texto, além do preenchimento, a partir das bordas esquerda e superior da caixa de texto. Quando uma imagem aparece na caixa de texto, a propriedade Margin especifica o espaçamento entre as bordas da imagem e as bordas esquerda e superior da caixa de texto. O espaçamento horizontal entre a borda direita da imagem e o texto é sempre de quatro pixels, independentemente da configuração da propriedade Margin do combo box. O cursor de texto aparece a dois pixels da borda direita da imagem. Você pode inserir espaço adicional fornecendo uma imagem contendo espaço em branco. Observação Mesmo se Margin estiver definido como 0, existe um espaço de três pixels a partir das bordas esquerda e superior para fornecer espaço para o cursor de texto. Especificar um valor para Margin adiciona pixels a esse preenchimento. No entanto, se uma imagem aparecer, Margin afeta apenas a margem entre a borda superior da caixa de texto e o texto. A margem esquerda do texto sempre aparece a quatro pixels da imagem para manter o alinhamento dos itens dentro da lista.

Se a propriedade Style do combo box estiver definida como 2 (Drop-down List), as imagens são exibidas na caixa de texto do combo box com dois pixels de espaçamento horizontal entre a borda direita da imagem e o texto.
