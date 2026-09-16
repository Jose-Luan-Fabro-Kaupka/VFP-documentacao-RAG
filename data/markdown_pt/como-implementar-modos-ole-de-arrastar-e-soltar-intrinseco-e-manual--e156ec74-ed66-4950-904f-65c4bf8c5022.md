# Como: implementar modos OLE de arrastar e soltar intrínseco e manual

O Visual FoxPro oferece suporte a dois modos OLE de arrastar e soltar para controles: intrínseco e manual. No modo intrínseco, as operações OLE de arrastar e soltar são tratadas pelo Visual FoxPro. No modo manual OLE de arrastar e soltar, você especifica programaticamente a função e o controle.

# Modo OLE de arrastar e soltar intrínseco

O modo OLE de arrastar e soltar intrínseco pode ser implementado em um aplicativo para fornecer suporte OLE de arrastar e soltar padrão sem programação adicional.

### Para implementar suporte OLE de arrastar e soltar intrínseco para um controle
- Defina sua propriedade OLEDragMode como 1 – Automatic, permitindo que o controle atue como uma origem de arrastar OLE.
- Defina a propriedade OLEDropMode do controle como 1 – Enabled, para permitir que o controle atue como um destino de soltar OLE.

Para operações OLE de arrastar e soltar intrínsecas, o Visual FoxPro determina se o destino de soltar suporta o formato dos dados sendo soltos nele; se o destino de soltar suporta o formato, a operação de soltar ocorre, caso contrário a operação de soltar não é permitida.

A tabela a seguir lista os controles do Visual FoxPro e os formatos de dados que eles suportam como origens de arrastar no modo intrínseco. Observe que CF_TEXT é texto, como o texto que você digitaria em uma caixa de texto, e CFSTR_VFPSOURCEOBJECT é uma referência de tipo de objeto a um controle ou objeto do Visual FoxPro. Para os controles abaixo que suportam o formato de dados CF_TEXT, você pode arrastar texto da parte de texto do controle.
 Formatos de dados da origem de arrastar
| Controle | Formato de dados (definido em Foxpro.h) |
| --- | --- |
| Container, Image, Line, PageFrame e Shape | CFSTR_VFPSOURCEOBJECT |
| CommandButton e Label | CFSTR_VFPSOURCEOBJECT e CF_TEXT |
| CheckBox, ComboBox, EditBox, ListBox, Spinner e TextBox | CFSTR_VFPSOURCEOBJECT, CF_TEXT e CFSTR_OLEVARIANT |

Os controles do Visual FoxPro e os formatos de dados que eles suportam como destinos de soltar no modo intrínseco estão listados na tabela a seguir. Para os controles listados nesta tabela, você pode soltar texto na parte de texto do controle. O texto é inserido no ponto de inserção.
 Formatos de dados do destino de soltar
| Controle | Formato de dados |
| --- | --- |
| EditBox e ComboBox (Quando a propriedade Style do ComboBox está definida como 0 - Dropdown Combo) | CF_TEXT |
| Spinner e TextBox | CFSTR_OLEVARIANT |

# Modo OLE de arrastar e soltar manual

Pode haver casos em que você deseja controlar o tipo de dados que pode ser solto em um destino de soltar ou fornecer funcionalidade adicional para uma operação de arrastar e soltar. Por exemplo, você pode converter dados para um formato suportado pelo destino de soltar ou exibir uma caixa de diálogo que pergunta ao usuário se ele deseja soltar os dados no destino de soltar. Para substituir o suporte OLE de arrastar e soltar intrínseco e fornecer maior controle sobre operações de arrastar e soltar, use OLE de arrastar e soltar manual.

### Para implementar suporte OLE de arrastar e soltar manual para um controle
- Escreva seu próprio código de evento ou método para o evento ou método que deseja substituir.

Inclua o comando NODEFAULT no código do evento ou método para substituir o comportamento de arrastar e soltar intrínseco do Visual FoxPro.

O Visual FoxPro oferece compatibilidade com versões anteriores (sem suporte OLE de arrastar) para aplicativos existentes quando OLEDragMode está definido como 0 (o padrão) e você não inclui codificação adicional de OLE de arrastar e soltar.
