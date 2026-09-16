# Propriedade Picture (Visual FoxPro)

Especifica uma imagem a ser exibida em um controle ou objeto. Disponível em tempo de design e em tempo de execução.

> **Observação:** Em tempo de design, se você definir a propriedade Picture para um arquivo que não existe, o Visual FoxPro exibe a mensagem apropriada, mas a propriedade permanece definida para o arquivo especificado. Em tempo de execução, se a propriedade Picture estiver definida para um arquivo que não existe, o Visual FoxPro ignora a propriedade Picture.

```foxpro
Control.Picture [ = cFileName ]
-Or
Control.Picture(nIndex) [ = cFileName ]
```

#### Parâmetros
 **cFileName**
Especifica o nome de um arquivo gráfico. Observação O Visual FoxPro suporta todos os formatos de arquivo gráfico tratados pelo Graphics Device Interface+ (GDI+). O Visual FoxPro suporta arquivos .gif animados para a propriedade Picture somente em um controle Image. Para obter mais informações sobre formatos de arquivo gráfico válidos, consulte Graphics Support in Visual FoxPro .
**nIndex**
Especifica um inteiro correspondente à ordem em que os itens são exibidos no controle. Para o primeiro item em um controle, nIndex = 1.

# Observações

Aplica-se a: CheckBox Control | CommandButton Control | ComboBox Control | Container Object | Control Object (Visual FoxPro) | Custom Object | Form Object | Header Object | Image Control (Visual FoxPro) | ListBox Control | OptionButton Control | Page Object | _SCREEN System Variable |

Em controles, as imagens aparecem centralizadas. Em formulários, a imagem é exibida como plano de fundo do formulário. Se a propriedade RowSourceType estiver definida como 7 (Files), imagens não são suportadas.

Para controles CommandButton e OptionButton, a imagem especificada é usada independentemente de o botão estar disponível, selecionado ou indisponível. Você pode especificar uma imagem diferente para cada estado do botão definindo as propriedades DownPicture e DisabledPicture.

Para controles CommandButton, CheckBox e OptionButton, você deve definir a propriedade Style para o controle correspondente. A tabela a seguir lista os valores que você deve definir para a propriedade Style do controle correspondente.

| Control | Style property |
| --- | --- |
| CommandButton | 0 (Standard) |
| CheckBox , OptionButton | 1 (Graphical) |

Para objetos Header, se o cabeçalho não contiver uma legenda, a imagem aparece no centro do cabeçalho. Se o cabeçalho contiver uma legenda, a propriedade Header Alignment determina como a imagem se alinha com o texto da legenda. Se Header Alignment estiver definido como left ou center, a imagem aparece à direita da legenda. Se Alignment estiver definido como right, a imagem aparece à esquerda da legenda.

Para objetos ToolBar, as dimensões recomendadas da imagem são 16 x 15 pixels (largura x altura).

Para controles ComboBox e ListBox, você pode usar a propriedade Picture como propriedade de valor único ou como matriz. Se você usar Picture como propriedade de valor único, todos os itens no controle mostram a mesma imagem. Se você usar Picture como matriz, que armazena uma imagem para cada item na lista, cada item pode ter uma imagem diferente. Por exemplo:

```foxpro
oCombobox.AddItem("Home")
oCombobox.AddItem("Community")
oCombobox.AddItem("Web Services")
oCombobox.Picture[1] = 'home.bmp'
oCombobox.Picture[2] = 'community.bmp'
oCombobox.Picture[3] = 'websvc.bmp'
```

Para controles Image, CheckBox e CommandButton, a propriedade Picture respeita a transparência da imagem.

> **Observação:** Para imagens GIF transparentes de alta resolução, o aspecto de transparência da imagem é suportado somente para o controle Image. Como o Visual FoxPro armazena apenas uma instância dessa imagem como recurso para uso interno, é possível usar essa imagem em outro controle, como um CommandButton, e manter a transparência. Para fazer isso, você primeiro precisa carregar a imagem em um controle Image e persistir esse controle (talvez oculto). Depois que a imagem foi carregada como recurso pelo controle Image, ela pode ser usada pelo CommandButton.
