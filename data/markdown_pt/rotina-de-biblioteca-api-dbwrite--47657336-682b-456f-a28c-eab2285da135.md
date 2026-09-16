# Rotina de Biblioteca API _DBWrite( )

Grava no disco o registro atual na área de trabalho especificada e atualiza todos os índices afetados.

```foxpro
int _DBWrite(int workarea)
int workarea;               /* Work area. */
```

# Observações

Sempre que o ponteiro de registro é movido para outro registro, essa atualização ocorre automaticamente. Se nenhum dado de campo foi substituído, _DBWrite( ) não tem efeito. _DBWrite( ) retorna 0 se a rotina for bem-sucedida. Se a rotina falhar, _DBWrite( ) retorna um inteiro negativo cujo valor absoluto é um número de erro do Visual FoxPro.

Para obter mais informações sobre como criar uma biblioteca API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir executa um _DBReplace( ) usando os dois parâmetros de chamada, um um campo de tabela passado por referência, o outro um valor do tipo apropriado. Ele executa um comando Visual FoxPro LIST NEXT 1 antes e depois de uma chamada a _DBWrite( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO DBWRITE
DO CreateTest
GO 3
=DBWRITE( @ABC, "Replacement Record 1")
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
   int RetValue;
   if (RetValue = _DBReplace(&parm->p[0].loc, &parm->p[1].val)) {
      _UserError("\\n_DBReplace() failed");
   }
   if (RetValue = _DBWrite(-1)) {
      _Error(-RetValue);
   }
   _Execute("LIST NEXT 1");
}
FoxInfo myFoxInfo[] = {
   {"DBWRITE", (FPFI) Example, 2, "R,?"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
