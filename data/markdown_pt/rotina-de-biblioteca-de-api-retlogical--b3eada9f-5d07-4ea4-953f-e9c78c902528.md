# Rotina de biblioteca de API _RetLogical( )

Define o valor de retorno da biblioteca como um valor lógico.

```foxpro
void _RetLogical(int flag)
int flag;                     /* Flag. */
```

# Observações

_RetLogical( ) considera zero como False e qualquer valor diferente de zero como True.

Para mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir é um lançamento de moeda. Retorna .T. ou .F. com base na função de biblioteca RAND( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO RETLOGIC
? RETLOGICAL()  && returns .T. or .F. pseudo-randomly
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   _RetLogical(rand() % 2);
}
FoxInfo myFoxInfo[] = {
   {"RETLOGICAL", (FPFI) Example, 0, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
