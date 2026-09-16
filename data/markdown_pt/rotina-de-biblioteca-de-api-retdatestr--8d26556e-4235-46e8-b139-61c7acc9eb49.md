# Rotina de biblioteca de API _RetDateStr( )

Define o valor de retorno da biblioteca como uma data.

```foxpro
void _RetDateStr(char FAR *string)
char FAR *string;            /* Date string. */
```

# Observações

Especifique a cadeia de caracteres de data no formato mm/dd/ano, em que o ano pode ter dois ou quatro dígitos.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir converte uma cadeia de caracteres em um tipo de dados de data e a retorna ao Visual FoxPro.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO RETDATES
? DATES("02/16/95")  && returns date {02/16/95}
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
