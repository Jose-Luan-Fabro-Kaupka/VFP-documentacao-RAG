# Propriedade SelectedItemBackColor

Especifica a cor de fundo para um item selecionado em um ComboBox ou ListBox ou célula (somente TextBox) em um controle Grid. SelectedItemBackColor está relacionada às propriedades HighlightForeColor e HighlightBackColor no sentido de que você precisa controlar a cor da célula selecionada em uma linha do Grid. Leitura/gravação em tempo de design e em tempo de execução. Há duas versões da sintaxe.

```foxpro
Control.SelectedItemBackColor [= nColor ]
```

```foxpro
Control.SelectedItemBackColor = RGB( nRedValue, nGreenValue, nBlueValue )
```

#### Parâmetros
 **nColor**
Tipo de dados Numeric. SelectedItemBackColor especifica um inteiro representando um único valor de cor. O Visual FoxPro deriva a configuração de cor padrão da configuração de cor do sistema operacional Windows para Selected Items. Para informações sobre valores de cor válidos, consulte Propriedades BackColor, ForeColor .

# Observações

Aplica-se a: Controle ComboBox | Controle ListBox | Controle Grid

Você pode encontrar a configuração de cor Selected Items na caixa de diálogo Advanced Appearance, que você pode abrir acessando o menu Iniciar, abrindo o Painel de controle, selecionando Display, clicando na guia Appearance, clicando em Advanced e selecionando Selected Items na lista suspensa Item.

Você também pode definir cores inserindo o valor RGB para a propriedade na janela Properties ou escolher cores dando um duplo clique na propriedade na janela Properties para exibir a caixa de diálogo Cor. Os valores de cor vermelho, verde e azul correspondentes à cor que você escolhe tornam-se as configurações para essas propriedades depois que você fecha a caixa de diálogo Cor.

No nível do controle Grid, SelectedItemBackColor e SelectedItemForeColor se aplicam somente a controles TextBox. Embora uma coluna do Grid possa conter muitos tipos diferentes de objetos, apenas o controle TextBox padrão é suportado. Você deve definir SelectedItemBackColor e SelectedItemForeColor individualmente no nível do controle para outros controles. A prioridade das configurações SelectedItemBack e SelectedItemForeColor do Grid sobre o comportamento de um controle TextBox específico na coluna é determinada da seguinte forma:
 - Quando Grid HighlightStyle está definido como 0, SelectedItemBackColor e SelectedItemForeColor do Grid são ignorados, e as propriedades da caixa de texto têm precedência. Se Grid HighlightStyle está definido com um valor de 2, apenas as cores de destaque persistem, e os itens selecionados são exibidos somente quando uma grade tem foco.
- Quando Grid HighlightStyle está definido com um valor maior que 0, o seguinte comportamento se aplica: As propriedades do controle TextBox controlam as cores reais da caixa de texto selecionada. Quando SelectedItemBackColor e SelectedItemForeColor do Grid são explicitamente definidos, as propriedades correspondentes para todos os controles TextBox da grade são definidas. Isso ocorre em tempo de design e em tempo de execução. As configurações de propriedade da grade têm precedência sobre configurações de propriedade conflitantes da caixa de texto. Se você deseja que SelectedItemBackColor e SelectedItemForeColor do TextBox substituam as propriedades correspondentes da grade, defina as propriedades individuais da caixa de texto depois de definir as propriedades da grade. Dica Você pode criar uma rotina que executa esse processo, o que oferece flexibilidade caso as propriedades da grade mudem em tempo de execução. Ao definir as propriedades BackColor e ForeColor do TextBox para controlar como a caixa de texto é exibida quando clicada para edição, as propriedades SelectedItemBackColor e SelectedItemForeColor do Grid se comportam como se toda a célula estivesse selecionada.

Você pode redefinir as cores de uma grade e suas caixas de texto para suas configurações padrão de classe chamando o método ResetToDefault para as propriedades SelectedItemForeColor e SelectedItemBackColor do Grid e TextBox.

> **Observação:** Isso difere de como o Visual FoxPro trata outras configurações de cor de grade. Por exemplo, quando você chama ResetToDefault na propriedade BackColor de uma grade, as colunas e caixas de texto subjacentes são definidas para a propriedade BackColor padrão da grade e não para as propriedades BackColor padrão das colunas e caixas de texto.
