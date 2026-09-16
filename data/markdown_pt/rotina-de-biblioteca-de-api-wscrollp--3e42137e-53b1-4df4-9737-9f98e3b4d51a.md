# Rotina de biblioteca de API _WScrollP( )

Rola uma porção do conteúdo de uma janela para a esquerda ou para a direita e para cima ou para baixo.

```foxpro
void _WScrollP(WHANDLE wh, Rect r, int dv, int dh)
WHANDLE wh;            /* Window handle. */
Rect r;                     /* Portion to scroll. */
int dv;                        /* Left or right. */
int dh;                     /* Up or down. */
```

# Observações
 - O parâmetro r descreve a porção da janela a ser rolada.
- O parâmetro dv descreve o número de pixels para rolar a janela para a esquerda ou para a direita. Se dv for negativo, o conteúdo da janela rola para a esquerda. Se dv for positivo, o conteúdo da janela rola para a direita.
- O parâmetro dh descreve o número de pixels para rolar a janela para cima ou para baixo. Se dh for negativo, o conteúdo da janela rola para cima. Se dh for positivo, o conteúdo da janela rola para baixo.

Se dv e dh forem 0, _WScrollP( ) limpa os caracteres dentro do retângulo.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir abre uma janela e desenha um padrão retangular de Xs. Esse retângulo também é o retângulo de rolagem. Primeiro, _WScrollP( ) rola o retângulo para cima e para a esquerda. Em seguida, rola o retângulo para baixo e para a direita.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WSCROLLP
```

### Código C

```foxpro
#include <pro_ext.h>
FAR WScrollEx(ParamBlk FAR *parm)
{
   WHANDLE wh;
   Point pos;
   Rect rect;
   wh = _WOpenP(2, 2, 160, 320, WEVENT | CLOSE, WINDOW_SCHEME,
      (char *) 0, WO_SYSTEMBORDER);
  _WShow(wh);
   rect.top   = 40;
   rect.left   = 40;
   rect.bottom = 100;
   rect.right   = 100;
   for (pos.v = rect.top; pos.v < rect.bottom; pos.v += 6)
   {
      for (pos.h = rect.left; pos.h < rect.right; pos.h +=6)
      {
         _WPosCursorP(wh, pos);
    _WPutChr(wh, 'X');
      }
   }
   _Execute("WAIT 'Press any key to _WScroll(wh, rect, -20, -20)'");
   _WScrollP(wh, rect, -20, -20);
   _Execute("WAIT 'Press any key to _WScroll(wh, rect, +40, +40)'");
   _WScrollP(wh, rect, +40, +40);
}
FoxInfo myFoxInfo[] =
{
   {"ONLOAD", WScrollEx, CALLONLOAD, ""},
};
FoxTable _FoxTable =
{
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
