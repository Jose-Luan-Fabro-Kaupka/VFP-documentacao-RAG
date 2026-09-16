# Rotina de biblioteca de API _FindWindow( )

Coloca o handle da janela à qual o ponto pt pertence na tela em wh.

```foxpro
int _FindWindow(WHANDLE FAR *wh, Point pt)
WHANDLE FAR *wh;      /* Pointer to window handle. */
Point pt;                     /* Point. */
```

# Observações

_FindWindow( ) retorna um inteiro indicando a porção da janela onde o ponto está localizado. Por exemplo, _FindWindow( ) retorna o valor inContent se o ponto estiver dentro da janela.

Os possíveis valores de retorno, conforme definidos em PRO_EXT.H, estão listados na tabela a seguir.
 Valores de retorno de _FindWindow( )
| Valor | Localização do ponto |
| --- | --- |
| inBorder | Na borda da janela |
| inHelp | Na região de ajuda |
| inContent | Na área de conteúdo/texto |
| inDrag | Na barra de título |
| inGrow | No controle de tamanho |
| inGoAway | Na caixa de fechar |
| inZoom | No controle de zoom |
| inVUpArrow | Na seta para cima na barra de rolagem vertical |
| inVDownArrow | Na seta para baixo na barra de rolagem vertical |
| inVPageUp | Na região page up da barra de rolagem vertical |
| inVPageDown | Na região page down da barra de rolagem vertical |
| inVThumb | No thumb na barra de rolagem vertical |
| inHUpArrow | Na seta para a direita na barra de rolagem horizontal |
| inHDownArrow | Na seta para a esquerda na barra de rolagem horizontal |
| inHPageUp | Na região page right da barra de rolagem horizontal |
| inHPageDown | Na região page left da barra de rolagem horizontal |
| inHThumb | No thumb na barra de rolagem horizontal |
| inMenuBar | Na barra de menu |

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir aguarda um clique do botão esquerdo do mouse e usa _FindWindow( ) para obter o handle da janela para a posição do mouse down.

### Código Visual FoxPro

```foxpro
WAIT WINDOW  "Click mouse on a window" NOWAIT
SET LIBRARY TO FINDWIND
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
FAR FindWindowFn(ParamBlk FAR *parm)
{
   WHANDLE wh;
   Point mousePos;
   int where;
//  Get mouse position when left button goes down
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
   {"ONLOAD", (FPFI) FindWindowFn, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
