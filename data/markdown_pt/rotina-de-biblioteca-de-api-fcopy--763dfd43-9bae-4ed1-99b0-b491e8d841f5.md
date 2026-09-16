# Rotina de biblioteca de API _FCopy( )

Tenta copiar len bytes da posição de deslocamento spos no arquivo de origem sc para a posição de deslocamento dpos no arquivo de destino dc.

```foxpro
int _FCopy(FCHAN dc, long dpos, FCHAN sc, long spos, long len)
FCHAN dc;                  /* File channel of destination file. */
long dpos;                  /* Offset position to start copying to. */
FCHAN sc;                  /* File channel of source file. */
long spos;                  /* Offset position to start copying from. */
long len;                     /* Number of bytes to copy. */
```

# Observações

_FCopy( ) retorna True (um inteiro diferente de 0) se tiver sucesso, ou False (0) se falhar.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir cria dois arquivos. Ele grava o texto "Hello, world" no primeiro desses arquivos e depois copia o conteúdo deste arquivo, começando no terceiro byte, para o segundo arquivo.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO FCOPY
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   FCHAN fchan1, fchan2;
   int len;
   fchan1 = _FCreate("temp1.txt", FC_NORMAL);
   _FPuts(fchan1, "Hello, world.");
   _FFlush(fchan1);
   len = _FSeek(fchan1, 0, FS_FROMEOF); // determine length of file
   fchan2 = _FCreate("temp2.txt", FC_NORMAL);
   _FCopy(fchan2, 0, fchan1, 2, len - 2);
   _FClose(fchan1);
   _FClose(fchan2);
}
FoxInfo myFoxInfo[] = {
   {"FCOPY", (FPFI) Example, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
