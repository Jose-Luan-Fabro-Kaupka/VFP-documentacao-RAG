# Rotina de biblioteca de API _WGetPort( )

Retorna o WHANDLE da janela atualmente selecionada para saída do usuário.

```foxpro
WHANDLE _WGetPort(void any)
void any;                     /* Pointer. */
```

# Exemplo

O exemplo a seguir exibe o identificador de janela retornado por _WGetPort( ) conforme a porta de saída atual é alterada.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WGETPORT
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
FAR Example(ParamBlk FAR *parm)
{
   WHANDLE wh;
   WHANDLE oldPort;
   wh = _WOpen(2,10,23,70,WEVENT | CLOSE,WINDOW_SCHEME,(Scheme FAR *)0,
      WO_SYSTEMBORDER);
   _WShow(wh);
   _PutStr("\n1) _WGetPort() ="); putLong(_WGetPort(), 10);
   oldPort = _WSetPort(wh);
   _PutStr("\n2) _WSetPort(wh) ="); putLong(oldPort, 10);
   _PutStr("\n3) _WGetPort() ="); putLong(_WGetPort(), 10);
   oldPort = _WSetPort(oldPort);
   _PutStr("\n4) _WSetPort(oldPort) =");  putLong(oldPort, 10);
   _PutStr("\nShould be back where we started.");
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) Example, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
