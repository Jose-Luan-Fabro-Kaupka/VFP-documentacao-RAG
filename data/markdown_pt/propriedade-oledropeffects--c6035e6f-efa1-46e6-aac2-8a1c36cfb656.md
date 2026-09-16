# Propriedade OLEDropEffects

Especifica o tipo de operações de soltar que um destino de soltar OLE suporta. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.OLEDropEffects[= nDropEffect]
```

# Valor de retorno
 **nDropEffect**
Especifica o tipo de operações de soltar que um destino de soltar OLE suporta. A tabela a seguir lista os valores de nDropEffect com uma descrição de cada um. nDropEffect Constante Foxpro.h Descrição 0 DROPEFFECT_NONE O destino de soltar não aceita os dados como destino de soltar. 1 DROPEFFECT_COPY Os dados podem ser copiados para o destino de soltar. 2 DROPEFFECT_MOVE Os dados podem ser movidos para o destino de soltar. 4 DROPEFFECT_LINK Os dados podem ser vinculados ao destino de soltar. Uma operação de soltar pode suportar várias operações de soltar somando vários valores para nDropEffect. Por exemplo, se nDropEffect for 3, o destino de soltar suporta operações de soltar de cópia e movimento (3 = 1 (copy) + 2 (move)).

# Observações

Aplica-se a: Controle CheckBox | Controle ComboBox | Controle CommandButton | Controle CommandGroup | Objeto Container | Objeto Control (Visual FoxPro) | Controle EditBox | Objeto Form | Controle Grid | Controle Image (Visual FoxPro) | Controle Label (Visual FoxPro) | Controle Line | Controle ListBox | Controle OptionButton | Controle OptionGroup | Objeto Page | Controle PageFrame | Objeto ProjectHook | Controle Shape | Controle Spinner | Controle TextBox (Visual FoxPro) | Objeto ToolBar

OLEDropEffects é uma propriedade de destino de soltar e deve ser definida no evento OLEDragOver.
