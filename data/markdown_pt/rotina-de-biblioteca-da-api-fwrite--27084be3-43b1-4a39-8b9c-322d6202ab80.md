# Rotina de biblioteca da API _FWrite( )

Grava exatamente length bytes do buffer no arquivo especificado por chan.

```foxpro
unsigned int _FWrite(FCHAN chan, char FAR *buffer, int length)
FCHAN chan;               /* File channel of file to write to. */
char FAR *buffer;            /* Buffer address. */
int length;                  /* Number of bytes to write. */
```

# Observações

_FWrite( ) não adiciona terminador ao arquivo nem converte os bytes. Retorna o número de bytes gravados.

# Exemplo

O exemplo cria um arquivo e grava dados com _FWrite( ).

### Código do Visual FoxPro

```foxpro
SET LIBRARY TO FWRITE
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   FCHAN fchan;
   fchan = _FCreate("temp.tmp", FC_NORMAL);
   _FWrite(fchan, "Hello, world.", _StrLen("Hello, world."));
   _FWrite(fchan, "\xd\xa", 2);
   _FWrite(fchan, "1234567890", 10);
   _FClose(fchan);
}
FoxInfo myFoxInfo[] = {
   {"FWRITE", (FPFI) Example, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
