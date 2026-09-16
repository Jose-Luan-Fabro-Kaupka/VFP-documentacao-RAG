# Rotina de biblioteca de API _EdGetChar( )

_EdGetChar( ) retorna o caractere na posição de deslocamento especificada no arquivo na janela de edição especificada.

```foxpro
TEXT _EdGetChar(WHANDLE wh, EDPOS thePos)
WHANDLE wh;         /* Handle of editing window. */
EDPOS thePos;            /* Offset position in file of character
 to be returned. */
```

# Exemplo

O exemplo a seguir abre para edição um arquivo especificado por um parâmetro e exibe na tela o conteúdo completo do arquivo.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EDGETCHA
= EDGETCHAR("x")
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
#define pFILENAME ((char FAR *) _HandToPtr(parm->p[0].val.ev_handle))
   WHANDLE wh;
   EDENV EdEnv;
   EDPOS edpos;
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length+1))
   {
      _Error(182); // "Insufficient memory"
   }
   _HLock(parm->p[0].val.ev_handle);
   pFILENAME[parm->p[0].val.ev_length] = '\0';
   wh = _EdOpenFile(pFILENAME, FO_READONLY);
   _HUnLock(parm->p[0].val.ev_handle);
   _EdGetEnv(wh, &EdEnv);
   for (edpos = 0; edpos <= EdEnv.length; edpos++)
   {
      _PutChr(_EdGetChar(wh, edpos));
   }
}
FoxInfo myFoxInfo[] = {
   {"EDGETCHAR", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
