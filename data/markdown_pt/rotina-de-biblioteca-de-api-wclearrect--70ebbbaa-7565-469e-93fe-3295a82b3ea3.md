# Rotina de biblioteca de API _WClearRect( )

Apaga a área retangular especificada da janela especificada alterando a área para a cor de fundo padrão.

```foxpro
void _WClearRect(WHANDLE wh, Rect r)
WHANDLE wh;            /* Window handle. */
Rect r;                     /* Rectangle to clear. */
```

# Observações

A posição de saída não é alterada.

A área do retângulo se estende da coordenada superior esquerda até, mas não incluindo, a coordenada inferior direita. Isso significa que você deve declarar as coordenadas inferior e direita como uma unidade a mais que o tamanho pretendido do retângulo.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acesso à API do Visual FoxPro.

# Exemplo

O exemplo a seguir cria uma janela e a preenche com Xs. Depois que o usuário pressiona uma tecla em resposta a um comando WAIT do Visual FoxPro, _WClearRect( ) limpa uma região retangular da janela.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WCLRECT
```

### Código C

```foxpro
#include <pro_ext.h>
FAR WClearEx(ParamBlk FAR *parm)
{
   WHANDLE wh;
   int row, col;
   Rect r;
   wh = _WOpen(2,2,20,70,WEVENT | CLOSE,WINDOW_SCHEME,(Scheme FAR *) 0,
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
   r.top    = 2;W
   r.left    = 2;
   r.bottom = 15;
   r.right  = 65;
   _WClearRect(wh, r);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) WClearEx, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
