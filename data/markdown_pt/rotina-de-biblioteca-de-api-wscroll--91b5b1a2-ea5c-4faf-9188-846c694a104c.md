# Rotina de biblioteca de API _WScroll( )

Rola uma porção do conteúdo de uma janela para a esquerda ou direita e para cima ou para baixo.

```foxpro
void _WScroll(WHANDLE wh, Rect r, int dv, int dh)
WHANDLE wh;            /* Window handle. */
Rect r;                     /* Portion to scroll. */
int dv;                        /* Left or right. */
int dh;                     /* Up or down. */
```

# Observações
 - O parâmetro r descreve a porção da janela a ser rolada.
- O parâmetro dv descreve o número de caracteres para rolar a janela para a esquerda ou direita. Se dv for negativo, o conteúdo da janela rola para a esquerda. Se dv for positivo, o conteúdo da janela rola para a direita.
- O parâmetro dh descreve o número de caracteres para rolar a janela para cima ou para baixo. Se dh for negativo, o conteúdo da janela rola para cima. Se dh for positivo, o conteúdo da janela rola para baixo.

Se dv e dh forem 0, _WScroll( ) limpa os caracteres dentro do retângulo.

Para mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir abre uma janela e desenha um padrão retangular de Xs. Este retângulo também é o retângulo de rolagem. Primeiro, o exemplo rola o retângulo duas posições para cima e duas posições para a esquerda. Em seguida, rola o retângulo quatro posições para baixo e quatro posições para a direita.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WSCROLL
```

### Código C

```foxpro
#include <pro_ext.h>
FAR WScrollEx(ParamBlk FAR *parm)
{
   WHANDLE wh;
   Point pos;
   Rect rect;
   wh = _WOpen(2,2,20,70,WEVENT | CLOSE,WINDOW_SCHEME,(Scheme FAR *) 0,
      WO_SYSTEMBORDER);
   _WShow(wh);
   rect.top   = 6;
   rect.left   = 6;
   rect.bottom = 12;
   rect.right   = 12;
   for (pos.v = rect.top; pos.v < rect.bottom; pos.v++)
   {
      for (pos.h = rect.left; pos.h < rect.right; pos.h++)
      {
         _WPosCursor(wh, pos);
         _WPutChr(wh, 'X');
      }
   }
   _Execute("WAIT WINDOW 'Press any key to _WScroll(wh,rect,-2,-2)'");
   _WScroll(wh, rect, -2, -2);
   _Execute("WAIT WINDOW 'Press any key to _WScroll(wh,rect,+4,+4)'");
   _WScroll(wh, rect, +4, +4);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) WScrollEx, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
