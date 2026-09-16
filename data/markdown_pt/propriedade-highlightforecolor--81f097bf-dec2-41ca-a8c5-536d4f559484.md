# Propriedade HighlightForeColor

Especifica a cor de primeiro plano ou de destaque do texto em uma linha de Grid quando ela está selecionada. A propriedade HighlightForeColor de uma grid se aplica somente quando a propriedade HighlightStyle da grid está definida com um valor maior que 0. Leitura/gravação em tempo de design e de execução.

```foxpro
Grid.HighlightForeColor [= nColor ]
```

#### Parâmetros
 **nColor**
Tipo de dados numérico. HighlightForeColor especifica um inteiro que representa um valor de cor único. O Visual FoxPro deriva a configuração de cor padrão da configuração de cor da fonte do sistema operacional Windows para Selected Items. Para informações sobre valores de cor válidos, consulte BackColor, ForeColor Properties.

# Observações

Aplica-se a: Grid Control | BROWSE Command

No Windows XP, você pode encontrar a configuração de cor da fonte Selected Items na caixa de diálogo Advanced Appearance. Para abrir a caixa de diálogo Advanced Appearance, clique com o botão direito na área de trabalho do Windows e clique em Properties. Na caixa de diálogo Display Properties, clique na guia Appearance, depois em Advanced e selecione Selected Items na lista Item. A cor da fonte do sistema operacional é especificada na caixa Color à direita da caixa Font.

No Windows 2000, você pode definir a cor da fonte para informações Selected Items na guia Appearance.

> **Observação:** Alterar a cor da fonte para Selected Items altera a configuração para todas as aplicações.

Você pode selecionar uma cor digitando o valor RGB na caixa de configurações de propriedades da janela Properties ou exibir a caixa de diálogo Color clicando duas vezes na propriedade na lista de propriedades da janela Properties. O valor RGB da cor selecionada na caixa de diálogo Color torna-se a configuração depois que você fecha a caixa de diálogo Color.

Depois de definir HighlightStyle com um valor maior que 0, o destaque permanece em vigor até que HighlightStyle seja definido como 0. Se HighlightStyle estiver definido com o valor 2, somente as cores de destaque persistem. Itens selecionados são exibidos somente quando uma grid tem o foco.

O destaque afeta todas as células em uma linha, exceto a atualmente selecionada, a menos que a propriedade AllowCellSelection da grid esteja definida como False (.F.), e substitui configurações de propriedades de cor como BackColor e DynamicBackColor para qualquer coluna na grid.

O exemplo a seguir mostra como você pode intercambiar as cores Selected Items e Selected Items font do Windows para HighlightForeColor e HighlightBackColor:

```foxpro
tmpColor1 = THIS.GrdCustomer.HighlightBackColor
tmpColor2 = THIS.GrdCustomer.HighlightForeColor
THIS.GrdCustomer.HighlightBackColor = tmpColor2
THIS.GrdCustomer.HighlightForeColor = tmpColor1
```
