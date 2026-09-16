# Função PADPROMPT( )

Retorna o texto de um título de menu.

```foxpro
PADPROMPT(cMenuTitleName [, cMenuBarName])
```

#### Parâmetros
**cMenuTitleName**
Especifica o nome do título de menu (pad) ou o nome interno de um título do menu do sistema.
 **cMenuBarName**
Especifica o nome da barra de menus que contém o título ou o nome interno da barra de menus do sistema. Quando cMenuBarName é omitido, a barra de menus ativa é usada como segundo parâmetro. Se nenhuma barra estiver ativa e cMenuBarName for omitido, será gerado um erro.

# Valor de retorno

Character.

# Observações

Barras de menus são criadas com DEFINE MENU, que cria a barra, e DEFINE PAD, que cria os títulos na barra.
 PADPROMPT( ) também funciona com o sistema de menus do Visual FoxPro. A barra não precisa estar ativa para PADPROMPT( ) retornar o texto de um título.

 Se um título tiver sido criado com barra invertida e sinal de menor (\<) para criar uma tecla de acesso, ou com barra invertida (\) para desabilitá-lo, PADPROMPT( ) retornará somente o texto, sem os caracteres especiais.

# Exemplo

 No exemplo a seguir, todos os títulos da barra de menus do sistema são listados:

```foxpro
? "System menu titles: "
FOR lnI = 1 TO CNTPAD("_msysmenu")
?? PADPROMPT( GETPAD( "_msysmenu", lnI), "_msysmenu") + " "
NEXT
```
