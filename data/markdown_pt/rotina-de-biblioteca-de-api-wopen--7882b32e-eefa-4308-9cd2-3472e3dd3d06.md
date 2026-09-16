# Rotina de biblioteca de API _WOpen( )

Cria uma nova janela nas coordenadas especificadas pelos parâmetros top, left, bottom e right.

```foxpro
WHANDLE _WOpen(int top, int left, int bottom, int right, int flag,
         int scheme_num, Scheme FAR *scheme, char FAR *bord)
int top;                     /* Row of top coordinate. */
int left;                     /* Column of left coordinate. */
int bottom;                  /* Row of bottom coordinate.  */
int right;                     /* Column of right coordinate. */
int flag;                     /* Attributes. */
int scheme_num;            /* Color scheme. */
Scheme FAR *scheme;      /* Points to color scheme to use. */
char FAR *bord;            /* Border type. */
```

# Observações

As coordenadas da janela podem estar fora da tela, mas a altura não pode exceder 120 e a largura não pode exceder 264. Memória adicional é alocada para manter a imagem fora da tela desta janela.

O parâmetro flag determina os atributos desta janela. O flag pode ser um ou mais dos seguintes valores de flag. Você pode combinar vários valores de flag usando o operador C | ou +. Bordas de janela típicas são definidas em PRO_EXT.H.

| Valor flag | Atributo da janela |
| --- | --- |
| WCURSOR | O ponto de inserção pode ser exibido nesta janela. |
| ZOOM | O usuário pode maximizar a janela. |
| ADJ | O usuário pode ajustar o tamanho da janela. |
| CLOSE | O usuário pode fechar a janela. |
| MOVE | O usuário pode mover a janela. |
| AUTOSCROLL | A janela rola quando a saída ultrapassa a linha inferior. |
| WEVENT | A janela recebe eventos de ativação e desativação. |
| SHADOW | A janela projeta uma sombra. |
| WMODAL | O usuário não pode enviar esta janela para o fundo. |
| WMINIMIZE | O usuário pode minimizar esta janela. |

O scheme_num pode ser qualquer número de esquema de cores válido, ou – 1 para indicar que o parâmetro scheme aponta para o esquema de cores a ser usado.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir cria janelas usando vários esquemas de cores e bordas diferentes. Em particular, observe o esquema de cores personalizado.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WOPEN
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   WHANDLE wh;
   Scheme customScheme =
   {
      (char) (BLACK_ON      | WHITE),
      (char) (RED_ON      | BLACK      | BLINK),
      (char) (WHITE_ON      | WHITE      | BRIGHT),
      (char) (CYAN_ON      | BLUE      | BRIGHT),
      (char) (GREEN_ON      | BROWN),
      (char) (BROWN_ON      | BROWN      | BRIGHT),
      (char) (MAGENTA_ON   | MAGENTA   | BRIGHT),
      (char) (RED_ON      | MAGENTA   | BRIGHT | BLINK),
      (char) (BROWN_ON      | GREEN      | BRIGHT),
      (char) (BLACK_ON      | CYAN),
      (char) (BLUE_ON      | CYAN),
   };
   _Execute("WAIT WINDOW 'Press any key to see a window \
      in WINDOW_SCHEME with WO_DOUBLEBOX border'");
   wh = _WOpen(2,2,20,70,WEVENT | CLOSE,WINDOW_SCHEME,(Scheme FAR *) 0,
      WO_DOUBLEBOX);
   _WShow(wh);
   _Execute("WAIT WINDOW 'Press any key to see a window \
      in ALERT_SCHEME with WO_SINGLEBOX border'");
   _WClose(wh);
   wh = _WOpen(2,2,20,70,WEVENT | CLOSE,ALERT_SCHEME, (Scheme FAR *) 0,
      WO_SINGLEBOX);
   _WShow(wh);
   _Execute("WAIT WINDOW 'Press any key to see a window \
      in WINDOW_SCHEME with WO_PANELBORDER border'");
   _WClose(wh);
   wh = _WOpen(2,2,20,70,WEVENT | CLOSE,WINDOW_SCHEME,(Scheme FAR *) 0,
      WO_PANELBORDER);
   _WShow(wh);
   _Execute("WAIT WINDOW 'Press any key to see a window \
      in a custom scheme with WO_SYSTEMBORDER border'");
   _WClose(wh);
   wh = _WOpen(2,2,20,70,WEVENT | CLOSE,-1,(Scheme FAR *) customScheme,
      WO_SYSTEMBORDER);
   _WShow(wh);
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) Example, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
