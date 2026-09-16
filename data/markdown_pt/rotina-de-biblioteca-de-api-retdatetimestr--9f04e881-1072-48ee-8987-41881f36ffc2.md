# Rotina de Biblioteca de API _RetDateTimeStr( )

Define o valor de retorno da biblioteca como um datetime.

```foxpro
void _RetDateTimeStr(char FAR *string)
char FAR *string;            /* Datetime string. */
```

# Observações

Especifique a cadeia de caracteres de datetime no formato mm/dd/ano hh:mm:ss, em que o ano pode ter dois ou quatro dígitos. Consulte a Função CTOT( ) para obter uma lista de formatos de datetime válidos para a cadeia de caracteres de datetime.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir converte um valor do tipo data para um valor do tipo datetime.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO RETDT
? xctot("2/16/95 12:07am")
```

### Código C

```foxpro
#include <pro_ext.h>
void FAR datetime(ParamBlk FAR *parm)
{
  MHANDLE mh;
  char FAR *instring;
   if ((mh = _AllocHand(parm->p[0].val.ev_length + 1)) == 0) {
      _Error(182); // "Insufficient memory"
   }
   _HLock(parm->p[0].val.ev_handle);
   instring = _HandToPtr(parm->p[0].val.ev_handle);
   instring[parm->p[0].val.ev_length] = '\0';
   _RetDateTimeStr(instring);
   _HUnLock(parm->p[0].val.ev_handle);
}
FoxInfo myFoxInfo[] = {
   {"XCTOT", (FPFI) datetime, 1, "C"}
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
