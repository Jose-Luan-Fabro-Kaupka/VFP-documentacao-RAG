# _FGets( ) API Library Routine

Copia para o buffer uma única linha do arquivo especificado, começando na posição atual no arquivo.

```foxpro
unsigned int _FGets(FCHAN chan, char FAR *buffer, int maxlen)
FCHAN chan;               /* File channel of file from which to copy. */
char FAR *buffer;            /* Buffer address. */
int maxlen;                  /* Maximum length of line in bytes. */
```

Observações

_FGets( ) copia uma linha de comprimento máximo, delimitada com um retorno de carruagem. O retorno da carruagem é traduzido para um terminador nulo e armazenado no buffer. Os feeds de linha são ignorados e não são copiados para o buffer. _FGets( ) retorna o número de bytes copiados para o buffer.

For more information on how to create an API library and integrate it with Visual FoxPro, see Accessing the Visual FoxPro API.

Exemplo

O exemplo a seguir abre um arquivo especificado por um parâmetro, e copia e mostra cada linha no arquivo.

### Visual FoxPro Code

```foxpro
SET LIBRARY TO FGETS
fc = FCREATE("x", 0)
= FPUTS(fc, REPL("X", 512), 512)
= FCLOSE(fc)
= XFGETS("x")
DELETE FILE x
```

Código C

```foxpro
#include <pro_ext.h>
#define BUFFSIZE 256
static char lineBuffer[BUFFSIZE];
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
   FCHAN fchan;
//   Null terminate file name
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
   while (!_FEOF(fchan))
   {
      _FGets(fchan, lineBuffer, BUFFSIZE);
      _PutStr(lineBuffer); _PutChr('\n');
   }
   _FClose(fchan);
}
FoxInfo myFoxInfo[] = {
   {"XFGETS", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```

Veja também
- _FRead( ) API Library Routine
- _FSeek( ) API Library Routine
- API Library Construction
- Accessing the Visual FoxPro API
