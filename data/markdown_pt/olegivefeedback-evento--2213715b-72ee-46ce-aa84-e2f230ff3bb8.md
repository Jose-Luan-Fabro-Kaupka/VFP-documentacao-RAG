# OLEGiveFeedback Evento

Ocorre após cada evento OLEDragOver. Permite que a fonte de arrastar especifique o tipo de operação de arrastar e soltar OLE e o feedback visual.

```foxpro
PROCEDURE Object.OLEGiveFeedback
LPARAMETERS nEffect, eMouseCursor
```

# Valor de retorno
 **nEffect**
A ação executada quando os dados são descartados no destino de descarte. O valor de nEffect é definido pelo destino de eliminação em seu evento OLEDragOver. A tabela a seguir lista os valores para nEffect com uma descrição de cada ação. nEffect Constante Foxpro.h Descrição 0 DROPEFFECT_NONE O destino de descarte não pode aceitar os dados. 1 DROPEFFECT_COPY Coloque os resultados em uma cópia. 2 DROPEFFECT_MOVE Eliminar resultados em um movimento. 4 DROPEFFECT_LINK Solte os resultados em um link.
**eMouseCursor**
Especifica o ponteiro do mouse exibido durante a operação de arrastar e soltar OLE. eMouseCursor pode ser um caractere ou valor numérico. eMouseCursor é um parâmetro output e é definido como zero na entrada do evento into. Se eMouseCursor for um valor de caractere, presume-se que o valor do caractere seja o nome de um arquivo gráfico do tipo .ani, .cur ou .ico. Se eMouseCursor for um valor numérico, o valor especifica o ponteiro do mouse exibido. A tabela a seguir lista os valores numéricos para eMouseCursor com uma descrição de cada ponteiro do mouse. eMouseCursor Constante Foxpro.h Descrição 0 MOUSE_DEFAULT Forma determinada pelo objeto the. (Padrão) 1 MOUSE_ARROW Seta. 2 MOUSE_CROSSHAIR Cruz. A ponteiro em cruz. 3 MOUSE_IBEAM I-Feixe. 4 MOUSE_ICON_POINTER Ícone. A pequeno quadrado branco dentro de um quadrado preto. 5 MOUSE_SIZE_POINTER Tamanho. A seta de quatro pontas apontando norte, sul, leste, oeste. 6 MOUSE_SIZE_NE_SW Tamanho NE SW. A seta dupla apontando para nordeste e sudoeste. 7 MOUSE_SIZE_N_S Tamanho NS. A seta dupla apontando para norte e sul. 8 MOUSE_SIZE_NW_SE Tamanho NW SE. A seta dupla apontando para noroeste e sudeste. 9 MOUSE_W_E Tamanho WE. A seta dupla apontando para oeste e leste. 10 MOUSE_UP_ARROW Seta para cima. 11 MOUSE_HOURGLASS Ampulheta. 12 MOUSE_NO_DROP Sem queda. 13 MOUSE_HIDE_POINTER Ocultar ponteiro. 14 MOUSE_ARROW2 Seta. 15 MOUSE_ARROW_HOURGLASS Flecha e ampulheta. 16 MOUSE_ARROW_QUESTION Seta e ponto de interrogação.

# Observações
Aplica-se a: CheckBox Controle | ComboBox Controle | CommandButton Controle | CommandGroup Controle | Container Objeto | Control Objeto (Visual FoxPro) | EditBox Controle | Form Objeto | Grid Controle | Image Controle (Visual FoxPro) | Label Controle (Visual FoxPro) | Line Controle | ListBox Controle | OptionButton Controle | OptionGroup Controle | Page Objeto | PageFrame Controle | ProjectHook Objeto | Shape Controle | Spinner Controle | TextBox Controle (Visual FoxPro) | ToolBar Objeto

OLEGiveFeedback é um evento de arrastar source que permite fornecer feedback visual ao usuário. Você pode alterar o cursor do mouse para indicar a operação que ocorre quando o mouse é posicionado sobre a origem de arrastar ou o destino de soltar. A inclusão de NODEFAULT não afeta o comportamento do método this.

Observe que você deve evitar criar estados de espera no evento OLEGiveFeedback com comandos e funções como WAIT WINDOW e MESSAGEBOX( ).
