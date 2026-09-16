# Rotina de biblioteca da API _FSeek( )

Move o ponteiro de arquivo para um novo local especificado por posição e modo.

```foxpro
long _FSeek(FCHAN chan, long position, int mode)
FCHAN chan;               /* File channel. */
long position;               /* Position in file. */
int mode;                     /* How to determine new location */
```

# Observações

Se mode for 0 (absoluto), o ponteiro será definido como position. Se for 1 (relativo ao ponteiro), position será somado à posição atual. Se for 2 (relativo ao fim), _FSeek( ) moverá o ponteiro além do fim. A função retorna a nova posição. Por exemplo, _FSeek(chan, 0L, 2) move para o fim e retorna o tamanho em bytes.

Para criar e integrar uma biblioteca de API, consulte Acesso à API do Visual FoxPro.

# Exemplo

O exemplo contém uma rotina de API que recebe o nome de um arquivo e um inteiro. Ela abre o arquivo, usa _FSeek( ) com FS_FROMBOF para mover o ponteiro ao deslocamento indicado e lê um byte.

### Código do Visual FoxPro

```foxpro
SET LIBRARY TO FSEEK
fc = FCREATE("x", 0)
= FPUTS(fc, "abcdefghijklmnopqrstuvwxyz", 26)
= FCLOSE(fc)
? XFSEEK("x", 2)  && displays 3rd byte of file x as an integer
? XFSEEK("x", 4)  && displays 5th byte of file x as an integer
DELETE FILE x
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   FCHAN fchan;
   char x;
   // Null terminate file name
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length+1))
   {
      _Error(182); // "Insufficient memory"
   }
   _HLock(parm->p[0].val.ev_handle);
   ((char FAR *) _HandToPtr(parm->p[0].val.ev_handle))
      [parm->p[0].val.ev_length] = '\0';
   if ((fchan=_FOpen((char FAR*)_HandToPtr(parm->p[0].val.ev_handle),
      FC_NORMAL)) < 0)
   {
      _UserError("Could not open file.");
   }
   _HUnLock(parm->p[0].val.ev_handle);
   _FSeek(fchan, parm->p[1].val.ev_long, FS_FROMBOF);
   _FRead(fchan, &x, 1);
   _RetInt(x, 10);
   _FClose(fchan);
}
FoxInfo myFoxInfo[] = {
   {"XFSEEK", (FPFI) Example, 2, "C,I"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
