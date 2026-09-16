# Rotina de biblioteca de API _EdGetLinePos( )

Retorna a posição de deslocamento do primeiro caractere da linha especificada no arquivo na janela de edição especificada.

```foxpro
EDPOS _EdGetLinePos(WHANDLE wh, EDLINE theLine)
WHANDLE wh;            /* Handle of editing window. */
EDLINE theLine;            /* Line number. */
```

# Exemplo

O exemplo a seguir abre uma sessão de edição para um arquivo especificado por um parâmetro e obtém o EDPOS da linha 12 chamando _EdGetLinePos( ). Em seguida, chama _EdGetLineNum( ) neste EDPOS, e isso retorna 12. Depois, incrementa o EDPOS e, a cada vez, chama _EdGetLineNum( ) até que o EDLINE retornado seja alterado. Nesse ponto, chama _EdGetLinePos( ) para a linha 13.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EDGETLPO
= EDGETLPOS("x")
```

### Código C

```foxpro
#include <pro_ext.h>
void putLong(unsigned long n)
{
   Value val;
   val.ev_type = 'I';
   val.ev_long = n;
   val.ev_width = 6;
   _PutValue(&val);
}
FAR Example(ParamBlk FAR *parm)
{
#define pFILENAME ((char FAR *) _HandToPtr(parm->p[0].val.ev_handle))
   WHANDLE wh;
   EDENV EdEnv;
   EDPOS edpos;
   EDLINE edlin, original;
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length+1))
   {
      _Error(182); // "Insufficient memory"
   }
   pFILENAME[parm->p[0].val.ev_length] = '\0';
   _HLock(parm->p[0].val.ev_handle);
   wh = _EdOpenFile(pFILENAME, FO_READONLY);
   _HUnLock(parm->p[0].val.ev_handle);
   edpos = _EdGetLinePos(wh, 12);
   _PutStr("\n_EdGetLinePos(wh, 12) =");
   putLong(edpos);
   original = edlin = _EdGetLineNum(wh, edpos);
   for (;;)
   {
      _PutStr("\n_EdGetLineNum(wh,");
      putLong(edpos);
      _PutStr(") = ");
      putLong(edlin);
      if (edlin != original)
      {
         break;
      }
      edpos++;
      edlin = _EdGetLineNum(wh, edpos);
   }
   edpos = _EdGetLinePos(wh, 13);
   _PutStr("\n_EdGetLinePos(wh, 13) ="); putLong(edpos);
}
FoxInfo myFoxInfo[] = {
   {"EDGETLPOS", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
