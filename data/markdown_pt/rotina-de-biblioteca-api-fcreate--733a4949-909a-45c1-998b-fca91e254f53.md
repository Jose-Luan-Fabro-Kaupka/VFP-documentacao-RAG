# Rotina de biblioteca API _FCreate( )

Atribui um canal do Visual FoxPro a um arquivo novo.

```foxpro
FCHAN _FCreate(char FAR *filename, int mode)
char FAR *filename;         /* Name of file to create. */
int mode;                     /* File attributes. */
```

# Observações

Se um arquivo com o nome especificado já existir, _FCreate( ) trunca o arquivo existente para zero bytes.

O parâmetro mode pode ser uma ou mais das seguintes flags: FC_READONLY, FC_SYSTEM, FC_HIDDEN e FC_TEMPORARY. Você pode combinar essas flags usando o operador C ou +. Uma flag adicional, FC_NORMAL, especifica que o arquivo não tem nenhum dos outros atributos. Arquivos FC_TEMPORARY são automaticamente excluídos quando você chama _FClose( ) para fechar o arquivo.

_FCreate( ) retorna o canal do arquivo se conseguir criar o arquivo, ou – 1 se falhar.

Para obter mais informações sobre como criar uma biblioteca API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir usa _FCreate( ) para criar vários arquivos usando as várias flags de modo de _FCreate( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO FCREATE
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   FCHAN fchan;
   fchan = _FCreate("normal.tmp", FC_NORMAL);
   _FClose(fchan);
   fchan = _FCreate("readonly.tmp", FC_READONLY);
   _FClose(fchan);
   fchan = _FCreate("hidden.tmp", FC_HIDDEN);
   _FClose(fchan);
   fchan = _FCreate("system.tmp", FC_SYSTEM);
   _FClose(fchan);
   fchan = _FCreate("temp.tmp", FC_TEMPORARY);
   _FClose(fchan);
   fchan = _FCreate("multi.tmp", FC_SYSTEM | FC_READONLY);
   _FClose(fchan);
}
FoxInfo myFoxInfo[] = {
   {"FCREATE", (FPFI) Example, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
