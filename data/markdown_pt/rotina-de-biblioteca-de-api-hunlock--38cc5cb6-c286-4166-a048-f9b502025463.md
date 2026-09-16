# Rotina de biblioteca de API _HUnLock( )

Desbloqueia um identificador de memória para que o Visual FoxPro possa acessá-lo durante a reorganização de memória.

```foxpro
void _HUnLock(MHANDLE hand)
MHANDLE hand;            /* Memory handle. /
```

# Observações

_HUnLock( ) não causa reorganização de memória.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir usa _RetDateStr( ) para retornar um tipo de data do Visual FoxPro, assumindo que o parâmetro de caractere é uma data válida. Ele emite _HUnLock( ) quando os identificadores de memória não precisam mais estar bloqueados, pois o desempenho do Visual FoxPro pode ser afetado negativamente por identificadores de memória bloqueados.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO HUNLOCK
? DATES("2/16/95")  && returns date {02/16/95}
```

### Código C

```foxpro
#include <pro_ext.h>
void FAR dates(ParamBlk FAR *parm)
{
   MHANDLE mh;
   char FAR *instring;
   if ((mh = _AllocHand(parm->p[0].val.ev_length + 1)) == 0)
   {
      _Error(182); // "Insufficient memory"
   }
   _HLock(parm->p[0].val.ev_handle);
   instring = _HandToPtr(parm->p[0].val.ev_handle);
   instring[parm->p[0].val.ev_length] = '\0';
   _RetDateStr(instring);
   _HUnLock(parm->p[0].val.ev_handle);
}
FoxInfo myFoxInfo[] = {
   {"DATES", (FPFI) dates, 1, "C"}
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
