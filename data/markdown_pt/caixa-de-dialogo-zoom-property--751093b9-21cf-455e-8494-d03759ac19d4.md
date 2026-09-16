# Caixa de diálogo Zoom <property>

Exibe o valor de texto da propriedade selecionada. Esta caixa de diálogo aparece ao escolher Zoom no menu de atalho da janela Properties ou no botão Zoom.

A caixa de diálogo Zoom permite editar valores de propriedades de leitura/gravação, exceto propriedades como Visible ou ColorSource. Você não pode editar o valor de uma propriedade somente leitura na caixa de diálogo Zoom; no entanto, pode selecionar e copiar o valor.

> **Dica:** No Visual FoxPro 9.0, você pode inserir mais de 255 caracteres (limitado a 8k), bem como caracteres estendidos, como CHR(13) (retorno de carro) e CHR(10) (avanço de linha), na caixa de diálogo Zoom para propriedades personalizadas definidas pelo usuário e certas propriedades nativas. Para obter mais informações sobre valores de propriedade estendidos, consulte Properties Window (Visual FoxPro).

> **Cuidado:** Valores de propriedade que excedem 255 caracteres ou incluem caracteres estendidos como CHR(13) (retorno de carro) ou CHR(10) (avanço de linha) são armazenados em um formato especial dentro do arquivo de biblioteca de classes (.vcx) ou formulário (.scx). O valor da propriedade conterá preenchimento especial com caracteres CHR(1). Esteja ciente de que classes em bibliotecas de classes visuais (.vcx) ou formulários (.scx) que contêm propriedades com esses valores não podem ser usadas em versões anteriores ao Visual FoxPro 9.0. Se você tentar modificar essas em uma versão anterior, ocorrerá um erro. Você ainda pode usar outras classes nos mesmos arquivos de biblioteca de classes visual (.vcx) com versões anteriores do Visual FoxPro, desde que não contenham valores de propriedade que excedam 255 caracteres ou incluam caracteres de retorno de carro ou avanço de linha.
