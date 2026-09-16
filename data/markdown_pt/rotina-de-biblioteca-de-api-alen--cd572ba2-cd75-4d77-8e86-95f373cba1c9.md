# Rotina de biblioteca de API _ALen( )

Retorna informações sobre as dimensões da matriz cujo índice de tabela de nomes é nti.

```foxpro
long _ALen(NTI nti, int mode)
NTI nti;                     /* Array name table index. */
int mode;                     /* Mode to determine return value. */
```

# Observações

Se mode for AL_ELEMENTS, _ALen( ) retorna o número total de elementos na matriz. Se mode for AL_SUBSCRIPT1, _ALen( ) retorna o valor do primeiro subscrito usado para declarar a matriz. Se mode for AL_SUBSCRIPT2, _ALen( ) retorna o valor do segundo subscrito usado para declarar a matriz.

Se nti não representar o nome de uma matriz existente, _ALen( ) retorna – 1 independentemente do valor de mode.

Para mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir fornece uma rotina de API do Visual FoxPro para cada um dos três valores possíveis de mode.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO ALEN
DIMENSION a[10, 11]
? ALENELEM(@a)  && returns 110
? ALENSUB1(@a)  && returns 10
? ALENSUB2(@a)  && returns 11
DIMENSION b[3]
? ALENELEM(@b)  && returns 3
? ALENSUB1(@b)  && returns 3
? ALENSUB2(@b)  && returns 0; no second subscript
c = .F.
? ALENELEM(@c)  && returns -1 because variable "c" is not an array
? ALENSUB1(@c)  && returns -1 because variable "c" is not an array
? ALENSUB2(@c)  && returns -1 because variable "c" is not an array
```

### Código C

```foxpro
#include <pro_ext.h>
void FAR alenElem(ParamBlk FAR *parm)
{
   _RetInt(_ALen(parm->p[0].loc.l_NTI, AL_ELEMENTS), 10);
}
void FAR alenSub1(ParamBlk FAR *parm)
{
   _RetInt(_ALen(parm->p[0].loc.l_NTI, AL_SUBSCRIPT1), 10);
}
void FAR alenSub2(ParamBlk FAR *parm)
{
   _RetInt(_ALen(parm->p[0].loc.l_NTI, AL_SUBSCRIPT2), 10);
}
FoxInfo myFoxInfo[] = {
   {"ALENELEM", (FPFI) alenElem, 1, "R"},
   {"ALENSUB1", (FPFI) alenSub1, 1, "R"},
   {"ALENSUB2", (FPFI) alenSub2, 1, "R"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
