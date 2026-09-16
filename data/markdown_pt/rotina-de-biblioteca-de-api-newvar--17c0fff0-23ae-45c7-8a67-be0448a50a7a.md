# Rotina de biblioteca de API _NewVar( )

Cria uma variável ou um array.

```foxpro
NTI _NewVar(char FAR *name, Locator FAR *loc, int flag)
char FAR *name;            /* Variable name. */
Locator FAR *loc;            /* Place. */
int flag;                     /* Scope. */
```

# Observações

A definição de tipo NTI significa Name Table Index. Consulte Rotina de biblioteca de API _NameTableIndex( ) para obter mais informações sobre o uso de Name Table Index.

O nome da variável ou array deve seguir as regras padrão do Visual FoxPro para nomes de variáveis. A nova variável é inicializada com o valor lógico False.

A configuração do campo Locator l_subs determina o tipo de variável ou array:
 - 0 – uma variável escalar
- 1 – um array unidimensional de tamanho l_sub1
- 2 – um array de tamanho l_sub1 por l_sub2 Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

O parâmetro flag pode ser NV_PUBLIC ou NV_PRIVATE. Variáveis NV_PRIVATE são criadas como se fossem criadas pela rotina do Visual FoxPro que chamou a rotina externa.

Se _NewVar( ) criar a variável com sucesso, o campo l_NTI é preenchido com o NTI não negativo da variável criada, e _NewVar( ) retorna esse número. Se _NewVar( ) falhar, retorna um inteiro negativo cujo valor absoluto é um número de erro interno do Visual FoxPro.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir usa _NewVar( ) para criar três variáveis.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO NEWVAR
*
* As defined in "pro_ext.h"
*
#define NV_PUBLIC   0
#define NV_PRIVATE   1
= xNewVar('var', 0, 0, 0, NV_PUBLIC)
DISPLAY MEMORY LIKE var
= xNewVar('onedim', 1, 5, 0, NV_PUBLIC)
DISPLAY MEMORY LIKE onedim
= xNewVar('twodim', 2, 5, 6, NV_PUBLIC)
DISPLAY MEMORY LIKE twodim
```

### Código C

```foxpro
#include <pro_ext.h>
void FAR NewVarEx(ParamBlk FAR *parm)
{
   char FAR *varName;
   Locator loc;
   int flag;
   int retValue;
   // Null terminate character string
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length+1))
   {
      _Error(182); // "Insufficient memory"
   }
   _HLock(parm->p[0].val.ev_handle);
   varName = (char FAR *) _HandToPtr(parm->p[0].val.ev_handle);
   varName[parm->p[0].val.ev_length] = '\0';
   loc.l_subs = parm->p[1].val.ev_long;
   loc.l_sub1 = parm->p[2].val.ev_long;
   loc.l_sub2 = parm->p[3].val.ev_long;
   flag = parm->p[4].val.ev_long;
   if ((retValue = _NewVar(varName, &loc, flag)) < 0)
   {
      // _NewVar() returns negative Visual FoxPro error number
      _Error(-retValue);
   }
   _HUnLock(parm->p[0].val.ev_handle);
}
FoxInfo myFoxInfo[] = {
   {"XNEWVAR", (FPFI) NewVarEx, 5, "C,I,I,I,I"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
