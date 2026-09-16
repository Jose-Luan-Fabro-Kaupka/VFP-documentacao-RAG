# Rotina de biblioteca de API _FEOF( )

```foxpro
int _FEOF(FCHAN chan)
FCHAN chan;               /* File channel of file. */
```

# Observações

_FEOF( ) retorna True (um inteiro diferente de 0) se o ponteiro de arquivo no arquivo especificado estiver atualmente no final do arquivo; ou False (0) se não estiver.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir cria um arquivo e define seu comprimento como 8192 bytes. Em seguida, move o ponteiro de arquivo para o início do arquivo e chama _FEOF( ), que retorna 0 (False). Depois, move o ponteiro de arquivo para o final do arquivo e chama _FEOF( ) novamente, que desta vez retorna 1 (True).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO FEOF
```

### Código C

```foxpro
#include <pro_ext.h>
void putLong(long n)
{
   Value val;
   val.ev_type = 'I';
   val.ev_long = n;
   val.ev_width = 10;
    PutValue(&val);
}
FAR Example(ParamBlk FAR *parm)
{
   FCHAN fchan =  FCreate("temp.txt", FC NORMAL);
    FCHSize(fchan, 8196);
    FFlush(fchan);
    FSeek(fchan, 0, FS FROMBOF);
    PutStr("\n FSeek(fchan, 0, FS FROMBOF)");
    PutStr("\n FEOF(fchan) ="); putLong(_FEOF(fchan));
   _FSeek(fchan, 0, FS_FROMEOF);
   _PutStr("\n_FSeek(fchan, 0, FS_FROMEOF)");
   _PutStr("\n_FEOF(fchan) ="); putLong(_FEOF(fchan));
}
FoxInfo myFoxInfo[] = {
   {"FEOF", (FPFI) Example, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
