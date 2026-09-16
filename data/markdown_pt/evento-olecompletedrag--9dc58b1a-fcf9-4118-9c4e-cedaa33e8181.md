# Evento OLECompleteDrag

Ocorre quando dados são soltos no destino de soltar ou a operação de arrastar e soltar OLE é cancelada.

```foxpro
PROCEDURE Object.OLECompleteDrag
LPARAMETERS nEffect
```

# Valor de retorno
 **nEffect**
Um valor passado do evento OLEDragDrop, correspondente à ação executada quando dados são soltos no destino de soltar. A tabela a seguir lista os valores de nEffect com uma descrição de cada ação. nEffect Constante Foxpro.h Descrição 0 DROPEFFECT_NONE O destino de soltar não aceitou os dados ou a operação de soltar foi cancelada. 1 DROPEFFECT_COPY Os dados foram copiados da origem de arrastar para o destino de soltar. 2 DROPEFFECT_MOVE Os dados foram movidos da origem de arrastar para o destino de soltar. 4 DROPEFFECT_LINK Os dados foram vinculados da origem de arrastar para o destino de soltar.

# Observações

Aplica-se a: Controle CheckBox | Controle ComboBox | Controle CommandButton | Controle CommandGroup | Objeto Container | Objeto Control (Visual FoxPro) | Controle EditBox | Objeto Form | Controle Grid | Controle Image (Visual FoxPro) | Controle Label (Visual FoxPro) | Controle Line | Controle ListBox | Controle OptionButton | Controle OptionGroup | Objeto Page | Controle PageFrame | Controle Shape | Controle Spinner | Controle TextBox (Visual FoxPro) | Objeto ToolBar

OLECompleteDrag é um evento de origem de arrastar e é o último evento a ocorrer durante uma operação de arrastar e soltar OLE. Incluir NODEFAULT impede que uma movimentação de texto exclua o texto.

Este evento permite que a origem de arrastar determine a ação executada nos dados no destino de soltar. O destino de soltar pode definir nEffect em seu evento OLEDragDrop e a origem de arrastar pode executar a ação apropriada com base no valor de nEffect. Por exemplo, se os dados foram movidos para o destino de soltar, a origem de arrastar deve remover os dados de si mesma.
