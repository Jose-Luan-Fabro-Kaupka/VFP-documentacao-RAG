# Rotina de biblioteca de API _WhToHwnd( )

Retorna o HWND do Windows do WHANDLE especificado.

```foxpro
HWND_WhToHwnd(WHANDLE wh)
WHANDLE wh;            /* Window handle. */
```

# Observações

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir cria uma janela e então obtém o HWND do Windows para a janela com o callback _WhToHwnd( ). Em seguida, para verificar o valor retornado por _WhToHwnd( ), o exemplo usa o HWND como argumento para uma função do Windows.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WHTOHWND
```

### Código C

```foxpro
#include <windows.h>
#include <pro_ext.h>
void putLong(long n, int width)
{
   Value val;
   val.ev_type = 'I';
   val.ev_long = n;
   val.ev_width = width;
   _PutValue(&val);
}
FAR WhToHwndEx(ParamBlk FAR *parm)
{
   RECT Rect;
   HWND hwnd;
   WHANDLE wh;
   Value val;
   wh = _WOpenP(10,10,120,240,CLOSE,WINDOW_SCHEME, (Scheme FAR *) 0,
      WO_SYSTEMBORDER);
   _WShow(wh);
//   Get Windows window handle and use as a parameter
//   to a Windows function
   hwnd = _WhToHwnd(wh);
   GetWindowRect(hwnd, &Rect); // Windows function
   _PutStr("\ntop   ="); putLong(Rect.top, 5);
   _PutStr("\nleft ="); putLong(Rect.left, 5);
   _PutStr("\nbottom ="); putLong(Rect.bottom, 5);
   _PutStr("\nright  ="); putLong(Rect.right, 5);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", WhToHwndEx, CALLONLOAD,  ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
