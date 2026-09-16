# SYS(2325) - WCLIENTWINDOW a partir de WHANDLE do Visual FoxPro

Retorna o WHANDLE de uma janela cliente a partir do WHANDLE da janela pai.

```foxpro
SYS(2325, nWHANDLE)
```

#### Parâmetros
 **nWHANDLE**
Especifica um WHANDLE inteiro para uma janela FoxPro. Um WHANDLE é uma estrutura interna do Visual FoxPro (representada por um inteiro) que é um wrapper em torno do hWnd da janela cliente interna.

# Valor de retorno

Numérico.

SYS(2325) retorna o WHANDLE (identificador de janela interno VFP) para uma janela cliente (WCLIENTWINDOW) de uma janela pai Visual FoxPro especificada. nWHANDLE é retornado se nWHANDLE for válido, mas não houver WCLIENTWINDOW. 0 é retornado se nWHANDLE for inválido.

# Observações

Esta função destina-se ao uso com rotinas no Visual FoxPro API Library Construction Kit. Consulte o tópico API Library Construction para obter mais informações sobre a criação de bibliotecas API.

No Visual FoxPro 9.0, BINDEVENT( ) suporta associação a eventos Window Message (Win Msg). BINDEVENT( ) captura eventos passados a um hWnd (Window Handle). Muitas janelas do Visual FoxPro têm uma janela cliente interna do tipo WCLIENTWINDOW que tem seu próprio hWnd. SYS(2325) permite determinar o WHANDLE de uma janela cliente interna.

SYS(2327) e SYS(2326) podem ser usados para converter entre um hWnd (Window Handle) e um WHANDLE do Visual FoxPro.
