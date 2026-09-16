# Propriedade OLEDragPicture

Especifica a imagem exibida sob o ponteiro do mouse durante uma operação de arrastar e soltar OLE. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.OLEDragPicture[= cFileName]
```

#### Parâmetros
 **cFileName**
Especifica o nome e o caminho do arquivo gráfico a ser exibido quando ocorre uma operação de arrastar e soltar OLE. O arquivo gráfico que você especificar pode ser do tipo .bmp, .dib, .jpg, .gif, .ani, .cur ou .ico. O arquivo gráfico normalmente é uma representação translúcida ou em contorno do objeto sendo arrastado. Para criar uma representação translúcida do objeto, use um arquivo de máscara em preto e branco (.msk).

# Observações

Aplica-se a: Controle CheckBox | Controle ComboBox | Controle CommandButton | Controle CommandGroup | Objeto Container | Objeto Control (Visual FoxPro) | Controle EditBox | Objeto Form | Controle Grid | Controle Image (Visual FoxPro) | Controle Label (Visual FoxPro) | Controle Line | Controle ListBox | Controle OptionButton | Controle OptionGroup | Objeto Page | Controle PageFrame | Controle Shape | Controle Spinner | Controle TextBox (Visual FoxPro) | Objeto ToolBar

OLEDragPicture é uma propriedade de origem de arrasto. A imagem é exibida quando o ponteiro do mouse está posicionado sobre o formulário que contém a origem de arrasto.
