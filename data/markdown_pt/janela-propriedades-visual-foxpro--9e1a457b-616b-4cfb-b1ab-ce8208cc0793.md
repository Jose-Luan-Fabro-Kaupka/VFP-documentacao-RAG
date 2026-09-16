# Janela Propriedades (Visual FoxPro)

Exibe propriedades, eventos e métodos e suas configurações quando disponíveis para um objeto selecionado.

> **Observação:** Os nomes de propriedades que são somente leitura e não podem ser editadas aparecem em itálico na lista de propriedades.

Para obter informações sobre como definir valores para propriedades, eventos e métodos de objetos, consulte Como: definir propriedades para objetos. Para comandos de atalho de teclado, consulte Atalhos de teclado (Visual FoxPro).

# Lista de objetos

Mostra o objeto atualmente selecionado e exibe uma lista de objetos disponíveis quando você clica na seta à direita da lista. Esta lista inclui o formulário atual, conjunto de formulários e todos os controles no formulário.

Se o Data Environment Designer estiver aberto, a lista de objetos inclui o ambiente de dados e todos os cursores e relacionamentos no ambiente de dados.

# Guias

Exibe propriedades, eventos e métodos por categoria:
 - All Todas as propriedades, eventos e métodos.
- Data Propriedades associadas a como os dados são exibidos ou manipulados pelo objeto.
- Methods Métodos e eventos.
- Layout Todas as propriedades de layout.
- Other Propriedades diversas e definidas pelo usuário.
- Favorites Suas propriedades, eventos e métodos favoritos. Para adicionar uma propriedade, evento ou método à guia Favorites, clique com o botão direito na propriedade, evento ou método e escolha Add to Favorites. Propriedades, eventos e métodos também podem ser adicionados programaticamente à guia Favorites. Consulte MemberData Extensibility para obter mais informações.

# Caixa de configurações de propriedade

Permite alterar o valor de uma propriedade de leitura/gravação quando selecionada na lista de propriedades.

> **Dica:** Se a propriedade selecionada tem configurações predefinidas, a caixa de configurações de propriedade contém uma lista de configurações das quais você pode escolher. Para abrir a lista, clique na seta à direita da caixa de configurações de propriedade.

> **Dica:** Você pode navegar pelas configurações clicando duas vezes no nome da propriedade na lista de propriedades. Se a configuração requer um nome de arquivo ou uma cor, clique no botão de reticências (...) para exibir a caixa de diálogo ou janela apropriada para selecionar um arquivo ou cor.

> **Observação:** A caixa de configurações de propriedade, Cancel e os botões Accept não estão disponíveis se o valor de uma propriedade exceder 255 caracteres ou contiver caracteres estendidos. Para editar a configuração da propriedade, use a caixa de diálogo Zoom ou o Expression Builder.

Os seguintes botões aparecem à esquerda da caixa de configurações de propriedade:
 - Cancel ( X ) Cancela as alterações que você fez na configuração e restaura o valor original.
- Accept ( símbolo de verificação) Confirma as alterações que você fez em uma configuração.
- Function ( símbolo Fx) Abre o Expression Builder. O botão Function está disponível quando o valor da propriedade é uma expressão. Você pode definir valores literais ou valores retornados por funções ou expressões. Para obter mais informações, consulte Caixa de diálogo Expression Builder .
- Zoom ( Z ) Abre a caixa de diálogo Zoom para que você possa editar o valor de uma propriedade de leitura/gravação. Para certos tipos de propriedades, o Visual FoxPro 9.0 fornece suporte para especificar valores que excedem 255 caracteres (limitado a 8K caracteres) diretamente na Janela Propriedades via a caixa de diálogo Zoom. Além disso, esses valores podem incluir retornos de carro e quebras de linha. Este suporte é limitado a propriedades personalizadas definidas pelo usuário, bem como a certas propriedades nativas. Propriedades nativas comuns que suportam valores estendidos incluem Value, Text, DisplayValue, UserValue, PictureVal, CommandClauses, _MemberData, CursorSchema, DataSource, bem como propriedades das classes CursorAdapter e XMLAdapter relacionadas a especificar uma fonte de dados, lista de campos ou comando. Dica Você pode determinar se uma propriedade suporta valores estendidos abrindo a caixa de diálogo Zoom para essa propriedade. Se a caixa de diálogo não incluir um botão Apply e você puder digitar um retorno de carro, então você selecionou uma propriedade que suporta valores estendidos. Observação Você ainda pode especificar valores estendidos para propriedades que não os suportam diretamente na caixa de diálogo Zoom definindo seu valor em código, como no evento Init desse objeto. Observe que valores digitados na caixa de diálogo Zoom que excedem 255 caracteres para propriedades que não suportam valores estendidos serão truncados quando a classe for salva. Cuidado Valores de propriedade que excedem 255 caracteres ou incluem caracteres estendidos como CHR(13) (retorno de carro) ou CHR(10) (quebra de linha) são armazenados em um formato especial dentro da biblioteca de classes (.vcx) ou arquivo de formulário (.scx). O valor da propriedade conterá preenchimento especial com caracteres CHR(1). Esteja ciente de que classes em bibliotecas de classes visual (.vcx) ou formulários (.scx) que contêm propriedades com esses valores não podem ser usadas em versões anteriores ao Visual FoxPro 9.0. Se você tentar modificar essas em uma versão anterior, ocorre um erro. Você ainda pode usar outras classes nos mesmos arquivos de biblioteca de classes visual (.vcx) com versões anteriores do Visual FoxPro, desde que não contenham valores de propriedade que excedam 255 caracteres ou incluam caracteres de retorno de carro ou quebra de linha. O botão Zoom pode não estar disponível para algumas propriedades. Para obter mais informações, consulte Caixa de diálogo Zoom <propriedade> .

# Lista de propriedades

Esta lista mostra todas as propriedades que podem ser alteradas em tempo de design e suas configurações atuais. Para obter Ajuda para uma propriedade específica, selecione a propriedade e pressione F1.

As configurações de propriedade na lista de propriedades podem aparecer da seguinte forma:
 - Configurações de propriedade que são expressões são precedidas por um sinal de igual (=).
- Configurações para propriedades, eventos e métodos que são somente leitura aparecem em itálico.
- Métodos e eventos exibem detalhes de herança da seguinte forma: Default -ou- Inherited cClassname ClassLibrary Para obter mais informações sobre como visualizar código herdado para um método ou evento, consulte Como: exibir código herdado para objetos, eventos e métodos .
