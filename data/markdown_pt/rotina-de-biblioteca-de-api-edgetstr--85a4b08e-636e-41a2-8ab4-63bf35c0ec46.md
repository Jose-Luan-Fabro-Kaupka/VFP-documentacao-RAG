# Rotina de biblioteca de API _EdGetStr( )

Coloca o texto entre e incluindo as posições de deslocamento especificadas no endereço especificado.

```foxpro
void _EdGetStr(WHANDLE wh, EDPOS thePos, EDPOS thePos,
               TEXT *theStr)
WHANDLE wh;            /* Handle of editing window. */
EDPOS thePos;               /* Starting offset position. */
EDPOS thePos;               /* Stopping offset position. */
TEXT *theStr;               /* Where to put the text. */
```

# Exemplo

O exemplo a seguir recebe um nome de arquivo como parâmetro e retorna os primeiros 16 bytes do arquivo.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EDGETSTR
? EDGETSTR("x") && returns the first 16 characters of file "x"
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   WHANDLE wh;
   char FAR *buffer;
   char FAR *pFileName;
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length+1))
   {
      _Error(182); // "Insufficient memory"
   }
   _HLock(parm->p[0].val.ev_handle);
   pFileName = _HandToPtr(parm->p[0].val.ev_handle);
   pFileName[parm->p[0].val.ev_length] = '\0';
   wh = _EdOpenFile(pFileName, FO_READONLY);
   _HUnLock(parm->p[0].val.ev_handle);
   if ((buffer = _Alloca(17)) == 0) {
      _Error(182); // "Insufficient memory"
   }
   _EdGetStr(wh, 0, 15, buffer);
   buffer[16] = '\0';
   _RetChar(buffer);
}
FoxInfo myFoxInfo[] = {
   {"EDGETSTR", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
