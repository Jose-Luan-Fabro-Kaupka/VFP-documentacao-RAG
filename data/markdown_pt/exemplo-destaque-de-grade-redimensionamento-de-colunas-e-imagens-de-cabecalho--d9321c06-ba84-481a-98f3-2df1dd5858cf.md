# Exemplo Destaque de grade, redimensionamento de colunas e imagens de cabeçalho

Arquivo: ...\Samples\Solution\Toledo\Griders.scx

Este exemplo demonstra como você pode executar as seguintes ações:
 - Selecionar estilo e cores para destaque de grade.
- Redimensionar colunas automaticamente para a largura dos dados na coluna.
- Bloquear a primeira coluna da grade para que ela não role.
- Especificar imagens nos cabeçalhos de coluna.

# Selecionando estilos de destaque de grade

Você pode usar estilos de destaque para controlar como o destaque aparece e se comporta em uma grade quando você seleciona linhas e o foco sai da grade. Para definir estilos de destaque, use a propriedade HighlightStyle do Grid.

No exemplo, para definir HighlightStyle, selecione um estilo na caixa de combinação no formulário. A caixa de combinação contém o seguinte código:

```foxpro
ThisForm.grdCustomers.HighlightStyle = VAL(this.Value)
```

Para obter mais informações sobre HighlightStyle, consulte Propriedade HighlightStyle.

Você também pode definir cores de destaque. Para obter mais informações, consulte Propriedade HighlightBackColor, Propriedade HighlightForeColor, Propriedade SelectedItemBackColor e Propriedade SelectedItemForeColor.

# Ajustando colunas à largura dos dados

Este exemplo redimensiona colunas de grade automaticamente para ajustar à largura dos dados na coluna usando o método AutoFit do Grid da seguinte forma:

```foxpro
ThisForm.grdCustomers.AutoFit()
```

Você também pode redimensionar colunas de grade clicando duas vezes no canto superior esquerdo da grade. Para redimensionar uma coluna individual automaticamente, clique duas vezes na linha divisória no lado direito da coluna. Você pode controlar este comportamento usando a propriedade AllowAutoColumnFit do Grid.

Para obter mais informações, consulte Método AutoFit e Propriedade AllowAutoColumnFit.

# Bloqueando colunas de grade

Você pode bloquear colunas para que permaneçam fixas ao rolar horizontalmente em uma grade usando a propriedade LockColumns do Grid.

No exemplo, você pode bloquear a primeira coluna na grade definindo `grdCustomers.LockColumns` como 1 como no seguinte código:

```foxpro
ThisForm.grdCustomers.LockColumns = 1
```

Você também pode bloquear a coluna Customer ID clicando no cabeçalho da coluna. O alfinete no cabeçalho da coluna indica se a coluna está bloqueada. Para bloquear colunas individuais, clique com o botão direito na área entre os cabeçalhos de coluna.

Para obter mais informações, consulte Propriedade LockColumns e Propriedade LockColumnsLeft.

# Exibindo imagens nos cabeçalhos de coluna

Você pode especificar uma imagem para um cabeçalho de coluna usando a propriedade Picture e definir a orientação da imagem usando a propriedade Alignment do cabeçalho.

No exemplo, uma imagem aparece no cabeçalho da coluna Nome da empresa para indicar a direção da ordem de classificação na coluna. Clicar no cabeçalho da coluna exibe imagens diferentes para indicar ordem de classificação ascendente ou descendente.

Para obter mais informações, consulte Propriedade Picture (Visual FoxPro) e Propriedade Alignment.
