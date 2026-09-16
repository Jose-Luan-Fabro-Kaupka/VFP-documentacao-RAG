# Função WEXIST( )

Determina se a janela definida pelo usuário especificada existe.

```foxpro
WEXIST(WindowName)
```

#### Parâmetros
 **WindowName**
Especifica o nome da janela. Também pode ser uma janela de sistema ou barra de ferramentas. WEXIST( ) retorna true (.T.) se ela estiver visível ou oculta e false (.F.) se estiver fechada, com exceções para as janelas Command e Debug.

# Valor de retorno

Logical

# Observações

WEXIST( ) retorna true (.T.) se a janela foi criada com DEFINE WINDOW; ela não precisa estar ativa nem visível, mas deve existir.

# Exemplo

```foxpro
DEFINE WINDOW wScreen1 FROM 10,10 TO 20,69
DEFINE WINDOW wScreen2 FROM 1,0 TO 19,79
CLEAR
? WEXIST('wScreen1')  && Displays .T.
STORE 'wScreen2' TO gcWinName
? WEXIST('win_name')  && Displays .F.
? WEXIST(gcWinName)  && Displays .T.
RELEASE WINDOWS wScreen1, wScreen2
```
