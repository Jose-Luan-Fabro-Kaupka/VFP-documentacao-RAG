# Rotina da biblioteca de API _GlobalToLocal( )

Traduz um ponto em coordenadas relativas à tela para coordenadas relativas à janela.

```foxpro
void _GlobalToLocal(Point FAR *pt, WHANDLE wh)
Point FAR *pt;               /* Point. */
WHANDLE wh;            /* Window handle. */
```

# Observações

Antes de chamar _GlobalToLocal( ), chame _FindWindow( ) para determinar qual janela possui o ponto.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessar a API do Visual FoxPro.

# Exemplo

O exemplo a seguir aguarda um clique do botão esquerdo do mouse e depois usa _FindWindow( ) para obter o identificador de janela para a posição do mouse. _GlobalToLocal( ) recebe tanto o identificador de janela quanto a posição absoluta do mouse como parâmetros e retorna a posição do mouse para uma posição relativa à janela.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO GLTOLOC
```

### Código C

```foxpro
#include <pro_ext.h>
void putLong(long n, int width)
{
   Value val;
   val.ev_type = 'I';
   val.ev_long = n;
   val.ev_width = width;
   _PutValue(&val);
}
FAR FindWindowEx(ParamBlk FAR *parm)
{
   WHANDLE wh;
   Point mousePos;
   int where;
   // Get mouse position when left button goes down
   _Execute("WAIT WINDOW 'Click In A Window' NOWAIT");
   while (_InKey(0, MOUSEACTIVE | HIDECURSOR) != 151);
   while (!_MousePos(&mousePos));
   switch (where = _FindWindow(&wh, mousePos))
   {
      case inBorder:
         _PutStr("\nMouse down inBorder"); break;
      case inHelp:
         _PutStr("\nMouse down inHelp"); break;
      case inContent:
         _PutStr("\nMouse down inContent"); break;
      case inDrag:
         _PutStr("\nMouse down inDrag"); break;
      case inGrow:
         _PutStr("\nMouse down inGrow"); break;
      case inGoAway:
         _PutStr("\nMouse down inGoAway"); break;
      case inZoom:
         _PutStr("\nMouse down inZoom"); break;
      case inVUpArrow:
         _PutStr("\nMouse down inVUpArrow"); break;
      case inVDownArrow:
         _PutStr("\nMouse down inVDownArrow"); break;
      case inVPageUp:
         _PutStr("\nMouse down inVPageUp"); break;
      case inVPageDown:
         _PutStr("\nMouse down inVPageDown"); break;
      case inVThumb:
         _PutStr("\nMouse down inVThumb"); break;
      case inHUpArrow:
         _PutStr("\nMouse down inHUpArrow"); break;
      case inHDownArrow:
         _PutStr("\nMouse down inHDownArrow"); break;
      case inHPageUp:
         _PutStr("\nMouse down inHPageUp"); break;
      case inHPageDown:
         _PutStr("\nMouse down inHPageDown"); break;
      case inHThumb:
         _PutStr("\nMouse down inHThumb"); break;
      case inMenuBar:
         _PutStr("\nMouse down inMenuBar"); break;
      default:
         _PutStr("\nMouse down someplace else"); break;
   }
   _GlobalToLocal(&mousePos, wh);
   _PutStr("\nPosition relative to window:");
   putLong(mousePos.v, 5);
   _PutChr(' ');
   putLong(mousePos.h, 5);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) FindWindowEx, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
