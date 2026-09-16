# Evento OLEDragDrop

Ocorre quando dados são soltos em um destino de drop e a propriedade OLEDropMode do destino de drop está definida como 1 – Enabled.

```foxpro
PROCEDURE Object.OLEDragDrop
LPARAMETERS oDataObject, nEffect, nButton,
  nShift,   nXCoord, nYCoord
```

# Valor de retorno
 **oDataObject**
Uma referência de objeto ao DataObject de OLE drag-and-drop, usada com os métodos GetData e GetFormat para retornar dados e formatos de dados no DataObject.
**nEffect**
Um valor passado para o evento OLECompleteDrag, indicando a ação realizada quando dados são soltos no destino de drop. nEffect é inicialmente um valor que indica as operações de OLE drag-and-drop suportadas pela fonte de arrastar. Dentro do evento OLEDragDrop você pode alterar o valor de nEffect, que é passado para o evento OLECompleteDrag. Se você alterar o valor de nEffect, certifique-se de incluir NODEFAULT no código do evento para impedir o comportamento padrão. A tabela a seguir lista os valores para nEffect que você pode passar para o evento OLECompleteDrag com uma descrição de cada ação. nEffect Constante Foxpro.h Descrição 0 DROPEFFECT_NONE O destino de drop não aceitou os dados ou a operação de drop foi cancelada. 1 DROPEFFECT_COPY Os dados foram copiados da fonte de arrastar para o destino de drop. 2 DROPEFFECT_MOVE Os dados foram movidos da fonte de arrastar para o destino de drop. 4 DROPEFFECT_LINK Os dados foram vinculados da fonte de arrastar para o destino de drop.
**nButton**
Contém um número que especifica qual botão do mouse foi liberado para soltar os dados no destino: 1 (esquerdo), 2 (direito) ou 4 (meio).
**nShift**
Contém um número especificando o estado das teclas modificadoras quando o mouse foi liberado para soltar os dados no destino de drop. As teclas modificadoras válidas são as teclas SHIFT, CTRL e ALT. Os valores retornados em nShift para teclas modificadoras individuais estão listados na tabela a seguir. nShift Tecla modificadora 1 SHIFT 2 CTRL 4 ALT Se mais de uma tecla modificadora é mantida pressionada quando o mouse é pressionado, o argumento nShift contém a soma dos valores para as teclas modificadoras. Por exemplo, se o usuário mantém CTRL pressionado ao liberar o botão do mouse, o argumento nShift contém 2. Mas se o usuário mantém CTRL+ALT pressionado ao liberar o botão do mouse, o argumento nShift contém 6.
**nXCoord , nYCoord**
Contém a posição horizontal ( nXCoord ) e vertical ( nYCoord ) do ponteiro do mouse dentro do Form quando o botão do mouse foi liberado para soltar os dados no destino de drop. Essas coordenadas são expressas em termos do sistema de coordenadas do Form na unidade de medida especificada pela propriedade ScaleMode do Form.

# Observações

Aplica-se a: CheckBox Control | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | Control Object (Visual FoxPro) | EditBox Control | Form Object | Grid Control | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OptionButton Control | OptionGroup Control | Page Object | PageFrame Control | ProjectHook Object | Shape Control | Spinner Control | TextBox Control (Visual FoxPro) | ToolBar Object

OLEDragDrop é um evento de destino de drop que ocorre apenas quando a propriedade OLEDropMode para o controle ou objeto está definida como 1 – Enabled. Este evento não ocorre se a propriedade OLEDropMode estiver definida como 0 – Disabled ou 2 – Pass to Container.

Se você realizar seu próprio processamento de drop no evento OleDragDrop, inclua NODEFAULT para impedir que o drop padrão ocorra. Neste caso, você deve então definir o valor nEffect resultante.
