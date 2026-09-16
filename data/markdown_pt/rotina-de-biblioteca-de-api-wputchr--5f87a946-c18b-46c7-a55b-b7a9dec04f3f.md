# Rotina de biblioteca de API _WPutChr( )

Exibe um caractere char na posição de saída na janela especificada e na cor atual.

```foxpro
void _WPutChr(WHANDLE wh, int char)
WHANDLE wh;            /* Window handle. */
int char;                     /* Character to display. */
```

# Observações

Caracteres especiais como nova linha, retorno de carro e sino são tratados como caracteres de controle e não são exibidos na tela.

Para mostrar o caractere que corresponde a um desses caracteres de controle, adicione 256 ao valor do caractere.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir usa _WPutChr( ) para exibir todos os valores de 8 bits em uma nova janela.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WPUTCHR
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   int i;
   WHANDLE wh;
   wh = _WOpen(2,2,20,70,WEVENT | CLOSE,WINDOW_SCHEME,(Scheme FAR *) 0,
      WO_SYSTEMBORDER);
   _WShow(wh);
   for (i = 0; i < 256; i++)
      _WPutChr(wh, i);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) Example, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
