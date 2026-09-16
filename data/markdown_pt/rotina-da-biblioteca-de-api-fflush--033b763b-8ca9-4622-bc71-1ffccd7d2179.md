# Rotina da biblioteca de API _FFlush( )

Grava em disco todos os buffers modificados na memória para o arquivo especificado.

```foxpro
int _FFlush(FCHAN chan)
FCHAN chan;               /* File channel of file to flush. */
```

# Observações

_FFlush( ) retorna 0 se conseguir gravar os buffers ou – 1 se falhar.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir cria um arquivo e define seu tamanho como 8196 bytes. A execução da linha de comando DIR TEMP.TXT do Visual FoxPro na janela Command mostra que o tamanho do arquivo no disco ainda é 0. Contudo, depois de executar = XFFLUSH( ), a emissão da linha de comando DIR TEMP.TXT mostra que o arquivo no disco reflete a chamada _FCHSize( ) e tem 8196 bytes.

### Código do Visual FoxPro

```foxpro
SET LIBRARY TO FFLUSH
DIR temp.txt  && size on disk is still 0
WAIT WINDOW "File Size = 0"
= XFFLUSH()
DIR temp.txt  && size on disk is 8196
WAIT WINDOW "File Size Does Not Equal 0"
CLOSE ALL
```

### Código C

```foxpro
#include <pro_ext.h>
static FCHAN fchan;
FAR CreateIt(ParamBlk FAR *parm)
{
   fchan = _FCreate("temp.txt", FC_NORMAL);
   _FCHSize(fchan, 8196);
}
FAR FFlushEx(ParamBlk FAR *parm)
{
   _FFlush(fchan);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) CreateIt, CALLONLOAD, ""},
   {"XFFLUSH", (FPFI) FFlushEx, 0, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
