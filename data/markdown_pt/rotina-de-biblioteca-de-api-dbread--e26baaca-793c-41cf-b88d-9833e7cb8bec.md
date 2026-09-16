# Rotina de biblioteca de API _DBRead( )

Move o ponteiro de registro atual para o registro especificado na área de trabalho especificada.

```foxpro
int _DBRead(int workarea, long record)
int workarea;               /* Work area. */
long record;                  /* Record number. */
```

# Observações

_DBRead( ) retorna 0 se a rotina for bem-sucedida. Se a rotina falhar, _DBRead( ) retorna um inteiro negativo cujo valor absoluto é um número de erro do Visual FoxPro.

Especificar 0 para record é equivalente a emitir GO TOP; especificar – 1 para record é equivalente a emitir GO BOTTOM.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir fornece funcionalidade semelhante à do comando Visual FoxPro GO. XGO(n) move o ponteiro de registro atual para o número de registro n na área de trabalho atual.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO DBREAD
DO CreateTest
USE Test SHARED
GO BOTTOM
? RECNO()
= XGO(2)
? RECNO()
PROCEDURE CreateTest
   CREATE TABLE test (ABC C(20))
   APPEND BLANK
   REPLACE ABC WITH "This is record 1"
   APPEND BLANK
   REPLACE ABC WITH "This is record 2"
   APPEND BLANK
   REPLACE ABC WITH "This is record 3"
   APPEND BLANK
   REPLACE ABC WITH "This is record 4"
   GO TOP
RETURN
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   _DBRead(-1, parm->p[0].val.ev_long);
}
FoxInfo myFoxInfo[] = {
   {"XGO", (FPFI) Example, 1, "I"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
