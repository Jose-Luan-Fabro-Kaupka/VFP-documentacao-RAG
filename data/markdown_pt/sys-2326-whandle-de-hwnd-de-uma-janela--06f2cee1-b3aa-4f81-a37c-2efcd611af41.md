# SYS(2326) - WHANDLE de hWnd de uma janela

Retorna um WHANDLE do Visual FoxPro a partir do hWnd de uma janela.

```foxpro
SYS(2326, nhWnd)
```

#### Parâmetros
 **nhWnd**
Especifica o hWnd inteiro (identificador de janela) da janela para a qual o WHANDLE interno do Visual FoxPro é retornado.

# Valor de retorno

Numérico. O WHANDLE inteiro retornado por SYS(2326) é uma estrutura interna do Visual FoxPro que envolve um hWnd.

# Observações

Esta função destina-se ao uso com rotinas do kit de construção de bibliotecas de API do Visual FoxPro. Consulte o tópico Construção de bibliotecas de API para obter mais informações sobre como criar bibliotecas de API.
