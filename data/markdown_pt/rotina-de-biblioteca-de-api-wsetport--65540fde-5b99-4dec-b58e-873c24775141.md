# Rotina de biblioteca de API _WSetPort( )

Altera a janela de saída do usuário para ser a janela especificada.

```foxpro
WHANDLE _WSetPort(WHANDLE wh)
WHANDLE wh;            /* Window handle. */
```

# Observações

_WSetPort( ) retorna o identificador da janela de saída do usuário anterior.

> **Observação:** Se sua rotina alterar a janela de saída do usuário, certifique-se de restaurar a janela de saída do usuário antes de retornar ao Visual FoxPro.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir cria uma janela e a torna a porta de saída. Ele grava algum texto nesta janela antes de voltar à porta de saída original.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WSETPORT
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
