# Rotina de biblioteca de API _FClose( )

Encerra o acesso a um arquivo.

```foxpro
int _FClose(FCHAN chan)
FCHAN chan;               /* File channel of file to close. */
```

# Observações

Quaisquer buffers modificados enquanto estavam abertos são automaticamente gravados em disco. Se o arquivo tiver o atributo TEMPORARY, FClose( ) o excluirá. _FClose( ) retorna 0 se o arquivo for fechado com êxito ou –1 caso contrário.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acesso à API do Visual FoxPro.

# Exemplo

O exemplo a seguir cria o arquivo Temp.txt, define seu tamanho como 8196 bytes e o fecha usando _FClose( ).

### Código do Visual FoxPro

```foxpro
SET LIBRARY TO FCLOSE
DIR temp.txt
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   FCHAN fchan = _FCreate("temp.txt", FC_NORMAL);
   _FCHSize(fchan, 8196);
   _FClose(fchan);
}
FoxInfo myFoxInfo[] = {
   {"FCHSIZE", (FPFI) Example, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
