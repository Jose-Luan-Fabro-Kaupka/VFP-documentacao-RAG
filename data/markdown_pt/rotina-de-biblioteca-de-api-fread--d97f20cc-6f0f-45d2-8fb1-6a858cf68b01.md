# Rotina de biblioteca de API _FRead( )

Copia para o buffer exatamente length bytes de um arquivo para buffer.

```foxpro
unsigned int _FRead(FCHAN chan, char FAR *buffer, int length)
FCHAN chan;               /* File channel of file from which to copy. */
char FAR *buffer;            /* Buffer address. */
int length;                  /* Number of bytes to be copied. */
```

# Observações

_FRead( ) não adiciona um terminador ao final dos bytes no buffer. Nenhuma tradução é executada nos bytes quando são armazenados no buffer. _FRead( ) retorna o número de bytes lidos.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir cria um arquivo de teste e coloca texto nele. O exemplo então tenta ler 32 bytes do arquivo usando _FRead( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO FREAD
```

### Código C

```foxpro
#include <pro_ext.h>
#define BUFFSIZE 32
static char buffer[BUFFSIZE];
FAR Example(ParamBlk FAR *parm)
{
   FCHAN fchan;
   int bytesRead;
   fchan = _FCreate("temp.tmp", FC_NORMAL);
   _FPuts(fchan, "Hello, world.");
   _FPuts(fchan, "Hello, world.");
   _FPuts(fchan, "Hello, world.");
   _FPuts(fchan, "Hello, world.");
   _FPuts(fchan, "Hello, world.");
   _FSeek(fchan, 0, FS_FROMBOF);
   bytesRead = _FRead(fchan, buffer, BUFFSIZE - 1);
   buffer[bytesRead] = '\0';
   _PutStr(buffer);
   _FClose(fchan);
}
FoxInfo myFoxInfo[] = {
   {"FREAD", (FPFI) Example, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
