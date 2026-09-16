# Rotina de biblioteca de API _DBRecCount( )

Retorna o número total de registros na tabela aberta na área de trabalho especificada.

```foxpro
long _DBRecCount(int workarea)
int workarea;               /* Work area. */
```

# Observações

Se nenhuma tabela estiver aberta na área de trabalho especificada, _DBRecCount( ) retorna um inteiro negativo cujo valor absoluto é um número de erro do Visual FoxPro.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acesso à API do Visual FoxPro.

# Exemplo

O exemplo a seguir chama _DBRecCount( ) para contar o número de registros na tabela aberta na área de trabalho atual.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO DBRECCNT
DO CreateTest
? DBRECCOUNT()   && call API routine
? RECCOUNT()   && call built-in Visual FoxPro Function
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
   _RetInt(_DBRecCount(-1), 10);
}
FoxInfo myFoxInfo[] = {
   {"DBRECCOUNT", (FPFI) Example, 0, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
