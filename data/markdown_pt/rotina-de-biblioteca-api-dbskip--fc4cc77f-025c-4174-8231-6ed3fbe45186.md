# Rotina de biblioteca API _DBSkip( )

_DBSkip( ) move o ponteiro de registro na área de trabalho especificada pelo número especificado de registros.

```foxpro
long _DBSkip(int workarea, long distance)
int workarea;               /* Work area. */
long distance;               /* Number of records to skip. */
```

# Observações

_DBSkip( ) respeita as expressões de índice e filtro ativas, assim como o comando SKIP do Visual FoxPro. A distância pode ser positiva ou negativa. _DBSkip( ) retorna o número do registro do novo registro.

Use _DBStatus( ) para verificar condições de final de arquivo e início de arquivo. Se você tentar avançar a partir do final do arquivo ou retroceder a partir do início do arquivo, _DBSkip( ) retorna um inteiro negativo cujo valor absoluto é um número de erro do Visual FoxPro.

Para obter mais informações sobre como criar uma biblioteca API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir funciona como o comando SKIP do Visual FoxPro.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO DBSKIP
ON ERROR DO expectError
DO CreateTest
USE
= DBSKIP(1)       && _Error() called: no DBF in use
USE test
GO TOP
= DBSKIP(-1)
= DBSKIP(-1)      && _Error() called: at top of file
GO BOTT
= DBSKIP(1)
= DBSKIP(1)      && _Error() called: at bottom of file
ON ERROR
PROCEDURE expectError
   ? "ERROR: " + MESSAGE()
RETURN
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
FAR Example(ParamBlk FAR *pblk)
{
   int RetCode;
   if ((RetCode = _DBSkip(-1, pblk->p[0].val.ev_long)) < 0) {
      _PutStr("\nError encountered in example program.");
      _Error(-RetCode);  // _DBSkip() returns negative error code
   }
   _RetInt(RetCode, 10);
}
FoxInfo myFoxInfo[] = {
   {"DBSKIP", (FPFI) Example, 1, "I"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
