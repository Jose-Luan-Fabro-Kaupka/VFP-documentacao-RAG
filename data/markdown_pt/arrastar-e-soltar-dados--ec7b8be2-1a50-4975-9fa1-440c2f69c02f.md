# Arrastar e soltar dados

Compreender alguns dos fundamentos de aplicativos OLE de arrastar e soltar facilita aproveitar ao máximo seus recursos.

O mouse é usado para arrastar e soltar dados entre aplicativos e controles. Por exemplo, você pode selecionar um conjunto de arquivos no Windows Explorer. Você pode então pressionar e manter o botão do mouse pressionado enquanto arrasta os arquivos e depois soltar o botão do mouse para soltá-los no Project Manager do Visual FoxPro, ou pode selecionar texto em um documento Word e soltar o texto em uma caixa de texto em um formulário do Visual FoxPro. Durante a operação OLE de arrastar e soltar, o cursor do mouse muda para indicar que uma operação OLE de arrastar e soltar está em vigor.

# Origem de arrasto

O aplicativo ou controle do qual os dados são movidos é chamado de origem de arrasto.

A tabela a seguir lista as propriedades, eventos e métodos disponíveis para uma origem de arrasto OLE.

| Propriedade, evento ou método | Descrição |
| --- | --- |
| Evento OLECompleteDrag | Ocorre quando os dados são soltos no destino de soltar ou a operação OLE de arrastar e soltar é cancelada. |
| Método OLEDrag | Inicia uma operação OLE de arrastar e soltar. |
| Propriedade OLEDragPicture | Especifica a imagem exibida sob o ponteiro do mouse durante uma operação OLE de arrastar e soltar. Você pode especificar um arquivo de imagem do tipo .bmp, .dib, .jpg, .gif, .ani, .cur e .ico. |
| Propriedade OLEDragMode | Especifica como uma origem de arrasto gerencia operações de arrasto OLE. |
| Evento OLEGiveFeedBack | Ocorre após cada evento OLEDragOver. Permite que a origem de arrasto especifique o tipo de operação OLE de arrastar e soltar e o feedback visual. |
| Evento OLESetData | Ocorre quando um destino de soltar chama o método GetData e não há dados em um formato especificado no DataObject OLE de arrastar e soltar. |
| Evento OLEStartDrag | Ocorre quando o método OLEDrag é chamado. |

# Destino de soltar

O aplicativo ou controle para o qual os dados são movidos é chamado de destino de soltar.

A tabela a seguir lista as propriedades e eventos disponíveis para um destino de soltar OLE.

| Propriedade ou evento | Descrição |
| --- | --- |
| Evento OLEDragDrop | Ocorre quando os dados são soltos em um destino de soltar e a propriedade OLEDropMode do destino de soltar está definida como 1 – Enabled. |
| Evento OLEDragOver | Ocorre quando os dados são arrastados sobre um destino de soltar e a propriedade OLEDropMode do destino de soltar está definida como 1 – Enabled. |
| Propriedade OLEDropEffects | Especifica o tipo de operações de soltar que um destino de soltar OLE suporta. |
| Propriedade OLEDropHasData | Especifica como uma operação de soltar é gerenciada. |
| Propriedade OLEDropMode | Especifica como um destino de soltar gerencia operações de soltar OLE. |

# Movendo dados

Para executar uma operação de arrastar e soltar para mover dados usando o botão do mouse padrão (esquerdo), selecione os dados que deseja mover na origem de arrasto. Após selecionar os dados, pressione e mantenha o botão do mouse pressionado enquanto move o ponteiro do mouse sobre o destino de soltar. Solte o botão do mouse para soltar os dados no destino de soltar. Durante a operação OLE de arrastar e soltar, o cursor do mouse muda para indicar que uma operação OLE de arrastar e soltar está em vigor.

Você também pode clicar no botão do mouse não padrão (direito) nos dados em uma origem de arrasto e arrastá-los para um destino de soltar. Dependendo do destino de soltar, um menu de contexto pode ser exibido quando você solta os dados no destino de soltar. O menu de contexto contém um conjunto de opções que permite escolher como os dados são processados pelo destino de soltar.

# Copiando dados

Você também pode copiar dados de uma origem de arrasto e colá-los em um destino de soltar. Pressione a tecla Ctrl enquanto clica com o mouse nos dados selecionados na origem de arrasto. O cursor do mouse exibe um sinal de mais (+) enquanto o mouse é arrastado para indicar que uma operação de Copiar está em vigor.

# Destinos e origens que não suportam OLE de arrastar e soltar

Você só pode mover ou copiar dados de uma origem de arrasto que suporta OLE de arrastar e soltar, e o destino de soltar também deve suportar OLE de arrastar e soltar. Observe que, embora um destino de soltar possa suportar OLE de arrastar e soltar, o destino de soltar não precisa aceitar os dados que você tenta soltar nele. Por exemplo, os dados que você está movendo ou copiando podem estar em um formato que o destino de soltar não suporta. Durante uma operação de arrastar e soltar, o cursor do mouse muda para um símbolo No Drop (um círculo riscado) para indicar que o mouse está posicionado sobre uma área de um aplicativo ou controle onde os dados não podem ser soltos.

# Cancelando uma operação

Você pode cancelar a operação OLE de arrastar e soltar pressionando ESC durante a operação.
