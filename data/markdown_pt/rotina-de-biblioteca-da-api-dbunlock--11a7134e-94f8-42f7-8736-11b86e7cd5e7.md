# Rotina de biblioteca da API _DBUnlock( )

Libera todos os bloqueios obtidos pelo usuário em registros ou no arquivo da área de trabalho especificada por workarea.

```foxpro
void _DBUnlock(int workarea)
int workarea;               /* Work area. */
```

# Exemplo

O exemplo a seguir usa _DBUnlock( ) para desbloquear todos os registros da tabela aberta na área de trabalho atual. O código do Visual FoxPro demonstra _DBUnlock( ) e verifica se ela está funcionando corretamente.

### Código do Visual FoxPro

```foxpro
SET LIBRARY TO DBUNLOCK
DO CreateTest
USE Test SHARED
GO 2
= XRLOCK()
LIST STAT  && shows that record #2 is locked
= XUNLOCK()
LIST STAT  && shows no records are locked
= XFLOCK()
LIST STAT  && shows that whole DBF is locked
= XUNLOCK()
LIST STAT  && shows no records are locked
PROCEDURE CreateTest
CREATE TABLE test (ABC C(20))
APPEND BLANK
REPLACE ABC WITH "Golly month of"
APPEND BLANK
REPLACE ABC WITH "A twelfth of"
APPEND BLANK
REPLACE ABC WITH "Hello, world"
APPEND BLANK
REPLACE ABC WITH "When in the"
GO TOP
RETURN
```

### Código C

```foxpro
#include <pro_ext.h>
FAR xLockRecord(ParamBlk FAR *parm)
{
   _DBLock(-1, DBL_RECORD);
}
FAR xLockFile(ParamBlk FAR *parm)
{
   _DBLock(-1, DBL_FILE);
}
FAR xUnLockFile(ParamBlk FAR *parm)
{
   _DBUnLock(-1);
}
FoxInfo myFoxInfo[] = {
   {"XRLOCK",  (FPFI) xLockRecord, 0, ""},
   {"XFLOCK",  (FPFI) xLockFile, 0, ""},
   {"XUNLOCK", (FPFI) xUnLockFile, 0, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
