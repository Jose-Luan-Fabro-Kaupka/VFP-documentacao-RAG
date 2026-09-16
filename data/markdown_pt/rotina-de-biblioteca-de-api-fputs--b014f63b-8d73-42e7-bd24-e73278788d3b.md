# Rotina de biblioteca de API _FPuts( )

Grava uma cadeia de caracteres terminada em nulo especificada em um arquivo, seguida por um par de retorno de carro/avanço de linha.

```foxpro
unsigned int _FPuts(FCHAN chan, char FAR *buffer)
FCHAN chan;               /* File channel of file to write to. */
char FAR *buffer;            /* String to write. */
```

# Observações

_FPuts( ) retorna o número total de bytes que grava no arquivo.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir cria um arquivo e grava o texto "Hello, world." no arquivo usando _FPuts( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO FPUTS
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   FCHAN fchan;
   fchan = _FCreate("temp.tmp", FC_NORMAL);
   _FPuts(fchan, "Hello, world.");
   _FClose(fchan);
}
FoxInfo myFoxInfo[] = {
   {"FPUTS", (FPFI) Example, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
