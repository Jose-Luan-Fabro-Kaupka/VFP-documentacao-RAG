# Método OLEDrag

Inicia uma operação de arrastar e soltar OLE.

```foxpro
PROCEDURE Object.OLEDrag(lDetectDrag)
```

#### Parâmetros
 **lDetectDrag**
Especifica quando o evento OLEStartDrag é executado. Se lDetectDrag for false (.F.), o evento OLEStartDrag é executado imediatamente. Se lDetectDrag for true (.T.), o evento OLEStartDrag é executado depois que o usuário pressionar o botão do mouse por um período suficiente para indicar que uma operação de arrastar está ocorrendo, ou o mouse for movido uma distância suficiente enquanto o botão do mouse estiver pressionado, novamente indicando que uma operação de arrastar está ocorrendo. Se você não especificar um valor para lDetectDrag , true (.T.) é retornado automaticamente.

# Observações

Aplica-se a: Controle CheckBox | Controle ComboBox | Controle CommandButton | Controle CommandGroup | Objeto Container | Objeto Control (Visual FoxPro) | Controle EditBox | Objeto Form | Controle Grid | Controle Image (Visual FoxPro) | Controle Label (Visual FoxPro) | Controle Line | Controle ListBox | Controle OptionButton | Controle OptionGroup | Objeto Page | Controle PageFrame | Controle Shape | Controle Spinner | Controle TextBox (Visual FoxPro) | Objeto ToolBar

OLEDrag é um método de origem de arrastar.
