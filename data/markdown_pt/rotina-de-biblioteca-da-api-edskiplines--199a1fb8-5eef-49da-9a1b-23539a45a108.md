# Rotina de biblioteca da API _EdSkipLines( )

Move o ponto de inserção para o início da linha localizada a int linhas de sua posição de deslocamento atual thePos.

```foxpro
EDPOS _EdSkipLines(WHANDLE wh, EDPOS thePos, int offset)
WHANDLE wh;            /* Handle of editing window. */
EDPOS thePos;               /* Current offset position. */
int offset;                     /* Number of lines to skip. */
```

# Observações

Você pode especificar um número positivo ou negativo de linhas.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acesso à API do Visual FoxPro.

# Exemplo

O exemplo a seguir abre para edição um arquivo especificado por um parâmetro. Ele usa _EdSkipLines( ) para localizar as posições de deslocamento e, em seguida, seleciona as linhas 3 e 4.

### Código do Visual FoxPro

```foxpro
SET LIBRARY TO EDSKIPLI
= SKIPLINE("x")
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
#define pFILENAME ((char FAR *) _HandToPtr(parm->p[0].val.ev_handle))
   WHANDLE wh;
   EDPOS edpos;
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length+1))
   {
      _Error(182); // "Insufficient memory"
   }
   pFILENAME[parm->p[0].val.ev_length] = '\0';
   _HLock(parm->p[0].val.ev_handle);
   wh = _EdOpenFile(pFILENAME, FO_READWRITE);
   _HUnLock(parm->p[0].val.ev_handle);
   // select next two lines
   edpos = _EdSkipLines(wh, 0, 2); // skip to two lines from top
   _EdSelect(wh, edpos, _EdSkipLines(wh, edpos, 2));
   _Execute("WAIT WINDOW 'Using _EdSkipLines() \
      to select lines 3 and 4'");
}
FoxInfo myFoxInfo[] = {
   {"SKIPLINE", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
