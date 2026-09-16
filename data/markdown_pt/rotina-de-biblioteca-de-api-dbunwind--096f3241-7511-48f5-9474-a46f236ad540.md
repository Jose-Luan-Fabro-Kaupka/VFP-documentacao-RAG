# Rotina de biblioteca de API _DBUnwind( )

Funciona como o comando GO BOTTOM do Visual FoxPro na área de trabalho especificada e, em seguida, retorna o número do registro atual.

```foxpro
long _DBUnwind(int workarea)
int workarea;               /* Work area. */
```

# Exemplo

O exemplo a seguir chama _DBUnwind( ) para a tabela aberta na área de trabalho atual.

### Código do Visual FoxPro

```foxpro
SET LIBRARY TO DBUNWIND
DO CreateTest
? DBUNWIND()   && returns new record #
SKIP
? EOF()       && now EOF() returns .T.
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
   _RetInt(_DBUnwind(-1), 10);
}
FoxInfo myFoxInfo[] = {
   {"DBUNWIND", (FPFI) Example, 0, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
