# Rotina de biblioteca da API _FError( )

Retorna o número do último erro de operação de arquivo registrado para qualquer canal de arquivo.

```foxpro
int _FError(void any)
void any;                     /* Pointer. */
```

# Exemplo

O exemplo a seguir usa _FOpen( ) para tentar abrir um arquivo chamado Nofile.abc, que presumivelmente não existe. Ele então chama _FError( ), que retorna o número de erro 2, para "arquivo não encontrado."

### Código Visual FoxPro

```foxpro
SET LIBRARY TO FERROR
```

### Código C

```foxpro
#include <pro_ext.h>
void putLong(long n)
{
   Value val;
   val.ev_type = 'I';
   val.ev_long = n;
   val.ev_width = 10;
   _PutValue(&val);
}
FAR Example(ParamBlk FAR *parm)
{
   FCHAN fchan = _FOpen("nofile.abc", FC_READONLY);
   _PutStr("\nAttempted to _FOpen() a file which does not exist.");
   _PutStr("\n_FError() ="); putLong(_FError());
}
FoxInfo myFoxInfo[] = {
   {"FERROR", (FPFI) Example, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
