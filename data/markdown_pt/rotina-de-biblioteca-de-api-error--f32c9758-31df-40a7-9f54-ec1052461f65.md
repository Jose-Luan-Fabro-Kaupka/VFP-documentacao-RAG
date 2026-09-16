# Rotina de biblioteca de API _Error( )

Sinaliza o erro especificado pelo valor em code para o tempo de execução Visual FoxPro.

```foxpro
void _Error(int code)
int code;                     /* Internal Visual FoxPro
 error number. */
```

# Observações

O parâmetro code é um número de erro interno Visual FoxPro e pode ser passado como valor positivo ou negativo. _Error( ) transfere o controle para o manipulador de erros Visual FoxPro para que o erro possa ser tratado como qualquer outro erro Visual FoxPro. O controle do fluxo do programa não retorna à rotina que chamou _Error( ), mesmo quando o usuário escolhe ignorar o erro. A execução retoma na próxima instrução Visual FoxPro.

Consulte o tópico Visual FoxPro Error Numbers na Ajuda para números de erro e seus significados.

> **Observação:** Não use _Error() de um manipulador de eventos.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir chama _Error( ) quando _DBSkip( ) retorna um número de erro. O código Visual FoxPro mostra como fazer _Error( ) ser chamado.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO ERROR
DO CreateTest
ON ERROR DO expectError
USE
= DBSKIP(1)  && _Error() called: no DBF in use
USE test
GO TOP
= DBSKIP(-1)
= DBSKIP(-1)    && _Error() called: at top of file
GO BOTT
= DBSKIP(1)
= DBSKIP(1)  && _Error() called: at bottom of file
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
