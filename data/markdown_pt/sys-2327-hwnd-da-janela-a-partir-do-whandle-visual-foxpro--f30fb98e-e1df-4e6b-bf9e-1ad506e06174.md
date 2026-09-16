# SYS(2327) - hWnd da janela a partir do WHANDLE Visual FoxPro

Retorna o hWnd de uma janela a partir do WHANDLE de uma janela Visual FoxPro.

```foxpro
SYS(2327, nWHANDLE)
```

#### Parâmetros
 **nWHANDLE**
Especifica um WHANDLE inteiro para uma janela FoxPro. Um WHANDLE é uma estrutura interna Visual FoxPro (representada por um inteiro) que é um wrapper em torno do hWnd da janela cliente interna.

# Valor de retorno

Numeric. SYS(2327) retorna um valor inteiro hWnd.

# Observações

O WHANDLE inteiro retornado é uma estrutura interna Visual FoxPro que é um wrapper em torno de um hWnd.

Esta função destina-se ao uso com rotinas no Visual FoxPro API Library Construction Kit. Consulte o tópico API Library Construction para obter mais informações sobre a criação de bibliotecas de API.
