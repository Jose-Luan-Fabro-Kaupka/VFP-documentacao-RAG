# GDI Além de Color Foundation Classe

The gpColor class encapsulates a GDI+ color, consisting of 4 positive integers (each ranging from 0 to 255) for red, green, blue and alpha components.

( > Categoria )
| --- | --- |
Catálogo padrão Visual FoxPro Catalog\Foundation Classes\Output\GDIplus
Classe gpColor
□ Classe base □ Personalizado
| Class Library | _GDIPLUS.vcx |
| Parent Class | gpBase ( GDI Plus Base Foundation Class ) |

Observações

A tabela a seguir lista propriedades públicas e métodos adicionados por esta classe à sua classe-mãe, gpBase. Também implementa os métodos Clone e Init.

Values listed as ARGB type in the table are composite colors represented in GDI+ native format. Bits 24-31 of these values hold the color's alpha component, bits 16-23 hold the red component, bits 8-15 hold green, and bits 0-7 hold blue.

Propriedades e métodos Descrição
| --- | --- |
O Alpha Property (transparência) componente de uma cor, com valores legais variando de 0 a 255 . Padrão: 0 Observações: O valor 0 representa transparência completa e o valor 255 representa opacidade completa. □
| ARGB Property | Color in native GDI+ (alpha,red,green,blue) format. The underlying GDI+ representation is a 32-bit signed integer, so legal values range from - 2^31 to ( 2^31-1 ). Default: 0 |
□ Blue Property □ Componente azul de uma cor, com valores legais variando de 0 a 255 . Predefinição: 0
| Clone Method | Clones a color object. Syntax: ? THIS.Clone(toColor) Return Values: Logical, representing success or failure. Parameters: toColor , required, the gpColor object to clone. |
Propriedades FoxRGB Cor no formato Visual FoxPro RGB, opaco com bits 0-7 representando vermelho, bits 8-15 representando verde e bits 16-23 representando azul. Predefinição: 0
Imóveis Verdes componente verde de uma cor, com valores legais variando de 0 a 255 . Predefinição: 0
| Init Method | Constructs a color value during initialization if passed appropriate arguments. Syntax: CREATEOBJECT("gpColor"[, tnRedOrARGB[, tnGreen[, tnBlue[, tnAlpha]]]]) Return Values: Logical, representing success or failure. If the method fails, the object does not instantiate. Parameters: tnRedOrARGB , required if immediate initialization of the color value is requested. An integer representing either the red component of the color value or the full ARGB-type composite color value. tnGreen , optional, an integer representing the green component of the color value. tnBlue , optional, an integer representing the blue component of the color value. tnAlpha , optional, an integer representing the alpha component of the color value. The default is 255, or completely opaque. |
□ Red Property □ Red component of a color , com valores legais variando de 0 a 255 . Predefinição: 0
| Set Method | Set a color value using separate Red,Green,Blue, and Alpha components. Syntax: THIS.Set(tnRed, tnGreen, tnBlue[, tnAlpha]) Return Values: None. Parameters: tnRed , required, an integer representing the red component of the color value. tnGreen , required, an integer representing the green component of the color value. tnBlue , required, an integer representing the blue component of the color value. tnAlpha , optional, an integer representing the alpha component of the color value. The default is 255, or completely opaque. |

Veja também
- Visual FoxPro Foundation Classes A-Z
- GDI Plus API Wrapper Foundation Classes
- Orientações para a utilização Visual FoxPro Classes da Fundação
