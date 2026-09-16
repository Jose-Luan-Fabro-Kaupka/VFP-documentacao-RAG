# Rotina de biblioteca de API _WClearRectP( )

Apaga a área retangular especificada de uma janela alterando-a para a cor de fundo padrão.

```foxpro
void _WClearRectP(WHANDLE wh, Rect r)
WHANDLE wh;            /* Window handle. */
Rect r;                     /* Rectangle to clear. */
```

# Observações

A área retangular é especificada em pixels. A posição de saída permanece inalterada.

A área do retângulo se estende da posição superior esquerda até, mas não incluindo, a posição inferior direita. Isso significa que você deve declarar as posições inferior e direita com um pixel a mais que o tamanho pretendido do retângulo.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir cria uma janela e a preenche com Xs. Depois que o usuário pressiona uma tecla em resposta ao comando WAIT do Visual FoxPro, _WClearRectP( ) limpa uma região retangular da janela.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WCLRECTP
```

### Código C

```foxpro
#include <pro_ext.h>
FAR WClearEx(ParamBlk FAR *parm)
{
   WHANDLE wh;
   int row, col;
   Rect r;
   wh = _WOpen(2, 2, 20, 70, CLOSE, WINDOW_SCHEME, (Scheme FAR *) 0,
      WO_SYSTEMBORDER);
   _WShow(wh);
   for (row = 0; row < _WHeight(wh); row++)
   {
      for (col = 0; col < _WWidth(wh); col++)
      {
         _WPutChr(wh, 'X');
      }
   }
   _Execute("WAIT WINDOW 'Press any key to clear window rectangle'");
   r.top    = 20;
   r.left    = 20;
   r.bottom = 100;
   r.right  = 300;
   _WClearRectP(wh, r);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", WClearEx, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
