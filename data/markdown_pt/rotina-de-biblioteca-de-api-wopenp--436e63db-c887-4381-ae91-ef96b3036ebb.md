# Rotina de biblioteca de API _WOpenP( )

Cria uma nova janela nas posições especificadas pelos parâmetros top, left, bottom e right.

```foxpro
WHANDLE _WOpenP(int top, int left, int bottom, int right, int flag,
         int scheme_num, Scheme FAR *scheme, char FAR *bord)
int top;                     /* Top coordinate in pixels. */
int left;                     /* Left coordinate in pixels. */
int bottom;                  /* Bottom coordinate in pixels. */
int right;                     /* Right coordinate in pixels. */
int flag;                     /* Attributes. */
int scheme_num;            /* Color scheme. */
Scheme FAR *scheme;      /* Points to color scheme to use. */
char FAR *bord;            /* Border type. */
```

# Observações

As posições da janela podem estar fora da tela. Memória adicional é alocada para manter a imagem fora da tela desta janela.

O parâmetro flag determina os atributos desta janela. O flag pode ser um ou mais dos valores de flag na tabela abaixo. Você pode combinar vários valores de flag usando o operador C | ou +. Bordas de janela típicas são definidas em PRO_EXT.H.

| Valor flag | Atributo da janela |
| --- | --- |
| WCURSOR | O ponto de inserção pode ser exibido nesta janela. |
| ZOOM | O usuário pode ampliar a janela. |
| ADJ | O usuário pode ajustar o tamanho da janela. |
| CLOSE | O usuário pode fechar a janela. |
| MOVE | O usuário pode mover a janela. |
| AUTOSCROLL | A janela rola quando a saída ultrapassa a linha inferior. |
| WEVENT | A janela recebe, ativa e desativa eventos. |
| SHADOW | A janela projeta uma sombra. |
| WMODAL | O usuário não pode enviar esta janela para o fundo. |
| WMINIMIZE | O usuário pode minimizar esta janela. |

O scheme_num pode ser qualquer número de esquema de cores válido, ou – 1 para indicar que o parâmetro scheme aponta para o esquema de cores a ser usado.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir cria janelas usando vários esquemas de cores e bordas diferentes. Em particular, observe o esquema de cores personalizado.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WOPENP
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   WHANDLE wh;
   char customScheme[12] =
   {
      BLACK_ON      | WHITE,
      RED_ON      | BLACK      | BLINK,
      WHITE_ON      | WHITE      | BRIGHT,
      CYAN_ON      | BLUE      | BRIGHT,
      GREEN_ON      | BROWN,
      BROWN_ON      | BROWN      | BRIGHT,
      MAGENTA_ON   | MAGENTA   | BRIGHT,
      RED_ON      | MAGENTA   | BRIGHT | BLINK,
      BROWN_ON      | GREEN      | BRIGHT,
      BLACK_ON      | CYAN,
      BLUE_ON      | CYAN,
   };
   _Execute("WAIT WINDOW 'Press any key to see a window \
      in WINDOW_SCHEME with WO_DOUBLEBOX border'");
   wh = _WOpenP(10, 10, 160, 320, WEVENT | CLOSE, WINDOW_SCHEME,
      (Scheme FAR *)0, WO_DOUBLEBOX);
   _WShow(wh);
   _Execute("WAIT WINDOW 'Press any key to see a window \
      in ALERT_SCHEME with WO_SINGLEBOX border'");
   _WClose(wh);
   wh = _WOpenP(10, 10, 160, 320, WEVENT | CLOSE, ALERT_SCHEME,
      (Scheme FAR *)0, WO_SINGLEBOX);
   _WShow(wh);
   _Execute("WAIT WINDOW 'Press any key to see a window \
      in WINDOW_SCHEME with WO_PANELBORDER border'");
   _WClose(wh);
   wh = _WOpenP(10, 10, 160, 320, WEVENT | CLOSE, WINDOW_SCHEME,
      (Scheme FAR *)0, WO_PANELBORDER);
   _WShow(wh);
   _Execute("WAIT WINDOW 'Press any key to see a window \
      in a custom scheme with WO_SYSTEMBORDER border'");
   _WClose(wh);
   wh = _WOpenP(10,10,160,320,WEVENT | CLOSE,-1,customScheme,
      WO_SYSTEMBORDER);
   _WShow(wh);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", Example, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
