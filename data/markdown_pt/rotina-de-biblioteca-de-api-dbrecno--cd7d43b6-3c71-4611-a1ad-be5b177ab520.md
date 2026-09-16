# Rotina de biblioteca de API _DBRecNo( )

Retorna o número do registro atual na tabela aberta na área de trabalho especificada.

```foxpro
long _DBRecNo(int workarea)
int workarea;               /* Work area. */
```

# Observações

Se nenhuma tabela estiver aberta na área de trabalho especificada, _DBRecNo( ) retorna um inteiro negativo cujo valor absoluto é um número de erro do Visual FoxPro. Se o ponteiro de registro estiver no final do arquivo, _DBRecNo( ) retorna um número que é 1 maior que o retornado por _DBRecCount( ).

Para mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir fornece funcionalidade semelhante à da função RECNO( ) do Visual FoxPro.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO DBRECNO
DO CreateTest
GO 3
? DBRECNO()
GO 6
? DBRECNO()
USE
? DBRECNO()  && returns -119
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
   APPEND BLANK
   REPLACE ABC WITH "This is record 5"
   APPEND BLANK
   REPLACE ABC WITH "This is record 6"
   GO TOP
RETURN
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   _RetInt(_DBRecNo(-1), 10);
}
FoxInfo myFoxInfo[] = {
   {"DBRECNO", (FPFI) Example, 0, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
