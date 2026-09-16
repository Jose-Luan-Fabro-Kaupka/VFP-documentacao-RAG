# Rotina de biblioteca de API _DBAppend( )

Tenta acrescentar um novo registro à tabela aberta na área de trabalho especificada.

```foxpro
int _DBAppend(int workarea, int carryflag)
int workarea;               /* Work area number. */
int carryflag;               /* SET CARRY setting. */
```

# Observações

A área de trabalho atual é representada por – 1. _DBAppend( ) retorna 0 se a rotina for bem-sucedida. Se a rotina falhar, _DBAppend( ) retorna um inteiro negativo cujo valor absoluto é um número de erro do Visual FoxPro.
 Valores para
| Valor | Efeito |
| --- | --- |
| 1 | Transporta informações do registro anterior para o novo registro. |
| 0 | Torna o novo registro em branco. |
| – 1 | Usa a configuração de SET CARRY para determinar se as informações do registro anterior são transportadas para o novo registro. |

_DBAppend( ) executa automaticamente qualquer bloqueio necessário. Se não conseguir bloquear o cabeçalho do arquivo, _DBAppend( ) falha e retorna um inteiro negativo cujo valor absoluto é um número de erro do Visual FoxPro.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acesso à API do Visual FoxPro.

# Exemplo

O exemplo a seguir usa _DBAppend( ) para acrescentar um registro à tabela aberta na área de trabalho atual.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO DBAPPEND
DO CreateTest
SET CARRY ON
= DBAPPEND(-1)   && SET CARRY is ON, so carry
SET CARRY OFF
= DBAPPEND(1)   && carry regardless of SET CARRY
= DBAPPEND(-1)   && SET CARRY is OFF, so no carry
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
FAR Example(ParamBlk FAR *parm)
{
   int RetCode;
   if ((RetCode = _DBAppend(-1, (int) parm->p[0].val.ev_long)) < 0) {
      _Error(-RetCode);
   }
}
FoxInfo myFoxInfo[] = {
   {"DBAPPEND", (FPFI) Example, 1, "I"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
