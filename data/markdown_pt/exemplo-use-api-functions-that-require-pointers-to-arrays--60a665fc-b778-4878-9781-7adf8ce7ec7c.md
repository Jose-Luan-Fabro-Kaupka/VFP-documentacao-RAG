# Exemplo Use API Functions That Require Pointers to Arrays

Arquivo: ...\Samples\Solution\Winapi\Syscolor.scx

Este exemplo usa duas funções da API do Windows para primeiro obter as configurações de cor do sistema (GetSysColor) e depois redefinir as cores do sistema para novos valores (SetSysColors). Dois dos três argumentos exigidos por SetSysColors são ponteiros para matrizes nativas C.

# GetSysColor

A função GetSysColor aceita um parâmetro inteiro, um número entre 0 e 18, e retorna um DWORD (inteiro sem sinal de 32 bits) indicando a configuração de cor atual.

```foxpro
DWORD GetSysColor(
    int nIndex    // display element
   );
```

nIndex é um valor que representa uma área da interface, conforme definido na lista a seguir:

```foxpro
#define COLOR_SCROLLBAR         0
#define COLOR_BACKGROUND        1
#define COLOR_ACTIVECAPTION     2
#define COLOR_INACTIVECAPTION   3
#define COLOR_MENU              4
#define COLOR_WINDOW            5
#define COLOR_WINDOWFRAME       6
#define COLOR_MENUTEXT          7
#define COLOR_WINDOWTEXT        8
#define COLOR_CAPTIONTEXT       9
#define COLOR_ACTIVEBORDER      10
#define COLOR_INACTIVEBORDER    11
#define COLOR_APPWORKSPACE      12
#define COLOR_HIGHLIGHT         13
#define COLOR_HIGHLIGHTTEXT     14
#define COLOR_BTNFACE           15
#define COLOR_BTNSHADOW         16
#define COLOR_GRAYTEXT          17
#define COLOR_BTNTEXT           18
#define COLOR_INACTIVECAPTIONTEXT 19
#define COLOR_BTNHIGHLIGHT      20
#if(WINVER >= 0x0400)
#define COLOR_3DDKSHADOW        21
#define COLOR_3DLIGHT           22
#define COLOR_INFOTEXT          23
#define COLOR_INFOBK            24
#define COLOR_DESKTOP           COLOR_BACKGROUND
#define COLOR_3DFACE            COLOR_BTNFACE
#define COLOR_3DSHADOW          COLOR_BTNSHADOW
#define COLOR_3DHIGHLIGHT       COLOR_BTNHIGHLIGHT
#define COLOR_3DHILIGHT         COLOR_BTNHIGHLIGHT
#define COLOR_BTNHILIGHT        COLOR_BTNHIGHLIGHT
#endif /* WINVER >= 0x0400 */
```

# SetSysColors

A função SetSysColors requer três argumentos: o número de elementos em duas matrizes e os endereços das duas matrizes.

```foxpro
BOOL WINAPI SetSysColors(
    int cElements,                  // number of elements to change
    CONST INT *lpaElements,         // address of array of elements
    CONST COLORREF *lpaRgbValues    // address of array of RGB values
   );
```

# Chamando SetSysColors no Visual FoxPro

O código a seguir é extraído de cmdSetSysColors.Click:

```foxpro
DECLARE INTEGER SetSysColors IN win32api INTEGER, STRING, STRING
```

Construa os elementos da primeira matriz em uma variável de caractere.

```foxpro
cElements = ""
FOR i = 0 TO 18
   cElements = cElements + THISFORM.DecToHex(i)
ENDFOR
```

Construa os elementos da segunda matriz em uma variável de caractere. O cursor que é percorrido foi preenchido com valores GetSysColor no Init do formulário.

```foxpro
cColors = ""
SCAN
   cColors = cColors + THISFORM.DecToHex(INT(color))
ENDSCAN
=SetSysColors(18,cElements,cColors)
```
