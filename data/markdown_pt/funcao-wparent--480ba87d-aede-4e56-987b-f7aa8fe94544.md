# Função WPARENT( )

Retorna o nome da janela pai da janela ativa ou especificada.

```foxpro
WPARENT([WindowName])
```

#### Parâmetros
 **WindowName**
Especifica uma janela cujo nome de janela pai WPARENT( ) retorna. WPARENT( ) retorna a cadeia de caracteres vazia se a janela especificada não tiver uma janela pai. Se você omitir WindowName , WPARENT( ) retorna o nome da janela pai da janela de saída ativa. WPARENT( ) retorna a cadeia de caracteres vazia se a janela de saída ativa não tiver uma janela pai.

# Valor de retorno

Character

# Observações

Você pode usar DEFINE WINDOW para criar uma janela e colocá-la em uma janela pai. A janela filha torna-se integrada à sua janela pai. Por exemplo, uma janela filha definida e ativada dentro de uma janela pai não pode ser movida para fora da janela pai. Se a janela pai é movida, a janela filha se move com ela.

# Exemplo

O exemplo a seguir define uma janela pai e uma janela filha. Em seguida, usa WPARENT( ) para identificar qual janela é a pai.

```foxpro
CLEAR ALL
CLEAR
DEFINE WINDOW wParent ;
   FROM 1,1 TO 20,20 ;
   TITLE 'wParent'     && Parent window
ACTIVATE WINDOW wParent
DEFINE WINDOW wChild ;
   FROM 1,1 TO 10,10 ;
   TITLE 'wChild' ;
   IN WINDOW wParent  && Child window
ACTIVATE WINDOW wChild
WAIT WINDOW 'The parent window is ' + WPARENT()
RELEASE WINDOW wParent, wChild
```
