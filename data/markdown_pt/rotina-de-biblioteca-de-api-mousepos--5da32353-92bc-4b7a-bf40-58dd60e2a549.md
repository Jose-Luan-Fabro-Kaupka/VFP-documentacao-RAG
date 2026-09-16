# Rotina de biblioteca de API _MousePos( )

Preenche pt com a posição atual do ponteiro do mouse.

```foxpro
int _MousePos(Point FAR *pt)
Point FAR *pt;               /* Pointer. */
```

# Observações

_MousePos( ) retorna True (um inteiro diferente de 0) se o botão esquerdo do mouse estiver pressionado quando a função é chamada, ou False (0) se o botão esquerdo do mouse não estiver pressionado.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir exibe a posição atual do ponteiro do mouse até detectar um clique do botão esquerdo do mouse.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO MOUSEPOS
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
FAR MousePosEx(ParamBlk FAR *parm)
{
   Point mousePos;
   while (!_MousePos(&mousePos))
   {
      _PutStr("\nvertical =");
      putLong(mousePos.v, 5);
      _PutStr("; horizontal =");
      putLong(mousePos.h, 5);
   }
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) MousePosEx, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
