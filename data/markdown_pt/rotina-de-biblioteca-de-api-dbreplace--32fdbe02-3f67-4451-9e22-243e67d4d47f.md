# Rotina de biblioteca de API _DBReplace( )

_DBReplace( ) coloca um novo valor em um campo.

```foxpro
int _DBReplace(Locator FAR *fld, Value FAR *val)
Locator FAR *fld;            /* Field to be replaced. */
Value FAR *val;            /* Value to be placed in field. */
```

# Observações

_DBReplace( ) retorna 0 se a substituição for bem-sucedida. Se a substituição falhar, _DBReplace( ) retorna um inteiro negativo cujo valor absoluto é um número de erro do Visual FoxPro. _DBReplace( ) pode ser usado em um campo memo para substituir seu valor por um novo valor menor que 65.000 bytes. Para executar operações em campos memo maiores que 65.000 bytes, você deve usar rotinas diretas de campo memo e rotinas de entrada/saída de arquivo em buffer.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir fornece funcionalidade semelhante ao comando REPLACE do Visual FoxPro, mas substitui o valor de apenas um registro por vez.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO DBREPLAC
DO CreateTest
? DBREPLACE(@ABC, "Replacement record 1")
? DBREPLACE(@ABC, 2)  && returns -302 - field ABC is character field
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
   _RetInt(_DBReplace(&parm->p[0].loc, &parm->p[1].val), 10);
}
FoxInfo myFoxInfo[] = {
   {"DBREPLACE", (FPFI) Example, 2, "R,?"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
