# Exemplo Adicionar itens de menu em tempo de execução

Arquivo: ...\Samples\Solution\Menus\Fillmenu.scx

Este exemplo ilustra a adição de itens de menu a um menu em tempo de execução.

A definição de menu neste exemplo é definida no Menu Designer, com um único prompt e um submenu vazio chamado `empty_pop`.

O código está incluído para ser executado quando um usuário escolhe qualquer item no menu.

```foxpro
PROCEDURE takeaction(cPrompt)
#DEFINE MSG_LOC "You chose " + cPrompt + "."
IF cPrompt = "Release this menu"
   RELEASE PAD dynmenu of _MSYSMENU
ELSE
   WAIT WINDOW MSG_LOC TIMEOUT 1
ENDIF
```

O código associado ao evento Click de cmdRefresh no formulário executa o menu.

```foxpro
DO dynamic.mpr
```

Então, para cada item na lista, o código define um item de menu com o prompt e o texto da mensagem.

```foxpro
FOR i = 1 TO THISFORM.lstMenu.ListCount
   DEFINE BAR i OF empty_pop PROMPT (ALLTRIM(THISFORM.lstMenu.List(i,1))) ;
      MESSAGE (THISFORM.lstMenu.List(i,2))
ENDFOR
```

Também há código para fornecer o prompt que permite ao usuário liberar o menu.

```foxpro
DEFINE BAR i + 1 OF empty_pop PROMPT "\-"
DEFINE BAR i + 2 OF empty_pop PROMPT "Release this menu" ;
   MESSAGE "Remove the Dynamic Items menu from the menu bar."
```
