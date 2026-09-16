# Rotina de biblioteca de API _PutChr( )

Exibe o caractere char na posição de saída na janela de saída atual em seu atributo normal (cor 0).

```foxpro
void _PutChr(int char)
int char;                     /* Character to display. */
```

# Observações

_PutChr( ) trata caracteres especiais como nova linha, retorno de carro e sino como caracteres de controle e não os exibe na tela.

Para exibir o caractere que corresponde a um desses caracteres de controle, adicione 256 ao valor do caractere.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acesso à API do Visual FoxPro.

# Exemplo

O exemplo a seguir usa _PutChr( ) para exibir todos os caracteres de 8 bits na tela.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO PUTCHR
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   int ch;
   for (ch = 0; ch < 256; ch++)
   {
      _PutChr(ch);
   }
}
FoxInfo myFoxInfo[] = {
   {"PUTCHR", (FPFI) Example, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
