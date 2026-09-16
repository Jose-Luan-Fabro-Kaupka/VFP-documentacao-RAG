# Evento OLESetData

Ocorre em uma origem de arrastar quando um destino de soltar chama o método GetData.

```foxpro
PROCEDURE Object.OLESetData
LPARAMETERS oDataObject, eFormat
```

# Valor de retorno
 **oDataObject**
Uma referência de objeto ao DataObject de OLE drag-and-drop, usada com o método SetData para colocar dados no DataObject.
**eFormat**
Um valor numérico ou de caractere que indica o formato dos dados que o método GetData solicita. A origem de arrastar usa este valor para determinar o formato dos dados a colocar no DataObject. Consulte o método GetData para uma tabela que lista os valores numéricos ou de caractere para cada formato de dados e uma descrição de cada formato.

# Observações

Aplica-se a: CheckBox Control | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | Control Object (Visual FoxPro) | EditBox Control | Form Object | Grid Control | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OptionButton Control | OptionGroup Control | Page Object | PageFrame Control | Shape Control | Spinner Control | TextBox Control (Visual FoxPro) | ToolBar Object

OLESetData é um evento de origem de arrastar. Incluir NODEFAULT não tem efeito sobre o comportamento deste método.

O evento OLESetData ocorre quando o método GetData é executado. Dentro do evento OLESetData você pode colocar dados no DataObject no formato especificado com o método SetData. Esta técnica é chamada "delay rendering" e permite colocar dados no DataObject somente quando solicitado.
