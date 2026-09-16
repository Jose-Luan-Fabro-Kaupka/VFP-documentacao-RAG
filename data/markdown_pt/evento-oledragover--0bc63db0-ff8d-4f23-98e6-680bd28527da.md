# Evento OLEDragOver

Ocorre quando os dados são arrastados sobre um destino de soltura e a propriedade OLEDropMode do destino está definida como 1 – Enabled.

```foxpro
PROCEDURE Object.OLEDragOver
LPARAMETERS oDataObject, nEffect, nButton,
  nShift,   nXCoord, nYCoord, nState
```

# Valor de retorno
**oDataObject**
Uma referência de objeto ao DataObject de arrastar e soltar OLE, usada com os métodos GetData e GetFormat para retornar dados e formatos de dados no DataObject.
**nEffect**
Um valor passado ao evento OLEGiveFeedback que indica a ação executada se os dados forem soltos no destino. Inicialmente, nEffect é um valor que indica as operações de arrastar e soltar OLE aceitas pela origem. A tabela a seguir lista os valores de nEffect com uma descrição de cada ação. nEffect Constante Foxpro.h Descrição 0 DROPEFFECT_NONE O destino não aceita os dados ou a operação de soltura é cancelada. 1 DROPEFFECT_COPY Os dados são copiados da origem para o destino. 2 DROPEFFECT_MOVE Os dados são movidos da origem para o destino. 4 DROPEFFECT_LINK Os dados são vinculados da origem ao destino.
**nButton**
Contém um número que especifica qual botão do mouse está pressionado quando os dados são arrastados sobre um destino: 1 (esquerdo), 2 (direito) ou 4 (central).
**nShift**
Contém um número que especifica o estado das teclas modificadoras quando os dados são arrastados sobre um destino. As teclas modificadoras válidas são SHIFT, CTRL e ALT. Os valores retornados em nShift para teclas individuais são listados na tabela a seguir. nShift Tecla modificadora 1 SHIFT 2 CTRL 4 ALT Se mais de uma tecla modificadora estiver pressionada ao pressionar o botão do mouse, o argumento nShift conterá a soma dos valores dessas teclas. Por exemplo, se o usuário mantiver CTRL pressionada ao soltar o botão do mouse, nShift conterá 2. Se mantiver CTRL+ALT, nShift conterá 6.
**nXCoord , nYCoord**
Contêm as posições horizontal (nXCoord) e vertical (nYCoord) do ponteiro do mouse dentro do Form quando os dados são arrastados sobre um destino. Essas coordenadas são expressas no sistema de coordenadas do Form, na unidade de medida especificada pela propriedade ScaleMode do Form.
**nState**
Contém um número que especifica a direção em que os dados são arrastados: para dentro do controle ou objeto, dentro dele ou para fora dele. Os valores de nState são listados na tabela a seguir. nState Descrição 0 Os dados são arrastados para dentro do controle ou objeto. As propriedades OLEDropEffects e OLEDropHasData podem ser definidas quando nState é zero. 1 Os dados são arrastados para fora do controle ou objeto. 2 Os dados são arrastados dentro do controle ou objeto.

# Observações

Aplica-se a: controle CheckBox | controle ComboBox | controle CommandButton | controle CommandGroup | objeto Container | objeto Control (Visual FoxPro) | controle EditBox | objeto Form | controle Grid | controle Image (Visual FoxPro) | controle Label (Visual FoxPro) | controle Line | controle ListBox | controle OptionButton | controle OptionGroup | objeto Page | controle PageFrame | objeto ProjectHook | controle Shape | controle Spinner | controle TextBox (Visual FoxPro) | objeto ToolBar

OLEDragOver é um evento de destino de soltura que ocorre somente quando a propriedade OLEDropMode do controle ou objeto está definida como 1 – Enabled. Esse evento não ocorre se OLEDropMode estiver definida como 0 – Disabled ou 2 – Pass to Container.

Evite criar estados de espera no evento OLEDragOver com comandos e funções como WAIT WINDOW e MESSAGEBOX( ).
