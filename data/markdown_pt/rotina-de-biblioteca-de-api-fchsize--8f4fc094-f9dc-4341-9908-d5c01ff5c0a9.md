# Rotina de biblioteca de API _FCHSize( )

Define o tamanho no disco do arquivo especificado para o comprimento especificado.

```foxpro
int _FCHSize(FCHAN chan, long length)
FCHAN chan;               /* File to change. */
long length;                  /* New length for the file in bytes. */
```

# Observações

O comprimento especificado pode estender ou truncar o arquivo. _FCHSize( ) retorna 0 se for bem-sucedido em alterar o comprimento do arquivo, ou – 1 se falhar.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir cria um arquivo Temp.txt e define seu tamanho para 8196 bytes usando _FCHSize( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO FCHSIZE
DIR  temp.txt
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   FCHAN fchan = _FCreate("temp.txt", FC_NORMAL);
   _FCHSize(fchan, 8196);
   _FClose(fchan);
}
FoxInfo myFoxInfo[] = {
   {"FCHSIZE", (FPFI) Example, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
