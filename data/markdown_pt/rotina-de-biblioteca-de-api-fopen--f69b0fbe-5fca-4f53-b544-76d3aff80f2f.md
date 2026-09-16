# Rotina de biblioteca de API _FOpen( )

Atribui um canal do Visual FoxPro a um arquivo existente.

```foxpro
FCHAN _FOpen(char FAR *filename, int mode)
char FAR *filename;         /* Name of existing file */
int mode;                     /* Mode option. */
```

# Observações

As seguintes opções de modo estão disponíveis: FO_READONLY, FO_WRITEONLY e FO_READWRITE. _FOpen( ) abre um arquivo com acesso exclusivo. _FOpen( ) retorna o canal do arquivo se tiver sucesso ao abrir o arquivo, ou retorna – 1 se não conseguir abrir o arquivo.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir cria um arquivo de teste. Ele então abre o arquivo no modo FO_READONLY e tenta gravar nele. Como resultado, _FError( ) retorna 5 para "Access denied." Em seguida, o exemplo abre o arquivo de teste no modo FO_WRITEONLY e tenta ler dele. Novamente, _FError( ) retorna 5.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO FOPEN
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
#define BUFFSIZE 256
static char lineBuffer[BUFFSIZE];
FAR Example(ParamBlk FAR *parm)
{
   FCHAN fchan;
   fchan = _FCreate("temp.tmp", FC_NORMAL);
   _FCHSize(fchan, 8192);
   _FClose(fchan);
   fchan = _FOpen("temp.tmp", FO_READONLY);
   _FPuts(fchan, "Hello, world");
   _PutStr("\nAttempt to _FPuts() to file _FOpen()d FO_READONLY");
   _PutStr("\n_FError() ="); putLong(_FError());
   _FClose(fchan);
   fchan = _FOpen("temp.tmp", FO_WRITEONLY);
   _FGets(fchan, lineBuffer, BUFFSIZE);
   _PutStr("\nAttempt to _FGets() from file _FOpen()d FO_WRITEONLY");
   _PutStr("\n_FError() ="); putLong(_FError());
   _FClose(fchan);
}
FoxInfo myFoxInfo[] = {
   {"FOPEN", (FPFI) Example, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
