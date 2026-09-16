# Rotina de biblioteca de API _DBRewind( )

Funciona como o comando GO TOP do Visual FoxPro na área de trabalho especificada e, em seguida, retorna o número do registro atual.

```foxpro
long _DBRewind(int workarea)
int workarea;               /* Work area. */
```

# Exemplo

O exemplo a seguir chama _DBRewind( ) para a tabela aberta na área de trabalho atual. Isso tem o mesmo efeito que o comando GO TOP do Visual FoxPro.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO DBREWIND
DO CreateTest
GO BOTTOM
? RECNO()
? DBREWIND()    && returns 1
? RECNO()  && yes, we're at record 1
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
   _RetInt(_DBRewind(-1), 10);
}
FoxInfo myFoxInfo[] = {
   {"DBREWIND", (FPFI) Example, 0, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
