# Rotina de biblioteca de API _DBLock( )

Tenta bloquear o registro atual ou a tabela aberta na área de trabalho especificada por workarea.

```foxpro
int _DBLock(int workarea, int RecOrFile)
int workarea;               /* Work area. */
int RecOrFile;               /* What is to be locked. */
```

# Observações

O parâmetro RecOrFile pode ser DBL_RECORD, para especificar o registro atual, ou DBL_FILE, para especificar o arquivo de tabela. _DBLock( ) retorna True (um inteiro diferente de 0) se o bloqueio for bem-sucedido, ou False (0) se o bloqueio não for bem-sucedido.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir fornece duas funções de API que você pode chamar do Visual FoxPro: XRLOCK( ), que bloqueia o registro atual da área de trabalho atual; e XFLOCK( ), que bloqueia a tabela aberta na área de trabalho atual. XRLOCK( ) chama _DBLock( – 1, DBL_RECORD( )), e XFLOCK( ) chama _DBLock( – 1, DBL_FILE( )).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO DBLOCK
DO CreateTest
USE Test SHARED
GO 2
= XRLOCK()
LIST STAT  && shows that record #2 is locked
= XFLOCK()
LIST STAT  && shows that whole DBF is locked
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
FoxInfo myFoxInfo[] =
{
   {"XRLOCK", (FPFI) xLockRecord, 0, ""},
   {"XFLOCK", (FPFI) xLockFile, 0, ""},
};
FoxTable _FoxTable =
{
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
