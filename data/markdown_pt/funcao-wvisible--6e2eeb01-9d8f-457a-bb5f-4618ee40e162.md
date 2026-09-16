# Função WVISIBLE( )

Determina se a janela especificada foi ativada e não está oculta.

```foxpro
WVISIBLE(WindowName)
```

#### Parâmetros
 **WindowName**
Especifica o nome da janela que WVISIBLE( ) avalia. No Visual FoxPro, você também pode especificar o nome de uma barra de ferramentas. Você também pode incluir a cadeia de caracteres vazia em WindowName para especificar a janela principal do Visual FoxPro.

# Valor de retorno

Lógico

# Observações

WVISIBLE( ) retorna verdadeiro (.T.) se a janela especificada é exibida ou ativada e não está oculta. Janelas são exibidas e ativadas com SHOW WINDOW e ACTIVATE WINDOW.

WVISIBLE( ) retorna falso (.F.) se a janela não foi ativada, foi ocultada com HIDE WINDOW, foi desativada com DEACTIVATE WINDOW ou não existe.

# Exemplo

O exemplo a seguir ativa a janela Data Session (representada pelo nome View). Usando a função WVISIBLE(), você pode imprimir na tela o estado visível da janela. A janela é fechada com Deactivate window e a função WVISIBLE() é usada novamente para imprimir o estado visível da janela.

```foxpro
ACTIVATE WINDOW View
? WVISIBLE( "View" ) && return .T.
DEACTIVATE WINDOW View
? WVISIBLE( "View" ) && return .F.
```
