# Rotina de biblioteca da API _RetFloat( )

Define o valor de retorno da biblioteca como um valor float.

```foxpro
void _RetFloat(double flt, int width, int dec)
double flt;                  /* Double precision floating point
 value. */
int width;                     /* Number of columns for number
 display. */
int dec;                     /* Number of decimal places. */
```

# Observações

O parâmetro width especifica o número de colunas que o Visual FoxPro usa ao exibir o número, incluindo um ponto decimal, se necessário. Se você não conhece a largura, use 20. O parâmetro dec especifica o número de casas decimais no número. Você deve definir corretamente o número de casas decimais para garantir que o Visual FoxPro processe o número corretamente. Se o número de casas decimais não for zero, width deve ser pelo menos dois maior que dec.

Para obter mais informações sobre como criar uma biblioteca da API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir usa _RetFloat( ) para retornar a representação em ponto flutuante de um parâmetro de data do Visual FoxPro.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO RETFLOAT
? RETFLOAT({2/16/95})  && returns float representation of date {2/16/95}
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   _RetFloat(parm->p[0].val.ev_real, 20, 4);
}
FoxInfo myFoxInfo[] = {
   {"RETFLOAT", (FPFI) Example, 1, "D"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
