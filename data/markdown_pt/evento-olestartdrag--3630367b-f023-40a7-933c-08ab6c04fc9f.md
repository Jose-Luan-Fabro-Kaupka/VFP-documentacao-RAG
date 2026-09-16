# Evento OLEStartDrag

Ocorre quando o método OLEDrag é chamado.

```foxpro
PROCEDURE Object.OLEStartDrag
LPARAMETERS oDataObject, nEffect
```

# Valor de retorno
 **oDataObject**
Uma referência de objeto ao DataObject de arrastar e soltar OLE. Você pode chamar qualquer um dos métodos do DataObject a partir do evento OLEStartDrag.
**nEffect**
As operações de arrastar OLE suportadas pela origem do arrasto. A tabela a seguir lista os valores de nEffect com uma descrição de cada ação. nEffect é um parâmetro de saída e é definido como três na entrada do evento, portanto você deve fornecer o valor de nEffect neste evento. Por exemplo, para permitir apenas operações de cópia, defina nEffect como 1 (DROPEFFECT_COPY). nEffect Foxpro.h constant Description 0 DROPEFFECT_NONE Drag source did not support any drag operations. 1 DROPEFFECT_COPY Drag source supports Copy operations. 2 DROPEFFECT_MOVE Drag source supports Move operations (the default). 4 DROPEFFECT_LINK Drag source supports link operations. A drag source can support multiple drag operations by adding multiple values together for nEffect . For example, if nEffect is 3, the drag source supports both copy and move drag operations (3 = 1 (copy) + 2 (move)).

# Observações

Aplica-se a: CheckBox Control | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | Control Object (Visual FoxPro) | EditBox Control | Form Object | Grid Control | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OptionButton Control | OptionGroup Control | Page Object | PageFrame Control | Shape Control | Spinner Control | TextBox Control (Visual FoxPro) | ToolBar Object

OLEStartDrag é um evento de origem de arrasto. Incluir NODEFAULT não tem efeito sobre o comportamento deste método.
